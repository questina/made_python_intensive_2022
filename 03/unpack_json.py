import json
from typing import Callable, List


def parse_json(json_str: str, keyword_callback: Callable,
               required_fields: List[str] = None, keywords: List[str] = None) -> None:
    """
    Function parses json and send specific json field with specific value to another function,
    which calculates some statistic
    :param json_str: input json as a string
    :param keyword_callback: function, which calculates statistic
    :param required_fields: specific json fields to calculate statistic
    :param keywords: specific values of required fields to calculate statistic
    :return: None
    """
    json_doc = json.loads(json_str)
    for field in json_doc:
        if field in required_fields:
            for keyword in json_doc[field].split():
                if keyword in keywords:
                    keyword_callback(keyword)
