import xlrd
import datetime

def parse_excel(file): 
    data = {}
    row = 9    # assigned row value for reading list

    excel_data = xlrd.open_workbook(file)
    
    pysheet = excel_data.sheet_by_index(0)
    
    data['Quote'] = pysheet.cell_value(1,2)
    

    date = xlrd.xldate_as_datetime(pysheet.cell_value(1,5), 0)

    if not date == "":
        data['Date'] = datetime.datetime.strftime(date,"%Y-%m-%d")   # converting date in given format
    else:
        print("Date is not present.\n")
    
    data['Items'] = []
   

    ''' reading list form excel and creating a dict '''
   
    while True:
        actual_row = row+1

        line_number = pysheet.cell_value(row,2)
        
        if line_number == "":
            
            print(f"Line Number is not present on row number {actual_row}\n",)

        part_number = pysheet.cell_value(row,3)

        if part_number == "":
            
            print(f"Part Number is not present on row number {actual_row}\n",)

        description = pysheet.cell_value(row,4)

        if description == "":
            
            print(f"Description is not present on row number {actual_row}\n",)
       
        price = pysheet.cell_value(row,6)

        if price == "":
            
            print(f"Price is not present on row number {actual_row}\n",)
        
        if not line_number == "" and not part_number == "" and not description == "" and not price == "" :
            data['Items'].append({'LineNumber':int(line_number),
                                'PartNumber':part_number,
                                'Description':description,
                                'Price':price})
            
        row += 1

        ''' breaking loop on reading  10 dashesh in first coloumn '''
        
        if str(pysheet.cell_value(row,1)).count('-') >= 10:
            break

    return data
        
result = parse_excel('Python_Skill_Test.xlsx')
print(result)