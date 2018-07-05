import csv, datetime
from pylab import *
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

def set_data(filename, username):
    days = []
    dib_rm_karma = []
    actual_karma = []

    with open (filename, 'r') as file:
        date = 0
        dib = 0
        karma = 0

        dat_prev = None
        dib_r_prev = None
        kar_prev = None

        reader = csv.reader(file)
        c = 0
        for row in reader:
            if c == 0:
                if 'author_karma' in row:
                    karma = row.index('author_karma')
                elif 'karma' in row:
                    karma = row.index('karma')
                dib = row.index('dib_rm')
                date = row.index('created_utc')
            else:
                if row[1] == username:
                    dat = datetime.datetime.strptime((row[date]), "%Y-%m-%d %H:%M:%S").date()
                    dib_r = float(row[dib])
                    kar = float(row[karma])
                    if dat!=dat_prev and dat_prev is not None:
                        days.append(dat_prev)
                        dib_rm_karma.append(dib_r_prev)
                        actual_karma.append(kar_prev)
                    dat_prev = dat
                    dib_r_prev = dib_r
                    kar_prev = kar
            c+=1

    return days, dib_rm_karma, actual_karma

def build_graph(days, dib_rm_karma, actual_karma):
    x_axis = range(len(days))
    figure()
    plot(x_axis, dib_rm_karma, color = "red", label = "DIB_RM")
    plot(x_axis, actual_karma, color = "blue", label = "Reddit")
    legend()
    xticks(x_axis, days, rotation = 45)
    plt.xlabel("Date")
    plt.ylabel("Rating")
    show()

def main():
    days, d, a = set_data('test_data_posts.csv', 'MisterBadIdea2')
    print(days)
    print(d)
    print(a)
    build_graph(days, d, a)


if __name__ =='__main__':
    main()


