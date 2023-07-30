import json

from lang import lang
from . import api_blueprint


@api_blueprint.route("/test/index", methods=["GET"])
def index():
    print(lang("200"))
    return json.dumps({"code": 0, "data": {}, "msg": ""})
