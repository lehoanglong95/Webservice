from flask import Flask, request
from sqlmanage.sqlmanager import SqlManager
from model.requestdata import RequestData
from hash_code_helper import hash_code_phone_number
from model.userinfo import take_list_userinfo_from_resultsql_list
from csv_helper import take_phone_list_from_csv, write_csv_from_tuple
from locationmapping import location_mapping

app = Flask("This is my first Flask App")

sql_manager = SqlManager(app)
(province_lists, district_lists) = sql_manager.take_location()

@app.route("/", methods=['GET'])
def home():
    return "Hello this is home page"

@app.route("/phonetofb/", methods=['POST'])
def phone_to_fb():
    request_data = RequestData(request.data)
    phone_list = take_phone_list_from_csv(request_data.file_location)
    hash_coded_phone_list = hash_code_phone_number(phone_list)
    results = sql_manager.take_data_from_phone_list(hash_coded_phone_list, request_data.gender, request_data.location, request_data.age, request_data.limit)
    res  = take_list_userinfo_from_resultsql_list(results)
    location_mapping_res = location_mapping(res, province_lists, district_lists)
    write_csv_from_tuple(location_mapping_res, "/home/longle/Desktop/result{}.csv".format(request_data.id))
    return "Success"

if __name__== '__main__':
    app.run(debug=True)