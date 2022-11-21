import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import seaborn as sns

IMG_PATH = './Img/'


# plot of price-time
def plot_trades(trial_id, trial, time, save = True):
    prices_file_name = trial_id + '_tape.csv'
    x = np.empty(0)
    y = np.empty(0)
    with open(prices_file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ttime = float(row[1])
            price = float(row[2])
            x = np.append(x, ttime)
            y = np.append(y, price)
    if save == True:
        fig_path = IMG_PATH + time + '/' + str(trial)
        plt.plot(x, y, 'x', color='black')
        plt.savefig(fig_path)
    plt.clf()
    return fig_path


def plot_all(market_run_time, order_interval, time, saveFlag = 1):
    # read profit file data
    file_str = './DataFile/%s/Profit_%d_%d_summary.csv' % (time, market_run_time, order_interval)
    profit_file = pd.read_csv(file_str)
    profit_file = profit_file.iloc[0:, 1:]

    fig_path = plot_boxplot(profit_file, time, saveFlag)
    plot_kdeplot(profit_file, time, saveFlag)
    plot_violinplot(profit_file, time, saveFlag)
    return fig_path


def plot_boxplot(profit_file, time, save):
    fig1 = sns.boxplot(data = profit_file)
    fig_path = IMG_PATH + time + '/' + 'Box_plot'
    if save == True:
        plot1 = fig1.get_figure()
        plot1.savefig(fig_path, dpi=400)
    plt.clf()
    fig_path = IMG_PATH + time + '/'
    return fig_path


def plot_kdeplot(profit_file, time, save):
    fig2 = sns.kdeplot(data = profit_file, fill=True)
    fig_path = IMG_PATH + time + '/' + 'Kdeplot'
    if save == True:
        plot2 = fig2.get_figure()
        plot2.savefig(fig_path)
    plt.clf()

def plot_violinplot(profit_file, time, save):
    fig3 = sns.violinplot(data = profit_file)
    fig_path = IMG_PATH + time + '/' + 'Violinplot'
    if save == True:
        plot3 = fig3.get_figure()
        plot3.savefig(fig_path, dpi=400)
    plt.clf()


# only for test
if __name__ == "__main__":
    plot_all(10, 30)