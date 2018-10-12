def location_mapping(datas, province_lists, district_lists):
    res = []
    for data in datas:
        province_name = -1
        district_name = -1
        if province_lists.__contains__(data[5]):
            province_name = province_lists[int(data[5])]
        if district_lists.__contains__(data[6]):
            district_name = district_lists[int(data[6])]
        res.append((data[0], data[1], data[2], data[3], data[4], province_name, district_name, data[7]))
    return res