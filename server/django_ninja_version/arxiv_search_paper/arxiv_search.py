# 封装一个函数，输入搜索内容，输出相关的10篇文章的list

import arxiv
from datetime import datetime
from deep_translator import GoogleTranslator
import json
from gpt_simplify.models import Paper

# 指定文件路径 (相对于manage.py)
file_path = "./arxiv_search_paper/cat_dic_en.json"
# 读取 JSON 文件
with open(file_path, "r") as f:
    cat_dic = json.load(f)
# print(cat_dic)

def arxiv_search_latest_10_papers(search_content: str) -> list:
    search_result_list = []

    # Construct the default API client.
    client = arxiv.Client()

    # Search for the 10 most recent articles matching the keyword
    # 注意对于有空格关键词多搜索格式，如camera localization要写成\"camera Localization\"，其中的\"表转义
    search = arxiv.Search(
        query=f"\"{search_content}\"",
        max_results=10,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    results = client.results(search)

    for r in client.results(search):
        cur_paper = {}
        cur_paper["paper_id"] = r.entry_id
        cur_paper["title_en"] = r.title
        print(cur_paper["title_en"]) # 输出log，看搜索没出问题
        cur_paper["title_ja"] = GoogleTranslator(source='en', target='ja').translate(text=r.title)
        cur_paper["authors"] = [author.name for author in r.authors]
        cur_paper["categories"] = [cat_dic[category] for category in r.categories if category in cat_dic]
        cur_paper["published"] = r.published.strftime("%Y-%m-%d %H:%M:%S%z")
        cur_paper["content_en"] = r.summary
        cur_paper["pdf_url"] = r.pdf_url
        search_result_list.append(cur_paper)
        
        # Paper.objects.create(
        #     paper_id = cur_paper["Paper_ID"],
        #     title_en = cur_paper["Title_En"],
        #     title_ja = cur_paper["Title_Ja"],
        #     authors = cur_paper["Authors"],
        #     categories = cur_paper["Categories"],
        #     published = cur_paper["Published"],
        #     content_en = cur_paper["Content_En"],
        #     pdf_url = cur_paper["Pdf_url"]
        # )
        if not Paper.objects.filter(paper_id=cur_paper["paper_id"]).exists():
            # json的key改为和数据库字段名一样后，就可以用**字典来传参
            Paper.objects.create(**cur_paper)

    # for paper in search_result_list:
    #     print(paper, end="\n\n")
    return search_result_list

# print(arxiv_search_latest_5_papers("computer vision")[1])