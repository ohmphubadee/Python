import pyodbc,datetime
from utils import Trace

dbConnectionString = 'DSN=MY-SERVER;UID=dba;PWD=dba'
dbVersionNo = '1'

LX_dbc = None
dbTimeStamp = None
dbConnectionTimeout = 30 # minutes

def OpenDBConnection():    # Returns cursor to DB
    # Open database connection (the first one calling this function does it)
    global LX_dbc, dbTimeStamp, dbConnectionTimeout
    crsr = None
    try:
        # If DB has not been accessed within timeout, close and open it again
        if LX_dbc != None and datetime.datetime.now() > dbTimeStamp + datetime.timedelta(seconds = dbConnectionTimeout*60):
            LX_dbc.close()
            LX_dbc = None
            Trace('Closed un-accessed DB connection (timeout: %d minutes)' % (dbConnectionTimeout))
        if LX_dbc == None:
            LX_dbc = pyodbc.odbc(dbConnectionString)
            Trace('Created DB connection')
        dbTimeStamp = datetime.datetime.now()
        crsr = LX_dbc.cursor()
    except:
        pass
    finally:
        return crsr

def CloseDBConnection():
    global LX_dbc, dbTimeStamp
    try:
        if LX_dbc != None:
            LX_dbc.close()
            LX_dbc = None
            Trace('Closed DB connection')
    except:
        pass
    finally:
        dbTimeStamp = None

def RunQuery(select):
    if type(select) != str:
        raise TypeError
    crsr = None
    try:
        crsr = OpenDBConnection()
        crsr.execute(select)
    finally:
        return crsr
