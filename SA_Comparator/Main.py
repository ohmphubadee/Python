from Converter import *
from Compare_Data import *
from Workbook import *
from SQL_Command import *

defult_header = ['Column1','Column2','Column3','Column4','Column5','Column6','Column7','Column8','Column9','Column10','Column11','Column12','Column13','Column14','Column15', 'Column16','Column17','Column18','Column19','Column20']

server_1 = input("First server name: ")
server_2 = input("Second server's name: ")

DSN1 = 'DSN=MY-SERVER;UID=dba;PWD=dba'
DSN2 = 'DSN=SERVER1;UID=dba;PWD=dba'

# Read Database by DSN
DB1 = Converter(DSN1) 
DB2 = Converter(DSN2)

# Compare Database1 and Database2 and return missmatch data from table and fill result in excel file

for table in DB1.tables:
    if isinstance(getattr(DB1,table),dict):
        result = CompareBySysid(getattr(DB1,table),getattr(DB2,table))
        header = Converter.Read_header(DSN1,table)
        header.insert(0,'Database')
        Create_Sheet_Type1(result,table,header)
    elif isinstance(getattr(DB1,table),list):
        result = Compare_table(getattr(DB1,table),getattr(DB2,table))
        header = Converter.Read_header(DSN1,table)
        header.insert(0,'Database')
        header.append('Comment')
        Create_Sheet_Type2(result,table,header)

print("Done!!")
