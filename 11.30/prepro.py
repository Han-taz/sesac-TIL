def median_func(data):
    col_list1=['ph','Sulfate','Trihalomethanes']
    for i in col_list1:
        if i == 'ph':
            data[i].fillna(7.036752104, inplace=True)
        elif col_list1 == 'Sulfate':
            data[i].fillna(333.0735457, inplace=True)
        else:
            data[i].fillna(66.6224851, inplace=True)
    return data