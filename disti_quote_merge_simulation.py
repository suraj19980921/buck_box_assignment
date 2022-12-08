import tabulate

class DistiQuoteMerge:

    def disti_merge(self,bom_list,disti):
        unified_list = []
        disti_bom_match = False
        error_flag = ''
        
        '''spliting disti against bom'''
        
        for bom in bom_list:
        
            bom_part_no = list(bom.keys())[0]
            bom_quantity = list(bom.values())[0]
           
            disti_index = 0
            
            for dist in disti:
            
                disti_part_no = list(dist.keys())[0]
                disti_quantity = list(dist.values())[0]

                if disti_part_no == bom_part_no :
                    disti_bom_match = True
                
                    if disti_quantity < bom_quantity:
                        assign_disti_quantity = disti_quantity
                        error_flag = 'X'
                    else:
                        assign_disti_quantity = bom_quantity
                    
                    
                    new_disti_quantity = disti_quantity - bom_quantity

                    if new_disti_quantity <= 0:
                        disti.pop(disti_index)
                    else:
                        disti.pop(disti_index)
                        disti.insert(disti_index,{disti_part_no:new_disti_quantity})
                        disti_quantity = new_disti_quantity
                    

                    unified_list.append({"bom_pn":bom_part_no, 
                                        "bom_qty":bom_quantity, 
                                        "Dsti_pn":disti_part_no,
                                        "Dsti_qty":assign_disti_quantity,
                                        "error_flag":error_flag})
                    error_flag = ''
                
                
                disti_index += 1

            
            '''adding bom in unified list which is not present in disti '''
            
            if not disti_bom_match:
                    unified_list.append({"bom_pn":bom_part_no, 
                                        "bom_qty":bom_quantity, 
                                        "Dsti_pn":"",
                                        "Dsti_qty":"",
                                        "error_flag":'X'})

            disti_bom_match = False
        


        '''adding remaining disti or which is not present in bom , in  unified list'''
        for dist in disti:
            disti_part_no = list(dist.keys())[0]
            disti_quantity = list(dist.values())[0]

            if disti_quantity >= 1:
                unified_list.append({"bom_pn":"", 
                                        "bom_qty":"", 
                                        "Dsti_pn":disti_part_no,
                                        "Dsti_qty":disti_quantity,
                                        "error_flag":'X'})

        self.table_representation(unified_list)
       

    '''function for tabular representation'''

    def table_representation(self,unified_list):
        dataset = unified_list
        header = dataset[0].keys()
        rows =  [x.values() for x in dataset]
        print(tabulate.tabulate(rows, header))
        




bom = [{"ABC":2},{"XYZ":1},{"IJK":1},{"ABC":1},{"IJK":1},{"XYZ":2},{"DEF":2}]

disti = [{"XYZ":2},{"GEF":2},{"ABC":4},{"IJK":2}]


test_obj = DistiQuoteMerge()
test_obj.disti_merge(bom,disti)