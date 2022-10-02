from unpack_json import parse_json


def run_test_unpack_json():

    def callback_function(keyword):
        cnt_keywords[keyword] = cnt_keywords.get(keyword, 0) + 1

    json_str = '{"fruits": "apple pineapple plum orange apple", "juice": "apple orange grape tomato carrot tomato", ' \
               '"vegetables": "tomato potato cucumber tomato"} '

    cnt_keywords = {}
    parse_json(json_str=json_str, keyword_callback=callback_function, required_fields=["juice", "fruits"],
               keywords=['apple', 'plum', 'pineapple'])

    assert cnt_keywords == {'apple': 3, 'pineapple': 1, 'plum': 1}

    cnt_keywords = {}
    parse_json(json_str=json_str, keyword_callback=callback_function, required_fields=["vegetables", "fruits"],
               keywords=['tomato', 'plum', 'carrot'])

    assert cnt_keywords == {'tomato': 2, 'plum': 1}

    cnt_keywords = {}
    parse_json(json_str=json_str, keyword_callback=callback_function, required_fields=["vegetables", "juice"],
               keywords=['tomato', 'plum', 'carrot', 'grape'])

    assert cnt_keywords == {'tomato': 4, 'carrot': 1, 'grape': 1}

    cnt_keywords = {}
    parse_json(json_str="{}", keyword_callback=callback_function, required_fields=["vegetables", "juice"],
               keywords=['tomato', 'plum', 'carrot', 'grape'])

    assert cnt_keywords == {}

    cnt_keywords = {}
    parse_json(json_str=json_str, keyword_callback=callback_function, required_fields=["food", "drinks"],
               keywords=['tomato', 'plum', 'carrot', 'grape'])

    assert cnt_keywords == {}

    cnt_keywords = {}
    parse_json(json_str=json_str, keyword_callback=callback_function, required_fields=["fruits", "vegetables"],
               keywords=['grape', 'banana', 'coconut'])

    assert cnt_keywords == {}

    cnt_keywords = {}
    parse_json(json_str=json_str, keyword_callback=callback_function, required_fields=[],
               keywords=['grape', 'banana', 'coconut'])

    assert cnt_keywords == {}

    cnt_keywords = {}
    parse_json(json_str=json_str, keyword_callback=callback_function, required_fields=["fruits", "vegetables"],
               keywords=[])

    assert cnt_keywords == {}


def run_test_avg_time():
    pass


def run_tests():
    run_test_unpack_json()
    run_test_avg_time()
    print("Passed all tests !")


if __name__ == "__main__":
    run_tests()
