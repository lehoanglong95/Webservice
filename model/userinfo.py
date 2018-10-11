class UserInfo:
    def __init__(self, result):
        self.msisdn = result[0]
        self.fb_id = result[1]
        self.gender = result[2]
        self.dob = result[3]
        self.name = result[4]
        self.province = result[5]
        self.district = result[6]
        self.ward = result[7]

def take_list_userinfo_from_resultsql_list(results):
    res = []
    if len(results) != 0:
        for result in results:
            for user_result in result:
                try:
                    user_info = UserInfo(user_result)
                    res.append((user_info.msisdn, user_info.fb_id, user_info.gender, user_info.dob, user_info.name,
                                user_info.province, user_info.district, user_info.ward))
                except:
                    continue
    return res