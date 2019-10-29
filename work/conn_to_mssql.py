import pyodbc

server = 'msln-iwdm1\iwmssql'
database = 'iwdm'
username = '<ingos\\testbalitsky>'
password = 'aQ!@WsdE#'
driver = '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()

cursor.execute("""use stkh;
select * from TUserInfo
where fio like '%Муштонина Ольга Алексеевна%'""")
row = cursor.fetchone()
while row:
    print(str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()