import my_panda as pd

mydataset = {'cars': ['BMW', 'Volvo', 'Ford', 'Benz'], 'passings': [3, 7, 2, 5]}

test = pd.DataFrame(mydataset)

print('number of rows:', test.num_rows)
print('number of columns:', test.num_columns)
print('size:', test.size)