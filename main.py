from flask import jsonify

import config
from app import create_app

# 创建应用 1
app = create_app(config)


@app.route("/")
def route_map():
    """
    主视图，返回所有视图网址
    """
    rules_iterator = app.url_map.iter_rules()
    return jsonify(
        {
            rule.endpoint: rule.rule
            for rule in rules_iterator
            if rule.endpoint not in ("route_map", "static")
        }
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
