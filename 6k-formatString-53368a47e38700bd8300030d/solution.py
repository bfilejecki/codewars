# Format a string of names like 'Bart, Lisa & Maggie'.

def namelist_v1(names):
    extracted_names = (x["name"] for x in names)
    names_string = ''
    for i, name in enumerate(extracted_names):
        if i == 0:
            names_string+=name
        elif i == len(names) - 1 :
            names_string+=f' & {name}'
        else:
            names_string+=f', {name}'
    return names_string

print(namelist_v1([ {'name': 'Bart'}, {'name': 'Lisa'} ]))