'''
Input : {‘a’: 1, ‘b’:2, ‘c’:3}
Output : 6

Input : {‘x’: 25, ‘y’:18, ‘z’:45}
Output : 88
'''
def dict_sum( sample_dict ):
    sum_dict = sum(sample_dict.values())
    return sum_dict

sample_dict = {'a': 100, 'b': 200, 'c': 300}
print(dict_sum(sample_dict))