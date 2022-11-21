'''
@File    :   main.py
@Contact :   996852067@qq.com
@License :   (C)Copyright 2021-2022

@Modify Time           @Author    @Version    @Desciption
------------           -------    --------    -----------
2022/11/10 下午6:45    xuzhiyuan     1.0       main entrance with UI
'''

import math
import os
import sys
import pandas as pd
from PyQt5.QtGui import QPixmap
from scipy import stats
import plot_Making
import tools
import data_Processing
import datetime
from PyQt5 import QtWidgets
from UI.UI_main import Ui_main_window
from BSE import market_session


FILE_PATH = './DataFile/'
IMG_PATH = './Img/'


class UI_BSE_WINDOW(QtWidgets.QMainWindow):
    # Main UI init function
    def __init__(self, parent=None):
        super(UI_BSE_WINDOW, self).__init__(parent)
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.init_combobox()
        self.init_spinbox()
        self.init_slots()

    # init all slots
    def init_slots(self):
        self.ui.pushButton_Start.clicked.connect(self.pushbutton_start_clicked)
        self.ui.pushButton_CopytoBuyer.clicked.connect(self.pushbutton_CopytoBuyer_clicked)
        self.ui.horizontalSlider.valueChanged.connect(self.slider_changed)

    # SLOT button start
    def pushbutton_start_clicked(self):
        print('start')
        # read data from UI
        self.get_trader_selection()
        self.get_basic_selection()
        # run BSE market
        self.start_BSE_simulation()



    # SLOT button CopytoBuyer
    def pushbutton_CopytoBuyer_clicked(self):
        for i in range(1, 5):
            combobox_str = 'self.ui.comboBox_t' + str(i) + '.currentIndex()'
            spinbox_str = 'self.ui.spinBox_t' + str(i) + '.value()'
            copy_traders_str = 'self.ui.comboBox_t' + str(i + 4) + '.setCurrentIndex(' + str(eval(combobox_str)) + ')'
            copy_numbers_str = 'self.ui.spinBox_t' + str(i + 4) + '.setValue(' + str(eval(spinbox_str)) + ')'
            eval(copy_traders_str)
            eval(copy_numbers_str)


    # market change time point
    def slider_changed(self):
        label_change = 'Stock_change time : ' + str(self.ui.horizontalSlider.value()) + '%'
        self.ui.label_change.setText(label_change)


    def init_combobox(self):
        # init Traders combobox
        Traders = ['None', 'SNPR', 'GVWY', 'SHVR', 'ZIC', 'ZIP']
        self.ui.comboBox_t1.addItems(Traders)
        self.ui.comboBox_t2.addItems(Traders)
        self.ui.comboBox_t3.addItems(Traders)
        self.ui.comboBox_t4.addItems(Traders)
        self.ui.comboBox_t5.addItems(Traders)
        self.ui.comboBox_t6.addItems(Traders)
        self.ui.comboBox_t7.addItems(Traders)
        self.ui.comboBox_t8.addItems(Traders)
        self.ui.comboBox_t1.setCurrentIndex(5)
        self.ui.comboBox_t5.setCurrentIndex(5)


        # init StepMode combobox
        StepMode = ['fixed', 'random', 'jittered']
        self.ui.comboBox_stepMode.addItems(StepMode)
        self.ui.comboBox_stepMode.setCurrentIndex(0)


        # init TimeMode comboBox
        TimeMode = ['periodic', 'drip-fixed', 'drip-jitter', 'drip-poisson']
        self.ui.comboBox_timeMode.addItems(TimeMode)
        self.ui.comboBox_timeMode.setCurrentIndex(0)


    def init_spinbox(self):
        # set Traders number
        self.ui.spinBox_t1.setValue(11)
        self.ui.spinBox_t5.setValue(11)

        # set Price range
        self.ui.spinBox_buyerRange1.setValue(50)
        self.ui.spinBox_buyerRange2.setValue(250)
        self.ui.spinBox_sellerRange1.setValue(50)
        self.ui.spinBox_sellerRange2.setValue(250)
        self.ui.spinBox_buyerRange3.setValue(200)
        self.ui.spinBox_buyerRange4.setValue(400)
        self.ui.spinBox_sellerRange3.setValue(200)
        self.ui.spinBox_sellerRange4.setValue(400)

        # set Market time
        self.ui.spinBox_marketTime.setValue(10)

        #set Total trials number
        self.ui.spinBox_totalTrials.setValue(10)
        self.ui.spinBox_orderInterval.setValue(30)

    # get seller & buyer & number
    def get_trader_selection(self):
        self.traders = []
        for i in range(1, 9):
            combobox_str = 'self.ui.comboBox_t' + str(i) + '.currentText()'
            if eval(combobox_str) != 'None':
                spinbox_str = 'self.ui.spinBox_t' + str(i) + '.value()'
                self.traders.append((i, eval(combobox_str), eval(spinbox_str)))

    def get_basic_selection(self):
        self.market_runtime = self.ui.spinBox_marketTime.value()
        self.order_interval = self.ui.spinBox_orderInterval.value()
        self.stepMode = self.ui.comboBox_stepMode.currentText()
        self.timeMode = self.ui.comboBox_timeMode.currentText()
        self.totalTrials = self.ui.spinBox_totalTrials.value()
        self.seller_price_range = []
        self.seller_price_range.append((self.ui.spinBox_sellerRange1.value(), self.ui.spinBox_sellerRange2.value()))
        if self.ui.spinBox_sellerRange3.value() != 0:
            self.seller_price_range.append((self.ui.spinBox_sellerRange3.value(), self.ui.spinBox_sellerRange4.value()))

        self.buyer_price_range = []
        self.buyer_price_range.append((self.ui.spinBox_buyerRange1.value(), self.ui.spinBox_buyerRange2.value()))
        if self.ui.spinBox_buyerRange3.value() != 0:
            self.buyer_price_range.append((self.ui.spinBox_buyerRange3.value(), self.ui.spinBox_buyerRange4.value()))

        self.market_change_time = self.ui.horizontalSlider.value()

        self.flag_saveImages = self.ui.checkBox_saveImages.isChecked()
        self.flag_verbose = self.ui.checkBox_verbose.isChecked()


    def info_into_plaintext(self, time):
        file_str = './DataFile/%s/Profit_%d_%d_summary.csv' % (time, self.market_runtime, self.order_interval)
        profit_file = pd.read_csv(file_str)
        profit_file = profit_file.iloc[0:, 1:]
        str_info = ''
        for col in profit_file.columns:
            strs = ("Trader :\t" + "[ {:} ]".format(col) +
                  "\n\t[ mean ] = " + "{:.2f}".format(profit_file[col].mean()) +
                  "\n\t[ std ] = " + "{:.2f}".format(profit_file[col].std())) + '\n'
            str_info = str_info + strs

            # Normalise data
            temp_data = (profit_file[col] - profit_file[col].mean()) / profit_file[col].std()
            statistic, pvalue = stats.kstest(temp_data, stats.norm.cdf)
            str_info = str_info + '\t[ Kstest pValue ]= ' + '{:.2f}'.format(pvalue) + '\n\n\n'

        self.ui.textEdit_info.setText(str_info)

    # create the corresponding folder for each Market-Use
    def create_folder(self):
        # get current time
        now = datetime.datetime.now()
        other_StyleTime = now.strftime("%H:%M:%S")
        print(other_StyleTime)
        str = 'mkdir ' + FILE_PATH + other_StyleTime
        strr = 'mkdir ' + IMG_PATH + other_StyleTime
        os.system(str)
        os.system(strr)
        return other_StyleTime

    # load image into ui
    def load_price_trader_map(self, map1_path):
        pixmap = QPixmap(map1_path)  # find map through path
        self.ui.label_map1.setPixmap(pixmap)
        self.ui.label_map1.setScaledContents(True)

    def load_box_vio_map(self, map2_path):
        pixmap = QPixmap(map2_path + 'Box_plot')  # find map through path
        self.ui.label_map2.setPixmap(pixmap)
        self.ui.label_map2.setScaledContents(True)

        pixmap = QPixmap(map2_path + 'Kdeplot')  # find map through path
        self.ui.label_map3.setPixmap(pixmap)
        self.ui.label_map3.setScaledContents(True)



    # ######################################### MAIN ################################################
    def start_BSE_simulation(self):
        # pre-work : file folder
        tools.touch_data_file()

        # set a time(Minutes) as a market day to run BSE
        market_run_time = self.market_runtime
        start_time = 0
        end_time = 60 * market_run_time
        mid_time = 0

        if self.market_change_time != 0:
            mid_time = self.market_change_time * 60 * 1/10

        '''

            Set price ranges eg:
                (80, 320) single ranges
                (80, 320, schedule_offsetfn) range with offset for dynamic market
                [(100, 200), (200, 300)] multiple ranges, can be used with 'stepmode' = 'random'
        '''
        price_range_seller = self.seller_price_range
        price_range_buyer = self.buyer_price_range

        '''
            @stepmode : @fixed :    prices are generated to give a constant difference between successive prices when sorted into order.
                        @random :   randomly choose one of the price ranges from tuple.
                        @jittered : starts with a fixed stepmode but then randomly adjusts simulating random noise.
        '''

        # another way to simulate dynamic market with 'Market Shocks'
        supply_schedule = [
            {'from': start_time, 'to': end_time, 'ranges': [price_range_seller[0]], 'stepmode': self.stepMode}]
        demand_schedule = [
            {'from': start_time, 'to': end_time, 'ranges': [price_range_buyer[0]], 'stepmode': self.stepMode}]

        if mid_time != 0:
            supply_schedule = [
                {'from': start_time, 'to': mid_time, 'ranges': [price_range_seller[0]], 'stepmode': self.stepMode},
                {'from': mid_time, 'to': end_time, 'ranges': [price_range_seller[1]], 'stepmode': self.stepMode}]
            demand_schedule = [
                {'from': start_time, 'to': mid_time, 'ranges': [price_range_buyer[0]], 'stepmode': self.stepMode},
                {'from': mid_time, 'to': end_time, 'ranges': [price_range_buyer[1]], 'stepmode': self.stepMode}]

        order_interval = self.order_interval
        '''
                @timemode : @periodic :     give new orders periodically for each beginning of interval.
                            @drip-fixed :   use p second as basics then generate 'fake constant orders'.
                            @drip-jitter :  same as drip-fixed mode with some noise.
                            @drip-poisson : following poisson distribution.
        '''
        order_schedule = {'sup': supply_schedule, 'dem': demand_schedule, 'interval': order_interval,
                          'timemode': self.timeMode}

        # set the type and number of the robots
        sellers = []
        buyers = []
        for i in range(0, len(self.traders)):
            if self.traders[i][0] <= 4:
                sellers.append((self.traders[i][1], self.traders[i][2]))
                continue
            buyers.append((self.traders[i][1], self.traders[i][2]))
        traders = {'sellers': sellers, 'buyers': buyers}

        timestamp = self.create_folder()
        timestamp = timestamp + '/'
        map_path1 = ''

        # output file name
        trail = 1
        n_trail = self.totalTrials
        while trail <= n_trail:
            trail_id = FILE_PATH + timestamp + 'Zhiyuan_%d_%d_%d' % (market_run_time, order_interval, trail)
            tdump = open(trail_id + '_avg_balance.csv', 'w')
            # random.seed(100)
            dump_all = True
            verbose = self.flag_verbose  # @True  output all file  @False output simple file

            # Use the function of BSE.py, start market simulation
            market_session(trail_id, start_time, end_time, traders, order_schedule, tdump, dump_all, verbose)
            tdump.close()

            # summarize robot & total profit into one single file
            map1_path = plot_Making.plot_trades(trail_id, trail, timestamp, save = self.flag_saveImages)

            data_Processing.get_profit_file(trail, n_trail, market_run_time, order_interval, trail_id, timestamp)
            tools.delete_verbose_file(trail_id, 1)

            trail += 1

        # analyzing include(mean, std, normal distribution, t-test, ANOVA) and output images
        map23_path = data_Processing.data_analyze(market_run_time, order_interval, timestamp, ImgSave = self.flag_saveImages)
        self.load_price_trader_map(map1_path)
        self.load_box_vio_map(map23_path)
        self.info_into_plaintext(timestamp)

        # ZIP vs Other Agent
        # data_Processing.agent_agent_winner(market_run_time, order_interval, timestamp)





# Schedule_offsetfn is the first way to simulate dynamic market
# which can dynamically change the supply and demand curves during an experiment.
# if supply and demand ranges use the same offset function, then equbilium price fluctuated over time
def schedule_offsetfn(t):
    pi2 = math.pi * 2
    c = math.pi * 3000
    wavelength = t / c
    gradient = 100 * t / (c / pi2)
    amplitude = 100 * t / (c / pi2)
    offset = gradient + amplitude * math.sin(wavelength * t)
    return int(round(offset, 0))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    current_ui = UI_BSE_WINDOW()
    current_ui.show()
    sys.exit(app.exec_())



