硬编码了的假数据可以去前端的fastapi复制

## 搜索论文

`/api/arxiv` get：检索结果先不要存在数据库，等点击了后数据库再存翻译的日语、简化的日语、关键字。这里应该设计成get

但需要翻译title (~~封装一个gpt翻译函数~~ deep-translator)



~~request body:~~ (get不应该有请求体，直接query parameter)

```json
{
	"Search": "xxx"
}
```

response body: 返回paper json的list

```json
[
	{
        "Paper_ID": "http://arxiv.org/abs/2206.34567v1",
        "Title_En": "Efficient Object Detection using Spatial Attention Mechanisms",
        "Title_Ja": "空間注意メカニズムを用いた効率的な物体検出",
        "Authors": [
            "Keisuke Yamada",
            "Aya Takahashi",
            "Hiroki Nakamura"
        ],
        "Categories": [
            "Computer Vision and Pattern Recognition"
        ],
        "Published": "2023-09-10 11:30:00+00:00",
        "Content_En": "This paper presents an efficient approach to object detection using spatial attention mechanisms. Our method focuses on enhancing the ability of models to attend to relevant regions in an image, resulting in improved detection accuracy. We introduce a novel spatial attention module that significantly reduces computational complexity while maintaining high performance. Experimental results on benchmark datasets demonstrate the effectiveness of our approach in achieving state-of-the-art results in object detection tasks.",
        "Pdf_url": "http://arxiv.org/pdf/2206.34567v1"
    },
]
```



