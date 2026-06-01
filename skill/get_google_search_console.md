## Google Search Console API 踩坑记录

### 文件位置
所有 GSC 相关文件都在 `gsc-tools/` 文件夹中：
- `client_secret.json` — OAuth2 凭据
- `token.json` — 访问令牌（过期需用 refresh_token 刷新）
- `gsc_query.py` — 查询脚本
- `gsc_auth_auto.py` — 授权脚本

**注意**：没有 venv，requests 库可能未安装。查询时优先用 curl（见下方"无 requests 时用 curl 查询"）。

### 获取 API 的步骤

1. **去 [Google Cloud Console](https://console.cloud.google.com/)**
   - 创建项目（如 `seo-query-497919`）
   - 启用 **Google Search Console API**

2. **创建 OAuth2 凭据**
   - 左侧菜单 → **API 和服务** → **凭据**
   - **创建凭据** → **OAuth 客户端 ID**
   - 应用类型选 **桌面应用**
   - 下载 JSON 文件，重命名为 `client_secret.json`

3. **配置 OAuth 同意屏幕**
   - 左侧菜单 → **OAuth 同意屏幕**
   - 填写应用名称（随便起，如 "AI"）
   - **测试用户** → 添加你的 Google 邮箱（否则会报 `access_denied`）

4. **获取授权码**
   - 运行 `python3 gsc_auth_auto.py`
   - 浏览器会打开授权链接
   - **坑点**：WSL 环境无法自动打开浏览器，会报 `gio: Operation not supported`
   - **解决**：手动复制输出的 URL 到浏览器打开

5. **处理 redirect_uri 错误**
   - **坑点**：生成的 URL 可能缺少 `redirect_uri` 参数，报 `Missing required parameter: redirect_uri`
   - **解决**：手动构建 URL，加上 `&redirect_uri=http://localhost`
   - **坑点**：`client_secret.json` 里 `redirect_uris` 是 `["http://localhost"]`，但 `InstalledAppFlow` 会用随机端口
   - **解决**：用 `requests` 库直接调用 token endpoint

6. **交换授权码获取 Token**
   - **坑点**：授权码是一次性的，过期很快（约 5 分钟）
   - **坑点**：`google_auth_oauthlib` 库的 `redirect_uri` 参数冲突
   - **解决**：用 `requests` 直接 POST 到 token endpoint

### 获取数据的方法

```python
import json
import requests

with open('gsc-tools/token.json') as f:
    token_data = json.load(f)

headers = {
    'Authorization': f'Bearer {token_data["access_token"]}',
    'Content-Type': 'application/json'
}

# 列出网站
resp = requests.get('https://www.googleapis.com/webmasters/v3/sites', headers=headers)

# 查询搜索数据
site_url = 'sc-domain:example.com'
body = {
    'startDate': '2024-01-01',
    'endDate': '2024-12-31',
    'dimensions': ['query'],  # 或 ['page'], ['date'], ['country', 'device']
    'rowLimit': 25,
}
resp = requests.post(
    f'https://www.googleapis.com/webmasters/v3/sites/{requests.utils.quote(site_url, safe="")}/searchAnalytics/query',
    headers=headers, json=body
)
```

### Token 过期怎么办

**方法一：用 refresh_token 自动刷新（推荐）**

Token 会过期，但 refresh_token 有效期较长（约7天）。用以下方法刷新：

```python
import json
import subprocess

with open('gsc-tools/token.json') as f:
    token_data = json.load(f)

with open('gsc-tools/client_secret.json') as f:
    client_data = json.load(f)

refresh_token = token_data['refresh_token']
client_id = client_data['installed']['client_id']
client_secret = client_data['installed']['client_secret']

result = subprocess.run([
    'curl', '-s', '-X', 'POST', 'https://oauth2.googleapis.com/token',
    '-d', f'client_id={client_id}',
    '-d', f'client_secret={client_secret}',
    '-d', f'refresh_token={refresh_token}',
    '-d', 'grant_type=refresh_token'
], capture_output=True, text=True)

new_token = json.loads(result.stdout)
new_token['refresh_token'] = refresh_token  # 保留原 refresh_token

with open('gsc-tools/token.json', 'w') as f:
    json.dump(new_token, f, indent=2)
```

**方法二：重新授权（refresh_token 也过期时）**

1. 删除 `gsc-tools/token.json`
2. 运行 `python3 gsc-tools/gsc_auth_auto.py`
3. 重新授权（重复步骤 4-6）

### 常见错误

| 错误                                         | 原因                     | 解决                                    |
| ------------------------------------------ | ---------------------- | ------------------------------------- |
| `Missing required parameter: redirect_uri` | URL 缺少 redirect_uri 参数 | 手动加上 `&redirect_uri=http://localhost` |
| `access_denied`                            | 应用未发布，用户未添加为测试用户       | 在 OAuth 同意屏幕添加测试用户邮箱                  |
| `invalid_grant`                            | 授权码过期或已使用              | 重新获取授权码并立即使用                          |
| `Operation not supported`                  | WSL 无法打开浏览器            | 手动复制 URL 到浏览器                         |
| `TimeoutError`                             | httplib2 网络问题          | 用 `requests` 库替代                      |
| `ModuleNotFoundError: No module named 'requests'` | venv 不存在或 requests 未安装 | 用 curl 替代，见下方"无 requests 时用 curl 查询" |
| `Invalid Credentials` (401)                | access_token 过期          | 用 refresh_token 刷新，见上方"Token 过期怎么办" |

### 无 requests 时用 curl 查询

项目没有 venv，requests 可能未安装。用 curl 替代：

```bash
# 先刷新 token（见上方"Token 过期怎么办"）
# 然后用 curl 查询

ACCESS_TOKEN=$(python3 -c "import json; print(json.load(open('gsc-tools/token.json'))['access_token'])")

# 列出网站
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" \
  "https://www.googleapis.com/webmasters/v3/sites"

# 查询搜索数据（URL 需要编码）
curl -s -X POST \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"startDate":"2026-05-01","endDate":"2026-05-31","dimensions":["query"],"rowLimit":25}' \
  "https://www.googleapis.com/webmasters/v3/sites/sc-domain%3Aparalives-cheats.com/searchAnalytics/query"
```

**注意**：site_url 中的 `:` 需要编码为 `%3A`，即 `sc-domain:example.com` → `sc-domain%3Aexample.com`

### 用户的 27 个网站

r6tracker.click, paralives-cheats.com, howtoadhd.life, aibarbiedolls.app, anynote.online, happyghast.info, hypackel.games, brainrotscodes.top, doritosscript.com, silverchain.shop, fasttoolhub.com, escala6x1.net, silksong.info, turboquant.net, gameoftruelove.com, treespuzzle.com, funclicker.click, tralalerotralala.wiki, cattle.run, tierlist.online, kalkulatorodsetek24.pl, smiledog.wiki, mysbti.fun, formalizer.app, survivalrace.fun, thefarmerwasreplaced.com, hypackel.xyz

