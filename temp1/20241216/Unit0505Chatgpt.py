import openai
import openai.error   #pip install openai

#設定API KEY
openai.api_key='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'

#讀取coffee.txt 的內容
with open('coffee.txt','r',encoding='utf-8') as f:  #將檔案讀取後,指定給f物件
    txt=f.read()

try:
    #第一件事情,內容摘要
    response=openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{
            'role':'user',
            'content':f'請將內容進行摘要：{txt}'
        }],
        max_tokens=100, 
        temperature=0.7    
    )

    # summary=response['choices'][0]['message']['content'].strip()
    summary=response['choices'][0].message.content.strip()  #摘要後指定給summary

    #將摘要結果寫入 summary.txt
    with open('summary.txt','w',encoding='utf-8') as wf:  #將檔案寫入後,指定給wf物件
        wf.write(summary)   #將summary 變數內容寫入到summary.txt

    print("摘要結果：")
    print(summary)  

    #第二件事情,依照摘要,生成文章
    response2=openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{
            'role':'user',
            'content':f'依照摘要,撰寫一篇具結構性的文章：{summary}'
        }],
        max_tokens=100, 
        temperature=0.7    
    )
    article=response2['choices'][0].message.content.strip() #生成文章後,指定給article

    #將文章寫到article.md (md,markdown)檔案
    with open('article.md','w',encoding='utf-8') as wf2:
        wf2.write(article)  #將article 的內容寫入到article.md 檔案

    print("新生成的文章是：")
    print(article)
except openai.error.AuthenticationError:
    print( "ERROR:API KEY 無效或是沒有設定,請查看API KEY...")
except openai.error.RateLimitError:
    print( "ERROR:已經到使用速率上限或額度,請稍後再試或檢查您的帳單...")
except openai.error.APIConnectionError:
    print( "ERROR:沒辦法連接到OPEN AI, 檢查一下您的網路吧...")
except openai.error.OpenAIError as e:
    print( f"ERROR: API 錯誤 {e}")
except Exception as ex:
    print( f'不知道發生什麼事了,{ex}')

