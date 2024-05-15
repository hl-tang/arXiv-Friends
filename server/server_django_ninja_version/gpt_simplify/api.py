from ninja import Router
from .models import ClickedPaper
from .schemas import GPTSimplifyIn, GPTSimplifyOut
from deep_translator import GoogleTranslator
from .gpt_operate import gpt_simplify_ja, gpt_extract_5_keywords

gpt_simplify_api = Router()

""" 这里也许是整个项目最难的点了
作法:先不要创建数据库记录,测试payload格式是否正常(特别注意authors和Categories是list对应JSONField(), SchemaIn应该是list而非str)
然后response先别SchemaOut, 自己写return灵活一点
可以先硬编码, 测试api是否正常に動ける
交互格式无误后,封装gpt处理函数
测试ok后, 再创建数据库记录
最后可以再SchemaOut规定输出json格式 (数据库字段名和返回json的key名不同,估计不能用SchemaOut)
"""

# extract_5_keywords可能不安定，拆成两个API(这样需要拆论文表了，把简化摘要和关键词作为论文表的弱entity)
@gpt_simplify_api.post("/simplify")
def gpt_simplify(request, payload: GPTSimplifyIn):
    # 如果数据库里已经存在，那直接返回，不必再问GPT (count+1)
    existing_paper = ClickedPaper.objects.filter(
        paper_id = payload.Paper_ID
    ).first()

    if existing_paper:
        existing_paper.clicked_count += 1
        existing_paper.save()
        return {
            "paper_id": existing_paper.paper_id,
            "Content_En": payload.Content_En,
            "Content_Ja": existing_paper.content_ja,
            "Content_plain": existing_paper.content_plain,
            "Keywords": existing_paper.keywords_list,
            "clicked_count": existing_paper.clicked_count
        }

    # 若不存在，则问gpt，然后数据库保存这条记录(clicked_count默认为1)
    # 先翻译abstract
    content_ja = GoogleTranslator(
        source='en', target='ja').translate(text=payload.Content_En)
    # GPT简化
    content_plain = gpt_simplify_ja(content_ja)
    # GPT提取5个关键词
    keywords_list = gpt_extract_5_keywords(content_ja)
    # 创建一条记录 (payload的字段名和数据库的字段名不一致，没法用payload.dict())
    # 不然可以 payload_dict = payload.dict(), payload_dict['other_field1'] = 'value1' 少写点dirty work
    clicked_paper = ClickedPaper.objects.create(
        paper_id = payload.Paper_ID,
        title_en = payload.Title_En,
        title_ja = payload.Title_Ja,
        author = payload.Authors,
        categories = payload.Categories,
        published = payload.Published,
        content_en = payload.Content_En,
        pdf_url = payload.Pdf_url,
        content_ja = content_ja,
        content_plain = content_plain,
        keywords_list = keywords_list,
        # count默认1
    )
    return {
        "paper_id": clicked_paper.paper_id,
        "Content_En": payload.Content_En,
        "Content_Ja": content_ja,
        "Content_plain": content_plain,
        "Keywords": keywords_list,
        "clicked_count": clicked_paper.clicked_count
    }
