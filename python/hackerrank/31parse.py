import csv

def read_data(filename):
    """Returns a list of lists representing the rows of the csv file data.

    Arguments: filename is the name of a csv file (as a string)
    Returns: list of lists of strings, where every line is split into a list of values.
        ex: ['Arsenal', 38, 26, 9, 3, 79, 36, 87]
    """
    listy = []
    with open('football.csv','r') as f:
        reader = csv.reader(f)
        teamrows = list(reader)
        for row in teamrows[1:]:
            z = [row[0]]
            rows = list(map(int,row[1:]))
            for e in rows:
                z.append(e)
            listy.append(z)
    return listy

def get_index_with_min_abs_score_difference(goals):
    """Returns the index of the team with the smallest difference
    between 'for' and 'against' goals, in terms of absolute value.

    Arguments: parsed_data is a list of lists of cleaned strings
    Returns: integer row index
    """
    min_diff = 100
    row_index = 0
    i = 0
    for row in goals:
        # print("Min.diff: " + str(min_diff) + " Row Index: " + str(row_index) + " i value: " + str(i))
        if abs(row[5]- row[6]) < min_diff:
            min_diff = abs(row[5]-row[6])
            row_index = i
            i+=1

        else:
            i+=1
    return row_index

def get_team(index_value, parsed_data):
    """Returns the team name at a given index.

    Arguments: index_value is an integer row index
               parsed_data is the output of `read_data` above

    Returns: the team name
    """
    return parsed_data[index_value][0]

def execute(filename):
    listy = read_data(filename)
    print(listy)
    row_index = get_index_with_min_abs_score_difference(listy)
    print(row_index)
    team = get_team(row_index,listy)
    print(team)
    return team

execute('football.csv')
