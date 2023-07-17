from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .api_call import search_paper, paper_detail
from .operate_database import search_titles, search_papers, add_title, add_content

from pdb import set_trace

# Arxiv_Searchのgetメソッドを用いたDebug用 
search = {
    "Search": "LLM cat:cs.CL"
}

# Create your views here.
class Arxiv_Search(APIView):
    def get(self, request):
        return Response("OK", status=status.HTTP_200_OK)
        # return Response(search_paper.main(search["Search"]))
    
    def post(self, request, *args, **kwargs):
        search_word = request.data
        # return Response(search_paper.main(search_word["Search"]))

        search_result_list = search_paper.get_papers(search_word['Search'])

        # 5つの論文の検索結果を返す
        search_list = []
        for paper in search_result_list:
            # Paper_IDを取得
            paper_id = paper["Paper_ID"]
            # 既に論文があればそのまま取得、なければ空のjson(=まだ検索されたことのない論文)を返す。
            paper_json = search_titles(paper_id)

            # 空のjson(=まだ検索されたことのない論文)ならば、DeepLを用いて日本語を追加したjsonを返す。
            if len(paper_json)==0:
                paper_json = search_paper.add_ja_title(paper)
                # データベースに追加
                # add_title(paper_json)
            
            # リストに追加
            search_list.append(paper_json)
        
        return Response(search_list)
        

# Paper_detailのgetメソッドを用いたDebug用  
contents =  {
        "Paper_ID": "http://arxiv.org/abs/2307.04721v1",
        "Title_En": "Large Language Models as General Pattern Machines",
        "Content_En": "We observe that pre-trained large language models (LLMs) are capable ofautoregressively completing complex token sequences -- from arbitrary onesprocedurally generated by probabilistic context-free grammars (PCFG), to morerich spatial patterns found in the Abstract Reasoning Corpus (ARC), a generalAI benchmark, prompted in the style of ASCII art. Surprisingly, patterncompletion proficiency can be partially retained even when the sequences areexpressed using tokens randomly sampled from the vocabulary. These resultssuggest that without any additional training, LLMs can serve as generalsequence modelers, driven by in-context learning. In this work, we investigatehow these zero-shot capabilities may be applied to problems in robotics -- fromextrapolating sequences of numbers that represent states over time to completesimple motions, to least-to-most prompting of reward-conditioned trajectoriesthat can discover and represent closed-loop policies (e.g., a stabilizingcontroller for CartPole). While difficult to deploy today for real systems dueto latency, context size limitations, and compute costs, the approach of usingLLMs to drive low-level control may provide an exciting glimpse into how thepatterns among words could be transferred to actions.",
        "Categories": [
            "Artificial Intelligence",
            "Computation and Language",
            "Robotics"
        ],
        "Authors": [
            "Suvir Mirchandani",
            "Fei Xia",
            "Pete Florence",
            "Brian Ichter",
            "Danny Driess",
            "Montserrat Gonzalez Arenas",
            "Kanishka Rao",
            "Dorsa Sadigh",
            "Andy Zeng"
        ],
        "Pdf_url": "http://arxiv.org/pdf/2307.04721v1",
        "Published": "2023-07-10T17:32:13Z",
        "Title_Ja": "一般的なパターン・マシンとしての大規模言語モデル"
    }

class Paper_detail(APIView):
    def get(self, request):
        return Response("OK", status=status.HTTP_200_OK)
        # return Response(paper_detail.main(contents))
    
    def post(self, request, *args, **kwargs):
        search_paper_json = request.data
        # return Response(paper_detail.main(search_json))
        
        # Paper_IDを取得
        paper_id = search_paper_json["Paper_ID"]
        # 既に日本語付き論文があればそのまま取得、なければ空のjson(=まだ検索されたことのない論文)を返す。

        paper_plusJa_json = search_papers(paper_id)


        # 空のjson(=まだ検索されたことのない論文)ならば、DeepLを用いて日本語の概要を追加したjsonを返す。
        if len(paper_plusJa_json)==0:
            paper_plusJa_json = search_paper.add_ja_title(search_paper_json)
            # データベースに追加
            # add_content_keywords(paper_plusJa_json)
        
        return Response(paper_plusJa_json)