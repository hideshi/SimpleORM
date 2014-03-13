from simpleorm import BaseDao
from collections import OrderedDict

class SelectEmployee(BaseDao):
    pass

if __name__ == '__main__':
    param = OrderedDict()
    param['name'] = 'Taro%'
    result = SelectEmployee(dbfile = 'test.db').execute(param)
    for elem in result:
        print(elem['ID'], elem['Name'], elem['age'], elem['bOsS'])
