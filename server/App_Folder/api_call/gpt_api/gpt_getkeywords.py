# 環境変数にAPIキーを設定
import os
from dotenv import load_dotenv
import openai
from pathlib import Path
import json
import time


load_dotenv(Path(__file__).parent.parent.joinpath(".env"))
openai.api_key = os.environ["OPENAI_API_KEY"]

# Textを受け取りキーワードと説明文のリストを返す
def keywords(content):
  time_sta = time.time()
  schema = {
  "type": "object",
  "properties": {
       "keywords_list": {
      "type": "array",
      "description": "Important Japanese key words in the abstract.",
      "items": { "type": "string" }
    },
    "keywords_description_list": {
      "type": "string",
      "description": "The explanation of Japanese key words."
    }
  },
  "required": ["keywords_list","keywords_description_list"]
}
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[
      {"role": "system", "content": "You are an expert in the field of this paper."},
      {"role": "user", "content": "Please extract five technical terms that are necessary to understand the following paper and prepare a description of them in Japanese.\n"+ content}
    ],
    functions=[{"name": "set_keywords", "parameters": schema}],
    function_call={"name": "set_keywords"},
    temperature=0,
  )
  try:
    result = json.loads(completion.choices[0].message.function_call.arguments)
  except:
    print("error")
    result = "gpt error"
    print(completion.choices[0].message.function_call.arguments)
    
  time_end = time.time()
  # 経過時間（秒）
  tim = time_end- time_sta
  print(tim)
  print(result)
  return(result)

# # Example Usage
# Text = 'D-AgreeはBERTを用いたオンライン議論プラットフォームです。ファシリテーションエージェントが議論中の投稿をIBIS構造に基づき分類し、合意形成のための適切なファシリテーションを行います'
# keywords(Text)

