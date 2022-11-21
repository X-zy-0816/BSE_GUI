'''
@File    :   data_Processing.py
@Contact :   996852067@qq.com
@License :   (C)Copyright 2021-2022

@Modify Time           @Author    @Version    @Desciption
------------           -------    --------    -----------
2022/11/10 下午6:45    xuzhiyuan     1.0       uesd to process data
'''


import pandas as pd
import plot_Making
from scipy import stats

title_flag = True


# aggregate the profit of all trades into single file
def get_profit_file(trail, n_trail, market_run_time, order_interval, trail_id, time):
    summary_filename = trail_id + '_avg_balance.csv'
    file_str = './DataFile/%s/Profit_%d_%d' % (time, market_run_time, order_interval)
    profit_file = open(file_str + '_summary.csv', 'a')

    # read the final profit of each robot
    with open(summary_filename, newline='') as csvfile:
        file_line = csvfile.readlines()[-1]
        columns = file_line.split(',')

    # write traders into file
    global title_flag
    if title_flag:
        title_flag = False
        profit_file.write('          ,')
        interval = 4
        # input robot & total profit into file
        while interval < len(columns) - 2:
            if interval != 4:
                profit_file.write(',')
            profit_file.write('%s' % columns[interval])
            interval += 4
        profit_file.write('\n')

    # write trail number line into file
    t_str = 'trail_%d/%d' % (trail, n_trail)
    profit_file.write('%s,' % t_str)

    # input corresponding total profit into file
    interval = 5
    while interval < len(columns) - 2:
        if interval != 5:
            profit_file.write(',')
        profit_file.write('%s' % columns[interval])
        interval += 4
    profit_file.write('\n')

    profit_file.close()

# def data_Ttest()

def data_analyze(market_run_time, order_interval, time, ImgSave = True):
    file_str = './DataFile/%s/Profit_%d_%d_summary.csv' % (time, market_run_time, order_interval)
    profit_file = pd.read_csv(file_str)
    profit_file = profit_file.iloc[0:, 1:]

    n = len(profit_file)
    print('[DATA]the total column is:', n, '\n')
    print('[DATA]the mean is:\n', profit_file.mean())
    print('[DATA]the std is:\n', profit_file.std())

    for col in profit_file.columns:
        print(stats.shapiro(profit_file[col]))
    temp_data = (profit_file - profit_file.mean()) / profit_file.std()
    print('\n')
    for col in temp_data.columns:
        print(stats.kstest(temp_data[col], stats.norm.cdf))

    # draw plot and save file
    fig_path = plot_Making.plot_all(market_run_time, order_interval, time, saveFlag = ImgSave)

    # make sure next time have title
    global title_flag
    title_flag = True




    # statistic, pvalue = stats.f_oneway(profit_file[' SHVR'], profit_file[' SNPR'], profit_file[' ZIC'],
    #                                    profit_file[' ZIP'])
    # if pvalue < 0.05:
    #     print("ANOVA: (p=" + "{:.20f}".format(pvalue) +
    #           " < 0.05). Reject null. The groups have a " +
    #           "different population mean.")
    # else:
    #     print("ANOVA: (p=" + "{:.2f}".format(pvalue) +
    #           " > 0.05). Cannot reject null hypothesis " +
    #           "that groups have same population mean.")

    return fig_path




# agent vs agent get the winner
def agent_agent_winner(market_run_time, order_interval, time,):
    file_str = './DataFile/%s/Profit_%d_%d_summary.csv' % (time, market_run_time, order_interval)
    profit_file = pd.read_csv(file_str)
    profit_file = profit_file.iloc[0:, 1:]
    ZIPWin = 0
    OtherWin = 0
    data = []
    data_2 = []
    Flag = True
    for col in profit_file.columns:
        for i in range(0, 100):
            if Flag == True:
                data.append(profit_file[col][i])
                continue
            data_2.append(profit_file[col][i])
        Flag = False
        # if profit_file[i][2] == max(profit_file[i][1], profit_file[i][2]):
        #     ZIPWin += 1
        #     continue
        # OtherWin += 1
    for i in range(0, 100):
        if data_2[i] == max(data[i], data_2[i]):
            ZIPWin += 1
            continue
        OtherWin += 1
    print('ZIP : ', ZIPWin)
    print('Other : ', OtherWin)




# only for test
if __name__ == "__main__":
    #agent_agent_winner(10, 30, '03:09:59')
    data_analyze(10, 30, '04:55:09')



# get the most profitable robot in each trail
# def get_profitable(filename, col_len):
#     profit_file = open(filename, 'a')
#     profit_tuple = []
#     for row in profit_file:
#         if row
#         profit_tuple.append('')
