import os
import openai
import json
#import numpy as np
#from numpy.linalg import norm
import re
from time import time,sleep
#from uuid import uuid4
#import datetime


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
        return infile.read()


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


def chatgpt_completion(messages, temp=0, model="gpt-4"):
    max_retry = 7
    retry = 0
    while True:
        try:
            response = openai.ChatCompletion.create(model=model, messages=messages, temperature=temp)
            text = response['choices'][0]['message']['content']
            filename = 'chat_%s_muse.txt' % time()
            if not os.path.exists('chat_logs'):
                os.makedirs('chat_logs')
            save_file('chat_logs/%s' % filename, text)
            return text
        except Exception as oops:
            retry += 1
            if retry >= max_retry:
                print(f"Exiting due to an error in ChatGPT: {oops}")
                exit(1)
            print(f'Error communicating with OpenAI: "{oops}" - Retrying in {2 ** (retry - 1) * 5} seconds...')
            sleep(2 ** (retry - 1) * 5)


if __name__ == "__main__":
    openai.api_key = open_file('key_openai.txt')
    summaries_dir = "post_ideas"
    prompt = "Starting from the first ever post generate 50 Facebook post ideas for a _______ business."
    conversation = list()
    conversation.append({'role': 'system', 'content': '''I am a content generator for Facebook posts that will always provide creative, and engaging content.'''})
    conversation.append({'role': 'user', 'content': prompt})
    summary = chatgpt_completion(conversation)
    print('\n\n\n\n', summary)
    save_file(os.path.join(summaries_dir), summary)