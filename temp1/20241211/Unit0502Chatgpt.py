import openai
import openai.error

#設定API KEY
openai.api_key='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'


#使用try...except 處理API的錯誤
try:
    response=openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'system','content':'您是我的好朋友,也是好幫手'},
            {'role':'user','content':'您好,請問冬至是什麼時候?'}
        ],
        max_tokens=100, #最高回應字數
        temperature=0.7 # 控制創造性的程度
    )
    completed_text=response['choices'][0]['message']['content']
    print(completed_text)
except openai.error.APIError as e:
    if "please check your plan and billing details" in str(e):
        print('error:請檢查您的OPEN AI 的帳單')
    else:
        print(f'API Error: {e}')

except openai.error.AuthenticationError:
    print('error: API KEY 無效,還是根本沒有設定')

except Exception as e:
    print(f'發生未知錯誤:{e}')


print('雖然ChatGPT 不理我,但我還在....沒有當機...')
