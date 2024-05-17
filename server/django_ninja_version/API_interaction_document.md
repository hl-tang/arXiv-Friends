硬编码了的假数据可以去前端的fastapi复制

## 搜索论文

`/api/arxiv` ~~get：检索结果先不要存在数据库，等点击了后数据库再存翻译的日语、简化的日语、关键字。~~ post: 检索结果存到数据库，简化的摘要や关键词作为论文表的弱entity. 考虑到用户收藏为未简化的论文

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



## GPT简化

添加摘要的日语翻译，然后gpt简化翻译，抽取5个关键词并解释

endpoint: `/api/simplify`

POST: 通过GPT处理的简化日语摘要，关键词 存在数据库。省得再次点击通篇文字在经过GPT处理，直接数据库返回。

存数据库里需要加一个字段count，统计点击了多少次用于recommendation



request body: 虽然只需要日语摘要就够了，但为了把其他字段都存到数据库里，所以请求体还是要其他的字段的。

```
{
	"Paper_ID": Paper_ID.value,
     "Title_En": Title_En.value,
     "Title_Ja": Title_Ja.value,
     "Authors": Authors.value,
     "Categories": Categories.value,
     "Published": Published.value,
     "Content_En": Content_En.value,
     "Pdf_url": Pdf_url.value
}
```

response body:

```
{
"Paper_ID":
"Content_En": "",
"Content_Ja": "",
"Content_plain": "",
"Keywords": [
	{"Keyword": "", "Description": ""},
	{"Keyword": "", "Description": ""},
	{"Keyword": "", "Description": ""},
	{"Keyword": "", "Description": ""},
	{"Keyword": "", "Description": ""}
]
"clicked_count":
}
```



## recommendation

返回数据库clicked_paper表，按照点击数降序

`/api/recommend` GET

response body和检索一样的list
