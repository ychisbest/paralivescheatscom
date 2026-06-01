# Paralives-Cheats.com 自我迭代计划

> 每 48 小时运行一次，每次执行一个迭代周期。所有改动都在 Astro 项目内完成，git push 后自动部署。

---

## 迭代规则

1. **每次迭代只做 1-2 个任务**，确保质量
2. **先读 GSC 数据**，根据实际搜索词调整策略
3. **先读后改**，不破坏现有内容
4. **每次迭代后 commit + push**

---

## 任务池（按优先级排序）

### Phase 1: 技术 SEO 基础（第 1-2 次迭代）

#### T1. 添加 sitemap.xml
```
文件: src/pages/sitemap.xml.ts
内容: 生成所有页面的 sitemap
原因: 帮助搜索引擎发现所有页面
```

#### T2. 添加 robots.txt
```
文件: public/robots.txt
内容: 允许所有爬虫，指向 sitemap
原因: 规范爬虫行为
```

#### T3. 添加结构化数据 (Schema Markup)
```
文件: src/layouts/Layout.astro
内容: 添加 FAQ Schema（首页已有FAQ内容）、WebSite Schema
原因: 富摘要展示，提升 CTR
```

#### T4. 修复 canonical URL
```
文件: src/layouts/Layout.astro
内容: 添加 <link rel="canonical"> 确保 HTTPS 唯一
原因: 避免 HTTP/HTTPS 重复索引
```

### Phase 2: 内容扩展（第 3-8 次迭代）

#### T5. 创建 /money-cheats 页面
```
目标关键词: paralives money cheat, paralives money cheats, cheat money in paralives
内容: 详细的钱币作弊码指南，包含所有钱币相关代码
GSC 数据: 4次展示，排名56，需要专门页面提升
```

#### T6. 创建 /pregnancy-cheats 页面
```
目标关键词: paralives pregnancy cheat, paralives get pregnant cheat, pregnancy cheats paralives
内容: 怀孕作弊码完整指南
GSC 数据: 6次展示，排名10-30
```

#### T7. 创建 /skill-cheats 页面
```
目标关键词: paralives skill cheats, setskilllevel paralives
内容: 技能作弊码指南，列出所有技能ID
```

#### T8. 创建 /wemod-trainer 页面
```
目标关键词: paralives wemod, paralives trainer
内容: WeMod 和 Trainer 的使用指南（说明作弊码替代方案）
GSC 数据: 15次展示，排名7-9
```

#### T9. 创建 /teleport-cheats 页面
```
目标关键词: paralives teleport cheat, paralives how to teleport, warpcharacter paralives
内容: 传送和位置相关作弊码
GSC 数据: 4次展示
```

#### T10. 创建 /needs-cheats 页面
```
目标关键词: paralives needs cheat, reliefallneeds, setneed paralives
内容: 需求作弊码完整指南
```

### Phase 3: 内容优化（第 9-12 次迭代）

#### T11. 优化首页 Title 和 Meta Description
```
当前: "Home | Paralives Cheats"
目标: "Paralives Cheats 2026 - All Cheat Codes (Money, Skills, Pregnancy) | Paralives Cheats"
原因: 提升 CTR
```

#### T12. 添加面包屑导航
```
所有子页面添加面包屑
添加 BreadcrumbList Schema
原因: 改善用户体验 + 富摘要
```

#### T13. 添加内部链接策略
```
在每个子页面底部添加"相关作弊码"链接
在首页添加指向所有子页面的文字链接
原因: 提升页面权重传递
```

#### T14. 优化 FAQ 内容
```
根据 GSC 搜索词添加新的 FAQ 条目
添加 FAQ Schema Markup
原因: 争夺精选摘要
```

### Phase 4: 高级优化（第 13+ 次迭代）

#### T15. 创建 /console-commands 页面
```
目标关键词: paralives console commands, how to open console paralives
内容: 控制台使用完整指南
```

#### T16. 创建 /cheat-codes 页面
```
目标关键词: paralives cheat codes, paralives cheat code
内容: 所有作弊码的快速参考表
```

#### T17. 创建 /paralives-kody 页面（波兰语）
```
目标关键词: paralives kody（49次展示，0% CTR）
内容: 波兰语版本的作弊码页面
原因: 最大的未开发机会
```

#### T18. 创建 /paralives-trucchi 页面（意大利语）
```
目标关键词: paralives trucchi, trucchi paralives（8次展示）
内容: 意大利语版本的作弊码页面
```

#### T19. 添加"最后更新时间"标签
```
在每个页面顶部显示"Updated: June 2026"
原因: 提升内容新鲜度信号
```

#### T20. 创建 /paralives-cheats-pc 页面
```
目标关键词: paralives cheats pc
内容: PC 版专用作弊码指南
```

---

## 执行流程

每次迭代按以下步骤执行：

```
1. 读取 GSC 数据（检查 token 是否过期，过期则刷新）
   - 使用 skill/gsc-tools/ 中的工具
   - 获取最近 28 天的查询数据

2. 分析数据
   - 哪些关键词展示量增加了？
   - 哪些页面 CTR 需要提升？
   - 有没有新的搜索词出现？

3. 从任务池选择任务
   - 优先选择与 GSC 数据最相关的任务
   - 如果没有特别相关的，按顺序执行

4. 执行任务
   - 创建/修改文件
   - 确保代码质量
   - 测试本地构建（如有必要）

5. 提交并推送
   - git add .
   - git commit -m "SEO: [任务描述]"
   - git push

6. 记录迭代日志
   - 更新本文件的"迭代历史"部分
```

---

## 迭代历史

### 迭代 0 - 2026-06-01
- 完成: 初始 SEO 分析
- GSC 数据: 5 clicks, 437 impressions
- 创建: seo-plan.md
- 更新: skill/get_google_search_console.md（添加踩坑记录）

### 迭代 1 - 2026-06-01（全量执行）
- 完成: T1-T20 全部任务
- **Phase 1 - 技术 SEO:**
  - T1: sitemap.xml — 已有 @astrojs/sitemap 集成，无需额外操作 ✓
  - T2: robots.txt — 已存在于 public/robots.txt ✓
  - T3: 添加结构化数据 — WebSite Schema + FAQ Schema（首页 + 所有子页面）✓
  - T4: 添加 canonical URL + Open Graph + Twitter Card 标签 ✓
- **Phase 2 - 内容扩展:**
  - T5: 创建 /money-cheats 页面 ✓
  - T6: 创建 /pregnancy-cheats 页面 ✓
  - T7: 创建 /skill-cheats 页面 ✓
  - T8: 创建 /wemod-trainer 页面 ✓
  - T9: 创建 /teleport-cheats 页面 ✓
  - T10: 创建 /needs-cheats 页面 ✓
- **Phase 3 - 内容优化:**
  - T11: 优化首页 Title 为 "Paralives Cheats 2026 - All Cheat Codes (Money, Skills, Pregnancy)" ✓
  - T12: 添加面包屑导航 + BreadcrumbList Schema（所有子页面）✓
  - T13: 添加内部链接策略 — 首页分类卡片 + 子页面相关链接 ✓
  - T14: FAQ Schema Markup（首页 + 所有子页面）✓
- **Phase 4 - 高级优化:**
  - T15: 创建 /console-commands 页面 ✓
  - T16: 创建 /cheat-codes 页面（完整速查表）✓
  - T17: 创建 /paralives-kody 页面（波兰语）✓
  - T18: 创建 /paralives-trucchi 页面（意大利语）✓
  - T19: 添加 "Updated: June 2026" 标签（所有页面）✓
  - T20: 创建 /paralives-cheats-pc 页面 ✓
- **额外改进:**
  - 创建可复用组件: CheatTable.astro, Breadcrumb.astro
  - 更新 SiteHeader 添加 Cheat Codes 导航链接
  - 更新 SiteFooter 添加所有子页面链接
  - 构建成功: 19 个页面全部生成

---

## GSC 数据快照

### 2026-06-01（首次）
- 总点击: 5
- 总展示: 437
- 平均 CTR: ~1.1%
- Top 关键词: paralives kody (49 imp), paralives wemod (12 imp), paralives cheats (8 imp)
- 主要问题: CTR 极低，页面索引不足

---

## 注意事项

1. **不要重复创建已有内容** — 首页已有大量作弊码内容，子页面应聚焦特定主题
2. **保持设计风格一致** — 使用现有的 brutal-shadow、border-[3px] 等样式
3. **每个页面都要有独特的 Title 和 Description**
4. **内部链接要自然** — 不要为了链接而链接
5. **GSC 数据有延迟** — 通常延迟 2-3 天

---

## 无法执行的任务（需要人工操作）

- ~~修改 nginx 配置（HTTPS 重定向）~~ — 需要服务器访问权限
- ~~提交 sitemap 到 GSC~~ — 需要 GSC 后台操作
- ~~修改 robots.txt 托管配置~~ — 需要 CDN/服务器配置
- 外链建设（Reddit、论坛发帖）— 需要人工操作
- Google Ads 或付费推广 — 需要预算

---

*最后更新: 2026-06-01*
