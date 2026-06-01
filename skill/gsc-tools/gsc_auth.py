#!/usr/bin/env python3
"""
Google Search Console OAuth2 授权脚本
自动启动本地服务器处理授权回调
"""

import os
import json
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import threading

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
CLIENT_SECRET_FILE = 'client_secret.json'
TOKEN_FILE = 'token.json'

# 全局变量存储授权码
auth_code = None
auth_state = None


class AuthHandler(BaseHTTPRequestHandler):
    """处理 OAuth 回调的 HTTP 处理器"""

    def do_GET(self):
        global auth_code, auth_state

        # 解析回调 URL
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        # 获取授权码和 state
        if 'code' in params:
            auth_code = params['code'][0]
            auth_state = params.get('state', [None])[0]

            # 发送成功响应
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'''
                <html>
                <head><title>Authorization Success</title></head>
                <body>
                <h1>&#10004; Authorization Successful!</h1>
                <p>You can close this window and return to the terminal.</p>
                </body>
                </html>
            ''')
        else:
            # 发送错误响应
            error = params.get('error', ['unknown'])[0]
            self.send_response(400)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(f'''
                <html>
                <head><title>Authorization Failed</title></head>
                <body>
                <h1>&#10008; Authorization Failed</h1>
                <p>Error: {error}</p>
                </body>
                </html>
            '''.encode())

    def log_message(self, format, *args):
        """禁用日志输出"""
        pass


def get_credentials():
    """获取 OAuth 2.0 凭据"""
    global auth_code, auth_state

    creds = None

    # 检查是否已有 token
    if os.path.exists(TOKEN_FILE):
        from google.oauth2.credentials import Credentials
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # 如果没有有效凭据，需要用户授权
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("正在刷新访问令牌...")
            from google.auth.transport.requests import Request
            creds.refresh(Request())
        else:
            print("=" * 60)
            print("Google Search Console API 授权")
            print("=" * 60)

            # 读取并修改 client_config 以使用特定端口
            with open(CLIENT_SECRET_FILE) as f:
                client_config = json.load(f)
            client_config['installed']['redirect_uris'] = ['http://localhost:8085']

            # 创建 OAuth flow
            flow = InstalledAppFlow.from_client_config(
                client_config, SCOPES
            )

            # 生成授权 URL
            auth_url, state = flow.authorization_url(
                prompt='consent',
                access_type='offline'
            )

            print(f"\n正在启动本地授权服务器...")
            print(f"请在浏览器中完成授权\n")

            # 尝试自动打开浏览器
            try:
                webbrowser.open(auth_url)
                print("已自动打开浏览器")
            except:
                print(f"无法自动打开浏览器，请手动访问：\n{auth_url}")

            # 启动本地服务器监听回调
            server = HTTPServer(('localhost', 8085), AuthHandler)
            print(f"\n等待授权回调 (http://localhost:8085)...")

            # 处理单个请求
            server.handle_request()

            if auth_code:
                # 使用授权码获取 token
                flow.fetch_token(code=auth_code)
                creds = flow.credentials
                print("✓ 授权成功!")
            else:
                print("✗ 授权失败")
                return None

        # 保存 token
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
        print(f"✓ 访问令牌已保存到 {TOKEN_FILE}")

    return creds


def main():
    """主函数"""
    creds = get_credentials()

    if creds:
        from googleapiclient.discovery import build
        service = build('searchconsole', 'v1', credentials=creds)
        print("\n✓ 已连接到 Google Search Console API")

        # 列出网站
        print("\n=== 你的网站属性 ===")
        sites = service.sites().list().execute()
        site_entries = sites.get('siteEntry', [])

        if not site_entries:
            print("没有找到网站属性")
        else:
            for site in site_entries:
                print(f"  站点: {site['siteUrl']}")
                print(f"  权限级别: {site.get('permissionLevel', 'N/A')}")
                print()
    else:
        print("无法连接到 API")


if __name__ == '__main__':
    main()
