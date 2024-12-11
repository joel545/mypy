import openai
#設定api key
api_key="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"
response= openai.completions.create(
    engine+"gpt-3.5-turbo",
    prompt="您好，請問冬至是什麼時候。"
    
)