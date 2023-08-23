from Converter import *
import datetime

def CompareBySysid(DB1,DB2):
    """Compare database1 and database2

    Args:
        DB1 (_type_): _description_
        DB2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    result = []
    
    for key in DB1:
        if key in DB2:            
            if DB1[key] != DB2[key]:
                result.append(['DB1'] + [key] + list(DB1[key]))
                result.append(['DB2'] + [key] + list(DB2[key]))
                
                # Create and write in LOG1.txt
                #with open('D:\SA Comparator\Output\LOG1.txt', 'a') as LOG1:
                #    current_date = datetime.datetime.now()
                #    LOG1.write(f'DB1:{key} | {DB1.sysobj[key][1:]}\n') 
                #    LOG1.write(f'DB2:{key} | {DB2.sysobj[key][1:]}\n')
                #    LOG1.write('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
                
                # add miss match data to result list
                
            continue
        
        else:
            result.append(['DB1'] + [key] + list(DB1[key]))
            result.append(['DB2'])

            #with open('D:\SA Comparator\Output\LOG2.txt', 'a') as LOG2:
            #    CompareBySysname(DB1[key][7],DB2)
            #    LOG2.write(f'{key} | {DB1[key][7]} exist in Database 1 not in Database 2\n')
    
    for key in DB2:
        if key in DB1:
            continue
        else:
            #with open('D:\SA Comparator\Output\LOG2.txt', 'a') as LOG2:
            #    CompareBySysname(DB2[key][7],DB1)
            #    LOG2.write(f'{key} | {DB2[key][7]} exist in Database 2 not in Database 1\n')
            
            result.append(['DB1'])
            result.append(['DB2'] + [key] + list(DB2[key]))
    return result

def CompareBySysname(target_value,DB):
    for key,values in DB.items():
        if target_value == values[7]:
            print(f'{values[7]} : {target_value}')


def Compare_table(DB1,DB2):

    result = []

    for data in DB1:
        if data in DB2:
            continue
        else:
            result.append(list(data))
            result[-1].append('Exist in Database1 not Database2')

    for data in DB2:
        if data in DB1:
            continue
        else:
            result.append(list(data))
            result[-1].append('Exist in Database2 not Database1')
    return result       