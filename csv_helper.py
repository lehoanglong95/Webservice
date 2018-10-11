import pandas as pd

def take_phone_list_from_csv(file_location):
    df = pd.read_csv(file_location, header=None)
    phone_list = []
    for index, row in df.iterrows():
        phone_list.append(str(row[0]))
    return phone_list

def write_csv_from_tuple(data, file_location):
    res_df = pd.DataFrame(data, columns=['msisdn', 'fb_id', 'gender', 'dob', 'name', 'province', 'district', 'ward'])
    res_df.to_csv(file_location, index=False)