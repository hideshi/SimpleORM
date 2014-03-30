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
