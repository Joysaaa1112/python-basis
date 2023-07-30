from zh_cn import lang as zh_cn_lang

# Path: lang\__init__.py


current_lang = "zh_cn"


def lang(code=None):
    if current_lang == "zh_cn":
        return zh_cn_lang["error_codes"].get(code, None)
