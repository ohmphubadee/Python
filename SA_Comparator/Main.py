from Converter import *
from Compare_Data import *
from Workbook import *

# Read Database by DSN
DB1 = Converter('DSN=MY-SERVER;UID=dba;PWD=dba') 
DB2 = Converter('DSN=SERVER1;UID=dba;PWD=dba')

# Compare Database1 and Database2 and return data missmatch from sysobj table and fill result in excel file
result = CompareBySysid(DB1.sysobj,DB2.sysobj)
Create_Sheet_Type1(result,'sysobj',["Database","SYSID","VERSIONNO","OBJNO","BLCKS","STRUCTYPE","OBJTYPENO","STATICBITS","INITSTAT","SYSNAME","ABBRNAME","TAG","DELFLAG","ACTMASK1","ACTMASK2","AUTHMASK1","AUTHMASK2","VALIDITY","COMMENTW","OPERNAMEW"])
result = CompareBySysid(DB1.hierarchy,DB2.hierarchy)
Create_Sheet_Type1(result,'hierarchy',['Database', 'hierarchy.SYSID', 'Child.SYSNAME', 'hierarchy.MASTERID', 'Master.SYSNAME', 'HIERARCHYTYPE', 'VERSIONNO', 'SEQNO'])

result = CompareBySysid(DB1.cmd,DB2.cmd)
Create_Sheet_Type1(result,'cmd',['Database','SYSID','CMDCODE','PARAMNT'])

result = Compare_table(DB1.actions,DB2.actions)
Create_Sheet_Type2(result,'actions',['Database'])



