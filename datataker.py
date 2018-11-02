from hash_code_helper import hash_code_phone_numbers, hash_code_fb_ids
from model.userinfo import take_list_userinfo_from_resultsql_list
from csv_helper import take_data_list_from_csv, write_csv_from_tuple
from locationmapping import location_mapping
from csv_helper import take_data_list_from_csv

class DataTaker:
    def __init__(self, request_data, sql_manager, provinces, districts):
        self.request_data = request_data
        self.sql_manager = sql_manager
        self.provinces = provinces
        self.districts = districts

    # def take_data(self):
    #     data_list = take_data_list_from_csv(self.request_data.file_location)
    #     if self.request_data.type == "fb":
    #         return self.take_data_from_fb_and_write_to_csv(data_list)
    #     else:
    #         return self.take_data_from_phone_and_write_to_csv(data_list)

    def take_data_from_db_and_write_to_csv(self, data_list):
        hash_coded_phone_list = hash_code_phone_numbers(data_list)
        print("location {}".format(self.request_data.location))
        results = self.sql_manager.take_data_from_phone_list(hash_coded_phone_list, self.request_data.gender,
                                                             self.request_data.location, self.request_data.age,
                                                             self.request_data.limit)
        if len(results) != 0:
           res = take_list_userinfo_from_resultsql_list(results)
           location_mapping_res = location_mapping(res, self.provinces, self.districts)
           print(location_mapping_res)
           link_download = "/usr/share/nginx/html/adv/storage/app/results/{}".format(self.request_data.file_name)
           self.sql_manager.update_request_status(self.request_data.id, link_download, len(data_list), len(location_mapping_res))
           write_csv_from_tuple(location_mapping_res, link_download)
           return "success"
        else:
           print("aaa")
           return "we cant find your data"

    def take_data_from_phone_and_write_to_csv(self):
       data_list = take_data_list_from_csv(self.request_data.file_location)
       if data_list == "file is not exist":
           return "file is not exist"
       else:
           try:
              if self.take_data_from_db_and_write_to_csv(data_list) == "success":
                 return "success"
              else:
                 return "we cant find your data"
           except:
              return "can not take data"
       return "success"


    def take_data_from_fb_and_write_to_csv(self):
        data_list = take_data_list_from_csv(self.request_data.file_location)
        if data_list == "file is not exist":
            print("file is not exist")
            return "file is not exist"
        else:
            print("fb query...", flush=True)
            hash_coded_fb_ids = hash_code_fb_ids(data_list)
            results = self.sql_manager.take_msisdn_from_fbid(hash_coded_fb_ids)
            res = []
            if len(results) != 0:
                for result in results:
                    for fb_id_result in result:
                        try:
                            res.append(fb_id_result[0])
                        except:
                            continue
            else:
                return "we cant find your data"
            print("phone from fb are {}".format(res), flush=True)
            try:
               if self.take_data_from_db_and_write_to_csv(res) == "success":
                 return "success"
               else:
                 return "we cant find your data"
            except:
               return "can not take data"    
        return "success"
