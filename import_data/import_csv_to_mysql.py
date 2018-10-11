# import pandas as pd
# import pymysql
#
# connect = pymysql.connect(host='localhost', port=3306, user='root', password='chigiang85', db='Fb')
# cursor = connect.cursor()
#
# query = "INSERT INTO fb_clone(msisdn, fb_id) VALUES (%s, %s)"
#
# df = pd.read_csv('/home/longle/Downloads/phone_profile_db/part-r-00000-cc305a94-cd77-4dde-b036-f7544b57f095.csv')
# for index, row in df.head(10).iterrows():
#     print(row['msisdn'])
#     print(row['fb_id'])