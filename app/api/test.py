import time

import openai
from flask import Response

from . import api_blueprint


def chat(message="800字文章"):
    start_time = time.time()
    # openai.organization = "org-f1KDKRG42NVHbqTJ1nGnqmDl"
    openai.api_key = ""
    response = chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
        temperature=0,
        stream=True,
    )
    collected_chunks = []
    collected_messages = []
    for chunk in response:
        chunk_time = time.time() - start_time
        collected_chunks.append(chunk)
        chunk_message = chunk["choices"][0]["delta"]
        collected_messages.append(chunk_message)
        yield chunk_message.get("content", "")
        # print(f"Message received {chunk_time:.2f} seconds after request: {chunk_message}")
    # return collected_messages


@api_blueprint.route("test")
def stream_api():
    return Response(chat(), content_type="text/event-stream")
