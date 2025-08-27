---
permalink: /
title: "About me: Ziyi Ye（叶子逸）"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
  dl {
    margin-bottom: 60px; /* 调整这个值以获得合适的间距 */
    clear: both;
  }

  /* 全局文本颜色 */
  body {
    color: #333; /* 主要文本颜色 */
    background-image: url('../images/bg.jpg'); /* 背景图片 */
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
  }

  /* 链接颜色 */
  a {
    color: #0066cc; /* 链接颜色 */
  }

  /* 作者名字颜色 */
  strong {
    color: #000; /* 作者名字颜色 */
  }

  /* 年份标题颜色 */
  .year-title {
    color: #666;
  }

  /* 会议标签样式 */
  .conference-label {
    position: absolute;
    top: 10px;
    left: -5px;
    background-color: #2c3e50;  /* 深蓝色背景 */
    color: white;  /* 白色文字 */
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 0.95em;
    font-weight: 600;
    letter-spacing: 0.5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    z-index: 1;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-style: italic;  /* 添加斜体 */
  }

  /* 鼠标悬停效果 */
  .conference-label:hover {
    background-color: #34495e;  /* 悬停时稍微变亮 */
    transition: background-color 0.2s ease;
  }

  dl dt img {
    width: 100%; /* 在移动端默认占满宽度 */
    aspect-ratio: 2/1; /* 设置宽高比为2:1，即高度为宽度的一半 */
    object-fit: cover; /* 确保图片不会被裁剪 */
    display: block;
    margin: 10px 10px 10px 0px; /* 适当的间距 */
    
    /* 添加美化效果 */
    border-radius: 8px; /* 让图片有轻微的圆角 */
    border: 2px solid #ddd; /* 添加淡灰色的边框 */
    box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2); /* 添加轻微阴影 */
    padding: 5px; /* 给图片一些内边距，让它不贴着边框 */
    background-color: #fff; /* 设置背景色，让图片更加干净 */
  }

  dl dt video {
    width: 100%; /* 在移动端默认占满宽度 */
    aspect-ratio: 2/1; /* 设置宽高比为2:1，即高度为宽度的一半 */
    object-fit: cover; /* 确保图片不会被裁剪 */
    display: block;
    margin: 10px 10px 10px 0px; /* 适当的间距 */
    
    /* 添加美化效果 */
    border-radius: 8px; /* 让图片有轻微的圆角 */
    border: 2px solid #ddd; /* 添加淡灰色的边框 */
    box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2); /* 添加轻微阴影 */
    padding: 5px; /* 给图片一些内边距，让它不贴着边框 */
    background-color: #fff; /* 设置背景色，让图片更加干净 */
  }

  /* 在桌面端（宽度大于768px）时固定宽度 */
  @media screen and (min-width: 768px) {
    dl dt img {
      width: 350px;
    }
    dl dt video {
      width: 350px;
    }
  }

  dl dt {
    position: relative;
  }

  hr {
    border: 1px solid #ebebeb; /* 调整分隔线的颜色和样式 */
    /* margin: 10px;  */
    clear: both; 
  }

  dl dd {
  margin-top: 5px; 
  margin-bottom: 5px;
  }

  dl dd strong {
  font-weight: bold;
  color: black;
  }

  .co-first {
    color: red;
  }

  .down {
    transform: rotate(180deg);
  }

  /* 教育和工作经历卡片样式 */
  .experience-card, .education-card {
    display: flex;
    align-items: center;
    gap: 25px;
    margin-bottom: 30px;
    padding: 20px;
    background: #f8f9fa;
    border-radius: 12px;
    transition: all 0.3s ease;
    border: 1px solid #e9ecef;
  }

  .experience-card:hover, .education-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    border-color: #dee2e6;
  }

  .experience-info, .education-info {
    flex: 1;
  }

  .experience-logo, .education-logo {
    flex-shrink: 0;
    width: 100px;
    height: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: white;
    border-radius: 10px;
    padding: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  }

  .experience-logo img, .education-logo img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }

  .experience-title, .education-title {
    font-size: 1.2em;
    margin-bottom: 8px;
    color: #2c3e50;
  }

  .experience-title a, .education-title a {
    color: #2c3e50;
    text-decoration: none;
    transition: color 0.3s ease;
  }

  .experience-title a:hover, .education-title a:hover {
    color: #3498db;
  }

  .experience-role, .education-role {
    color: #666;
    font-style: italic;
    margin-bottom: 5px;
  }

  .experience-topics, .education-topics {
    color: #666;
    font-style: italic;
  }

  .section-title {
    font-size: 1.8em;
    color: #2c3e50;
    margin: 40px 0 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid #ecf0f1;
  }

  /* 奖学金和荣誉部分样式 */
  .honors-list {
    list-style: none;
    padding: 0;
  }

  .honors-list li {
    margin-bottom: 15px;
    padding: 15px 20px;
    background: #f8f9fa;
    border-radius: 8px;
    border-left: 4px solid #3498db;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .honors-list li:hover {
    transform: translateX(5px);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }

  .honors-list li strong {
    color: #2c3e50;
  }

  .honors-list li a {
    color: #3498db;
    text-decoration: none;
    transition: color 0.3s ease;
  }

  .honors-list li a:hover {
    color: #2980b9;
  }

  /* 服务部分样式 */
  .service-section {
    margin-bottom: 30px;
  }

  .service-section h3 {
    color: #2c3e50;
    font-size: 1.3em;
    margin: 25px 0 15px;
    padding-bottom: 8px;
    border-bottom: 2px solid #ecf0f1;
  }

  .service-list {
    list-style: none;
    padding: 0;
  }

  .service-list li {
    margin-bottom: 12px;
    padding: 12px 15px;
    background: #f8f9fa;
    border-radius: 6px;
    transition: transform 0.3s ease;
  }

  .service-list li:hover {
    transform: translateX(5px);
  }

  .service-list li a {
    color: #3498db;
    text-decoration: none;
    transition: color 0.3s ease;
  }

  .service-list li a:hover {
    color: #2980b9;
  }
</style>

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>
I am an Assistant Professor in [Institute of Trustworthy Embodied AI at Fudan University](https://teai.fudan.edu.cn/). I received my Ph.D. from [THUIR](http://www.thuir.cn/), [Department of Computer Science and Technology in Tsinghua University](http://www.cs.tsinghua.edu.cn/), Beijing, China. My supervisor is [Prof. Yiqun Liu](http://www.thuir.cn/group/~YQLiu/). My major research interests are about Web search, large language models, and embodied AI. 
My current research focuses on <strong>Embodied AI</strong>, my primary areas of interest include:
<ul>
    <li><strong>Multimodal Large Models for Embodiment:</strong> Developing foundational models that can understand and integrate diverse sensory inputs (vision, language, touch, etc.) to perform complex tasks.</li>
    <li><strong>Human-AI Interaction:</strong> Exploring intuitive and effective ways for humans to collaborate and communicate with autonomous agents.</li>
    <li><strong>Autonomous Evolution & Lifelong Learning:</strong> Investigating mechanisms that enable agents to continuously learn from experience, adapt to new environments, and evolve their capabilities.</li>
</ul>
<!-- I have published more than 20 papers at the top international AI conferences <a href='https://scholar.google.com/citations?user=M3Qsb6cAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>. -->

I served as a reviewer and SPC/PC member for Nature Comm. Bio., ICLR, Neurips, TOIS, SIGIR, WWW, MM, CIKM, TOMM, and KDD.
I am the CCIR Student Contact since 2024, please contact me if you have any questions about IR matters. 
<p style="color: red;">
    I am actively looking for self-motivated students to join my research group. If you are passionate about building the future of AI, please feel free to reach out.
</p>

# 🔥 News
<div style="max-height: 350px; overflow-y: auto; padding: 20px; background: #f8f9fa; border-left: 4px solid #2c3e50; margin: 0px 0;">
<style>
  div::-webkit-scrollbar {
    width: 8px;
  }

  div::-webkit-scrollbar-track {
    background: #e9ecef;
    border-radius: 4px;
  }

  div::-webkit-scrollbar-thumb {
    background: #2c3e50;
    border-radius: 4px;
  }

  div::-webkit-scrollbar-thumb:hover {
    background: #1a252f;
  }

  /* 为 Firefox 设置滚动条样式 */
  div {
    scrollbar-width: thin;
    scrollbar-color: #2c3e50 #e9ecef;
  }
</style>
<ul style="list-style-type: none; padding-left: 0; margin: 0;">
<li> 8.2025, our paper titled <b>SimVBG: Simulating Individual Values by Backstory Generation</b> is accepted by EMNLP 2025.</li>
<li> 5.2025, our paper titled <b>EEG reveals the cognitive impact of polarized content in short video scenarios</b> is available in Nature Scientific Reports.</li>
<li> 4.2025, thrilled to announce that I have three co-authered paper accepted by SIGIR 2025.</li>
<li> 4.2025, I will attend ICLR 2025 in person for our paper titled <b>Learning LLM-as-a-Judge for Preference Alignment</b>.</li>
<li> 3.2025, our paper titled <b>Generative Language Reconstruction from Brain Recordings</b> is published in Nature Communications Biology.</li>
<li> 9.2024, our paper titled <b>Pre-trained Model for EEG-based Emotion Recognition</b> won the <b>Best Paper Nomination</b> at CCIR 2024.</li>
<li> 12.2023, I gave an invited talk in the Institute of Information in University of Amsterdam about <b>Language Generation from Brain Recordings</b>. <a href="https://yeziyi1998.github.io/files/Language_Generation_from_Brain_Recordings_240312.pdf" target="_blank">Slide</a></li>
<li> 07.2023, I gave an invited talk to Lenovo Inc about <b>Context-based Brain Decoding</b>. <a href="https://yeziyi1998.github.io/files/Language_Generation_from_Brain_Recordings_240312.pdf" target="_blank">Slide</a>
</li>
<li> 09.2023, I gave an invited talk in Machine Learning Section of Copenhagen University about <b>Brain-Computer Interface for Search</b>. <a href="https://yeziyi1998.github.io/files/BMI4Search_KU_230918.pdf" target="_blank">Slide</a></li>
</ul>
</div>

# 📝 Publications

<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">Dissertation</div><video width="100%" height="auto" controls preload="metadata" poster="">
    <source src="https://yeziyi1998.github.io/files/output.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video></div></div>
<div class='paper-box-text' markdown="1">

- My Ph.D.'s dissertation: [Brain Computer Interface for Information Retrieval](https://yeziyi1998.github.io/files/thesis.pdf).
- The integration of Brain-Computer Interface (BCI) technology into information retrieval systems can enhance understanding of users’ cognitive processes, decode information needs, and model user feedback, thereby improving the performance of a search system. 
- Relevant papers are published in [Nature Commun. Biol.](https://doi.org/10.1038/s42003-025-07731-7), [SIGIR](http://www.thuir.cn/group/~YQLiu/publications/SIGIR2022Ye.pdf), [Multimedia](https://arxiv.org/abs/2402.15708), [TOIS](https://arxiv.org/abs/2312.05669), and etc.
</div>
</div> -->

<dl>
  <dt><img align="left"  width="100"
  hspace="10" wspace="20" src="../images/SIGIR25zhu.png">
<span class="conference-label">SIGIR 2025</span>
</dt>
<dd><a href="https://dl.acm.org/doi/pdf/10.1145/3726302.3729909"><strong>LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods</strong></a></dd>
<dd>Shuqi Zhu, <strong>Ziyi Ye</strong>, Yi Zhong, Qingyao Ai, Yujia Zhou, Yiqun Liu</dd>
</dl>

<hr>

<dl>
  <dt><img align="left"  width="100"
  hspace="10" wspace="20" src="../images/survey2025li.png">
<span class="conference-label">Arxiv 2025</span>
</dt>
<dd><a href="https://arxiv.org/pdf/2412.05579?"><strong>Brain Image Reconstruction with Retrieval-Augmented Diffusion</strong></a></dd>
<dd>Haitao Li, Qian Dong, Junjie Chen, Huixue Su, Yujia Zhou, Qingyao Ai, <strong>Ziyi Ye</strong>, Yiqun Liu</dd>
</dl>

<hr>

<dl>
  <dt><video align="left"  width="100"
  hspace="10" wspace="20" controls preload="metadata" poster="">
    <source src="https://yeziyi1998.github.io/files/output.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
<span class="conference-label">Dissertation</span>
</dt>
<dd>My Ph.D.'s dissertation: <a href="https://yeziyi1998.github.io/files/thesis.pdf"><strong>Brain Computer Interface for Information Retrieval</strong></a></dd>
<dd> Relevant papers are published in <a href="https://doi.org/10.1038/s42003-025-07731-7">Nature Commun. Biol. </a>, <a href="http://www.thuir.cn/group/~YQLiu/publications/SIGIR2022Ye.pdf">SIGIR</a>, <a href="https://arxiv.org/abs/2402.15708"> Multimedia </a>, <a href="https://arxiv.org/abs/2312.05669">TOIS</a>, and etc. </dd>
</dl>

<hr>

<dl>
  <dt><img align="left"  width="100"
  hspace="10" wspace="20" src="../images/ICLR2025.png">
<span class="conference-label">ICLR 2025</span>
</dt>
  <dd><a href="https://openreview.net/forum?id=HZVIQE1MsJ"><strong>Learning LLM-as-a-Judge for Preference Alignment</strong></a></dd>
<dd><strong>Ziyi Ye</strong>, Xiangsheng Li, Qiuchi Li, Qingyao Ai, Yujia Zhou, Wei Shen, Dong Yan, Yiqun Liu</dd>
</dl>

<hr>

<dl>
  <dt><img align="left"  width="100"
  hspace="10" wspace="20" src="../images/NCB2025.png">
<span class="conference-label">Nature Communications Biology</span>
</dt>
  <dd><a href="https://doi.org/10.1038/s42003-025-07731-7"><strong>Generative Language Reconstruction from Brain Recordings</strong></a></dd>
<dd><strong>Ziyi Ye</strong>, Qingyao Ai, Yiqun Liu, Maarten de Rijke, Min Zhang, Christina Lioma, and Tuukka Ruotsalo</dd>
</dl> 

<!-- | **Brain-Computer Interface Meets Information Retrieval: Perspective on Next-generation Information System** |
| :------ |
| ***Ziyi Ye***, Qingyao Ai, Yiqun Liu |
| MM 2024 BCI4MM workshop. [\[Paper\]](https://arxiv.org/abs/2402.15708) | -->

<!-- | **Query Augmentation with Brain Signals** |
| :------ |
| ***Ziyi Ye***, Jingtao Zhan, Qingyao Ai, Yiqun Liu, Maarten de Rijke, Christina Lioma, and Tuukka Ruotsalo |
| MM 2024 full paper, Oral Acceptance Rate: 3.97%, CCF A. [\[Paper\]](https://arxiv.org/abs/2402.15708) [\[Code\]](https://github.com/YeZiyi1998/Brain-Query-Augmentation) | -->

<!-- | **Relevance Feedback with Brain Signals** | 
| :------ | 
| ***Ziyi Ye***, Xiaohui Xie, Qingyao Ai, Yiqun Liu, Zhihong Wang, Weihang Su, and Min Zhang | 
| TOIS, CCF A. [\[Paper\]](https://arxiv.org/abs/2312.05669) [\[Code\]](https://github.com/THUIR/Brain-Relevance-Feedback) | 

| **Why Don't You Click: Understanding Human Reading Comprehension with Brain Signals** | 
| :------ | 
| ***Ziyi Ye***, Xiaohui Xie, Yiqun Liu, Zhihong Wang, Xuancheng Li, Jiaji Li, Xuesong Chen, Min Zhang, and Shaoping Ma | 
| SIGIR 2022 full paper, Acceptance Rate: 20.3%, CCF A. [\[Paper\]](http://www.thuir.cn/group/~YQLiu/publications/SIGIR2022Ye.pdf) [\[Code & Dataset\]](http://www.thuir.cn/Search_Brainwave/) | 

| **Towards a Better Understanding of Human Reading Comprehension with Brain Signals** | 
| :------ | 
| ***Ziyi Ye***, Xiaohui Xie, Yiqun Liu, Zhihong Wang, Xuesong Chen, Min Zhang, and Shaoping Ma | 
| The Web Conf 2022 full paper, Acceptance Rate: 17.7%, CCF A. [\[Paper\]](https://doi.org/10.1145/3485447.3511966) [\[Code\]](https://github.com/YeZiyi1998/UERCM) |  -->

<!-- | **Brain Topography Adaptive Satisfaction Modeling for Interactive Information Access** | 
| :------ | 
| ***Ziyi Ye***, Xiaohui Xie, Yiqun Liu, Zhihong Wang, Xuesong Chen, Min Zhang, and Shaoping Ma | 
| MM 2022 full paper, Acceptance Rate: 27.9%, CCF A. [\[Paper\]](https://dl.acm.org/doi/abs/10.1145/3503161.3548258) [\[Code\]](https://github.com/YeZiyi1998/DL4EEG-Classification) |  -->

<!-- | **A Hybrid Framework for Session Context Modeling** | 
| :------ | 
|  Jia Chen, Jiaxin Mao, Yiqun Liu, ***Ziyi Ye***, Weizhi Ma, Chao Wang, Min Zhang and Shaoping Ma | 
| TOIS, CCF A. [\[Paper\]](https://dl.acm.org/doi/abs/10.1145/3448127) |  -->

[See my full publication list.](https://scholar.google.com/citations?user=M3Qsb6cAAAAJ&hl=zh-CN)

# 📖 Experience

| Year | Experience |
| :------ | :------ | 
| *08.2025-* | Assistant Professor, Institute of Trustworthy Embodied AI, Fudan University, China. |
| *08.2020-06.2025* | Ph.D. student, Department of Computer Science and Technology, Tsinghua University, China. |
| *11.2023-02.2024* | Guest Ph.D. student, Institute of Informatics, University of Amsterdam, Netherlands. |
| *07.2023-11.2023* | Guest Ph.D. student, Department of Computer Science (DIKU) and the Pioneer Centre for AI, University of Copenhagen, Denmark. |
| *08.2016-07.2020* | B.S. student, Department of Computer Science and Technology, Tsinghua University, China. |

# 🎖 Honors and Awards
* 2025, **Outstanding Graduate of Beijing**.
* 2025, **Qihang Gold Award**, Tsinghua University.
* 2022, **China National Scholarship**, Chinese Government.
* 2017, 2018, 2023, 2024\. Overall Excellence Scholarship, Tsinghua University.
* 2019, Academic Excellence Scholarship, Tsinghua University.
* 2016, **Silver medal in Chinese Mathematical Olympiad(CMO)**, China Mathematical Federation.

# 📚 Teaching Experience
* 2024\. Teaching assistant at GenAI summer school, Tsinghua University. (Instructor of "Retrieval-argumented generation".)
* 2020-2025\. Teaching assistant at "Fundamental Search Engine", Tsinghua University.

# 🏆 Competitions
* We won the 1st place in TASK 2 (Relevant Statue Retrieval Task) of AILA 2019 (Artificial Intelligence for Legal Assisstance). [Working Notes](http://ceur-ws.org/Vol-2517/T1-8.pdf).
* We won the 1st place in the NTCIR-15 Micro-activity Retrieval Task. [Working Notes](http://research.nii.ac.jp/ntcir/workshop/OnlineProceedings15/pdf/ntcir/06-NTCIR15-MART-LiJ.pdf).

# 📊 Datasets
* [Search-Brainwave Dataset](http://www.thuir.cn/Search_Brainwave/). In our SIGIR'22 Full Paper *Why Don’t You Click: Understanding Non-Click Results in Web Search with Brain Signals*.

* [UERCM Dataset](https://cloud.tsinghua.edu.cn/d/4ede7ce124cc46f3b42e/?p=%2Fdataset&mode=list). In our The Web Conf’22 Full Paper *Towards a Better Understanding of Human Reading Comprehension with Brain Signals*.

* [TianGong-CRL Dataset](http://www.thuir.cn/TianGong-CRL/). In our ASIST'20 Poster *Investigating COVID-19-Related Query Logs of Chinese Search Engine Users*.
