from distutils.core import setup

setup(
      name = 'SimpleORM'
    , py_modules = ['simpleorm']
    , scripts = ['simpleorm.py']
    , version = '0.2.1'
    , license = 'LGPL'
    , platforms = ['MacOS', 'POSIX']
    , description = 'Simple SQLite3 Object Relational Mapper for Python.'
    , author = 'hideshi'
    , author_email = 'hideshi.ogoshi@gmail.com'
    , url = 'https://github.com/hideshi/SimpleORM'
    , keywords = ['SQLite3', 'ORM', 'Framework']
    , classifiers = [
          'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)'
        , 'Operating System :: MacOS :: MacOS X'
        , 'Operating System :: POSIX :: Linux'
        , 'Programming Language :: Python'
        , 'Development Status :: 4 - Beta'
        , 'Environment :: Web Environment'
        , 'Environment :: Console'
        , 'Intended Audience :: Developers'
        , 'Topic :: Software Development :: Libraries :: Application Frameworks'
        , 'Topic :: Database'
        ]
    , long_description = """\
Simple SQLite3 Object Relational Mapper for Python.

Requirements
------------
* Python 3.3 or later

Features
--------
* Under construction

Setup
-----
::

   $ pip install SimpleORM

History
-------
0.1.0 (2014-03-13)
~~~~~~~~~~~~~~~~~~
* first release

0.1.1 (2014-03-14)
~~~~~~~~~~~~~~~~~~
* fixed bugs
* added one more example

0.2.0 (2014-03-30)
~~~~~~~~~~~~~~~~~~
* added dynamic SQL function

0.2.1 (2014-03-30)
~~~~~~~~~~~~~~~~~~
* fixed bug

Example
-------

Define select statement in the source code and get return value as instances of Employee class.

.. code-block:: python

    from simpleorm import BaseDao
    from classes import Employee
    from collections import OrderedDict

    class SelectEmployeeAll(BaseDao):
        sql = '''
    SELECT A.ID
          ,A.NAME
          ,B.NAME AS BOSS_NAME
      FROM EMPLOYEE A
      LEFT OUTER JOIN EMPLOYEE B
        ON B.ID = A.BOSS
    '''

    if __name__ == '__main__':
        param = OrderedDict()
        result = SelectEmployeeAll(dbfile = 'test.db', return_type = Employee).execute(param)
        for elem in result:
            print(elem.id, elem.name, elem.boss_name)


.. code-block:: python

    class Employee:
        id = None
        name = None
        boss_name = None


Define select statement out of the source code and get return value as tuple.

.. code-block:: python

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


.. code-block:: sql

    -- select_employee.sql
    SELECT ID
          ,NAME
          ,AGE
          ,BOSS
      FROM EMPLOYEE
     WHERE NAME LIKE ?
     ORDER BY AGE ASC 


Define dynamic select statement.

.. code-block:: python

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


.. code-block:: sql

    -- select_employee_dynamic.sql
    SELECT ID
          ,NAME
          ,AGE
          ,BOSS
      FROM EMPLOYEE
     WHERE NAME LIKE ?
    if param.get('_flg', False) == True
           AND AGE >= ?
    end
     ORDER BY AGE ASC


Define insert statement.

.. code-block:: python

    from simpleorm import BaseDao
    from collections import OrderedDict

    class InsertEmployee(BaseDao):
        sql = 'INSERT INTO EMPLOYEE (ID, NAME, AGE, BOSS) VALUES (?, ?, ?, ?)'

    if __name__ == '__main__':
        param = OrderedDict()
        param['id'] = 4
        param['name'] = 'Jiro Tanaka'
        param['age'] = 24
        param['boss'] = 3
        result = InsertEmployee(dbfile = 'test.db').execute(param)
        print(result)


Bulk insert.

.. code-block:: python

    from simpleorm import BaseDao
    from collections import OrderedDict

    class InsertEmployee(BaseDao):
        sql = 'INSERT INTO EMPLOYEE (ID, NAME, AGE, BOSS) VALUES (?, ?, ?, ?)'

    if __name__ == '__main__':
        param = list()
        for i in range(10000):
            elem = OrderedDict()
            elem['id'] = i
            elem['name'] = '{}'.format(i)
            elem['age'] = i
            elem['boss'] = None
            param.append(elem)

        result = InsertEmployee(dbfile = 'test.db', commit_interval = 100, isolation_level = 'DEFERRED').execute(param)
        print('Rows affected:{}'.format(result))

"""
)
