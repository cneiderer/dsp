# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
from operator import itemgetter

def main():
#    print("\nTesting version 1 (i.e., the easy way with pandas):")
#    smallest_goal_difference_v1()

#    print("\nTesting version 2 (i.e., the harder way with pure python):")
#    smallest_goal_difference_v2()

    print("\nTesting read_data(filename)")
    filename = 'football.csv'
    data = read_data(filename)
    for row in data:
        print(row)

    ridx = get_index_with_min_abs_score_difference(data)
    print(ridx)

    team = get_team(ridx, data)
    print(team)

def read_data(filename):
    """Returns a list of lists representing the rows of the csv file data.

    Arguments: filename is the name of a csv file (as a string)
    Returns: list of lists of strings, where every line is split into a list of values. 
        ex: ['Arsenal', 38, 26, 9, 3, 79, 36, 87]
    """
    with open(filename) as csv_file:
        freader = csv.reader(csv_file)
        data = []
        for rdata in freader:
            data.append(rdata)
    
    return data

def get_index_with_min_abs_score_difference(data):
    """Returns the index of the team with the smallest difference
    between 'for' and 'against' goals, in terms of absolute value.

    Arguments: parsed_data is a list of lists of cleaned strings
    Returns: integer row index
    """
    header = data[0]
    team_idx = header.index('Team')
    gf_idx = header.index('Goals')
    ga_idx = header.index('Goals Allowed')

    gd = []
    for idx, team_data in enumerate(data[1:]):
        gd.append((idx, int(team_data[gf_idx]) - int(team_data[ga_idx])))
    
    return min(gd, key=itemgetter(1))[0]
    
def get_team(ridx, data):
    """Returns the team name at a given index.
    
    Arguments: index_value is an integer row index
               parsed_data is the output of `read_data` above
               
    Returns: the team name
    """
    header = data[0]
    team_idx = header.index('Team')

    return data[1:][ridx][team_idx]

def smallest_goal_difference_v1():

    import pandas as pd

#    csv_file = '/home/cneiderer/ds/metis/metisgh/prework/dsp/python/football.csv'
    csv_file = 'football.csv'
    df = pd.read_csv(csv_file)
    print(df['Team'][(df['Goals']-df['Goals Allowed']).idxmin()])


def smallest_goal_difference_v2():
    
    import csv
    from operator import itemgetter

#    csv_file = '/home/cneiderer/ds/metis/metisgh/prework/dsp/python/football.csv'
    csv_file = 'football.csv'    
    with open(csv_file) as csv_file:
        freader = csv.reader(csv_file)
        data = []
        for ridx, rdata in enumerate(freader):
            if ridx == 0:
                header = rdata
            else:
                data.append(rdata)

    team_idx = header.index('Team')
    gf_idx = header.index('Goals')
    ga_idx = header.index('Goals Allowed')

    gd = []
    for idx, team_data in enumerate(data):
        gd.append((idx, int(team_data[gf_idx]) - int(team_data[ga_idx])))

    print(data[min(gd, key=itemgetter(1))[0]][team_idx])


if __name__ == "__main__":
    main()
