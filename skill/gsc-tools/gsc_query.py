#!/usr/bin/env python3
"""
Google Search Console API 查询脚本
"""

import json
import requests
from datetime import datetime, timedelta

TOKEN_FILE = 'token.json'


def get_headers():
    """获取 API 请求头"""
    with open(TOKEN_FILE) as f:
        token_data = json.load(f)
    return {
        'Authorization': f'Bearer {token_data["access_token"]}',
        'Content-Type': 'application/json'
    }


def list_sites():
    """列出所有网站"""
    resp = requests.get(
        'https://www.googleapis.com/webmasters/v3/sites',
        headers=get_headers(),
        timeout=30
    )
    if resp.status_code == 200:
        return resp.json().get('siteEntry', [])
    return []


def query_analytics(site_url, start_date, end_date, dimensions=['query'], row_limit=25):
    """查询搜索分析数据"""
    url = f'https://www.googleapis.com/webmasters/v3/sites/{requests.utils.quote(site_url, safe="")}/searchAnalytics/query'

    body = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': dimensions,
        'rowLimit': row_limit,
    }

    resp = requests.post(url, headers=get_headers(), json=body, timeout=30)

    if resp.status_code == 200:
        return resp.json().get('rows', [])
    else:
        print(f'Error: {resp.status_code} - {resp.json()}')
        return []


def format_date(date_str):
    """格式化日期显示"""
    return datetime.strptime(date_str, '%Y-%m-%d').strftime('%m/%d')


def main():
    # 列出网站
    sites = list_sites()
    print(f'找到 {len(sites)} 个网站\n')

    # 查询第一个网站的搜索数据
    if sites:
        site_url = sites[0]['siteUrl']
        print(f'正在查询: {site_url}\n')

        # 最近 28 天数据
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=28)).strftime('%Y-%m-%d')

        # 按查询词统计
        print('=== 热门搜索词 (最近28天) ===')
        rows = query_analytics(site_url, start_date, end_date, ['query'], 20)
        for row in rows:
            print(f'  {row["keys"][0]}')
            print(f'    点击: {row["clicks"]}, 展示: {row["impressions"]}, CTR: {row["ctr"]:.2%}, 排名: {row["position"]:.1f}')

        # 按页面统计
        print('\n=== 热门页面 ===')
        rows = query_analytics(site_url, start_date, end_date, ['page'], 10)
        for row in rows:
            print(f'  {row["keys"][0]}')
            print(f'    点击: {row["clicks"]}, 展示: {row["impressions"]}')


if __name__ == '__main__':
    main()
