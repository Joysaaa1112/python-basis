import time

import openai

from . import api_blueprint


def test():
    openai.organization = "org-f1KDKRG42NVHbqTJ1nGnqmDl"
    openai.api_key = "sk-xxx"
    print(openai.Model.list())


def stream():
    count = 0
    for i in range(10):
        time.sleep(0.5)
        count += i
        data = f"data: {count}\n\n"
        yield data


@api_blueprint.route("test")
def stream_api():
    test()
    return ""
    # return Response(stream(), content_type="text/event-stream")
