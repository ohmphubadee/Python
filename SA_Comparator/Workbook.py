import openpyxl
from openpyxl.styles import PatternFill, Font, Color

def Create_Sheet_Type1(datas,table,header=[]):
    
    # Create a new Excel workbook or open an existing one
    try:
        workbook = openpyxl.load_workbook('D:\SA Comparator\Result.xlsx')
    except FileNotFoundError:
        workbook = openpyxl.Workbook()
        workbook.active.title = table
    
    # Create or get the desired worksheet based on the sheet number
    
    if table in workbook.sheetnames:
        sheet = workbook[table]
    else:
        sheet = workbook.create_sheet(table)
        

    Create_Header(sheet,header)
    
    # Fill Data missmatch 
    for no,data in enumerate(datas, start=1):
        row_index = sheet.max_row + 1
        if no%2 == 0:
            for i in range(max(len(datas[no-2]),len(data))):
                    row_color = sheet.cell(row=row_index, column=i+1)
                    row_color.fill = PatternFill(start_color="CCFFFF", end_color="CCFFFF", fill_type="solid")
        for col_idx, value in enumerate(data, start=1):
            cell = sheet.cell(row=row_index, column=col_idx)
            cell.value = value
            if no%2 == 0:               
                for i, (elem1, elem2) in enumerate(zip(datas[no-2], data)):                 
                    if elem1 != elem2 and i > 1: 
                        cell = sheet.cell(row=row_index, column=i+1)
                        cell.font = Font(color=Color(rgb="FF0000"))
                
    Adjust_Column(sheet)
    # Save the workbook to a file
    workbook.save('D:\SA Comparator\Result.xlsx')

def Create_Sheet_Type2(datas,table,header=[]):
    
    #header = ['A','b','c','d']
    # Load the existing workbook
    workbook = openpyxl.load_workbook('D:\SA Comparator\Result.xlsx')

    # Create a new sheet (Sheet2)
    sheet = workbook.create_sheet(title=table)

    Create_Header(sheet,header)

    # Fill Data missmatch
    for data in datas:
        row_index = sheet.max_row + 1
        for col_idx, value in enumerate(data, start=1):
            cell = sheet.cell(row=row_index, column=col_idx)
            cell.value = value
    
    Adjust_Column(sheet)
    workbook.save('D:\SA Comparator\Result.xlsx')

def Adjust_Column(sheet):
    # Adjusting column width to fit content
    for column in sheet.columns:
        max_length = 0
        column_name = column[0].column_letter  # Get the column name (e.g., 'A', 'B', etc.)

        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass

        adjusted_width = (max_length + 2) * 1.2  # Adding a little extra width for padding
        sheet.column_dimensions[column_name].width = adjusted_width

def Create_Header(sheet,header):
    # Fill header
    for col_idx,head in enumerate(header,start=1):     
        cell = sheet.cell(row=1, column=col_idx)
        cell.fill = PatternFill(start_color="3399FF", end_color="3399FF", fill_type="solid")
        cell.value = head