from django.test import TestCase

# Create your tests here.


import openai

openai.api_key = "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"

model_engine = "text-davinci-002"
prompt = "我的女朋友叫李白，请你写一封100字的情书"

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,
)

message = completions.choices[0].text
print(message)