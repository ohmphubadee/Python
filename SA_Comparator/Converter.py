import os
from DB_Connect import RunQuery
from SQL_Command import *

class Converter():
    # don't have primary key
    table_type1 = ['actions','adjtypes','attribute','cond','crosref','crossev','dyndata','ecgrp','ecgrpuse','evconv','evsim','extitems','extsysif','hierarchytypes','nameparts','pretests','propmap',
                   'simpretests','spreading','tabdescr','tabgrp','texts','utcdiff','valueset','valuetext','users','hierarchy']

    # have primary key
    table_type2 = ['adjacency','applmenu','automaton','cmd','cmdresp','cmdset','cmdstruct','cmdtypegrp','dirty','dynprop','evcond','event','measure','msgtype','objtype','objtypegrp',
                   'operator','opernote','pattern','profileitem','request','route2','scale','site','sound','soundalarmmasks','state','sysobj','sysvalues','track','train','vehicle','viewrects']
    
    # Difine path of Table_List.txt
    #table_list_path = os.path.join(os.getcwd(), 'Result.xlsx')
    table_list_path = 'D:\SA Comparator\Table_List.txt'

    #tables = ['sysobj','hierarchy','actions','cmd','track','texts']

    def __init__(self,DSN):
        """Create repository for each query

        Args:
            DSN (string): Server's name
        """
        self.Read_Table_List(self.table_list_path)

        for table in self.tables:
            if table in self.table_type2:
                query = Get_query(table)
                if query == None:
                    query = f'SELECT * FROM {table}'
                self.Read_BySysid(DSN,query,table)
            elif table in self.table_type1:
                query = Get_query(table)
                if query == None:
                    query = f'SELECT * FROM {table}'
                self.Read_Table(DSN,query,table)
            else:
                print(f'{table} table not exist')
        
    # Read data from table to dictionary
    def Read_BySysid(self,DSN,query,table):
        """Create list, read database and store data to dictionary

        Args:
            DSN (string): Server's name
            query (string): SQL Command
            table (string): table name
        """
        
        setattr(self, table, {})  
        crsr = RunQuery(query,DSN)
        rows = crsr.fetchall()
        for row in rows:
            getattr(self, table)[row[0]] = row[1:]
        setattr(self, table, dict(sorted(getattr(self, table).items())))   
    
    # Read Column name from table but not work for IBM solid
    def Read_header(DSN,table):
        exclude_values = ['CREATED', 'UPTIMEID', 'MODIFIED']
        query = f"SELECT COLUMN_NAME FROM columns WHERE TABLE_NAME = '{table.upper()}'"
        header_q = RunQuery(query,DSN)       
        header = header_q.fetchall()
        header = [item[0] for item in header if item[0] not in exclude_values]
        return header
    
    # Read data from table to list
    def Read_Table(self,DSN,query,table):
        """Create list, read database and store data to list

        Args:
            DSN (string): Server's name
            query (string): SQL Command
            table (string): table name
        """
        setattr(self, table, [])
        crsr = RunQuery(query,DSN)    
        rows = crsr.fetchall()
        setattr(self, table, rows)

    # Read table want to compare from Table_List.txt
    def Read_Table_List(self,table_list_path): 
        try:
            with open(table_list_path, 'r') as file:
                content = file.read().split(',')
                if content == ['']:
                    content = self.table_type1 + self.table_type2
        except FileNotFoundError:
            print(f"File '{table_list_path}' not found.")
            content = self.table_type1 + self.table_type2
        except Exception as e:
            print("An error occurred:", e)
            content = self.table_type1 + self.table_type2
        
        self.tables = content
        