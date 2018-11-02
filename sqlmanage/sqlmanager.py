from sqlmanage.sqlhelper import SqlHelper

class SqlManager:

     def __init__(self, app):
         self.sql_helper = SqlHelper(app)

     def take_data_from_phone_list(self, phone_list, gender, locations, age, limit):
        # phone list is 2d list of phone with phone_list[index] contains all phone which have hash code is index
        results = []
        print(phone_list,flush=True)
        for index, hash_coded_phone in enumerate(phone_list):
            if len(hash_coded_phone) != 0:
                try:
                    result = self.sql_helper.user_data_query_by(hash_coded_phone, gender, locations, age, limit, index)
                    results.append(result)
                except:
                    continue
        return results

     def take_location(self):
         province_lists = {}
         district_lists = {}
         results = self.sql_helper.location_query()
         for result in results:
             province_lists[int(result[2])] = str(result[3])
             district_lists[int(result[0])] = str(result[1])
         return (province_lists, district_lists)

     def take_msisdn_from_fbid(self, fb_ids):
         results = []
         for index, hash_coded_fb_id in enumerate(fb_ids):
             if len(hash_coded_fb_id) != 0:
                 result = self.sql_helper.msisdn_query_by(hash_coded_fb_id, index)
                 results.append(result)
         return results

     def update_request_status(id, link_download,number_import, success_import):
         print("a")
         self.sql_helper.update_request_status(id, link_download, number_import, success_import)
