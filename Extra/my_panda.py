
def DataFrame(self):
    for i in range(len(self.keys())):
        print('    ', list(self.keys())[i], end='')
    print('\n-----------------------')
    for ind, _ in enumerate(list(self.values())[0]):
        print(ind, '  ',list(self.values())[0][ind],'         ', list(self.values())[1][ind])
    print('-----------------------')
    return subpd(self) # create a new object

    
class subpd:
    def __init__(self, dictionary):
        self.num_columns = len(dictionary.keys())
        self.num_rows = len(list(dictionary.values())[0])
        self.size = (len(list(dictionary.values())[0]), len(dictionary.keys()))


    
