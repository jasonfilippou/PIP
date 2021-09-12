from collections import Set
from typing import List


def _differ_by_one(str1, str2):
    assert str1 is not None and str2 is not None, "Don't give me trash input, please"
    try:
        len(str1) + len(str2)
    except ValueError:
        raise AssertionError("We were given a non-iterable in our input.")
    if abs(len(str1) - len(str2)) >= 2:
        return False
    elif str1 == str2:
        return  True
    str1, str2 = sorted(str1.strip()), sorted(str2.strip())
    (str1, str2) = (str2, str1) if len(str1) >= len(str2) else (str1, str2)     # str1 will now be the shortest of the two strings, if one of them is actually shorter than the other!
    found_difference = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:          # detected a difference of character. str2[i] is guaranteed to be a safe access since str1 is either one char shorter or exactly as long as str2
            if found_difference:        # If there's already one difference, buh-bye
                return False
            else:
                found_difference = True
    if not found_difference and len(str2) == len(str1) + 1:
        return True
    else:
        return found_difference


def _generate_all_candidates(string: str) -> List[str]:
    ret_val = set()
    for ch in _lowercase_english_chars():
        ret_val.add(ch + string)
        ret_val.add(string + ch)
    for i in range(len(string)):
        ret_val.add(string[:i] + string[i + 1:])                # Don't forget the neighbor that consists of the string itself minus the current character!
        for ch in _lowercase_english_chars():
            ret_val.add(string[:i] + ch + string[i:])           # One character added!
            if ch != string[i]:
                ret_val.add(string[:i] + ch + string[i + 1:])   # One character changed!
    return ret_val


def _lowercase_english_chars():
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


if __name__ == '__main__':
    # strings = [("jason", "mason"),
    #            ("jason", "masok"),
    #            ("berber", "berbe"),
    #            ("berber", "berba"),
    #            ("rick", "ricks"),
    #            ("rick", "aricks"),
    #            ("rick", "morty"),
    #            ("pencil", "pencil")]
    #
    # for (str1, str2) in strings:
    #     print(f"{str1} and {str2} differ by one: {_differ_by_one(str1, str2)}.")

    print(_generate_all_candidates("a"))
    print(_generate_all_candidates("ab"))
    print(_generate_all_candidates("abc"))
