def get_longest_substring(input_str: str):
    if not bool(input_str):
        return None
    elif len(input_str) == 1:
        return input_str

    if len(input_str) == 2:
        if input_str[0] == input_str[1]:
            return input_str
        else:
            return None

    start = 0
    end = 0
    for i in range(0, len(input_str)):
        len1 = expand_from_middle(input_str, i, i)
        len2 = expand_from_middle(input_str, i, i + 1)
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - ((max_len - 1) // 2)
            end = i + (max_len // 2)

    return input_str[start:end + 1]


def expand_from_middle(in_str, left, right):
    if not bool(in_str) or left > right:
        return 0
    while left >= 0 and right < len(in_str) and in_str[left] == in_str[right]:
        left -= 1
        right += 1
    return right - (left + 1)
