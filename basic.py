import random
import math

import plot_Making
import tools
import data_Processing

from BSE import market_session

FILE_PATH = './DataFile/'


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

    # pre-work : file folder
    tools.touch_data_file()

    # set a time(Minutes) as a market day to run BSE
    market_run_time = 10
    start_time = 0
    end_time = 60 * market_run_time

    '''
		Set price ranges eg: 
			(80, 320) single ranges
			(80, 320, schedule_offsetfn) range with offset for dynamic market
			[(100, 200), (200, 300)] multiple ranges, can be used with 'stepmode' = 'random'
	'''
    price_range1 = (50, 200)
    price_range2 = (250, 450)

    '''
		@stepmode : @fixed :    prices are generated to give a constant difference between successive prices when sorted into order. 
					@random :   randomly choose one of the price ranges from tuple.
					@jittered : starts with a fixed stepmode but then randomly adjusts simulating random noise.
	'''
    # another way to simulate dynamic market with 'Market Shocks'
    supply_schedule = [{'from': start_time, 'to': 60 * 5, 'ranges': [price_range1], 'stepmode': 'fixed'},
                       {'from': 60 * 5, 'to': end_time, 'ranges': [price_range2], 'stepmode': 'fixed'}]
    demand_schedule = [{'from': start_time, 'to': 60 * 5, 'ranges': [price_range1], 'stepmode': 'fixed'},
                       {'from': 60 * 5, 'to': end_time, 'ranges': [price_range2], 'stepmode': 'fixed'}]

    # set trade interval as market session
    order_interval = 30

    '''
			@timemode : @periodic :     give new orders periodically for each beginning of interval.
                        @drip-fixed :   use p second as basics then generate 'fake constant orders'.
						@drip-jitter :  same as drip-fixed mode with some noise.
						@drip-poisson : following poisson distribution.
	'''
    order_schedule = {'sup': supply_schedule, 'dem': demand_schedule, 'interval': order_interval,
                      'timemode': 'periodic'}

    # set the type and number of the robots

    sellers = [('ZIP', 11), ('ZIC', 11)]
    #sellers = [('ZIP', 20)]
    buyers = sellers
    traders = {'sellers': sellers, 'buyers': buyers}

    # output file name
    trail = 1
    n_trail = 1
    while trail <= n_trail:
        trail_id = FILE_PATH + 'Zhiyuan_%d_%d_%d' % (market_run_time, order_interval, trail)
        tdump = open(trail_id + '_avg_balance.csv', 'w')
        # random.seed(100)
        dump_all = True
        verbose = False  # @True  output all file  @False output simple file

        # Use the function of BSE.py, start market simulation
        market_session(trail_id, start_time, end_time, traders, order_schedule, tdump, dump_all, verbose)
        tdump.close()
        plot_Making.plot_trades(trail_id)
        # summarize robot & total profit into one single file
        # data_Porocessing.get_profit_file(trail, n_trail, market_run_time, order_interval, trail_id)
        tools.delete_verbose_file(trail_id, 1)
        trail += 1

    # analyzing include(mean, std, normal distribution, t-test, ANOVA) and output images
    # data_Porocessing.data_analyze(market_run_time, order_interval, ImgSave=True)
