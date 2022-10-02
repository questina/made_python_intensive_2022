import json


def parse_json(json_str: str, keyword_callback, required_fields=None, keywords=None):
    json_doc = json.loads(json_str)
    for field in json_doc:
        if field in required_fields:
            for keyword in json_doc[field].split():
                if keyword in keywords:
                    keyword_callback(keyword)
