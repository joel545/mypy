import openai
import openai.error
import pandas as pd

#設定API KEY
openai.api_key='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'

data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-03'],
    'Product': ['Product A', 'Product B', 'Product A', 'Product B', 'Product A', 'Product B'],
    'Sales': [150, 100, 200, 120, 180, 110]
}

df=pd.DataFrame(data)

#將資料轉為文字格式,當作提示prompt 傳給chatgpt
data_text=df.to_string(index=False)

prompt=f'以下是銷售資料\n{data_text}\n\n根據這些資料,請告訴我哪些產品銷售表現最好,並解釋為什麼'


#使用try...except 處理API的錯誤
try:
    response=openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'system','content':'您是我的好朋友,也是好幫手'},
            {'role':'user','content':prompt}
        ],
        max_tokens=100, #最高回應字數
        temperature=0.7 # 控制創造性的程度
    )
    analysis=response['choices'][0]['message']['content']
    print(analysis)
except openai.error.APIError as e:
    print(f"API ERROR: {e}")
except Exception as e:
    print(f"ERROR : {e}")
   

print('雖然ChatGPT 不理我,但我還在....沒有當機...')
