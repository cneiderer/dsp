# Hint:  use Google to find python function

from datetime import datetime

# Convert date string to datetime object
def convert_str_to_obj(ex, date_str):
    # Get format
    if ex is 'a':
        format_str = '%m-%d-%Y'
    elif ex is 'b':
        format_str = '%m%d%Y'
    else:
        format_str = '%d-%b-%Y'    
    # Convert str to obj and return
    return datetime.strptime(date_str, format_str)

# Calculate number of days between dates
def calculate_delta(ex, date_start, date_stop):    
    delta = convert_str_to_obj(ex, date_stop) - convert_str_to_obj(ex, date_start)
#    return delta.days
    print("exercise-{ex}: {delta} days".format(ex=ex, delta=delta.days))

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015' 
calculate_delta('a', date_start, date_stop)

####b)  
date_start = '12312013'  
date_stop = '05282015'  
calculate_delta('b', date_start, date_stop)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'
calculate_delta('c', date_start, date_stop)

 
