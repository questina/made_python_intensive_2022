from typing import List


def find_anagrams(text: str, pattern: str) -> List[int]:
    """
    This function finds the positions in text for anagrams of input pattern
    :param text: input text, where to find anagrams
    :param pattern: pattern, which anagrams needs to find in text
    :return: array of positions of start of the anagram string
    """
    if len(pattern) == 0 or len(text) == 0:
        return []

    ans = []
    cnt_dict = {}
    for char in pattern:
        cnt_dict[char] = cnt_dict.get(char, 0) + 1
    j = 0
    i = 0
    cnt = len(cnt_dict)
    while j < len(text):
        if text[j] in cnt_dict:
            cnt_dict[text[j]] -= 1
            if cnt_dict[text[j]] == 0:
                cnt -= 1
        if j - i + 1 < len(pattern):
            j += 1
        elif j - i + 1 == len(pattern):
            if cnt == 0:
                ans.append(i)
            if text[i] in cnt_dict:
                cnt_dict[text[i]] += 1
                if cnt_dict[text[i]] == 1:
                    cnt += 1
            i += 1
            j += 1
    print(ans)
    return ans
