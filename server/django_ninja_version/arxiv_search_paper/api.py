from .arxiv_search import arxiv_search_latest_5_papers
# 不知道为什么相对导入 .arxiv_search不成功 （直接py运行这个文件是不对的，但django runserver起来的话是.arxiv_search或者写全app.文件）
# print(arxiv_search_latest_5_papers("smart contract"))
from ninja import Router
from .schemas import ArxivIn

arxiv_search_paper_api = Router()

# post这样是work的，但我觉得语义上还是get合适。
# 但get会报错 TypeError: Failed to execute 'fetch' on 'Window': Request with GET/HEAD method cannot have body.
# get请求不应该有请求体 (postman里get带请求体依然成功得到request，但openapi的文档里测试却不允许)
""" @arxiv_search_paper_api.post("/arxiv")
def search_paper(request, payload: ArxivIn):
    return arxiv_search_latest_5_papers(payload.Search) """

# 带path/query parameter
# http://127.0.0.1:8000/api/arxiv?search_content=smart%20contract
# post因为把搜索的论文数据写入数据库，语义上是post
@arxiv_search_paper_api.post("/arxiv")
def search_paper(request, search_content: str):
    return arxiv_search_latest_5_papers(search_content)