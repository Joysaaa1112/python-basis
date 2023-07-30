import json

from . import api_blueprint


@api_blueprint.route("/test")
def index():
    return json.dumps({"code": 0, "data": {}, "msg": "success"})
