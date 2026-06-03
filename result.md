# Paralives 作弊码完整指南

## 📋 目录

- [如何打开作弊控制台](#如何打开作弊控制台)
- [金钱作弊码](#金钱作弊码)
- [时间作弊码](#时间作弊码)
- [角色属性作弊码](#角色属性作弊码)
- [需求作弊码](#需求作弊码)
- [怀孕与生育作弊码](#怀孕与生育作弊码)
- [年龄与死亡作弊码](#年龄与死亡作弊码)
- [职业作弊码](#职业作弊码)
- [建造模式作弊码](#建造模式作弊码)
- [火灾作弊码](#火灾作弊码)
- [报纸与邮件作弊码](#报纸与邮件作弊码)
- [调试与杂项作弊码](#调试与杂项作弊码)
- [性能作弊码](#性能作弊码)
- [彩蛋命令](#彩蛋命令)
- [其他命令窗口](#其他命令窗口)

---

## 如何打开作弊控制台

### Windows 系统
- 按 **Ctrl + Shift + C**
- 或按 **Ctrl + F1**

### macOS 系统
- 按 **Command + Fn/Globe + F1**

控制台会出现在屏幕右上角（初始为最小化状态），点击圆形图标可以展开为全屏宽度或全屏。

> **重要提示：** 在 Paralives 中，你不需要先输入 `testingcheats true` 或类似命令 — 控制台随时可用，直接打开并输入即可。

> **小技巧：** 如果你忘记了某个命令，可以在游戏中输入 `HELP`，控制台会显示所有可用作弊码的完整目录。

---

## 金钱作弊码

这些是最常用的作弊码，可以让你无需工作就能建造梦想之家。

| 作弊码 | 效果 | 格式示例 |
| --- | --- | --- |
| `SETMONEY` | 将家庭余额更改为指定金额 | `SETMONEY 20000` |
| `PRINTMONEY` | 给予指定数量的 paradimes | `PRINTMONEY 20000` |
| `PAYDAY` | 给予选定 Para 的工资 | `PAYDAY` |
| `PIGGYBANK` | 给予 1,000 paradimes | `PIGGYBANK` |
| `MAKEITRAIN` | 给予 10,000 paradimes | `MAKEITRAIN` |
| `JACKPOT` | 给予 50,000 paradimes | `JACKPOT` |
| `LOTTERY` | 给予随机金额（1-100,000 之间） | `LOTTERY` |
| `GENERATEBILL` | 向邮箱发送更新的银行对账单 | `GENERATEBILL` |
| `CLEARBILLS` | 清除邮箱中的所有账单 | `CLEARBILLS` |
| `CLEARSELECTEDCHARACTERSBILLS` | 清除选定 Para 的所有账单 | `CLEARSELECTEDCHARACTERSBILLS` |
| `TOGGLEOGMONEYCHANGES` | 在控制台中记录金钱变化 | `TOGGLEOGMONEYCHANGES` |
| `CAUSEOUTAGE` | 切断选定地段的电力 | `CAUSEOUTAGE` |
| `FIXOUTAGE` | 修复选定地段的停电问题 | `FIXOUTAGE` |

---

## 时间作弊码

不再等待正确的时间或日期。

| 作弊码 | 效果 | 格式示例 |
| --- | --- | --- |
| `SETTIMESCALE` | 设置游戏时间流速（默认为 1） | `SETTIMESCALE 2` |
| `PAUSETIME` | 暂停/恢复游戏时间 | `PAUSETIME` |
| `SETTIME` | 设置游戏内时间 | `SETTIME 14:30` |
| `SETDAY` | 设置星期几 | `SETDAY Friday` |
| `ADVANCEDAYS` | 前进指定天数 | `ADVANCEDAYS 3` |
| `SEASON` | 更改季节 | `SEASON Summer` |

---

## 角色属性作弊码

编辑角色的各种属性。

| 作弊码 | 效果 | 格式示例 |
| --- | --- | --- |
| `LEVELUPSKILL` | 提升选定 Para 的特定技能 | `LEVELUPSKILL Piano` |
| `SETSKILLLEVEL` | 将特定技能设置为特定等级 | `SETSKILLLEVEL Cooking 10` |
| `PRINTAGE` | 显示选定 Para 的年龄 | `PRINTAGE` |
| `RESETPERSONALITY` | 重置选定 Para 的人格等级（恢复为 1，移除特质和升级） | `RESETPERSONALITY` |
| `SHOWCHARACTERRELATIONSHIPS` | 显示选定 Para 的所有关系和关系标签 | `SHOWCHARACTERRELATIONSHIPS` |
| `COMPLETECURRENTWANTS` | 自动完成选定 Para 的所有当前想要 | `COMPLETECURRENTWANTS` |
| `LEARNALLRECIPES` | 学习所有食谱 | `LEARNALLRECIPES` |
| `LEARNALLSKINS` | 学习所有皮肤/外观选项 | `LEARNALLSKINS` |
| `OPENPARAMAKER` | 打开 Paramaker 角色编辑器 | `OPENPARAMAKER` |
| `GETEQUIPMENT` | 显示创建此角色时选择的所有选项 | `GETEQUIPMENT` |
| `GETSEX` | 告诉你选定 Para 的性别 | `GETSEX` |
| `SHOWCURRENTCHARACTERGUID` | 显示选定角色的 GUID（唯一标识符） | `SHOWCURRENTCHARACTERGUID` |

---

## 需求作弊码

管理角色的各种需求。

| 作弊码 | 效果 | 格式示例 |
| --- | --- | --- |
| `FILLALLNEEDS` | 填满所有需求 | `FILLALLNEEDS` |
| `FILLNEED` | 填满特定需求 | `FILLNEED Hunger` |
| `DRAINNEED` | 排空特定需求 | `DRAINNEED Energy` |
| `SETNEED` | 将特定需求设置为特定值 | `SETNEED Hygiene 50` |
| `ENABLENEEDDECAY` | 启用/禁用需求衰减 | `ENABLENEEDDECAY false` |
| `FREEZENEEDS` | 冻结所有需求（不再衰减） | `FREEZENEEDS` |

**可操作的需求类型：**
- Hunger（饥饿）
- Energy（能量）
- Hygiene（卫生）
- Fun（娱乐）
- Social（社交）
- Bladder（膀胱）
- Comfort（舒适）

---

## 怀孕与生育作弊码

| 作弊码 | 效果 | 格式示例 |
| --- | --- | --- |
| `GETPREGNANT` | 使选定 Para 怀孕（需指定婴儿数量 1-3） | `GETPREGNANT 1` |
| `GIVEBIRTH` | 选定 Para 分娩（不需要怀孕） | `GIVEBIRTH` |

---

## 年龄与死亡作弊码

| 作弊码 | 效果 | 格式示例 |
| --- | --- | --- |
| `SETAGE` | 设置选定 Para 的年龄 | `SETAGE 35` |
| `NEWLIFESTAGE` | 将 Para 老化到下一个生命阶段 | `NEWLIFESTAGE` |
| `PREVIOUSLIFESTAGE` | 将 Para 回退到上一个生命阶段 | `PREVIOUSLIFESTAGE` |
| `NEXTGROWTHSPURT` | 如果适用，将 Para 移动到下一个生长期 | `NEXTGROWTHSPURT` |
| `KILL` | 杀死选定的 Para | `KILL` |
| `REVIVE` | 复活选定的 Para | `REVIVE` |
| `DISABLEAGING` | 禁用/启用老化 | `DISABLEAGING true` |

---

## 职业作弊码

| 作弊码 | 效果 | 格式示例 |
| --- | --- | --- |
| `GETJOB` | 获得指定工作 | `GETJOB Cooking` |
| `QUITJOB` | 辞去当前工作 | `QUITJOB` |
| `PROMOTE` | 晋升当前职位 | `PROMOTE` |
| `DEMOTE` | 降级当前职位 | `DEMOTE` |
| `SETJOBLEVEL` | 设置工作等级 | `SETJOBLEVEL 5` |

---

## 建造模式作弊码

| 作弊码 | 效果 | 格式示例 |
| --- | --- | --- |
| `REPAIRALLITEMS` | 修复所有物品（移除损坏状态） | `REPAIRALLITEMS` |
| `UNSPOILALLITEMS` | 移除所有变质状态 | `UNSPOILALLITEMS` |
| `SETITEMSTATE` | 更改选定物品的状态 | `SETITEMSTATE IsOn 1` |
| `SHOWITEMSTATES` | 显示选定物品的动画和交互数据 | `SHOWITEMSTATES` |
| `ADDITEMTOINVENTORY` | 使用物品 ID 将指定物品添加到 Para 的库存 | `ADDITEMTOINVENTORY ClutterClothingRingEngagement` |
| `SHOWITEMINFOS` | 显示建造模式中当前选定对象的物品 ID | `SHOWITEMINFOS` |
| `PRINTINVENTORY` | 显示 Para 库存中所有物品的物品 ID | `PRINTINVENTORY` |
| `CLEARINVENTORY` | 移除 Para 库存中的所有物品 | `CLEARINVENTORY` |
| `SPAWNALLITEMS` | 在地段上生成每件物品（可能会使游戏崩溃！） | `SPAWNALLITEMS` |
| `UNLOCKALLITEMS` | 解锁所有物品 | `UNLOCKALLITEMS` |

---

## 火灾作弊码

| 作弊码 | 效果 | 格式示例 |
| --- | --- | --- |
| `EXTINGUISHALLFIRES` | 扑灭所有活跃火灾 | `EXTINGUISHALLFIRES` |
| `EXTINGUISHSELECTEDCHARACTERSONFIRE` | 扑灭选定 Para 身上的火 | `EXTINGUISHSELECTEDCHARACTERSONFIRE` |
| `SETITEMONFIRE` | 将选定物品点燃 | `SETITEMONFIRE` |
| `SETSELECTEDCHARACTERSONFIRE` | 将选定的 Para 点燃 | `SETSELECTEDCHARACTERSONFIRE` |

---

## 报纸与邮件作弊码

| 作弊码 | 效果 | 格式示例 |
| --- | --- | --- |
| `GENERATEBILL` | 向邮箱发送更新的银行对账单 | `GENERATEBILL` |
| `CLEARBILLS` | 清除邮箱中的所有账单 | `CLEARBILLS` |
| `RESETMUSEUMDONATIONS` | 清除所有博物馆捐款 | `RESETMUSEUMDONATIONS` |

---

## 调试与杂项作弊码

| 作弊码 | 效果 | 格式示例 |
| --- | --- | --- |
| `ALIASES` | 列出所有别名 | `ALIASES` |
| `CLEAR` | 清除作弊命令框 | `CLEAR` |
| `HELP` | 显示所有作弊码列表 | `HELP` |
| `SCHEDULE` | 安排命令每帧执行，输出显示在屏幕左上角 | `SCHEDULE FPS` |
| `STOP` | 停止之前安排的作弊命令 | `STOP` |
| `UNSTUCK` | 将选定 Para 移动到导航网格上的正确位置 | `UNSTUCK` |
| `UNSTUCKALL` | 将所有 Para 移动到导航网格上的正确位置 | `UNSTUCKALL` |
| `CANCELALLCHARACTERSINTERACTIONS` | 取消整个城镇的所有排队交互 | `CANCELALLCHARACTERSINTERACTIONS` |
| `CANCELALLHOUSEHOLDINTERACTIONS` | 取消整个家庭的所有排队交互 | `CANCELALLHOUSEHOLDINTERACTIONS` |
| `SHOWCURRENTSOCIALGROUPCONVERSATION` | 在作弊命令中显示当前社交群组对话 | `SHOWCURRENTSOCIALGROUPCONVERSATION` |
| `SHOWSOCIALGROUPSCLUSTERS` | 在作弊命令中显示所有当前社交群组集群 | `SHOWSOCIALGROUPSCLUSTERS` |
| `DELETEALLSOCIALGROUPS` | 结束任何当前的社交群组 | `DELETEALLSOCIALGROUPS` |
| `SHOWMANAGERLISTSCOUNT` | 当前地段的管理器列表出现在作弊命令中 | `SHOWMANAGERLISTSCOUNT` |
| `VIEWMEMORYLOG` | 在作弊命令中显示特定 Para 的记忆日志 | `VIEWMEMORYLOG` |

---

## 性能作弊码

| 作弊码 | 效果 | 格式示例 |
| --- | --- | --- |
| `FPS` | 显示帧率 | `FPS` |
| `VSYNC` | 启用/禁用垂直同步 | `VSYNC false` |
| `RESOLUTION` | 设置分辨率 | `RESOLUTION 1920x1080` |
| `WINDOWED` | 切换窗口模式 | `WINDOWED true` |
| `QUALITY` | 设置图形质量 | `QUALITY High` |

---

## 彩蛋命令

在作弊控制台中输入这些会产生有趣的效果。

| 作弊码 | 效果 |
| --- | --- |
| `BEAR` | 创建熊的 ASCII 艺术 |
| `CAT` | 显示一只猫 |
| `EIGHTBALL` | 给出随机的 Magic 8 Ball 结果 |
| `HOTEL` | 在控制台中显示 "Trivago" |
| `RAGEQUIT` | 关闭游戏 |

---

## 其他命令窗口

通过按 **Ctrl + F1** 打开的作弊命令窗口是最有用的。但是，如果你点击窗口中 "Cheat Commands" 左侧的向下箭头，可以发现 Paralives 的其他一些有趣信息。

这会显示四个其他窗口：

1. **Cheat Commands** - 作弊命令（最常用）
2. **Parafolk Profiler** - 角色分析器（有用）
3. 其他调试窗口

---

## ⚠️ 重要提示

1. **保存游戏** - 在使用可能大幅改变世界或角色的作弊码之前，始终保存游戏
2. **大小写不敏感** - 命令可以任意大小写输入（`MAKEITRAIN` 和 `makeitrain` 效果相同）
3. **需要选择角色** - 某些作弊码只对选定的角色有效，在输入命令前点击一个 Parafolk
4. **早期访问** - 游戏刚进入早期访问，某些作弊码可能不稳定
5. **使用 HELP** - 在游戏中输入 `HELP` 可查看完整命令列表

---

## 📚 参考来源

- [IGN - Paralives Cheats List and Console Commands](https://www.ign.com/wikis/paralives/Paralives_Cheats_List_and_Console_Commands)
- [Eurogamer - Paralives cheat codes and console commands](https://www.eurogamer.net/paralives-cheats)
- [The Gamer - How To Use Cheat Commands In Paralives](https://www.thegamer.com/paralives-cheat-command-list-how-to-use)
- [Sims Community - Paralives Cheats And How To Use Them](https://simscommunity.info/2026/05/20/paralives-cheats-and-how-to-use-them)
- [The Sims Tree - Paralives Cheats: Full List](https://thesimstree.com/en/news-about-the-sims/tst-news/paralives-cheats-full-list-and-how-to-use-them-%E2%80%93-money,-skills,-age,-and-more.html)
- [Paralives Wiki - Cheats](https://paralives.wiki.gg/wiki/Cheats)
- [PC Gamer - Paralives cheats list](https://www.pcgamer.com/games/life-sim/paralives-cheats)
- [Esports.gg - Paralives cheats guide](https://esports.gg/guides/gaming/paralives-cheats-guide)
- [Radio Times - Paralives cheats](https://www.radiotimes.com/technology/gaming/paralives-cheats-cheat-codes)

---

*最后更新：2026年6月2日*
