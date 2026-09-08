# Ziyi Ye 的学术主页

纯 HTML + CSS 静态主页，参考 [Jianlan Luo 的主页](https://jianlanluo.github.io/) 的简洁学术风格。无 Jekyll、Ruby、Bundler 或 npm 依赖。内容直接写在 `index.html`，浏览器关闭 JavaScript 也能完整阅读并滚动浏览历史新闻。

## 本地预览与调试

需要 Python 3，无需安装第三方包：

```bash
bash run_server.sh
```

打开 http://127.0.0.1:4000 。修改 HTML、CSS 或图片后自动刷新；浏览器开发者工具可直接调试布局、移动端和资源请求。按 Ctrl+C 停止。端口占用时运行 `bash run_server.sh --port 4001`。

也可以直接双击 `index.html` 打开（图片和样式使用相对路径），或使用 `python3 -m http.server 4000 --bind 127.0.0.1`，这两种方式需要手动刷新。自动刷新脚本只由开发服务器注入，不进入线上 HTML。

## 修改内容

| 文件 | 用途 |
| --- | --- |
| `index.html` | 姓名、联系方式、简介、新闻、论文、经历、教学等全部内容 |
| `assets/css/academic.css` | 版式、字体、颜色及移动端样式 |
| `images/` | 头像和论文图片 |
| `files/` | PDF、视频等文件 |
| `about.html`、`about/index.html` | 保留旧 `/about.html`、`/about/` 地址的跳转 |
| `CNAME` | 生产域名 `ziyiye.cn` |

详细示例见 [HTML 内容编辑指南](docs/editing.md)。

新增论文时复制一个 `<article class="publication">`，修改图片、标题、链接、作者、会议和简介。新闻直接编辑 `<ul class="news-list">`，所有新闻放在高度最多 320px 的滚动区域内；可在 CSS 的 `.news-scroll` 中调整高度。

图片、GIF、HTML5 视频、PDF 链接和新闻滚动均可直接由 HTML 实现。首页当前不展示动态引用数，已移除未使用的 Scholar 抓取脚本及其定时任务。

## 打包与部署

纯静态页面无需编译。可选地运行：

```bash
bash build.sh
```

该命令重新生成 `_site/`，只复制网页和资源，不包含开发脚本和旧模板资产。不要手动编辑或提交 `_site/`。

GitHub Pages 可沿用「Deploy from a branch」并选择发布分支的根目录；根目录的 `.nojekyll` 禁用 Jekyll 处理。若改用 GitHub Actions 部署，可上传 `_site/` 为 Pages artifact。`CNAME` 保留自定义域名。

改版在 `redesign/academic-homepage` 分支完成；GitHub Pages 从 `master` 分支根目录发布。以后可新建分支修改，先检查本地预览，再合并到 `master` 并推送上线。

Jekyll 模板、Markdown 首页和 Gemfile 已移除，原文件可从 `master` 分支或 Git 历史找回。已清理旧字体、JavaScript 插件、旧样式、模板文档、缓存和原作者赞助配置。论文图片和 PDF/视频附件保留原路径，避免破坏旧链接。

## 致谢

原项目基于 [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io)，保留其 LICENSE；原模板包含 Minimal Mistakes、AcademicPages 和 Font Awesome 的相关成果。
