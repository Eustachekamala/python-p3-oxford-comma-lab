# import ipdb
'''This function takes a list of items and returns a string with the Oxford comma.'''
def oxford_comma(items):
    #! Handle single-element list
    if len(items) == 1:
        return items[0]
    
    #! Handle two-element list
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    
    #! Handle lists with more than two elements
    else:
        return ', '.join(items[:-1]) + f", and {items[-1]}"

