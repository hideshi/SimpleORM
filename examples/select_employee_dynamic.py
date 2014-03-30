from simpleorm import BaseDao
from collections import OrderedDict

class SelectEmployeeDynamic(BaseDao):
    pass

if __name__ == '__main__':
    param = OrderedDict()
    param['name'] = 'Taro%'
    param['age'] = 20
    param['_flg'] = True
    result = SelectEmployeeDynamic(dbfile = 'test.db').execute(param)
    for elem in result:
        print(elem['ID'], elem['Name'], elem['age'], elem['bOsS'])

    param2 = OrderedDict()
    param2['name'] = 'Taro%'
    result2 = SelectEmployeeDynamic(dbfile = 'test.db').execute(param2)
    for elem in result2:
        print(elem['ID'], elem['Name'], elem['age'], elem['bOsS'])
