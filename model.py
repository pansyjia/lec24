#model.py
import csv

BB_FILE_NAME = 'umbball.csv'

bb_seasons = []
# create the list
def init_bball(csv_file_name=BB_FILE_NAME):
    global bb_seasons
    with open(csv_file_name) as f:
        reader = csv.reader(f)
        next(reader) # throw away headers
        next(reader) # throw away headers
        global bb_seasons
        bb_seasons = [] # reset, start clean
        for r in reader:
            r[3] = int(r[3])
            r[4] = int(r[4])
            r[5] = float(r[5])
            bb_seasons.append(r)

FB_FILE_NAME = 'umfootball.csv'

fb_seasons = []
# create the list
def init_fball(csv_file_name=FB_FILE_NAME):
    global fb_seasons
    with open(csv_file_name) as f:
        reader = csv.reader(f)
        next(reader) # throw away headers
        next(reader) # throw away headers
        global fb_seasons
        fb_seasons = [] # reset, start clean
        for r in reader:
            r[3] = int(r[3])
            r[4] = int(r[4])
            r[6] = float(r[6])
            fb_seasons.append(r)


def get_bball_seasons(sortby='year', sortorder='desc'):
    if sortby == 'year':
        sortcol = 1
        # index no. 1, 3, 5
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 5
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    # sort a list of list
    sorted_list = sorted(bb_seasons, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list


def get_fball_seasons(sortby='year', sortorder='desc'):
    if sortby == 'year':
        sortcol = 1
        # index no. 1, 3, 5
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 5
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    # sort a list of list
    sorted_list = sorted(fb_seasons, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list
