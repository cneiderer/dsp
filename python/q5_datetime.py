# Hint:  use Google to find python function

from datetime import datetime

def main():
    ####a) 
    date_start = '01-02-2013'  
    date_stop = '07-28-2015' 
    format_str = '%m-%d-%Y'
    print('ex-a): {} days'.format(calculate_delta(date_start, date_stop, format_str)))

    ####b)  
    date_start = '12312013'  
    date_stop = '05282015'  
    format_str = '%m%d%Y'
    print('ex-b): {} days'.format(calculate_delta(date_start, date_stop, format_str)))

    ####c)  
    date_start = '15-Jan-1994'  
    date_stop = '14-Jul-2015'
    format_str = '%d-%b-%Y'
    print('ex-c): {} days'.format(calculate_delta(date_start, date_stop, format_str)))


def calculate_delta(date_start, date_stop, format_str):    
    '''Calculate number of days between dates'''

    delta = datetime.strptime(date_stop, format_str) - datetime.strptime(date_start, format_str)
    return delta.days
#    print('exercise-{0}: {1} days'.format(ex, delta.days))


if __name__ == "__main__":
    main()
 
