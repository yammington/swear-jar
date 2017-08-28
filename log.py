import datetime as dt


def Log(string):
    ts = dt.datetime.now()
    print('['+str(ts)+']:'+string)
