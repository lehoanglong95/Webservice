def java_string_hashcode(s):
    h = 0
    for c in s:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000


def partition(s):
    raw_code = java_string_hashcode(s) % 20
    if raw_code < 0:
        raw_code = raw_code + 20
    return raw_code

def hash_code_phone_number(phone_list):
    result = [[]]
    for _ in range(0, 20):
        result.append([])
    for phone in phone_list:
        code = partition((phone))
        result[code].append(phone)
    return result