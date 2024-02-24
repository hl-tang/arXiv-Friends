# 封装一个函数，输入搜索内容，输出相关的10篇文章的list

import arxiv
import datetime
from deep_translator import GoogleTranslator

def arxiv_search_latest_5_papers(search_content: str) -> list:
    search_result_list = []

    # Construct the default API client.
    client = arxiv.Client()

    # Search for the 10 most recent articles matching the keyword
    # 注意对于有空格关键词多搜索格式，如camera localization要写成\"camera Localization\"，其中的\"表转义
    search = arxiv.Search(
        query=f"\"{search_content}\"",
        max_results=5,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    results = client.results(search)

    for r in client.results(search):
        cur_paper = {}
        cur_paper["Paper_ID"] = r.entry_id
        cur_paper["Title_En"] = r.title
        cur_paper["Title_Ja"] = GoogleTranslator(source='en', target='ja').translate(text=r.title)
        cur_paper["Authors"] = [author.name for author in r.authors]
        cur_paper["Published"] = r.published.strftime("%Y-%m-%d %H:%M:%S%z")
        cur_paper["Content_En"] = r.summary
        cur_paper["Pdf_url"] = r.pdf_url

        search_result_list.append(cur_paper)

    # for paper in search_result_list:
    #     print(paper, end="\n\n")
    return search_result_list

# print(arxiv_search_latest_5_papers("computer vision")[1])