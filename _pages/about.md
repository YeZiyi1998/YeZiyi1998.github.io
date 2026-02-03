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

  .media-container {
    float: left; /* 让整个容器向左浮动 */
    position: relative; /* 这是为了让 conference-label 能正确定位 */
    width: 100%; /* 在移动端默认占满宽度 */
    hspace: 10;
    margin-right: 30px;
    wspace: 20
  }

  .media-container img,
  .media-container video {
    width: 100%;
    aspect-ratio: 2/1;
    object-fit: cover;
    margin: 10px 20px 10px 0px; /* 调整右边距以留出空间 */
    
    /* 美化效果保持不变 */
    border-radius: 8px;
    border: 2px solid #ddd;
    box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
    padding: 5px;
    background-color: #fff;
  }

  /* 全局文本颜色 */
  body {
    color: #333; /* 主要文本颜色 */
    font-size: 1.05em; /* 略微放大整体字体 */
    background-image: url('../images/bg.jpg'); /* 背景图片 */
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
  }

  /* 链接颜色 */
  a {
    color: #0066cc; /* 链接颜色 */
    text-decoration: none !important; /* 去掉所有超链接下划线 */
  }

  a:hover {
    text-decoration: none !important;
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

  /* 在桌面端（宽度大于768px）时固定宽度 */
  @media screen and (min-width: 768px) {
    .media-container {
      width: 350px; /* 在桌面端给容器一个固定宽度 */
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

  /* 只放大论文标题（在链接里的 strong），不影响作者名字 */
  dl dd a strong {
    font-size: 1.55em;
  }

  /* 论文标题虽然有超链接，但不显示下划线 */
  dl dd a {
    text-decoration: none;
  }

  dl dd a:hover {
    text-decoration: none;
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
I am an Assistant Professor in [Institute of Trustworthy Embodied AI at Fudan University（复旦大学可信具身智能研究院）](https://teai.fudan.edu.cn/) and a member of [Fudan Vision and Learning Lab（复旦大学视觉与学习实验室，FVL）](https://fvl.fudan.edu.cn/). I received my Ph.D. from [THUIR](http://www.thuir.cn/), [Department of Computer Science and Technology in Tsinghua University](http://www.cs.tsinghua.edu.cn/), Beijing, China.

My major research interests are about multimodel computing, Web search, large language models, and embodied AI. <strong>My goal is to build an intelligent system that can understand human needs, perform human-like behaviors, and interact with humans more effectively.
</strong> My primary areas of interest include:
<ul>
    <li><strong>Multimodal Computing:</strong> Developing models that can understand and integrate diverse sensory inputs (vision, language, touch, human signals, etc.) to perform complex, human-like tasks.</li>
    <li><strong>Human-AI Interaction:</strong> Exploring intuitive and effective ways for autonomous agents to collaborate and communicate with human.</li>
    <li><strong>Cognition of AI:</strong> Investigating how cognitive abilities and complex behaviors emerge in AI system through evolutionary processes.</li>
</ul>

<!-- I have published more than 20 papers at the top international AI conferences <a href='https://scholar.google.com/citations?user=M3Qsb6cAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>. -->


<p style="color: red;"><b>
    I am actively looking for self-motivated students to join my research group. If you are passionate about building the future of AI and Human, please feel free to reach out. 本人依托<a href="https://teai.fudan.edu.cn/" target="_blank" style="color: red;">复旦大学可信具身智能研究院</a>和<a href="https://fvl.fudan.edu.cn/" target="_blank" style="color: red;">复旦大学视觉与学习实验室</a>，正积极招募具有自驱力的学生加入研究团队，诚邀有志于揭示人类智能与机器智能的认知基础、推动人机智能深度协同交互的同学随时沟通（邮箱：zyye@fudan.edu.cn）。
</b></p>

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
<li> 2026.01, our paper titled <b>Robotic Grasping and Placement Controlled by EEG-Based Hybrid Visual and Motor Imagery</b> is accepted by ICRA 2026.</li>
<li> 2026.01, our paper titled <b>SLEEP2VEC: Unified Cross-modal Alignment
for Heterogeneous Nocturnal Biosignals</b> is accepted by ICLR 2026.</li>
<li> 2025.10, I was invited to join the discussion about <b>World Model</b> at CCF YOCSEF. <a href="https://www.ccf.org.cn/YOCSEF/News/2025-10-12/849421.shtml" target="_blank">News</a></li>
<li> 2025.10, I gave an invited talk about <b>AI System Empowered by Neuro Feedback</b> at Computational Neuro-Linguistics Forum.<a href="https://xufengduan.github.io/Computational-Neurolinguistics-Forum/events/2025-10-Ye-Zianyi/">Video</a></li>
<li> 2025.08, I gave an invited talk about <b>"Tips for New Researchers"</b> at NLPCC 2025. <a href="https://yeziyi1998.github.io/files/NLPCC 2025 Ye.en.talk.pdf" target="_blank">Slides</a></li>
<li> 2025.08, our paper titled <b>SimVBG: Simulating Individual Values by Backstory Generation</b> is accepted by EMNLP 2025.</li>
<li> 2025.05, our paper titled <b>EEG reveals the cognitive impact of polarized content in short video scenarios</b> is available in Nature Scientific Reports.</li>
<li> 2025.04, thrilled to announce that I have three co-authered paper accepted by SIGIR 2025, titled <b>Brain Image Reconstruction with Retrieval-Augmented Diffusion</b>, <b>Parametric Retrieval Augmented Generation</b>, and <b>Understanding the Effect of Opinion Polarization in Short Video Browsing</b>.</li>
<li> 2025.04, I will attend ICLR 2025 in person for our paper titled <b>Learning LLM-as-a-Judge for Preference Alignment</b>.</li>
<li> 2025.03, our paper titled <b>Generative Language Reconstruction from Brain Recordings</b> is published in Nature Communications Biology.</li>
<li> 2024.09, our paper titled <b>Pre-trained Model for EEG-based Emotion Recognition</b> won the <b>Best Paper Nomination</b> at CCIR 2024.</li>
<li> 2023.12, I gave an invited talk in the Institute of Information in University of Amsterdam about <b>Language Generation from Brain Recordings</b>. <a href="https://yeziyi1998.github.io/files/Language_Generation_from_Brain_Recordings_240312.pdf" target="_blank">Slide</a></li>
<li> 2023.07, I gave an invited talk to Lenovo Inc about <b>Context-based Brain Decoding</b>. <a href="https://yeziyi1998.github.io/files/Language_Generation_from_Brain_Recordings_240312.pdf" target="_blank">Slide</a>
</li>
<li> 2023.09, I gave an invited talk in Machine Learning Section of Copenhagen University about <b>Brain-Computer Interface for Search</b>. <a href="https://yeziyi1998.github.io/files/BMI4Search_KU_230918.pdf" target="_blank">Slide</a></li>
</ul>
</div>

# 📝 Publications

<dl>
  <dt>
    <div class="media-container">
      <img src="../images/ICRA2026liu.png" wspace=20 hspace=10>
      <span class="conference-label">ICRA 2026</span>
    </div>
  </dt>
  <dd><a href="https://ziyiye.cn/files/ICRA26_3090_MS.pdf"><strong>Robotic Grasping and Placement Controlled by EEG-Based Hybrid Visual and Motor Imagery</strong></a></dd>
  <dd>Yichang Liu, Tianyu Wang, <strong>Ziyi Ye</strong>, Yawei Li, Yanwei Fu, Yu-gang Jiang, Shouyan Wang</dd>
</dl>

<hr>

<dl>
  <dt>
    <div class="media-container">
      <img src="../images/ICLR2026jin.png" wspace=20 hspace=10>
      <span class="conference-label">ICLR 2026</span>
    </div>
  </dt>
  <dd><a href="https://openreview.net/pdf?id=DDXhRN66eV"><strong>SLEEP2VEC: Unified Cross-modal Alignment
for Heterogeneous Nocturnal Biosignals</strong></a></dd>
  <dd>Weixuan Yuan, Zengrui Jin, Yichen Wang, Donglin Xie, <strong>Ziyi Ye</strong>, Chao Zhang, Xuesong Chen</dd>
</dl>

<hr>

<dl>
  <dt>
    <div class="media-container">
      <img src="../images/EMNLP25du.png" wspace=20 hspace=10>
      <span class="conference-label">EMNLP 2025</span>
    </div>
  </dt>
  <dd><a href="https://aclanthology.org/2025.emnlp-main.662.pdf"><strong>SimVBG: Simulating Individual Values by Backstory Generation</strong></a></dd>
  <dd>Bangde Du, <strong>Ziyi Ye</strong>, Zhijing Wu, Monika Jankowska, Shuqi Zhu, Qingyao Ai, Yujia Zhou, Yiqun Liu</dd>
</dl>

<hr>

<dl>
  <dt>
    <div class="media-container">
      <img src="../images/SIGIR25zhu.png" wspace=20 hspace=10>
      <span class="conference-label">SIGIR 2025</span>
    </div>
  </dt>
  <dd><a href="https://dl.acm.org/doi/pdf/10.1145/3726302.3729909"><strong>Brain Image Reconstruction with Retrieval-Augmented Diffusion</strong></a></dd>
  <dd>Shuqi Zhu, <strong>Ziyi Ye</strong>, Yi Zhong, Qingyao Ai, Yujia Zhou, Yiqun Liu</dd>
</dl>

<hr>

<dl>
  <dt>
    <div class="media-container">
      <img src="../images/SIGIR2025su.png">
      <span class="conference-label">SIGIR 2025</span>
    </div>
  </dt>
  <dd><a href="https://dl.acm.org/doi/pdf/10.1145/3726302.3729957"><strong>Parametric Retrieval Augmented Generation</strong></a></dd>
  <dd>Weihang Su, Yichen Tang, Qingyao Ai, Junxi Yan, Changyue Wang, Hongning Wang, <strong>Ziyi Ye</strong>, Yujia Zhou, Yiqun Liu</dd>
</dl>

<hr>

<!-- <dl>
  <dt>
    <div class="media-container">
      <img src="../images/survey2025li.png">
      <span class="conference-label">Arxiv 2025</span>
    </div>
  </dt>
  <dd><a href="https://arxiv.org/pdf/2412.05579?"><strong>LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods</strong></a></dd>
  <dd>Haitao Li, Qian Dong, Junjie Chen, Huixue Su, Yujia Zhou, Qingyao Ai, <strong>Ziyi Ye</strong>, Yiqun Liu</dd>
</dl> -->

<hr>

<dl>
  <dt>
    <div class="media-container">
      <video controls preload="metadata" poster="">
        <source src="https://yeziyi1998.github.io/files/output.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <span class="conference-label">Dissertation</span>
    </div>
  </dt>

<dd>My Ph.D.'s dissertation: <a href="https://yeziyi1998.github.io/files/thesis.pdf"><strong>Brain Computer Interface for Information Retrieval</strong></a></dd>
  <dd> Relevant papers are published in <a href="https://doi.org/10.1038/s42003-025-07731-7">Nature Commun. Biol. </a>, <a href="http://www.thuir.cn/group/~YQLiu/publications/SIGIR2022Ye.pdf">SIGIR</a>, <a href="https://arxiv.org/abs/2402.15708"> Multimedia </a>, <a href="https://arxiv.org/abs/2312.05669">TOIS</a>, and etc. </dd>
</dl>

<hr>

<dl>
  <dt>
    <div class="media-container">
      <img src="../images/ICLR2025.png">
      <span class="conference-label">ICLR 2025</span>
    </div>
  </dt>
  <dd><a href="https://openreview.net/forum?id=HZVIQE1MsJ"><strong>Learning LLM-as-a-Judge for Preference Alignment</strong></a></dd>
  <dd><strong>Ziyi Ye</strong>, Xiangsheng Li, Qiuchi Li, Qingyao Ai, Yujia Zhou, Wei Shen, Dong Yan, Yiqun Liu</dd>
</dl>

<hr>

<dl>
  <dt>
    <div class="media-container">
      <img src="../images/NCB2025.png">
      <span class="conference-label">Nature Communications Biology</span>
    </div>
  </dt>
  <dd><a href="https://doi.org/10.1038/s42003-025-07731-7"><strong>Generative Language Reconstruction from Brain Recordings</strong></a></dd>
  <dd><strong>Ziyi Ye</strong>, Qingyao Ai, Yiqun Liu, Maarten de Rijke, Min Zhang, Christina Lioma, and Tuukka Ruotsalo</dd>
</dl>

<hr>

[See my full publication list.](https://scholar.google.com/citations?user=M3Qsb6cAAAAJ&hl=zh-CN)

# 📖 Experience

| Year | Experience |
| :------ | :------ | 
| *08.2025-* | Assistant Professor, Institute of Trustworthy Embodied AI, Fudan University, China. |
| *08.2020-06.2025* | Ph.D. student, Department of Computer Science and Technology, Tsinghua University, China. |
| *11.2023-02.2024* | Guest Ph.D. student, Institute of Informatics, University of Amsterdam, Netherlands. |
| *07.2023-11.2023* | Guest Ph.D. student, Department of Computer Science (DIKU) and the Pioneer Centre for AI, University of Copenhagen, Denmark. |
| *08.2016-07.2020* | B.S. student, Department of Computer Science and Technology, Tsinghua University, China. |

# 📝 Academic Service
- **Journal Reviewer:** *Nature*, *Nature Comm. Bio.*, *Nature Dis. Com.*, *ACM TOIS*, *ACM TKDD*, *ACM TOMM*, *SCIS*

- **Conference Senior PC / PC Member:** *ICLR*, *NeurIPS*, *ICML*, *SIGIR*, *WWW*, *ACM MM*, *CVPR*, *CIKM*, *KDD*, *ACL*, *EMNLP*

 
-**Other Service:** *CCIR Student Contact* (2024.8–2025.8)

# 🎖 Honors and Awards
* 2025, **Ph.D. Dissertation Award of ACM Shanghai**.
* 2025, **Ph.D. Dissertation Award of CIPS**.
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

* [EEG-Imagenet Dataset](https://arxiv.org/pdf/2406.07151). In our Paper *EEG-imagenet: An electroencephalogram dataset and benchmarks with image visual stimuli of multi-granularity labels*.

* [EEG-SVC Dataset](https://dl.acm.org/doi/pdf/10.1145/3626772.3657890). In our SIGIR'25 Full paper *EEG-svrec: An eeg dataset with user multidimensional affective engagement labels in short video recommendation*.

* [Search-Brainwave Dataset](http://www.thuir.cn/Search_Brainwave/). In our SIGIR'22 Full Paper *Why Don’t You Click: Understanding Non-Click Results in Web Search with Brain Signals*.

* [UERCM Dataset](https://cloud.tsinghua.edu.cn/d/4ede7ce124cc46f3b42e/?p=%2Fdataset&mode=list). In our The Web Conf’22 Full Paper *Towards a Better Understanding of Human Reading Comprehension with Brain Signals*.

* [TianGong-CRL Dataset](http://www.thuir.cn/TianGong-CRL/). In our ASIST'20 Poster *Investigating COVID-19-Related Query Logs of Chinese Search Engine Users*.
