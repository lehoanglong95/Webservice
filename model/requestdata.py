import json

#0 nu 1 nam

def take_string_data_from_json(json_result, field_name):
    try:
        return json_result[field_name]
    except:
        return ""

def take_number_data_from_json(json_result, field_name):
    try:
        return int(json_result[field_name])
    except:
        return -1

def take_list_data_from_json(json_result, field_name):
    try:
        return json_result[field_name]
    except:
        return []

class RequestData:
    def __init__(self, data):
        json_result = json.loads(data)
        self.id = take_string_data_from_json(json_result, "id")
        self.type = take_string_data_from_json(json_result, "type")
        self.file_location = take_string_data_from_json(json_result, "file_location")
        self.age = take_list_data_from_json(json_result, "age")
        self.location = take_list_data_from_json(json_result, "location")
        self.gender = take_number_data_from_json(json_result, "gender")
        self.limit = take_number_data_from_json(json_result, "limit")
