from flask import Flask, request
from sqlmanage.sqlmanager import SqlManager
import json
from hash_code_helper import hash_code_phone_number
from model.userinfo import UserInfo, take_list_userinfo_from_resultsql_list
from csv_helper import take_phone_list_from_csv, write_csv_from_tuple

app = Flask("This is my first Flask App")

sql_manager = SqlManager(app)

@app.route("/", methods=['GET'])
def home():
    return "Hello this is home page"

@app.route("/phonetofb/", methods=['POST'])
def phone_to_fb():
    if request.method == 'POST':
        json_result = json.loads(request.data)
        print(json_result['id'])
        print(json_result['file_location'])
        print(type(json_result['location']))
        # try:
        #     age = json_result['age']
        # except:
        #     pass
        # id = request.args.get('id')
        # file_location = request.args.get('file_location')
        # print(id)
        # print(file_location)
    # new_file_location = "/" + str(filelocation).replace('.', '/')
    # phone_list = take_phone_list_from_csv(new_file_location)
    # hash_coded_phone_list = hash_code_phone_number(phone_list)
    # results = sql_manager.take_data_from_phone_list(hash_coded_phone_list)
    # res  = take_list_userinfo_from_resultsql_list(results)
    # write_csv_from_tuple(res, "/home/longle/Desktop/result10.csv")
    return "Success"

if __name__== '__main__':
    app.run(debug=True)