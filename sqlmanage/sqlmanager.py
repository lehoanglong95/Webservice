from sqlmanage.sqlhelper import SqlHelper

class SqlManager:

     def __init__(self, app):
         self.sql_helper = SqlHelper(app)

     def take_data_from_phone_list(self, phone_list):
        # phone list is 2d list of phone with phone_list[index] contains all phone which have hash code is index
        results = []
        for index, hash_coded_phone in enumerate(phone_list):
            if len(hash_coded_phone) != 0:
                new_phone_list = "(" + ",".join("'" + str(x)[0:len(str(x))] + "'" for x in hash_coded_phone) + ")"
                result = self.sql_helper.query_by_id(new_phone_list, index)
                results.append(result)
        return results