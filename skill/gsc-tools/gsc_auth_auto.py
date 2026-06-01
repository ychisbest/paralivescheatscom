#!/usr/bin/env python3
"""
Google Search Console OAuth2 授权脚本
使用 InstalledAppFlow 自动处理
"""

import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
CLIENT_SECRET_FILE = 'client_secret.json'
TOKEN_FILE = 'token.json'


def main():
    print("=" * 60)
    print("Google Search Console API 授权")
    print("=" * 60)

    # 读取 client_config
    with open(CLIENT_SECRET_FILE) as f:
        client_config = json.load(f)

    # 使用 InstalledAppFlow，它会自动处理 redirect_uri
    flow = InstalledAppFlow.from_client_config(client_config, SCOPES)

    # 使用 run_local_server，自动启动本地服务器并处理回调
    # 使用默认的 http://localhost:xxxx（随机端口）
    print("\n正在启动本地授权服务器...")
    print("请在弹出的浏览器中完成授权\n")

    creds = flow.run_local_server(port=0)

    # 保存 token
    with open(TOKEN_FILE, 'w') as token:
        token.write(creds.to_json())
    print(f"\n✓ 访问令牌已保存到 {TOKEN_FILE}")

    # 测试连接
    service = build('searchconsole', 'v1', credentials=creds)
    print("✓ 已连接到 Google Search Console API")

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


if __name__ == '__main__':
    main()
