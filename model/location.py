import json

class Location:
    def __init__(self, ward, district, province):
        self.ward = ward
        self.district = district
        self.province = province

    def to_json(self):
        json_obj = json.dumps(self.__dict__)
        return json_obj