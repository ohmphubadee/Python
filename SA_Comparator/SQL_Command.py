def Get_query(key):
    SQL_command = {'actions':"SELECT * FROM actions",
                'hierarchy':"SELECT * FROM hierarchy",
                'sysobj':'SELECT SYSID,VERSIONNO,OBJNO,BLCKS,STRUCTYPE,OBJTYPENO,STATICBITS,INITSTAT,SYSNAME,ABBRNAME,TAG,DELFLAG,ACTMASK1,ACTMASK2,AUTHMASK1,AUTHMASK2,VALIDITY,COMMENTW,OPERNAMEW FROM sysobj',
                'track':"SELECT * FROM track",
                'cmd':"SELECT * FROM cmd",
                'texts':"SELECT * FROM texts"
                }
    
    return SQL_command.get(key, None)