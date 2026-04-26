# 🎼 ViewTuner 视觉调音师

![版本](https://img.shields.io/badge/版本-2.0.0-blue) ![平台](https://img.shields.io/badge/平台-Obsidian全平台-green) ![许可证](https://img.shields.io/badge/许可证-专有软件-orange) ![状态](https://img.shields.io/badge/状态-正式版-brightgreen)

> **"全能易用一站式【美化+工具】平台 | obsidian变好用的必备基础设施"**  
> *不用敲一行代码，即可获得舒适的美化体验* ✨

## 📝 更新日志

### v2.0.0 (2026-04-06)

#### ✨ 新功能
- ✨ 发版2.0

#### 🔧 优化
- ⚡ 加快运行速度，提高内部耦合性


### v1.19.5 (2026-04-06)

#### 🔧 优化
- ⚡ 更新售价表与实际一致


### v1.19.4 (2026-04-06)

#### ✨ 新功能
- ✨ 导出网格PDF正常化


### v1.19.3 (2026-04-06)

#### ✨ 新功能
- ✨ PDF 导出 v6.2
- ✨ 清空 + 仅注入版式风格区段 CSS

#### 🔧 优化
- ⚡ CSS 选择器修复
- ⚡ 缺少空格导致阅读模式下版式风格从未生效
- ⚡ 移除 [VT-PDF] 调试日志 


### v1.19.2 (2026-04-06)

#### 🔧 优化
- ⚡ 1. saveSettings() 改为防抖保存
- ⚡ 2. cleanupAllStyles()补充缺少 body class
- ⚡ 3. CSS 变量清理完善
- ⚡ 5. 每个版本迁移块包裹 try-catch


### v1.19.1 (2026-04-06)

#### 🔧 优化
- ⚡ 增强内部功能耦合性
- ⚡ 1.5.3光标动画
- ⚡ 1.7.6YAML属性自动收起
- ⚡ 这两个功能同时开启后，鼠标悬浮YMAL区，光标动画更稳定


### v1.19.0 (2026-04-06)

#### 🔧 优化
- ⚡ 优化默认设置项
- ⚡ 设置开关跳动稳定化


### v1.18.1 (2026-04-06)

#### 🔧 优化
- ⚡ 更新打包环境


### v1.18.0 (2026-04-05)

#### ✨ 新功能
- ✨ 设置项可搜索，自动补全可跳转

#### 🔧 优化
- ⚡ PDF导出默认化


### v1.17.8 (2026-03-18)

#### 🔧 优化
- ⚡ 开发者环境维护


### v1.17.7 (2026-03-01)

#### 🔧 优化
- ⚡ 修复阅读视图 Banner 显示
- ⚡ 优化「插入头图」按钮移动端显示


### v1.17.6 (2026-02-28)

#### ✨ 新功能
- ✨ 注入设置界面标题颜色样式（使用 Obsidian 标准标题颜色变量）

#### 🔧 优化
- ⚡ 状态栏显示顺序优化拖拽句柄，改为 grip-vertical 图标


### v1.17.5 (2026-02-28)

#### ✨ 新功能
- ✨ 加入「熵减引擎」系列标识


### v1.17.4 (2026-02-28)

#### ✨ 新功能
- ✨ 升级打包脚本


### v1.17.3 (2026-02-26)

#### 🔧 优化
- ⚡ 清理图片对齐样式


### v1.17.2 (2026-02-24)

#### ✨ 新功能
- ✨ 更新打包脚本


### v1.17.1 (2026-02-11)

#### ✨ 新功能
- ✨ 支持外部图床注释修改
- ✨ 提升图片谐调师稳定性
- ✨ 注: 外部图床不在下方显示注释


### v1.17.0 (2026-02-10)

#### ✨ 新功能
- ✨ 图片谐调师增加对图床和外链图片的大小调节控制

#### 🔧 优化
- ⚡ 图片谐调师兼容外部图床加载


### v1.16.4 (2026-02-09)

#### ✨ 新功能
- ✨ 实现新标签页设置界面悬浮滚动按钮


### v1.16.3 (2026-02-08)

#### ✨ 新功能
- ✨ 加入官方设置界面显示按钮
- ✨ 设置下拉到最后，切换其他设置标签页更方便


### v1.16.2 (2026-02-06)

#### ✨ 新功能
- ✨ 【1.7.3状态栏显示】增加状态栏排序功能
- ✨ 实现精细化控制状态栏内容从左到右的排序功能


### v1.16.1 (2026-02-04)

#### ✨ 新功能
- ✨ 完美集成光标动画


### v1.16.0 (2026-02-04)

#### ✨ 新功能
- ✨ 集成集成光标行号美化
- ✨ 注明来源


### v1.15.5 (2026-02-04)

#### 🔧 优化
- ⚡ 修复右键图片删除图片链接会导致该笔记下所有该名字的图片都删除的bug
- ⚡ 新逻辑
- ⚡ 右键图片时获取 DOM 行号，删除时自动扣除 frontmatter 偏移量，精确定位并删除对应行的图片链接；无行号时仅在单匹配情况下删除，避免误删同名图片。


### v1.15.4 (2026-02-04)

#### ✨ 新功能
- ✨ 解决Callout名称英文大写导致的渲染问题：

#### 🔧 优化
- ⚡ 根本原因
- ⚡ Obsidian将 > [!AI] 渲染为 <div data-callout="ai"> （强制小写）
- ⚡ 插件生成的CSS选择器 [data-callout="AI"] 无法匹配
- ⚡ 导致自定义样式失效
- ⚡ 当前优雅的在不破坏原机制的前提下，自动将输入的大写英文转换为小写
- ⚡ 同时保持全中文字符命名


### v1.15.3 (2026-02-04)

#### ✨ 新功能
- ✨ 增加MD颜色渲染下的自定义方案各选项独立开关
- ✨ 启用自定义方案后，可精细化单独定义各选项颜色开关是否开启
- ✨ 如果关闭则跟随主题呈现默认状态


### v1.15.2 (2026-02-04)

#### ✨ 新功能
- ✨ 添加编辑器宽度控制总开关功能
- ✨ 关闭状态下LiveScene编辑器宽度控制滑块同步隐藏
- ✨ 关闭状态下状态栏隐藏宽度控制滑块


### v1.15.1 (2026-02-04)

#### ✨ 新功能
- ✨ 集成网格背景的版式风格
- ✨ Thanks for Moksha


### v1.15.0 (2026-01-31)

#### 🔧 优化
- ⚡ 兼容段落间距在阅读模式下滑块调整
- ⚡ 致谢重玄、Heart of Stone


### v1.14.3 (2026-01-28)

#### ✨ 新功能
- ✨ 新增尊贵源码验证逻辑


### v1.14.2 (2026-01-28)

#### ✨ 新功能
- ✨ 更新激活管理信息


### v1.14.0 (2026-01-25)

#### 🔧 优化
- ⚡ 更新`整点火火薯条`致谢信息


### v1.13.20 (2026-01-25)

#### 🔧 优化
- ⚡ 修订ISC和MIT许可证信息


### v1.13.19 (2026-01-22)

#### 🔧 优化
- ⚡ 优化文件夹创建lucide图标显示失败的bug


### v1.13.18 (2026-01-21)

#### 🔧 优化
- ⚡ 修复【标注构建师_Callout Builder】lucide图标预览和创建失败的bug


### v1.13.17 (2026-01-21)

#### ✨ 新功能
- ✨ 标签页emoji图标修订为更现代的lucide图标


### v1.13.16 (2026-01-19)

#### 🔧 优化
- ⚡ 更新授权信息


### v1.13.15 (2026-01-16)

#### ✨ 新功能
- ✨ 新增功能
- ✨ Canvas 白板渲染纸张纹理
- ✨ 并优化其适配Live Scene


### v1.13.14 (2026-01-15)

#### ✨ 新功能
- ✨ 同步兼容2026专业版激活


### v1.13.13 (2026-01-14)

#### ✨ 新功能
- ✨ 更新液态玻璃信息描述


### v1.13.12 (2026-01-13)

#### ✨ 新功能
- ✨ 粘贴到 Callout 块功能实现


### v1.13.11 (2026-01-13)

#### ✨ 新功能
- ✨ 给`编辑器宽度控制设置`启用添加说明小字


### v1.13.10 (2026-01-13)

#### ✨ 新功能
- ✨ 文件夹图标和文件类型图标新增删除弹窗保护确认

#### 🔧 优化
- ⚡ 修复下面六个删除框，使其更符合obsidian删除模态框最佳实践
- ⚡ 纸张纹理预设删除
- ⚡ MD渲染配色方案删除
- ⚡ 彩虹文件树方案删除
- ⚡ 记忆填空自定义语法删除
- ⚡ Callout模板删除（设置页）
- ⚡ Callout模板删除（管理类方法）


### v1.13.9 (2026-01-13)

#### 🔧 优化
- ⚡ 修复重命名预设、保存显示预设模态框有问题下方无法弹出保存和取消按钮的bug
- ⚡ thanks， 粉白の土豆 for discovering the bug in this program


### v1.13.8 (2026-01-11)

#### ✨ 新功能
- ✨ 给【插入 Callout 模板】模态框添加主题切换按钮, 实现对插入块的深浅切换查看


### v1.13.7 (2026-01-11)

#### 🔧 优化
- ⚡ 选择Callout模板命名为插入Callout模板
- ⚡ 修复彩虹文件树跟随深浅切换颜色未跟随切换的bug
- ⚡ 修复callout预览框跟随深浅切换颜色未跟随切换的bug


### v1.13.6 (2026-01-11)

#### ✨ 新功能
- ✨ 按钮位置自定义选择顶部或底部机制
- ✨ 选择顶部可以自由移动位置


### v1.13.5 (2026-01-11)

#### ✨ 新功能
- ✨ 实现文件库区域移动侧边栏功能


### v1.13.4 (2026-01-11)

#### ✨ 新功能
- ✨ 清理内存泄露, 整体优化标注构建师_Callout Builder模块


### v1.13.3 (2026-01-11)

#### ✨ 新功能
- ✨ 增加callout 块预设功能
- ✨ 修订预览区显示逻辑
- ✨ 预览区明暗切换按钮
- ✨ 增加双色兼容逻辑


### v1.13.2 (2026-01-10)

#### ✨ 新功能
- ✨ 优化右键菜单图标显示


### v1.13.1 (2026-01-10)

#### ✨ 新功能
- ✨ 增加Callout右键拓展菜单功能


### v1.13.0 (2026-01-10)

#### ✨ 新功能
- ✨ 更新
- ✨ Callout 模板整体架构、按钮、交互逻辑


### v1.12.6 (2026-01-10)

#### ✨ 新功能
- ✨ 加入了折叠功能

#### 🔧 优化
- ⚡ 优化了部分按钮的排版
- ⚡ 优化了部分错误逻辑


### v1.12.5 (2026-01-09)

#### ✨ 新功能
- ✨ 集成 Callouts 自定义引用块功能


### v1.12.4 (2026-01-05)

#### ✨ 新功能
- ✨ 打包脚本重命名修订readme阅读符号前缀


### v1.12.3 (2026-01-03)

#### [NEW] New Features
- [+] 更新几位大师描述信息


### v1.12.2 (2026-01-03)

#### [NEW] New Features
- [+] 整体调试、满足阶段性发布要求


### v1.12.1 (2026-01-03)

#### [OPT] Improvements
- [*] 提升稳定性
- [*] 修复尺寸滚动和放大的bug


### v1.12.0 (2026-01-03)

#### [NEW] New Features
- [+] 基于MD语言的图片对齐方案的实现


### v1.11.24 (2026-01-02)

#### [NEW] New Features
- [+] 修订实用功能名称和描述
- [+] 完善补充逻辑
- [+] 整体提升稳定性


### v1.11.23 (2026-01-01)

#### [OPT] Improvements
- [*] 提升稳定性
- [*] Bug #1: imageCaptionObserver 重复创建导致内存泄漏
- [*] Bug #2: 大量 setTimeout 未被定时器管理系统追踪


### v1.11.22 (2026-01-01)

#### [OPT] Improvements
- [*] 修复bug
- [*] Bug #1: imageCaptionObserver 重复创建导致内存泄漏
- [*] Bug #2: 大量 setTimeout 未被定时器管理系统追踪


### v1.11.21 (2025-12-31)

#### [NEW] New Features
- [+] 图片谐调家功能性完善
- [+] 注释相关逻辑健全
- [+] 对齐相关逻辑健全
- [+] 其他相关UI优化


### v1.11.20 (2025-12-31)

#### [NEW] New Features
- [+] 拓展完善的图片附件位置存放
- [+] 拓展完善的时间戳命名前缀
- [+] 优化模态框布局


### v1.11.19 (2025-12-31)

#### [NEW] New Features
- [+] 图片粘贴弹窗与相关设置逻辑完成


### v1.11.18 (2025-12-30)

#### [NEW] New Features
- [+] 图片功能甄选完善


### v1.11.17 (2025-12-30)

#### [NEW] New Features
- [+] 图片右键菜单功能完善


### v1.11.16 (2025-12-30)

#### [NEW] New Features
- [+] 初步实现图片对齐和图片注释


### v1.11.15 (2025-12-30)

#### [NEW] New Features
- [+] 实现 Alt+滚轮控制图片大小免费功能


### v1.11.14 (2025-12-29)

#### [NEW] New Features
- [+] 图片查看器界面优化


### v1.11.13 (2025-12-29)

#### [NEW] New Features
- [+] 拓展`图片查看器`功能


### v1.11.12 (2025-12-29)

#### [OPT] Improvements
- [*] 优化滚动条美化描述信息


### v1.11.11 (2025-12-28)

#### [NEW] New Features
- [+] 更新插件说明信息


### v1.11.10 (2025-12-28)

#### [OPT] Improvements
- [*] 1341


### v1.11.9 (2025-12-28)

#### [OPT] Improvements
- [*] 2512281339


### v1.11.8 (2025-12-28)

#### [OPT] Improvements
- [*] 校验性测试2512281321


### v1.11.7 (2025-12-28)

#### [OPT] Improvements
- [*] 修复切换场景的保存问题


### v1.11.6 (2025-12-28)

#### [OPT] Improvements
- [*] 修复livesence场景切换bug


### v1.11.5 (2025-12-27)

#### [NEW] New Features
- [+] 优化README文档


### v1.11.4 (2025-12-27)

#### [OPT] Improvements
- [*] 修复完善:Live Scene 模态框中的全部功能修改后：
点击"取消" - 会恢复到打开模态框时的原始状态
点击模态框外部或按 ESC - 同样会恢复原始状态
点击"保存" - 才会真正保存所有修改

### v1.11.3 (2025-12-27)

#### [NEW] New Features
- [+] 更新用户一叶知秋的贡献记录


### v1.11.2 (2025-12-27)

#### [NEW] New Features
- [+] 实现状态栏悬浮隐藏功能


### v1.11.1 (2025-12-26)

#### [OPT] Improvements
- [*] 开启"启用毛玻璃效果"开关后会立即生效


### v1.11.0 (2025-12-25)

#### [OPT] Improvements
- [*] 修复段落间距在编辑模式不生效
- [*] 优化关闭样式


### v1.10.13 (2025-12-25)

#### [OPT] Improvements
- [*] 点击外部区域会正确执行取消逻辑，恢复原始设置值，而不是保留调整后的预览效果。


### v1.10.12 (2025-12-25)

#### [OPT] Improvements
- [*] 实现"拖动滑块预览不保存，需要点击保存按钮才真正保存"的功能。


### v1.10.11 (2025-12-25)

#### [OPT] Improvements
- [*] 修复编辑视图：列表间距没用的bug


### v1.10.10 (2025-12-23)

#### [NEW] New Features
- [+] 在Live面板直观地调整标题的上下间距
- [+] 支持编辑模式调整下间距


### v1.10.9 (2025-12-23)

#### [OPT] Improvements
- [*]  Live Scene 预设不控制"UI 布局/功能开关"，只控制"视觉效果"相关的内容
- [*] 解除对hideRibbon（左侧功能区隐藏）的控制


### v1.10.8 (2025-12-23)

#### [NEW] New Features
- [+] 实现表前空行隐藏功能


### v1.10.7 (2025-12-23)

#### [OPT] Improvements
- [*] 文本行高功能优化，引入重玄的CSS方案(感谢)
- [*] 阅读模式和编辑模式行高完全一致


### v1.10.6 (2025-12-23)

#### [OPT] Improvements
- [*] 修复Time Scene不干预功能开关


### v1.10.5 (2025-12-17)

#### [OPT] Improvements
- [*] 信息更新


### v1.10.4 (2025-12-17)

#### [NEW] New Features
- [+] 成功实施 ViewTuner v3 精确间距控制方案，通过拆分 5 个独立滑块、动态 UI 显示、向后兼容迁移和 Maple 标记定位修复，在保证 CodeMirror 核心功能的前提下，提供了更清晰、更精确的间距调整体验。


### v1.10.3 (2025-12-17)

#### [OPT] Improvements
- [*] 行号显示正常
- [*] 文本点击都可以出现光标
- [*] 文本行高功能失效
- [*] 段落间距功能失效
- [*] 标题间距功能失效


### v1.10.2 (2025-12-12)

#### [OPT] Improvements
- [*] 优化lucide图标在文件夹立刻显示


### v1.10.1 (2025-12-11)

#### [NEW] New Features
- [+] 增加普通文本颜色自定义


### v1.10.0 (2025-12-11)

#### [NEW] New Features
- [+] 实现MD渲染颜色深浅双重设置


### v1.9.22 (2025-12-11)

#### [NEW] New Features
- [+] 支持"页内标题颜色"自定义
- [+] "页内标题颜色"融入预设方案


### v1.9.21 (2025-12-11)

#### [NEW] New Features
- [+] 深入贯彻落实强迫症的美学编号


### v1.9.20 (2025-12-11)

#### [OPT] Improvements
- [*] 优化刷新按钮
- [*] 优化滚动状态保持
- [*] 优化文字说明


### v1.9.19 (2025-12-11)

#### [NEW] New Features
- [+] 优化默认参数


### v1.9.18 (2025-12-10)

#### [NEW] New Features
- [+] 清空许可证验证缓存


### v1.9.17 (2025-12-10)

#### [OPT] Improvements
- [*] 稳定性增强


### v1.9.16 (2025-12-10)

#### [NEW] New Features
- [+] Live Scene移动端自适应宽度


### v1.9.15 (2025-12-10)

#### [OPT] Improvements
- [*]  Live Scene 按钮去除移动端限制


### v1.9.14 (2025-12-10)

#### [NEW] New Features
- [+] 支持移动端状态栏显示


### v1.9.13 (2025-12-10)

#### [OPT] Improvements
- [*] 验证后未保存状态
- [*] 关闭插件彩虹文件夹树未清理干净色彩


### v1.9.12 (2025-12-10)

#### [NEW] New Features
- [+] 更新稳定性


### v1.9.11 (2025-12-10)

#### [OPT] Improvements
- [*] 修复DEFAULT_SETTINGS的不完整导致无法运行


### v1.9.10 (2025-12-10)

#### [NEW] New Features
- [+] 深度合并 + 版本迁移 = 高级配置管理系统


### v1.9.9 (2025-12-10)

#### [NEW] New Features
- [+]  样式初始化顺序按模块分组
- [+]  主题重复初始化


### v1.9.8 (2025-12-10)

#### [OPT] Improvements
- [*] 修复了设置界面的5个Bug（滚动位置保持、导航状态保持、错误处理、直接查询）


### v1.9.7 (2025-12-10)

#### [NEW] New Features
- [+] 支持库外文件夹作为头图文件库
- [+] 支持解析库外文件作为头图

#### [OPT] Improvements
- [*] 优化日志提示信息


### v1.9.6 (2025-12-09)

#### [NEW] New Features
- [+] 全局按钮间距控制
- [+] 按钮隐藏管理


### v1.9.5 (2025-12-09)

#### [OPT] Improvements
- [*] 顺序优化


### v1.9.4 (2025-12-09)

#### [OPT] Improvements
- [*] 布局优化


### v1.9.3 (2025-12-09)

#### [NEW] New Features
- [+] Time Scene功能
- [+] 根据当前的实现自动切换适宜的场景
- [+] 根据当前场景启动obsidian选择适宜的场景


### v1.9.2 (2025-12-08)

#### [NEW] New Features
- [+] 主题按钮更换更稳定API
- [+] 联动官方明暗双向调整


### v1.9.1 (2025-12-07)

#### [NEW] New Features
- [+] 升级打包脚本机制


### v1.9.0 (2025-12-06)

#### [NEW] New Features
- [+] Live Scene灵动场景全新升级


### v1.8.39 (2025-12-06)

#### [NEW] New Features
- [+] live


### v1.8.38 (2025-12-06)

#### [OPT] Improvements
- [*] 修复图谱设置布局错乱


### v1.8.37 (2025-12-06)

#### [OPT] Improvements
- [*] 界面隐藏功能模块修复
- [*] 已修复Bug #1（核心逻辑错误）、Bug #2 & #3（性能优化）以及Bug #6（逻辑冗余），并跳过了ROI较低的Bug #4 & #5


### v1.8.36 (2025-12-06)

#### [NEW] New Features
- [+] 新增 '隐藏 ⇄ 默认' 循环模式及完善图标状态

#### [OPT] Improvements
- [*] 修复记忆填空模块Bug #1（自定义样式未清理导致的泄漏）


### v1.8.35 (2025-12-06)

#### [OPT] Improvements
- [*] 已修复Bug #4（安全删除配色方案，防止当前方案被删后状态错误）和Bug #2（统一表格样式应用逻辑）


### v1.8.34 (2025-12-06)

#### [OPT] Improvements
- [*] 修复了QuickDisplayAdjustModal的3个Bug（事件监听器清理 + rafId防御性清理 + style元素清理），实现完整的onClose()方法，解决了严重的内存泄漏和性能下降问题


### v1.8.33 (2025-12-06)

#### [OPT] Improvements
- [*] 修复了编辑器宽度控制的4个Bug（DOM引用清理 + 清理顺序注释 + 用户输入持久化 + Pro检查优化），解决了内存泄漏风险、数据丢失和用户体验问题。


### v1.8.32 (2025-12-06)

#### [OPT] Improvements
- [*] 修复了图标系统的4个Bug（2个严重内存/事件泄漏 + 1个性能优化 + 1个管理统一），解决了插件卸载资源残留和大文件夹库滚动卡顿问题


### v1.8.31 (2025-12-06)

#### [OPT] Improvements
- [*] 修复Banner模块
- [*] #1 cleanup方法 - 原本已存在完整实现
- [*] #2 缓存键优化 - 字符串拼接代替JSON
- [*] #3 blob URL智能释放 - 延迟5秒+使用检查
- [*] #4 保存失败恢复 - Position/Scale双重UI回滚
- [*] #5 定时器泄漏 - safetyTimeout已正确清理
- [*] #6 Banner重建 - 总是移除旧元素防泄漏
- [*] #7 触摸监听器 - cleanup中显式移除


### v1.8.30 (2025-12-06)

#### [OPT] Improvements
- [*] 优化纸张纹理管理模块
- [*] 重复代码行--消除冗余，提升可维护性
- [*] 统一styleEl注入方法--防止内存泄漏和ID冲突，提升稳定性
- [*] 滑块onChange立即保存--防止数据丢失，提升用户体验
- [*] 预设数量限制--防止配置文件无限增长


### v1.8.29 (2025-12-06)

#### [OPT] Improvements
- [*] 已修复授权模块3个Bug：**设备指纹localStorage持久化**（避免重启后重复注册）、**删除unbindDevice方法和CSS**（清理未使用代码）、**LicenseManager单例化+5分钟缓存**（性能优化）。


### v1.8.28 (2025-12-06)

#### [OPT] Improvements
- [*] 功能侧边栏隐藏
- [*] 增加移动端兼容性


### v1.8.27 (2025-12-06)

#### [OPT] Improvements
- [*] 支持移动端Pro运行逻辑


### v1.8.26 (2025-12-06)

#### [OPT] Improvements
- [*] 确保在任何"关闭"或"回退"场景下，inline code的自定义样式都会被正确移除，避免样式残留。


### v1.8.25 (2025-12-06)

#### [OPT] Improvements
- [*] 自定义代码块颜色融入MD颜色渲染


### v1.8.24 (2025-12-05)

#### [OPT] Improvements
- [*] 优化内联样式，使用CSS统一管理动态样式
- [*] CSS控制布局和定位，JS控制数据与交互
- [*] 编辑模式和阅读模式分别处理，精确适配不同容器结构


### v1.8.23 (2025-12-05)

#### [OPT] Improvements
- [*] 阅读视图头图标题间距优化;右侧空白优化


### v1.8.22 (2025-12-05)

#### [OPT] Improvements
- [*] 修复插件banner在阅读视图下无法正常显示的问题


### v1.8.21 (2025-12-05)

#### [NEW] New Features
- [+] 纸质纹理基础优化完成
- [+] 新标签页打开设置快捷方式


### v1.8.20 (2025-12-05)

#### [OPT] Improvements
- [*] 纸张纹理功能融入


### v1.8.19 (2025-12-03)

#### [OPT] Improvements
- [*] 优化头图默认设置为更友好的190


### v1.8.18 (2025-11-28)

#### [NEW] New Features
- [+] Pro布局优化完成
- [+] 性能调节完成


### v1.8.17 (2025-11-28)

#### [OPT] Improvements
- [*] test0605


### v1.8.16 (2025-11-28)

#### [OPT] Improvements
- [*] test0600


### v1.8.15 (2025-11-28)

#### [OPT] Improvements
- [*] test0553


### v1.8.14 (2025-11-28)

#### [OPT] Improvements
- [*] test0418


### v1.8.13 (2025-11-28)

#### [OPT] Improvements
- [*] test0413


### v1.8.12 (2025-11-28)

#### [NEW] New Features
- [+] test0403


### v1.8.11 (2025-11-28)

#### [OPT] Improvements
- [*] test


### v1.8.10 (2025-11-28)

#### [OPT] Improvements
- [*] test


### v1.8.9 (2025-11-28)

#### [NEW] New Features
- [+] pro机制完善


### v1.8.8 (2025-11-27)

#### [NEW] New Features
- [+] 插件Pro版精细升级调整


### v1.8.7 (2025-11-26)

#### [OPT] Improvements
- [*] 测试


### v1.8.6 (2025-11-26)

#### [OPT] Improvements
- [*] 保护测试


### v1.8.5 (2025-11-26)

#### [NEW] New Features
- [+] 测试文件完整性


### v1.8.4 (2025-11-26)

#### [NEW] New Features
- [+] 头图功能完善增强



### v1.8.3 (2025-11-26)

#### [NEW] New Features
- [+] ViewTuner标签页视图设置功能


### v1.8.2 (2025-11-26)

#### [OPT] Improvements
- [*] BUG版:修复图片上方一行点击无法出现光标


### v1.8.1 (2025-11-25)

#### [OPT] Improvements
- [*] 优化maple标题选择器过大


### v1.8.0 (2025-11-24)

#### [NEW] New Features
- [+] 文件夹引导线美化融入彩虹文件夹树
- [+] 彩虹文件夹引导线跟随彩虹颜色
- [+] 彩虹文件夹引导线也可独立颜色
- [+] 引导线可调节透明度

#### [OPT] Improvements
- [*] 解决状态栏优化的行高和右侧边距滑块移动无变化的问题


### v1.7.16 (2025-11-24)

#### [OPT] Improvements
- [*] 引导线无序列表与文件夹列表分离


### v1.7.15 (2025-11-24)

#### [NEW] New Features
- [+] 支持给obsidian引导线增加自定义颜色


### v1.7.14 (2025-11-24)

#### [OPT] Improvements
- [*] 修复记忆填空功能在显示答案模式下加粗丢失的问题


### v1.7.13 (2025-11-24)

#### [NEW] New Features
- [+] 编辑器宽度、深浅模式融入配置预设
- [+] 可跟随配置预设自由调整状态


### v1.7.12 (2025-11-24)

#### [OPT] Improvements
- [*] 完善显示调整的彩色文件夹树方案调用逻辑


### v1.7.11 (2025-11-24)

#### [OPT] Improvements
- [*] 修复彩虹文件树方案未跟随配置预设


### v1.7.10 (2025-11-23)

#### [NEW] New Features
- [+] 彩色文件夹增加12种预设另可自定义颜色


### v1.7.9 (2025-11-23)

#### [NEW] New Features
- [+] 彩色文件夹滚动稳定
- [+] 提供三种基础色


### v1.7.8 (2025-11-23)

#### [NEW] New Features
- [+] 优化二级文件夹图标展示


### v1.7.7 (2025-11-22)

#### [NEW] New Features
- [+] 文件夹和文件类型图标支持Lucide


### v1.7.6 (2025-11-22)

#### [NEW] New Features
- [+] 支持仅前二级文件夹显示文件夹图标


### v1.7.5 (2025-11-22)

#### [OPT] Improvements
- [*] 优化界面隐藏性能


### v1.7.4 (2025-11-22)

#### [NEW] New Features
- [+] 加入粗斜体颜色自定义配置


### v1.7.3 (2025-11-22)

#### [NEW] New Features
- [+] 头图编辑模式纯净版

### v1.7.1 (2025-11-22)

#### [OPT] Improvements
- [*] 头图性能优化，简便一体


### v1.7.0 (2025-11-21)

#### [NEW] New Features
- [+] 支持头图功能


### v1.6.5 (2025-11-21)

#### [NEW] New Features
- [+] "引用块边框颜色"选择器可自定义颜色


### v1.6.4 (2025-11-21)

#### [OPT] Improvements
- [*] 🐛 修复 11 个未管理的事件监听器，消除内存泄漏
- [*] ⚡ 显著提升性能，特别是鼠标移动时的响应速度
- [*] 🔧 改进滑块事件管理，确保完全清理
- [*] 🎯 优化状态栏按钮事件注册


### v1.6.3 (2025-11-21)

#### [OPT] Improvements
- [*] 内存管理
- [*] ✅ 完全消除定时器泄漏风险
- [*] ✅ 插件卸载时正确清理所有资源
- [*] ✅ 长时间使用不会出现内存累积
- [*] 数据管理
- [*] ✅ 限制 
- [*] data.json
- [*]  中状态记忆最多 100 个文件
- [*] ✅ 自动清理不存在文件的记录
- [*] ✅ 减少保存操作的数据量


### v1.6.2 (2025-11-14)

#### [OPT] Improvements
- [*] - [*] 修复标题和标题与表格之间空白区域无法点击定位光标的问题
- [*] - [*] 修复分割线导致上方文字无法点击定位光标的问题



### v1.6.1 (2025-11-13)

#### [NEW] New Features
- [+] 显示调整在状态栏按钮可显示隐藏
- [+] 删除写作模式在实用功能标签页描述，为集成入显示调整的配置预设做准备
- [+] 更新README.md说明文档

### v1.6.0 (2025-11-13)

#### [OPT] Improvements
- [*] 插件卸载资源清理修复


### v1.5.10 (2025-11-12)

#### [OPT] Improvements
- [*] DOM查询性能优化 - 实现查询缓存和防抖机制，减少重复查询
- [*] 事件监听器管理完善 - 统一管理所有事件监听器，确保正确清理


### v1.5.9 (2025-11-12)

#### [OPT] Improvements
- [*] 修复定时器内存泄漏问题


### v1.5.8 (2025-11-12)

#### [OPT] Improvements
- [*] 优化CSS样式重复注入问题


### v1.5.7 (2025-11-12)

#### [OPT] Improvements
- [*] 修复搜索界面图标显示Bug


### v1.5.7 (2025-11-12)

#### [FIX] Bug Fixes
- [-] BUG版本，勿用


### v1.5.6 (2025-11-11)

#### [NEW] New Features
- [+] 增加`标题间距`调整选项
- [+] 可调整各级标题与下方正文之间的间距


### v1.5.5 (2025-11-11)

#### [OPT] Improvements
- [*] ✅ 稳定性提高
- [*] ✅ 无内存泄漏风险
- [*] ✅ 性能优化到位
- [*] ✅ 资源清理完善
- [*] ✅ API 稳定可靠


### v1.5.4 (2025-11-11)

#### [NEW] New Features
- [+] 定时器管理-onload：保存所有初始化定时器到 this.initTimeouts 数组
- [+] 资源清理-onunload：添加完整的定时器清理逻辑
- [+] 防抖优化-handleLayoutChange：添加 200ms 防抖机制
- [+] API 版本管理-compareVersions：新增版本比较工具函数


### v1.5.3 (2025-11-11)

#### [OPT] Improvements
- [*]  修复applyImageAlignment() 被重复调用
- [*] 独立的 layout-change 事件监听器合并为一个统一的 handleLayoutChange() 方法


### v1.5.2 (2025-11-11)

#### [OPT] Improvements
- [*] 修复文件类型图标设置开关、文件夹图标开关切换后未刷新设置面板的问题
- [*] 继续提升导航栏按钮自动隐藏性能


### v1.5.1 (2025-11-11)

#### [OPT] Improvements
- [*] 解决Composer 标记样式在阅读模式下会跟标题内容黏在一起BUG


### v1.5.0 (2025-11-11)

#### [NEW] New Features
- [+] YMAL属性自动收起功能
- [+] YMAL属性自动收起状态保持功能(实验功能)


### v1.4.3 (2025-11-09)

#### [NEW] New Features
- [+] README.MD文档更新


### v1.4.2 (2025-11-09)

#### [OPT] Improvements
- [*] 兼容性增强


### v1.4.1 (2025-11-09)

#### [OPT] Improvements
- [*] 修复稳定性


### v1.4.0 (2025-11-08)

#### [NEW] New Features
- [+] 新功能，来自 Composer 主题
- [+] 1. MD 表格美化 - 边框样式新增 `学术三线表`
- [+] 2. 界面图标隐藏下新增 `导航栏自动隐藏`
- [+] 3. 文件列表美化新增 `彩虹文件树`


### v1.3.1 (2025-11-08)

#### [NEW] New Features
- [+] 集成 Composer 主题的`竖杠`标题标记样式
- [+] 针对 Composer 主题的`竖杠`标题标记颜色做出自定义颜色、跟随主题色、彩色适配viewtuner插件增强


### v1.3.0 (2025-11-08)

#### [NEW] New Features
- [+] 优化完成界面隐藏功能


### v1.2.11 (2025-11-08)

#### [NEW] New Features
- [+] "界面图标隐藏"添加 Baseline 风格的自动折叠功能


### v1.2.10 (2025-11-08)

#### [OPT] Improvements
- [*] 隐藏图标后显示圆点可点击


### v1.2.9 (2025-11-08)

#### [OPT] Improvements
- [*] 优化隐藏图标避免快捷键冲突，shift+左键恢复显示


### v1.2.8 (2025-11-07)

#### [NEW] New Features
- [+] 界面图标隐藏功能支持


### v1.2.7 (2025-11-05)

#### [OPT] Improvements
- [*] 修复Bug:【显示调整重置按钮】点击按钮不改变当前预设，只重置参数值


### v1.2.6 (2025-11-03)

#### [NEW] New Features
- [+] 打通配色方案到 `显示调整` 小窗口
- [+] 增加【配置预设-关闭配置】选项及其功能

#### [OPT] Improvements
- [*] 优化MD渲染高级美化选项命名


### v1.2.5 (2025-11-03)

#### [OPT] Improvements
- [*] 1. 边框圆角显示优化
- [*] 2. 主题切换按钮、页首图标按钮、宽度滑块开关按钮修改开关打开逻辑更符合直觉


### v1.2.4 (2025-11-02)

#### [NEW] New Features
- [+] 打包脚本升级


### v1.2.3 (2025-11-02)

#### [OPT] Improvements
- [*] 优化当前打包脚本的版本命名逻辑


### v1.2.2 (2025-11-02)

#### [OPT] Improvements
- [*] 优化打包脚本


### v1.2.1 (2025-11-01)

#### [FIX] Bug Fixes
- [-] 修复readme.md文档错误被更新打包脚本替换为其他内容


### v1.1.2 (2025-10-30)

#### ✨ 新增
- ✅ 优化性能


### v1.1.1 (2025-10-30)

#### 🔧 优化
- ⚡ 更新测试


### v1.1.0 (2025-10-30)

#### ✨ 新增
- ✅ 重置README.md文档
- ✅ 优化工作流配置


### v1.0.2 (2025-10-30)

#### ✨ 新增
- ✅ 毛玻璃效果智能排除：显示调整模态框自动排除毛玻璃，确保实时预览清晰
- ✅ 标题居中功能优化：将"重置为默认"改为"一键全开"，更符合用户习惯
- ✅ 默认配置优化：使用开发者精心调优的理想配置作为默认值

#### 🔧 优化
- ⚡ CSS选择器优化：使用 `:has()` 选择器提升毛玻璃排除的精准度
- 🎨 代码注释优化：为关键配置项添加详细注释

#### 🐛 修复
- 🔧 修复显示调整模态框宽度设置丢失的问题
- 🔧 修复重复代码导致的潜在问题

### v1.0.1 (2025-10-28)

#### ✨ 新增
- ✨ 完整的Lucide图标库 (1,640个图标)
- ✨ 记忆填空功能
- ✨ 9种专业写作模式
- ✨ 显示调整快捷面板

#### 🔧 优化
- ⚡ 性能优化，加载速度提升30%
- 🎨 界面优化，更流畅的动画效果
- 📱 移动端适配优化

#### 🐛 修复
- 🐛 修复表格样式在某些主题下的显示问题
- 🐛 修复宽度控制在移动端的兼容性
- 🐛 修复JSON文件BOM编码导致的插件识别问题

### v1.0.0 (2025-10-25)

- 🎉 首次发布
- 🎨 集成20+功能模块
- 📱 全平台支持

---




### 📥 获取 ViewTuner
*添加微信 `Lyon1893` 备注"获取正式版ViewTuner"*  

---

## 💡 为什么开发 ViewTuner？

**从刚需出发的诞生故事：**

我一直懒得折腾obsidian美化与各种主题——直到开发`插件大哥`TreeBuilder遇到了一些问题：
因TreeBuilder测试需要，我需要频繁在明亮和深色模式下进行切换

所以一口气调试出来当前的`插件小弟`——ViewTuner视觉调音师V0.0.1
![ViewTuner视觉调音师明暗切换功能演示](https://img.cdn1.vip/i/6903188398d8f_1761810563.webp)

接着，我想到从论坛学到的一段CSS代码。虽然只有三行，但对于认为默认编辑器宽度太窄的我来说，无疑是刚需。
![编辑器宽度调节CSS代码](https://img.cdn1.vip/i/69031925c10db_1761810725.webp)
然而随着使用场景增多，每次想调整理想宽度都要打开CSS文件，体验太"刚"了。`下图为默认编辑器缺点`
![默认编辑器缺点](https://img.cdn1.vip/i/6903197b6b02c_1761810811.webp)
于是我想到——**正好让动态调整需求与 ViewTuner 来个合体！** 🎯
![编辑器宽度调节演示](https://img.cdn1.vip/i/69031a677cc9d_1761811047.webp)
这个时候，我开始意识到：  
> **对于 Obsidian 而言，一个舒适的编辑体验是一切的前提，亦是美化之路提高体验的第一步。**

于是，这个起初不起眼的小插件💪成长为现在集成 **31+ 功能模块**、**150+ 功能自定义** 的全能&自由美化插件。

---

## 🎯 核心优势

### 🚀 开箱即用
- ✅ **零配置启用** - 安装即用，默认配置已调优
- ✅ **无需代码** - 图形界面配置所有功能
- ✅ **实时预览** - 所有调整立即生效

### 🎨 全方位美化
- ✅ **基础美化** - 9大基础美化模块
- ✅ **MD渲染增强** - 8大Markdown渲染优化
- ✅ **实用功能** - 6大效率工具（含Live Scene 8个子功能）

### 🔧 灵活定制
- ✅ **5种预设配色** + 自定义方案
- ✅ **9种写作模式** 适配不同场景
- ✅ **1,640个Lucide图标** 供全局使用

### 📱 全平台兼容
- ✅ Windows / Mac / Linux
- ✅ Android / iOS
- ✅ 完美兼容绝大多数 Obsidian 主题

### 🎬 Live Scene 灵动场景（独家）
- ✅ **一键场景切换** - 工作、阅读、写作模式瞬间切换
- ✅ **智能时间适配** - 早中晚自动调整显示效果
- ✅ **综合调优** - 同时调整亮度、字体、行高、色彩、版式

---

## ✨ 功能特性

### 🎨 基础美化（8项）

| 功能 | 说明 | 亮点 |
|------|------|------|
| 🖱️ **滚动条美化** | 自定义滚动条样式和交互效果 | 自动隐藏/悬浮显示 |
| ✨ **毛玻璃效果** | 为界面元素添加现代化毛玻璃背景 | 可调节模糊/透明度 |
| 🖼️ **图片美化** | 图片圆角美化，使其更柔和 | 柔和圆角 |
| 📏 **间距控制** | 调整全局按钮间距、状态栏行高和间距 | 紧凑布局/自定义间距 |
| 💻 **代码行号** | 为代码块添加行号显示 | 智能显示行号 |
| 🔗 **链接图标美化** | 为内部链接和外部链接添加图标 | 区分链接类型 |
| 🎯 **界面隐藏** | 左侧边栏按钮隐藏/状态栏显示隐藏/侧边栏隐藏/导航栏自动隐藏/YAML属性自动收起/文件库区域移动侧边栏 | Baseline风格自动折叠/状态记忆 |
| 📁 **文件列表美化** | 自由为文件类型和💎文件夹自定义设置emoji/lucide图标 | 💎自定义图标/12种彩虹配色 |


### 📄 MD渲染高级美化（8项）

| 功能 | 说明 | 亮点 |
|------|------|------|
| 🎨 **MD颜色渲染** | 提供多套精美标题、链接、文本颜色预设方案 | 5种预设 + 💎自定义 |
| 📐 **MD标题居中配置** | 为页内标题、H1-H6标题提供居中显示控制 | 逐级控制/一键全开 |
| 🏷️ **MD标题等级标记** | 在编辑模式显示H1-H6标题标记 | Maple/Blue Topaz/Composer风格 |
| 📏 **MD标题下划线** | 为标题#添加底部下划线装饰 | 实线/虚线/点线可选 |
| 📝 **MD无序列表美化** | 为无序列表-添加美观符号和引导线 | 彩色符号/引导线 |
| ➖ **MD分隔行美化** | 为分隔线---添加渐变效果和装饰图标 | 6种分隔线样式 |
| 📊 **MD表格美化配置** | 全宽表格、行号、斑马纹、边框等 | 学术三线表/斑马纹/悬浮高亮 |
| 📈 **Dataview表格美化配置** | 美化dataview插件的表格样式 | 与原生表格统一风格 |

### 🔧 实用功能（6项）

| 功能 | 说明 | 亮点 |
|------|------|------|
| 🎬 **Live Scene 灵动场景** | 💎一键切换场景配置，综合调整亮度、字体、行高、色彩、版式风格等显示参数 | 实时预览/预设管理/一键重置 |
| ├─ 显示调整 | Live Scene快捷面板 | 亮度/行高/段距/标题间距/字体大小 |
| ├─ 版式风格 | 9种专业版式风格 | 公文/护眼/缩进/焦点/卡片... |
| ├─ 深浅切换 | 快速切换明暗主题 | 状态栏一键切换 |
| ├─ 编辑器宽度控制 | 动态调整编辑器阅读宽度 | 滑块实时调整/4个预设 |
| ├─ 纸张纹理 | 为编辑器添加纸张质感背景 | 多种纹理预设/自定义 |
| ├─ Time Scene时间场景 | 根据时间自动切换场景预设 | 定时切换/实时监测 |
| ├─ ViewTuner设置视图 | 新标签页打开设置 | 快捷方式 |
| ├─ 移动端状态栏 | 移动端状态栏显示支持 | 移动端适配 |
| 🖼️ **头图调色师_Banner Colorist** | 💎在笔记顶部显示横幅图片，让你的笔记更加美观 | 拖拽调整/缩放控制 |
| 🧠 **记忆填空师_MemoryCloze Master** | 💎生成挖空题样式辅助记忆 | `==答案==` 语法/悬浮显示 |
| 🧰 **图片谐调师_Image Harmonizer** | 💎图片工具集：图片注释、对齐、大小控制、查看器、粘贴命名 | 图片工具集 |
| 🎨 **图标搬运师_Iucide Curator** | 1,640个精美矢量图标库，供所有插件使用 | 全局API/供所有插件使用 |
| 📦 **标注构建师_Callout Builder** | 💎快速创建和管理Obsidian标注块（Callout），支持自定义样式和图标 | 可视化编辑/样式预设/图标选择 |

---

## 获取 ViewTuner

### 📥 获取方式

**添加微信获取正式版：**
- 微信号：`Lyon1893`
- 备注：**获取正式版ViewTuner**
- 获取专属知识库&安装包

### 🔥 版本定价

**💡 关于定价**  

我知道你和我一样在美化上走过许多弯路----VT一个满足99%基础美化需求的插件， 希望能帮到你!

如果你没有很强的自定义需求，免费版已经够了，如果你需要进一步美化，推荐你购买专业版

> **💡 专业版价格**

| 版本 | 售价 | 适用范围 | 核心权益 |
|------|------|----------|----------|
| **ViewTuner Free** | ¥0 / $0 | 个人使用 | 基础美化功能 |
| 1️⃣ **ViewTuner Pro** | ¥68 / $10 | 个人永久使用（99台设备） | 完整功能 + 首年免费更新 + 专属群聊 + 教程文档 + 首年答疑 |
| 2️⃣ **ViewTuner ProMax** | ¥98 / $20 | 家庭永久使用（999台设备） | Pro全部功能 + 永久免费更新 + 永久答疑 + 私聊反馈 |
| 🔓 **无限制版（源码）** | ¥368 / $100 | 个人使用 + 可申请部分功能商业授权 | DIY全部功能 + 开发路径指导30min |

**版本说明：**
- **Free版**：提供80%基础美化功能，覆盖日常使用场景
- **Pro版**：【主打推荐】完整功能，含高级自定义选项、美化工具、一键配置、交流社群等
- **ProMax版**：【长期使用】Pro全部功能 + 永久维护更新，与作者沟通更方便
- **无限制版**：适合有开发能力的用户，可自定义修改源码

### 📧 购买方式

**微信购买**：
- 添加微信：`Lyon1893`
- 备注：**获取正式版ViewTuner**
- 说明需要的版本（Pro / ProMax / 无限制版）

### ✅ 购买后享受

- 🎯 **永久授权** - 一次购买，终身使用，无设备数量限制（实际限制见版本说明）
- 🔄 **免费更新** - Pro首年免费更新，ProMax永久免费更新（除非插件停止开发）
- 🎁 **新功能优先** - 优先体验新功能
- 💬 **专属社群** - 加入专属交流群，与其他用户交流经验
- 📚 **完整教程** - 获取详细使用教程和配置文档
- 🛠️ **答疑支持** - Pro首年答疑链接反馈，ProMax永久答疑 + 私聊反馈

### ⚖️ 使用声明

- Pro版限个人使用，ProMax版限家庭使用
- 未经授权对外传播，作者保留追究法律责任的权利
- 购买即表示同意以上使用条款

---

## 📦 安装方法

### 手动安装

1. **📥 获取安装包**
   
   添加微信：`Lyon1893`
   备注：**获取正式版ViewTuner**
   
   获取最新版本的安装包和相关权益

2. **🔑 获取专属知识库密码**
   
   进入专属知识库，下载插件

3. **📦 解压到插件目录**
   ```
   你的库/.obsidian/plugins/
   ```

4. **🔄 重启 Obsidian**
   - 完全关闭 Obsidian（包括系统托盘）
   - 重新打开

5. **✅ 启用插件**
   - 设置 → 第三方插件 → 启用 ViewTuner

---

## 🐛 故障排除

### 插件无法加载

**症状**：插件列表中显示，但无法启用

**解决方案**：
1. 检查文件完整性：
   - ✅ `main.js` 是否存在
   - ✅ `manifest.json` 是否存在
   - ✅ 文件是否二次修改（main.js无法二次修改）

2. 查看控制台错误&重启 Obsidian：
   - 按 `Ctrl+Shift+I` 打开开发者工具
   - 查看 Console 面板的错误信息
   - 完全关闭 Obsidian（包括系统托盘）
   - 重新打开

3. 如果上面办法不能解决
   - 录制BUG视频或截图(越详细越好)
   - 反馈给Lyon

### 功能不生效

**症状**：开启某个功能后，没有看到效果

**解决方案**：
1. **检查总开关**：
   - 某些功能有"总开关"和"子开关"
   - 例如：标题居中需要先开启"启用【MD标题居中】功能"，再开启各级标题

2. **检查插件冲突**：
   - 尝试禁用其他美化类插件
   - 逐个启用以排查冲突

3. **重载插件**：
   - 按 `Ctrl+R` 重载
   - 或在设置中禁用再启用


### 样式错乱

**症状**：界面出现异常样式

**解决方案**：
1. **切换主题测试**：
   - 尝试切换到官方主题
   - 检查是否是主题兼容性问题

2. **检查自定义CSS**：
   - 临时禁用自定义CSS片段
   - 排查是否有CSS冲突

3. **重置插件设置**：
   - 在设置面板点击"重置为默认"
   - 或删除 `data.json` 重新启动

### 性能问题

**症状**：Obsidian 变卡顿

**解决方案**：
1. **关闭高耗性能功能**：
   - 液态玻璃效果（如果设备性能较弱）
   - 复杂的表格样式

2. **减少图标数量**：
   - 文件图标功能仅对常用文件类型启用

3. **优化显示设置**：
   - 降低动画效果

---

## 📜 开源致谢与许可声明

ViewTuner 在开发过程中集成了部分优秀开源主题的代码和设计理念，我们尊重并遵守这些开源项目的许可证。

> **声明**：ViewTuner 已尽力审核并标注所有使用的开源代码来源。若您发现有遗漏或不当之处，请联系 Lyon（微信：Lyon1893），我们将立即补充致谢或移除相关内容。感谢您的支持与理解。

以下是相关项目的许可信息：

---

### Lucide Icons

ViewTuner 集成了 [Lucide Icons](https://github.com/lucide-icons/lucide) 图标库 v0.548.0：
- 提供了 1640+ 个高质量图标供插件使用

**许可证信息：**
```
ISC License

Copyright (c) Lucide Contributors

Permission to use, copy, modify, and/or distribute this software for any purpose
with or without fee is hereby granted, provided that the above copyright notice
and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
```
**致谢：** 感谢 [Lucide Icons](https://lucide.dev) 项目为开源社区提供的优质图标库。

---

### Baseline 主题

ViewTuner 集成了 [Baseline 主题](https://github.com/colineckert/obsidian-baseline) 的部分功能：
- 自动折叠的界面图标隐藏

**许可证信息：**
```
MIT License

Copyright (c) 2022 Colin Eckert

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
**致谢：** 感谢 [colineckert](https://github.com/colineckert) 开发的 Baseline 主题。

---

### Blue Topaz 主题

ViewTuner 借鉴了 [Blue Topaz 主题](https://github.com/whyt-byte/Blue-Topaz_Obsidian-css) 的部分功能与样式：
- H1-H6 标题标记、下划线、代码行号、图片对齐等美化

**许可证信息：**
```
MIT License

Copyright (c) 2021 whyt-byte

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
**致谢：** 感谢 [whyt-byte](https://github.com/whyt-byte) 开发的 Blue Topaz 主题。

---

### Maple 主题

ViewTuner 参考了 [Maple 主题](https://github.com/subframe7536/obsidian-theme-maple) 的美化样式：
- H1-H6 标题标记、动画效果等

**许可证信息：**
```
MIT License

Copyright (c) 2021 subframe7536

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
**致谢：** 感谢 [subframe7536](https://github.com/subframe7536) 开发的 Maple 主题。

---

### Composer 主题

ViewTuner 集成了 [Composer 主题](https://github.com/vran-dev/obsidian-composer) 的以下功能：
- 🎼 Composer 风格的标题标记样式（简约竖杠）
- 🌈 彩虹文件树（Rainbow Tree）
- 📚 学术三线表样式
- 🧭 导航栏按钮自动隐藏效果
- 🖼️ 图片圆角效果

**许可证信息：**
```
MIT License

Copyright (c) 2025 vran

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
**致谢：** 感谢 [vran](https://github.com/vran-dev) 开发的 Composer 主题，为 Obsidian 社区提供了优秀的设计理念和代码实现。

---

### PKMer 社区 CSS 片段

ViewTuner 集成了 [PKMer 社区](https://pkmer.cn) 分享的光标行美化 CSS 片段：
- 当前行高亮、行号高亮竖线、当前行下划线、当前行阴影等样式
- 在原基础上小幅度优化以适配ViewTuner整体美化逻辑

**来源信息：**
- 网站：https://pkmer.cn
- 文章：[Obsidian 样式：编辑模式下当前行高亮](https://pkmer.cn/Pkmer-Docs/10-obsidian/obsidian%E5%A4%96%E8%A7%82/css-%E7%89%87%E6%AE%B5/obsidian%E6%A0%B7%E5%BC%8F-%E7%BC%96%E8%BE%91%E6%A8%A1%E5%BC%8F%E4%B8%8B%E5%BD%93%E5%89%8D%E8%A1%8C%E9%AB%98%E4%BA%AE/)

**致谢：** 感谢 PKMer 社区 & ViewTuner用户 `千钰丷` 的相关链接分享。

---

### Animated Cursor 插件

ViewTuner 集成了 [Animated Cursor](https://github.com/likemuuxi/animated-cursor) 插件的光标动画功能：
- 光标平滑移动动画、闪烁动画、彗星拖尾效果等

**许可证信息：**
```
MIT License

Copyright (c) 2025 Kotaindah55 (Sheva ihza)

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
**致谢：** 感谢 [Kotaindah55 (Sheva Ihza)](https://github.com/Kotaindah55) 和 [likemuuxi (Muuxi)](https://github.com/likemuuxi) 开发的 Animated Cursor 插件。

---

## 📞 支持与反馈

### 💬 联系方式

- **微信**：`_Helloworld2025`
- **哔哩哔哩**：[https://b23.tv/jy2QmcH](https://b23.tv/jy2QmcH)

### 🤝 问题反馈

欢迎反馈问题和建议！

**反馈时请提供：**
- 🔢 插件版本号
- 💻 操作系统（Windows/Mac/Linux/Android/iOS）
- 📋 Obsidian 版本
- 📝 详细问题描述
- 📸 截图或录屏（如有）

---

## 🎁 请我喝咖啡

如果 ViewTuner 帮到了你，欢迎请我喝杯咖啡 ☕

![微信赞赏码](https://youke1.picui.cn/s1/2025/10/30/690323886d3d4.png)

你的支持是我持续更新的动力！🚀

---

## 📄 ViewTuner 许可证

**ViewTuner 专有软件许可协议**

Copyright (c) 2025 Lyon. All rights reserved.

### 📋 许可模式

ViewTuner 采用 **Freemium（免费增值）** 商业模式：
- **免费版**：提供基础功能，个人非商业使用
- **付费版**（Pro/ProMax）：提供完整功能和技术支持

**重要说明**：
- ViewTuner 本身为专有软件，采用商业许可模式
- ViewTuner 集成的开源组件仍遵循其原有的开源许可证（详见"开源致谢与许可声明"部分）
- 本许可协议适用于 ViewTuner 的原创部分

### ⚖️ 使用条款

#### ✅ 你可以：
- 个人非商业使用（免费版无需授权，付费版需购买授权）
- 在自己的设备上安装和使用（付费版）
- 享受所有功能和后续更新（根据购买版本）

#### ❌ 你不可以：
- 未经授权复制、分发、分享、泄露激活码给他人
- 未经授权复制、分发、分享、泄露源码给他人
- 反向工程、反编译、修改源代码
- 用于商业目的（需单独商业授权）
- 移除或修改版权声明

### 💰 授权方式
> 前500老粉优惠价
1. **免费版**：¥0 - 基础功能，个人使用
2. **Pro版**：¥38（老粉价）/ ¥68（正式价）- 完整功能 + 首年更新 + 答疑
3. **ProMax版**：¥68（老粉价）/ ¥98（正式价）- Pro全部功能 + 永久更新 + 永久答疑
4. **无限制版**：¥368 - 源码访问 + DIY功能
5. **商业授权**：请联系作者洽谈

### 📧 购买授权

- **微信**：`Lyon1893`
- **哔哩哔哩**：[https://b23.tv/jy2QmcH](https://b23.tv/jy2QmcH)

### ⚠️ 免责声明

本软件按"原样"提供，不提供任何明示或暗示的保证。作者不对使用本软件造成的任何损失承担责任。

### 🔒 版权保护

未经授权的分发、破解、盗版行为将被视为侵权，作者保留追究法律责任的权利。

---

## 🙏 致谢

### 特别感谢

感谢所有使用和支持 ViewTuner 的用户！

**Friends支持：**
- **重玄** - status-width-slider插件优化灵感、脚注行高同步CSS方案、滚动条优先级优化建议、Maple主题标题标记样式建议等
- **光头特工** - 首行缩进"先缩进，再排除"的优秀CSS设计思路等
- **小熊拍肚肚🐻** - 粗斜体颜色自定义建议、UI混乱问题反馈等
- **一叶知秋** - 悬浮状态栏CSS实现建议
- **整点火火薯条** - 授权沟通信息截图插入到VT宣传视频，作为引出更新及时的引子
- **CTC** - ViewTuner的开发与维护

**技术支持：**
- [Obsidian](https://obsidian.md) 团队 - 提供优秀的平台
- [Lucide Icons](https://lucide.dev) - 提供精美的图标库
- Obsidian 社区 - 提供丰富的灵感和反馈

### 我的其他项目

- [🌳 **TreeBuilder** - 立体知识树构建师]（https://xcn807ss52h7.feishu.cn/wiki/SkK1wKFaIiVgRTke4HocMzOinSc）

---

<div align="center">

**让你的 Obsidian 更美观、更高效！** ✨

*Made with ❤️ by Lyon*

[@Light Your Obsidian Network](https://b23.tv/jy2QmcH)

</div>

