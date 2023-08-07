import os
import openai
from config import apikey
#print(apikey)
#exit()
# openai.api_key = 1

openai.api_key = apikey

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  prompt="write a story for me",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)