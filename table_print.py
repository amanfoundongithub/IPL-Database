import prettytable 

def PrintMyTable(lst: list,title: str) -> None:
    '''
    Prints the lst with the given title
    '''

    mytable = prettytable.PrettyTable()

    mytable.title = title 

    mytable.field_names = lst[0].keys()

    for rows in lst:
        mytable.add_row(rows.values())
    
    print(mytable) 
    