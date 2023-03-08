def median_func(data):
    null_list=['ph', 'Sulfate', 'Trihalomethanes']
    null_dict={'ph': 7.036752104, 'Sulfate': 333.0735457, 'Trihalomethanes': 66.6224851}
    
    data.fillna(null_dict ,inplace=True)
        
    return data