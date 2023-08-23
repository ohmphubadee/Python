from DB_Connect import RunQuery
from utils import Trace

class Converter():
    def __init__(self,DSN):
        """Create repository for each query

        Args:
            DSN (string): Server's name
        """
        self.sysobj = {}
        self.hierarchy = {}
        self.actions = []
        self.cmd = {} 
        self.evsim = []    
        self.Read_BySysid(DSN,'SELECT SYSID,VERSIONNO,OBJNO,BLCKS,STRUCTYPE,OBJTYPENO,STATICBITS,INITSTAT,SYSNAME,ABBRNAME,TAG,DELFLAG,ACTMASK1,ACTMASK2,AUTHMASK1,AUTHMASK2,VALIDITY,COMMENTW,OPERNAMEW FROM sysobj',"sysobj")
        self.Read_BySysid(DSN,"SELECT hierarchy.SYSID, Child.SYSNAME, hierarchy.MASTERID, Master.SYSNAME, hierarchy.HIERARCHYTYPE, hierarchy.VERSIONNO, hierarchy.SEQNO FROM hierarchy JOIN sysobj as Child ON Child.SYSID = hierarchy.SYSID JOIN sysobj as Master ON Master.SYSID = hierarchy.MASTERID","hierarchy")
        self.Read_Table(DSN,"SELECT * FROM actions",'actions')
        self.Read_BySysid(DSN,"SELECT * FROM cmd",'cmd')
        self.Read_Table(DSN,"SELECT * FROM evsim",'evsim')

    # Read data from sysobj table
    def Read_BySysid(self,DSN,query,table):
        setattr(self, table, {})     
        crsr = RunQuery(query,DSN)
        rows = crsr.fetchall()
        for row in rows:
            getattr(self, table)[row[0]] = row[1:]
        setattr(self, table, dict(sorted(getattr(self, table).items())))
    
    # Read Column name from table but not work for IBM solid
    def Read_header(self,table,DSN):
        query = f'DESCRIBE TABLE {table} RAW'
        header_q = RunQuery(query,DSN)       
        header = header_q.fetchall()
        return header
    
    def Read_Table(self,DSN,query,table):
        setattr(self, table, [])
        crsr = RunQuery(query,DSN)    
        rows = crsr.fetchall()
        setattr(self, table, rows)

