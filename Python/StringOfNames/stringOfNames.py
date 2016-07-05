def namelist(names):
    output = ""
    for i, name in enumerate(d['name'] for d in names): 
        if len(names) == i+2: output += name + " & "
        elif len(names) == i+1: output += name
        else: output += name + ", "
    return output