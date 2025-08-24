l=[36.5, 37.0, 39.2, 35.6, 38.7]
c_to_f=list(map(lambda x:((x*(9/5))+32),l))
above_100=list(filter(lambda x:x>100, c_to_f))
print(f'temprature in fahrenheit {c_to_f}')
print(f'temprautre in above_100 {above_100}')