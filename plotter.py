#! /usr/bin/python

import matplotlib
matplotlib.use('Agg') 

import os
import sys
import numpy as np
import pandas as pd
import datetime
#import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.dates as mdates
from matplotlib import dates
#matplotlib.use('Agg')
from datetime import date
import csv

try:
	filename = sys.argv[1]
except:
	filename = datetime.datetime.now().strftime("%Y%m%d")
	print filename

dataF = np.genfromtxt('log/'+filename, delimiter='\t', invalid_raise=0, names=['None', 'time', 'intensity'])

fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111)

dts = map(datetime.datetime.fromtimestamp, dataF['time'])
fds = dates.date2num(dts)
hfmt = dates.DateFormatter('%H:%M')
ax.xaxis.set_major_locator(dates.HourLocator())
ax.xaxis.set_major_formatter(hfmt)

plt.plot(fds, dataF['intensity'], 'ro', c='blue', lw=1.5, label='Intenzita') # tepla voda
plt.ylim(-16.5,-8)


ax.set_ylabel('value [X]')
ax.set_xlabel('Cas [h]')
fig.suptitle('Slunce, ' + filename, fontsize=14, fontweight='bold')
plt.grid()
plt.savefig('/media/nfs/Slunce_sumy/OUT/'+filename+'.png', bbox_inches='tight', dpi=300)

try:
    plt.show()
except:
    print "Neni X"
