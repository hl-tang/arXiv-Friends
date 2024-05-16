import os
from dotenv import load_dotenv
from openai import OpenAI
import json

# .env放在项目根目录下, manage.py同级(其实放哪都行)
load_dotenv()

client = OpenAI(
    base_url=os.environ.get("OPENAI_PROXY_URL"),
    api_key=os.environ.get("OPENAI_API_KEY")
)


def gpt_simplify_ja(content_ja: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "次の日本語の文章を短く分かりやすくして"},
            {"role": "user", "content": content_ja}
        ]
    )
    return completion.choices[0].message.content

# txt = "不正行為を回避するには、侵入検知システム (IDS) が不可欠です。ほとんどの場合、IDS は機械学習アプローチによって改善されますが、パケット (各レコード) 内に存在するヘッダー (または特徴) が増えるため、モデルの効率は低下しています。提案されたモデルは、非負行列因数分解とカイ二乗分析を使用して実用的な特徴を抽出します。特徴の数が増えると、指数関数的な時間が増加し、モデルの過学習のリスクが増加します。両方の手法を使用して、提案されたモデルは階層的なアプローチを採用し、特徴の二次誤差とノイズを削減します。提案されたモデルは 3 つの公的に利用可能なデータセットに実装されており、大幅な改善が得られます。最近の調査によると、提案されたモデルは、NSL-KDD 2017 と CICD 2017 でそれぞれ 4.66% と 0.39% パフォーマンスが向上しました。"
# print(gpt_simplify_ja(txt))

def gpt_extract_5_keywords(content_ja: str) -> list:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "次の日本語の文章から5つのkeywordを抽出して解釈すること。このような形で返って: {\"Keyword\": \"\", \"Description\": \"\"}*5"},
            {"role": "user", "content": "各{Keyword, Description}対象の間, 空行で分断すること"},
            {"role": "user", "content": content_ja}
        ]
    )
    # return completion.choices[0].message.content
    k_d_str = completion.choices[0].message.content
    print(k_d_str)
    kd_str_list = k_d_str.split("\n")
    print(kd_str_list)
    # kd_dict_list = [json.loads(item) for item in kd_str_list] # kd_str_list: ['{"K", "D"}', '', '{"K", "D"}'], 遇到'' json.loads就bug了
    kd_dict_list = [json.loads(item) for item in kd_str_list if item.strip()] # 防止有item是空
    print(kd_dict_list)
    return kd_dict_list

# txt = "不正行為を回避するには、侵入検知システム (IDS) が不可欠です。ほとんどの場合、IDS は機械学習アプローチによって改善されますが、パケット (各レコード) 内に存在するヘッダー (または特徴) が増えるため、モデルの効率は低下しています。提案されたモデルは、非負行列因数分解とカイ二乗分析を使用して実用的な特徴を抽出します。特徴の数が増えると、指数関数的な時間が増加し、モデルの過学習のリスクが増加します。両方の手法を使用して、提案されたモデルは階層的なアプローチを採用し、特徴の二次誤差とノイズを削減します。提案されたモデルは 3 つの公的に利用可能なデータセットに実装されており、大幅な改善が得られます。最近の調査によると、提案されたモデルは、NSL-KDD 2017 と CICD 2017 でそれぞれ 4.66% と 0.39% パフォーマンスが向上しました。"
# k_d_str = gpt_extract_5_keywords(txt) #测试时return completion.choices[0].message.content
# print(k_d_str) # "{"K", "D"}\n{"K", "D"}"
# kd_str_list = k_d_str.split("\n")
# print(kd_str_list) # ['{"K", "D"}', '{"K", "D"}']
# kd_dict_list = [json.loads(item) for item in kd_str_list]
# print(kd_dict_list) # [{"K", "D"}, {"K", "D"}]

# print(gpt_extract_5_keywords(txt))
