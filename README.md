# 辽河能碳管理系统（PWA 版）

> 沈阳市辽河特种玻璃厂 —— 工业企业能碳核算、监测、分析与报告管理平台
> 版本：11.0（PWA） | 支持安装为桌面/手机应用，支持离线缓存

## 项目简介

面向工业企业的能源与碳排放一体化管理工具，覆盖 **能源消费核算 → 碳排放计算 → 能效对标 → 碳资产管理 → 报告生成** 全流程，内置 **24 个功能模块**（含 6 个智能模块：智能预警、策略推荐、减排方案模拟器、能耗与碳排放预测、重点用能设备管理、碳配额管理）。

## 功能模块

- **数据采集与核算**：实时采集（用电/光伏）、月度数据输入、参数对照表（折标系数/碳排放因子）
- **核心指标看板**：首页大屏（综合能耗、碳排放总量、绿电减排、产品产量、单位强度指标）
- **碳排放核算**：化石燃料燃烧排放、电力排放、绿电减排贡献
- **能效管理**：能耗查询、能源消费分析、能效对标、能流分析、能效平衡与优化
- **碳管理**：碳排放管理、供应链碳管理、产品碳足迹（ISO 14067 / GB/T 24067）、碳核查支撑、碳资产管理
- **智能模块**：智能预警（月环比波动检测）、策略推荐、减排模拟器、能耗预测（线性回归）、设备能耗台账、碳配额管理
- **报告生成**：碳足迹报告、能源利用状况报告、温室气体排放报告（PDF/Excel/ZIP 导出）

## 技术栈

| 项目 | 说明 |
| --- | --- |
| 前端 | 原生 HTML + JavaScript（无构建工具） |
| 样式 | Tailwind CSS（CDN） |
| 图表 | Chart.js（Canvas 渲染） |
| PDF 导出 | html2pdf.js |
| PWA | manifest.json + Service Worker（离线缓存 + 安装支持） |

## 数据说明

- 内置**模拟演示数据**（未连接真实能源采集系统时使用）
- 用户输入的数据保存在**浏览器本地**（localStorage），换设备/换浏览器不互通
- 对接真实数据需后端 API 或能源采集系统接口（见「数据输入」模块使用说明）

## 部署到 GitHub Pages

1. 在 GitHub 新建仓库（Public 或 Private 均可），仓库名如 `liaohe-energy-carbon`
2. 将本目录下所有文件上传到仓库根目录（**必须包含 `index.html`、`manifest.json`、`sw.js`、`icons/`**）
3. 仓库 Settings → Pages → Build and deployment → Source 选择 `Deploy from a branch` → 分支 `main` / 根目录 `/(root)` → Save
4. 等待 1-2 分钟，访问 `https://<你的用户名>.github.io/<仓库名>/` 即可
5. 浏览器打开后，地址栏或菜单出现「安装应用」图标，可安装为桌面 PWA

## 本地运行

直接用浏览器打开 `index.html` 即可（数据为模拟模式）。PWA 的 Service Worker 在 `file://` 协议下不会注册，安装/离线功能需通过 HTTPS 访问（GitHub Pages 天然支持）。

## 目录结构

```
├── index.html                  # 页面入口（GitHub Pages / PWA）
├── manifest.json                # PWA 清单（应用名称、图标、主题色）
├── sw.js                        # Service Worker（缓存与离线）
├── icons/                       # 应用图标（192/512 + maskable）
│   ├── icon-192.png
│   ├── icon-512.png
│   ├── icon-maskable-192.png
│   └── icon-maskable-512.png
└── scripts/
    └── gen_icons.py             # 图标生成脚本（Pillow）
```
