import pyodbc,datetime
import xml.etree.ElementTree
from utils import Trace

dbTimeStamp = None
crsr = None

def OpenDBConnection(DSN):
    
    connection = None
    try:
        connection = pyodbc.connect(DSN)
        #Trace(f'Created DB connection {DSN}')
        return connection

    except (Exception, pyodbc.Error) as error:
        Trace("Error while connecting to Solid IBM: ", error)   
         
def CloseDBConnection(connection):
    connection.close()
    Trace('Closed DB connection ')
    

def RunQuery(select,DSN):
    if type(select) != str:
        raise TypeError
    crsr = None
    
    try:
        crsr = OpenDBConnection(DSN)
        crsr = crsr.cursor()
        crsr.execute(select)
    
    finally:
        return crsr