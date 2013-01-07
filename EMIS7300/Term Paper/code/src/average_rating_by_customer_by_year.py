#!/usr/bin/env python
from __future__ import division
import csv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as stats
from array import array


colors = {1999: '#eeefff',
          2000: '#eeefff',
          2001: '#eeefff',
          2002: '#eeefff',
          2003: '#eeefff',
          2004: '#eeefff',
          2005: '#eeefff'
          }


for year in range(1999, 2006):
    print year

#    values = np.array([])
    values = array('h', [])
    for row in csv.reader(open('C:/school/emis7300/term paper/work/ratings_' + str(year) + '.csv','rb')):
        if values.buffer_info()[1] % 10000 == 0:
            print str(values.buffer_info()[1]) + ',' ,
#        if values.size >= 100000:
#            break
#        values = np.append(values, float(row[0]))
        values.append(int(row[0]))
    print ""
    
    mu, sigma, numbins = np.mean(values), np.std(values), 500
    print '\tsize=\t' + str(values.buffer_info()[1])
    print '\tmu=\t' + str(round(mu,3))
    print '\tsigma=\t' + str(round(sigma,3))
    print '\tskew=\t' + str(round(stats.skew(values),3))
    print '\tkurtosis=\t' + str(round(stats.kurtosis(values),3))

    # the histogram of the data

#    n, bins, patches = plt.hist(values, numbins, normed=True, facecolor=colors[year], alpha=0.5)
#
#    plt.text(mu + ((year - 2003)/3), 1.0, r'$\mu=$' + str(round(mu,3)) + ',\n$\sigma=' + str(round(sigma, 3)) + '$')



#plt.xlabel('Rating')
#plt.ylabel('Probability')
#plt.title(r'$\mathrm{Ratings\ By\ Year:}' + '$')
#
##    plt.title(r'$\mathrm{Average\ Rating\ By\ Movie:}\ n=' + str(values.size) + ',\ \mu=' + str(round(mu,3)) + ',\ \sigma=' + str(round(sigma, 3)) + '$'+ '\n$\mathrm{}kurtosis=' + str(round(stats.kurtosis(values),3)) + ',\ skew=' + str(round(stats.skew(values),3)) + '$')
#plt.axis([1, 5, 0, 3.2])
#plt.grid(True)
#
#plt.show()
