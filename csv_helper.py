import pandas as pd

def take_data_list_from_csv(file_location):
    try:
        df = pd.read_csv(file_location, header=None)
        list_data = []
        for index, row in df.iterrows():
            list_data.append(str(row[0]))
        return list_data
    except:
        return "file is not exist"

def write_csv_from_tuple(data, file_location):
    res_df = pd.DataFrame(data, columns=['msisdn', 'fb_id', 'gender', 'dob', 'name', 'province', 'district', 'ward'])
    print(file_location)
    res_df.to_csv(file_location, index=False)
