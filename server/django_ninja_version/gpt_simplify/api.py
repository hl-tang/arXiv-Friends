from ninja import Router
from .models import Paper, SimplifyAbstract
from .schemas import GPTSimplifyIn
from deep_translator import GoogleTranslator
from .gpt_operate import gpt_simplify_ja, gpt_extract_5_keywords
from user_authentication.models import UserBrowsePaperHistory, TouristSession

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
# @gpt_simplify_api.post("/simplify")


def translate_and_simplify_abstract(request, payload: GPTSimplifyIn):
    # 因为点击了详细页面，count+1
    clicked_paper = Paper.objects.filter(paper_id=payload.paper_id).first()
    clicked_paper.clicked_count += 1
    clicked_paper.save()

    # 如果数据库里已经存在，那直接返回，不必再问GPT (count+1)
    existing_simplified_abstract = SimplifyAbstract.objects.filter(
        paper_id=payload.paper_id
    ).first()

    if existing_simplified_abstract:
        return {
            "paper_id": clicked_paper.paper_id,
            "content_en": payload.content_en,
            "content_ja": existing_simplified_abstract.content_ja,
            "content_plain": existing_simplified_abstract.content_plain,
            # "Keywords": existing_paper.keywords_list,
            "clicked_count": clicked_paper.clicked_count
        }

    # 若不存在，则问gpt，然后数据库保存这条记录
    # 先翻译abstract
    content_ja = GoogleTranslator(
        source='en', target='ja').translate(text=payload.content_en)
    # GPT简化
    content_plain = gpt_simplify_ja(content_ja)
    print(content_plain)
    # GPT提取5个关键词
    # keywords_list = gpt_extract_5_keywords(content_ja)
    # 创建一条记录 (payload的字段名和数据库的字段名不一致，没法用payload.dict())
    # 不然可以 payload_dict = payload.dict(), payload_dict['other_field1'] = 'value1' 少写点dirty work
    simplified_abstract = SimplifyAbstract.objects.create(
        paper_id=payload.paper_id,
        content_ja=content_ja,
        content_plain=content_plain,
        # keywords_list = keywords_list,
    )
    return {
        "paper_id": clicked_paper.paper_id,
        "content_en": payload.content_en,
        "content_ja": content_ja,
        "content_plain": content_plain,
        # "Keywords": keywords_list,
        "clicked_count": clicked_paper.clicked_count
    }


@gpt_simplify_api.post("/simplify")
def simplify_access(request, payload: GPTSimplifyIn):
    if request.user.is_authenticated:
        # create参数严格要和数据库里的一样，和model定义的一样没用，按数据库的字段名为准 _id_id
        # 已经在历史里就不要再添加了
        if not UserBrowsePaperHistory.objects.filter(user_id=request.user.id, paper_id=payload.paper_id).exists():
            UserBrowsePaperHistory.objects.create(
                user_id=request.user.id, paper_id=payload.paper_id)
        return translate_and_simplify_abstract(request, payload)
    else:
        # 游客24内只能使用api3次
        return {
            "paper_id": payload.paper_id,
            "content_en": payload.content_en,
            "content_ja": None, # ninja的修饰器自动把dict转成json了 None->null
            "content_plain": None,
            "msg": "tourist access can only access 3 times in 24h"
        }


# 关键词一方面gpt不安定，一方面不实用，打算把关键词展示栏换成用户写笔记,笔记作为浏览历史的弱实体
""" @gpt_simplify_api.post("/keywords")
def gpt_get_keywords():
    pass """
