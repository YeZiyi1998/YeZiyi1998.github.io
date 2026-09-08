# HTML 内容编辑指南

日常主要改两个文件：`index.html` 管内容，`assets/css/academic.css` 管样式。图片放 `images/`，PDF 和视频放 `files/`。不要修改 `_site/`，它是打包输出，下次打包会被覆盖。

## 1. 打开预览

在仓库目录运行：

```bash
bash run_server.sh
```

浏览器打开 http://127.0.0.1:4000 。如果已有预览服务在运行，直接打开即可。用编辑器打开根目录 `index.html`，修改并保存，预览会自动刷新。

搜索下面这些词就能定位内容：

| 要修改的内容 | 在 index.html 中搜索 |
| --- | --- |
| 姓名、头像、邮箱 | `个人信息` 或 `class="profile"` |
| 个人介绍、招生信息 | `I am an Assistant Professor` 或 `recruitment` |
| 新闻 | `id="news"` |
| 研究方向 | `id="research"` |
| 论文 | `id="selected-publications"` |
| 工作和教育经历 | `id="experience"` |
| 服务、荣誉、教学 | `id="academic-service"`、`id="honors-and-awards"`、`id="teaching-experience"` |
| 数据集 | `id="datasets"` |

HTML 里的 `<!-- 中文说明 -->` 是编辑提示，不会显示在网页上。

顶部导航在 `class="section-nav"` 内。增加入口时添加 `<a href="#区域id">标签文字</a>`，对应区域需有相同的 `id`；例如 `href="#news"` 对应 `id="news"`。手机端可左右滑动导航。

## 2. 修改文字和链接

```html
<p>这是一个段落，<strong>这部分加粗</strong>。</p>
<a href="https://example.com/">点击后显示的链接文字</a>
<a href="mailto:zyye@fudan.edu.cn">zyye@fudan.edu.cn</a>
```

文字放在开始和结束标签之间。`href` 是点击后去往的地址，`src` 是图片或视频的地址。修改邮箱时，同时修改 `mailto:` 后面的地址和显示文字。

保留现有的 `class` 和 `id`，它们控制样式和页面内跳转。HTML 中不能直接使用 Markdown 的 `**加粗**` 或 `[链接](地址)`。

## 3. 添加一条 News

找到 `<ul class="news-list">`，在它下一行插入一条 `<li>`，新消息放最上方：

```html
<li>2026.09, our paper <b>Your Paper Title</b> is accepted by Conference Name.
  <a href="https://example.com/paper">Paper</a>
</li>
```

删除一条新闻时，删除对应的完整 `<li>…</li>`。所有新闻都放在同一个列表里，外层滚动框会自动处理高度，不用计算显示条数。

修改 News 区域高度：在 `assets/css/academic.css` 搜索 `.news-scroll`，将 `max-height: 320px` 改为你希望的高度，如 `400px`。

## 4. 添加一篇论文

先把论文图片放到 `images/`，例如 `my-paper-2026.png`。找到 `<div class="publications">`，在它下方复制以下结构，并替换示例内容：

```html
<article class="publication">
  <a class="publication-image" href="https://example.com/project"
     aria-label="Your Paper Title">
    <img src="images/my-paper-2026.png"
         alt="Overview of Your Paper Title"
         loading="lazy" width="1600" height="800">
  </a>
  <div>
    <h3><a href="https://example.com/project">Your Paper Title</a></h3>
    <p class="authors">First Author, <strong>Ziyi Ye</strong>, Last Author</p>
    <p class="venue">Conference 2026</p>
    <p class="paper-description">A short description of the work.</p>
  </div>
</article>
```

示例的 `width` 和 `height` 应改为图片的实际像素尺寸，用于预留正确比例；显示宽度由 CSS 控制，桌面为 340px，手机为单栏。

图片链接和标题链接是两个独立的 `href`，通常一起改。`alt` 描述图片，`aria-label` 描述链接，方便辅助阅读。删除论文时从 `<article class="publication">` 删到它对应的 `</article>`。

需要增加 Paper / Code 链接时，在论文的描述下面加：

```html
<p><a href="files/my-paper.pdf">Paper</a> / <a href="https://github.com/your-account/your-project">Code</a></p>
```

先将 PDF 放进 `files/`。新文件名建议用英文、数字和短横线，避免空格。已有附件不要随意改名，因为别人可能正在引用它的旧地址。

## 5. 更新经历或其他列表

经历是表格，每个 `<tr>` 是一行，两个 `<td>` 分别是时间和内容。把新记录放在 `<tbody>` 内：

```html
<tr>
  <td><em>09.2026–Present</em></td>
  <td>Your role, Institution, Country.</td>
</tr>
```

荣誉、教学、数据集等是普通列表，复制对应的 `<li>…</li>` 修改即可。

## 6. 改头像、样式或放视频

替换头像最简单的方式是覆盖 `images/profile.png`；该图片也用于浏览器图标。换成其他文件名时，修改 HTML 中头像的 `src` 和图标的 `href`。

在 `assets/css/academic.css` 中：

- `.academic-page` 的 `max-width` 控制页面最大宽度。
- `body` 的 `font` 控制正文大小和行距。
- `--link` 控制链接颜色。
- `.publication` 控制论文图片和文字布局。
- `@media` 内的规则控制小屏幕布局，修改时也检查手机尺寸。

如需视频，放进 `files/` 后可以插入：

```html
<video controls preload="metadata" style="max-width: 100%;">
  <source src="files/my-demo.mp4" type="video/mp4">
  Your browser does not support video playback.
</video>
```

## 7. 保存后检查

1. 看文字、图片是否正常，点击新加的链接。
2. 缩窄浏览器窗口，检查手机布局；浏览器开发者工具可查看资源 404。
3. 需要打包时运行 `bash build.sh`，生成 `_site/`，无需安装编译依赖。
4. 用 `git diff` 查看修改，再提交到当前分支。合并到实际发布分支后才会上线。

常见问题：图片不显示时检查大小写和路径；文字被当成标签时用 `&lt;` 表示 `<`、`&gt;` 表示 `>`；在正文或链接属性中用 `&amp;` 表示 `&`。浏览器开发者工具中临时改的内容不会保存到文件，确认样式后要同步改源文件。

## 8. 裁剪论文配图的展示区域

VLA-Pro 的图片链接有额外的 `publication-image--vla-pro` 类。CSS 用 `aspect-ratio: 1113 / 654` 和顶部对齐，仅显示原图的 a、b 两部分，隐藏 c。原图文件保持完整，桌面和手机都按相同比例裁剪。修改该比例可调整显示范围；移除额外的类即可恢复完整图片。
