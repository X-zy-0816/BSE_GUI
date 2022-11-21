import os


# pre-work : file folder
def touch_data_file(data_path = './DataFile', img_path = './Img'):
    if os.access(data_path, os.F_OK):
        print("Data_File folder exist")
    else:
        print("Data_File is not accessible. Creating file")
        osString = 'mkdir ' + data_path
        os.system(osString)

    if os.access(img_path, os.F_OK):
        print("Img_File folder exist")
    else:
        print("Img_File is not accessible. Creating file")
        osString = 'mkdir ' + img_path
        os.system(osString)


# delete test file
def delete_output_file(trial_id, flag):
    if flag == True:
        os.system('rm {}*'.format(trial_id))
        # os.system('rm avg_balance.csv')


# delete detail file (Useless for now)
def delete_verbose_file(trail_id, flag):
    if flag == True:
        os.system('rm {}_LOB_frames.csv'.format(trail_id))
        os.system('rm {}_strats.csv'.format(trail_id))

# use for delete all output files
def delete_all():
    os.system('rm ./DataFile/Zhiyuan*')
    os.system('rm ./DataFile/Profit*')
    os.system('rm ./Img/*')


if __name__ == "__main__":
    delete_all()
