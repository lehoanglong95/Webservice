from hash_code_helper import hash_code_phone_number, hash_code_fb_id
from model.userinfo import take_list_userinfo_from_resultsql_list
from csv_helper import take_data_list_from_csv, write_csv_from_tuple
from locationmapping import location_mapping

class DataTaker:
    def __init__(self, request_data, sql_manager, provinces, districts):
        self.request_data = request_data
        self.sql_manager = sql_manager
        self.provinces = provinces
        self.districts = districts

    def take_data(self):
        data_list = take_data_list_from_csv(self.request_data.file_location)
        if self.request_data.type == "fb":
            self.take_data_from_fb_and_write_to_csv(data_list)
        else:
            self.take_data_from_phone_and_write_to_csv(data_list)

    def take_data_from_phone_and_write_to_csv(self, data_list):
        hash_coded_phone_list = hash_code_phone_number(data_list)
        results = self.sql_manager.take_data_from_phone_list(hash_coded_phone_list, self.request_data.gender,
                                                        self.request_data.location, self.request_data.age, self.request_data.limit)
        res = take_list_userinfo_from_resultsql_list(results)
        location_mapping_res = location_mapping(res, self.provinces, self.districts)
        write_csv_from_tuple(location_mapping_res, "/home/longle/Desktop/result{}.csv".format(self.request_data.id))

    def take_data_from_fb_and_write_to_csv(self, data_list):
        hash_coded_fb_ids = hash_code_fb_id(data_list)
        results = self.sql_manager.take_msisdn_from_fbid(hash_coded_fb_ids)
        res = []
        if len(results) != 0:
            for result in results:
                for fb_id_result in result:
                    try:
                        res.append(fb_id_result[0])
                    except:
                        continue
        self.take_data_from_phone_and_write_to_csv(res)