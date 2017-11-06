# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


def main():
    print("\nTesting version 1 (i.e., the easy way with pandas):")
    smallest_goal_difference_v1()

    print("\nTesting version 2 (i.e., the harder way with pure python):")
    smallest_goal_difference_v2()

def smallest_goal_difference_v1():

    import pandas as pd

    csv_file = '/home/cneiderer/ds/metis/metisgh/prework/dsp/python/football.csv'
    df = pd.read_csv(csv_file)
    print(df['Team'][(df['Goals']-df['Goals Allowed']).idxmin()])


def smallest_goal_difference_v2():
    
    import csv
    from operator import itemgetter

    csv_file = '/home/cneiderer/ds/metis/metisgh/prework/dsp/python/football.csv'
    
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
