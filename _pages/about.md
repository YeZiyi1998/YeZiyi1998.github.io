---
permalink: /
title: "About me: Ziyi Ye（叶子逸）"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I graduated with a Ph.D. from [THUIR](http://www.thuir.cn/), [Department of Computer Science and Technology in Tsinghua University](http://www.cs.tsinghua.edu.cn/), Beijing, China. My supervisor is [Prof. Yiqun Liu](http://www.thuir.cn/group/~YQLiu/). My major research interests are about Web search, brain machine interface, large language models, and etc. 
<!-- I have published more than 20 papers at the top international AI conferences <a href='https://scholar.google.com/citations?user=M3Qsb6cAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>. -->

I served as a reviewer and SPC/PC member for Nature Comm. Bio., ICLR, Neurips, TOIS, SIGIR, WWW, MM, CIKM, TOMM, and KDD.
I am the CCIR Student Contact since 2024, please contact me if you have any questions about IR matters. 

# 📖 Experience

| Year | Education |
| :------ | :------ | 
| *08.2020-06.2025* | Ph.D. student, Department of Computer Science and Technology, Tsinghua University, China. |
| *11.2023-02.2024* | Guest Ph.D. student, Institute of Informatics, University of Amsterdam, Netherlands. |
| *07.2023-11.2023* | Guest Ph.D. student, Department of Computer Science (DIKU) and the Pioneer Centre for AI, University of Copenhagen, Denmark. |
| *08.2016-07.2020* | B.S. student, Department of Computer Science and Technology, Tsinghua University, China. |


# 🔥 News
* 5.2025, our paper titled ***EEG reveals the cognitive impact of polarized content in short video scenarios*** is available in Nature Scientific Reports.
* 4.2025, thrilled to announce that I have three co-authered paper accepted by SIGIR 2025.
* 4.2025, I will attend ICLR 2025 in person for our paper titled ***Learning LLM-as-a-Judge for Preference Alignment***.
* 3.2025, our paper titled ***Generative Language Reconstruction from Brain Recordings*** is published in Nature Communications Biology.
* 9.2024, our paper titled ***Pre-trained Model for EEG-based Emotion Recognition*** won the **Best Paper Nomination** at CCIR 2024.
* 12.2023, I gave an invited talk in the Institute of Information in University of Amsterdam about ***Language Generation from Brain Recordings***. [Slide](https://yeziyi1998.github.io/files/Language_Generation_from_Brain_Recordings_240312.pdf)
* 07.2023, I gave an invited talk to Lenovo Inc about ***Context-based Brain Decoding***. [Slide](https://yeziyi1998.github.io/files/Language_Generation_from_Brain_Recordings_240312.pdf)
* 09.2023, I gave an invited talk in Machine Learning Section of Copenhagen University about ***Brain-Computer Interface for Search***. [Slide](https://yeziyi1998.github.io/files/BMI4Search_KU_230918.pdf)


# 📝 Publications

| **Brain Computer Interface for Information Retrieval** |
| :------ | 
|  My Ph.D.'s dissertation, [Link](https://yeziyi1998.github.io/files/thesis.pdf) |

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Dissertation</div><video width="100%" height="auto" controls preload="metadata" poster="">
    <source src="https://yeziyi1998.github.io/files/output.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video></div></div>
<div class='paper-box-text' markdown="1">

- My Ph.D.'s dissertation explores the integration of Brain-Computer Interface (BCI) technology into information retrieval systems to enhance understanding of users’ cognitive processes, decode information needs, and model user feedback, thereby improving the performance of a search system. 
- Relevant papers are published in [Nature Commun. Biol.](https://doi.org/10.1038/s42003-025-07731-7), [SIGIR](http://www.thuir.cn/group/~YQLiu/publications/SIGIR2022Ye.pdf), [Multimedia](https://arxiv.org/abs/2402.15708), [TOIS](https://arxiv.org/abs/2312.05669), and etc.
</div>
</div>

| **Learning LLM-as-a-Judge for Preference Alignment** | 
| :------ | 
|  ***Ziyi Ye***, Xiangsheng Li, Qiuchi Li, Qingyao Ai, Yujia Zhou, Wei Shen, Dong Yan, Yiqun Liu | 
| ICLR 2025. [\[Paper\]](https://openreview.net/forum?id=HZVIQE1MsJ).|

| **Generative Language Reconstruction from Brain Recordings** | 
| :------ | 
|  ***Ziyi Ye***, Qingyao Ai, Yiqun Liu, Maarten de Rijke, Min Zhang, Christina Lioma, and Tuukka Ruotsalo | 
| Nature Commun. Biol. [\[Paper\]](https://doi.org/10.1038/s42003-025-07731-7). [\[Code\]](https://github.com/YeZiyi1998/Brain-language-generation) |

| **Brain-Computer Interface Meets Information Retrieval: Perspective on Next-generation Information System** |
| :------ |
| ***Ziyi Ye***, Qingyao Ai, Yiqun Liu |
| MM 2024 BCI4MM workshop. [\[Paper\]](https://arxiv.org/abs/2402.15708) |

| **Query Augmentation with Brain Signals** |
| :------ |
| ***Ziyi Ye***, Jingtao Zhan, Qingyao Ai, Yiqun Liu, Maarten de Rijke, Christina Lioma, and Tuukka Ruotsalo |
| MM 2024 full paper, Oral Acceptance Rate: 3.97%, CCF A. [\[Paper\]](https://arxiv.org/abs/2402.15708) [\[Code\]](https://github.com/YeZiyi1998/Brain-Query-Augmentation) |

| **Relevance Feedback with Brain Signals** | 
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
| The Web Conf 2022 full paper, Acceptance Rate: 17.7%, CCF A. [\[Paper\]](https://doi.org/10.1145/3485447.3511966) [\[Code\]](https://github.com/YeZiyi1998/UERCM) | 

| **Brain Topography Adaptive Satisfaction Modeling for Interactive Information Access** | 
| :------ | 
| ***Ziyi Ye***, Xiaohui Xie, Yiqun Liu, Zhihong Wang, Xuesong Chen, Min Zhang, and Shaoping Ma | 
| MM 2022 full paper, Acceptance Rate: 27.9%, CCF A. [\[Paper\]](https://dl.acm.org/doi/abs/10.1145/3503161.3548258) [\[Code\]](https://github.com/YeZiyi1998/DL4EEG-Classification) | 

| **A Hybrid Framework for Session Context Modeling** | 
| :------ | 
|  Jia Chen, Jiaxin Mao, Yiqun Liu, ***Ziyi Ye***, Weizhi Ma, Chao Wang, Min Zhang and Shaoping Ma | 
| TOIS, CCF A. [\[Paper\]](https://dl.acm.org/doi/abs/10.1145/3448127) | 

[See my full publication list.](https://scholar.google.com/citations?user=M3Qsb6cAAAAJ&hl=zh-CN)

# 🎖 Honors and Awards
* 2025, Outstanding Graduate of Beijing, .
* 2025, Qihang Gold Award, Tsinghua University.
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
