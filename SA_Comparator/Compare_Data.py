from Converter import *
from Workbook import *

def CompareBySysid(DB1,DB2):
    """Compare database1 and database2 from dictionary type

    Args:
        DB1 (dictionary): table data from database1
        DB2 (dictionary): table data from database2

    Returns:
        list: result from comparation
    """
    result_changed = []
    result_removed = []
    result_added = []
    
    for key in DB1:
        if key in DB2:            
            if DB1[key] != DB2[key]:
                result_changed.append(['DB1'] + [key] + list(DB1[key]))
                result_changed.append(['DB2'] + [key] + list(DB2[key]))
            continue
        
        else:
            result_removed.append(['DB1'] + [key] + list(DB1[key]))
    
    for key in DB2:
        if key in DB1:
            continue
        else: 
            result_added.append(['DB2'] + [key] + list(DB2[key]))
    
    return result_changed,result_removed,result_added

def CompareBySysname(target_value,DB):
    for key,values in DB.items():
        if target_value == values[7]:
            print(f'{values[7]} : {target_value}')

def Compare_table(DB1,DB2):
    """Compare database1 and database2 from list type

    Args:
        DB1 (list): table data from database1
        DB2 (list): table data from database2

    Returns:
        list: result from comparation
    """
    result = []

    for data in DB1:
        if data in DB2:
            continue
        else:
            result.append(['DB1'] + list(data))
            result[-1].append('Exist in Database1 not Database2')

    for data in DB2:
        if data in DB1:
            continue
        else:
            result.append(['DB2'] + list(data))
            result[-1].append('Exist in Database2 not Database1')

    return result