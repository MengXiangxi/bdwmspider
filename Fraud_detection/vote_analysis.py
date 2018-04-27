import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

def parse_vote(f_name, init_time):
    '''
    parse_vote() parsing the vote results

    f_name - file name for the csv file
    init_time - the time when voting started

    t - A list of time stamps of vote casting, sorted, int
    s - A list of current voted ID count corresponding to `t`, int
    '''

    data = pd.read_csv(f_name, header=None, sep=r"\s*")
    date_format = "%Y年%m月%d日%H:%M:%S"  # To read the date
    t = [] # A list of time lapse in second
    for i in data.loc[:,2]:
        date_str = str(i)
        t.append((datetime.strptime(date_str, date_format) - init_time).total_seconds())
    t.sort()

    s = [] # A list of current voted ID count corresponding to `t`
    for j in range(len(t)):
        s.append((j + 1) / (len(t) + 1))
    return t, s

# Parse the results for yafeng
init_time_1 = datetime(2018, 4, 16, 10, 2, 7)
t1, s1 = parse_vote('yafeng.txt', init_time_1)

# Parse the results for naiiive
init_time_2 = datetime(2017, 12, 11, 22, 46, 4)
t2, s2 = parse_vote('naiiive.txt', init_time_2)

# Plot with Matplotlib
plt.plot(t1,s1,label='yafeng')
plt.plot(t2,s2,label='naiiive')
plt.plot([0, 604800], [0, 1]) # Diagonal line
plt.legend(loc='lower right') # Legend
plt.show()
