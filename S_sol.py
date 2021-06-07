def s_test_sol(n):

    import os
    import csv

    directory = os.fsencode('C:/Users/lucaj/PycharmProjects/Simulator/test times')
    filelist = []
    namelist = []

    for folder in os.listdir(directory):
        filepath = os.fsdecode(directory)+'/'+os.fsdecode(folder)+'/'+'line_p_pa.xy'
        namelist.append(os.fsdecode(folder))
        filelist.append(filepath)

    x = []
    y = []

    with open(filelist[n], 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=' ')
        for row in plots:
            x.append(float(row[0]))
            y.append(float(row[2]))
    data = [x, y, namelist[n]]
    return data


def s_t_sol(time):

    import csv

    x = []
    y = []
    filepath = 'C:/Users/lucaj/PycharmProjects/Simulator/graph_data/singleGraph/'+str(time)+'/line_p_pa.xy'
    with open(filepath, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=' ')
        for row in plots:
            x.append(float(row[0]))
            y.append(float(row[2]))
    data = [x, y]
    return data
