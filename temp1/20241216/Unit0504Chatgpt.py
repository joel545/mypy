import openai
import openai.error   #pip install openai

#設定API KEY
openai.api_key='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'


#第一則訊息為system 訊息,用於設定機器人角色的風格
history=[
    {"role":"system",
     "content":"Hello,我的助理，請以簡潔的方式回答問題。"}
]

def chat_gpt(userInput):
    #將使用者輸入的內容,附加到歷史對話
    history.append({
        "role":"user",
        "content":userInput
    })

    try:
        response=openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=history,
            max_tokens=100, 
            temperature=0.7             
        )
        #取得模型回應
        reply=response['choices'][0]['message']['content'].strip()

        #把回應的內容附到歷史對話
        history.append({
            "role":"assistant",
            "content":reply
        })
        return reply
    except openai.error.AuthenticationError:
        return "ERROR:API KEY 無效或是沒有設定,請查看API KEY..."
    except openai.error.RateLimitError:
        return "ERROR:已經到使用速率上限,請等等,稍後再試..."
    except openai.error.APIConnectionError:
        return "ERROR:沒辦法連接到OPEN AI, 檢查一下您的網路吧..."
    except openai.error.OpenAIError as e:
        return f"ERROR: API 錯誤 {e}"
    except Exception as ex:
        return f'不知道發生什麼事了,{ex}'
    

if __name__=="__main__":
    print("歡迎來到Bumblebee Robot 聊天室，請輸您想說的八卦,\n也可以輸入「exit」 或 「quit」 say 881!")
    while True:
        userInput=input("使用者：").strip()
        if userInput.lower() in ["exit","quit"]:
            print('Bumblebee: 881, 下次再見')
            break   #離開迴圈,不會再回來了
        response=chat_gpt(userInput)
        print(f"Bumblebee:{response}")



