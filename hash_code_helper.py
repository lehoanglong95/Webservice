def java_string_hashcode(s):
    h = 0
    for c in s:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000

def base_partition(s, number_partition):
    raw_code = java_string_hashcode(s) % number_partition
    if raw_code < 0:
        raw_code = raw_code + number_partition
    return raw_code

def msisdn_partition(s):
    return base_partition(s, 20)

def fbid_partition(s):
    return base_partition(s, 10)

def hash_code_phone_numbers(phone_list):
    result = [[]]
    for _ in range(0, 20):
        result.append([])
    for phone in phone_list:
        code = msisdn_partition(phone)
        result[code].append(phone)
    return result

def hash_code_fb_ids(fb_ids):
    result = [[]]
    for _ in range(0, 10):
        result.append([])
    for fb_id in fb_ids:
        code = fbid_partition(fb_id)
        result[code].append(fb_id)
    return result