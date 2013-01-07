#!/usr/bin/env python
import csv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as stats

values = np.array([])
for row in csv.reader(open('C:/school/emis7300/term paper/work/avg_rating_per_movie.csv','rb')):
    if values.size % 1000 == 0:
        print values.size
#    if values.size >= 5000:
#        break
    values = np.append(values, float(row[0]))

mu, sigma, numbins = values.mean(), values.std(), 100
print 'size=\t' + str(values.size)
print 'mu=\t' + str(mu)
print 'sigma=\t' + str(sigma)
print stats.skew(values)

# the histogram of the data
n, bins, patches = plt.hist(values, numbins, normed=True, facecolor='green', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=1)

#pdfy, pdfx = statistics.pdf(values)
#cdfx, cdfy = statistics.cdfp(values)
#pdfl = plt.plot(bins, pdfy, 'g--', linewidth=1)

normed_data=(values-mu)/sigma
print 'kstest:',
print(stats.kstest(normed_data,'norm'))
print 'anderson-darling:',
print(stats.anderson(normed_data,'norm'))
print 'shapiro-wilk',
print(stats.shapiro(values))

plt.xlabel('Average Rating')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Average\ Rating\ By\ Movie:}\ n=' + str(values.size) + ',\ \mu=' + str(round(mu,3)) + ',\ \sigma=' + str(round(sigma, 3)) + '$'+ '\n$\mathrm{}kurtosis=' + str(round(stats.kurtosis(values),3)) + ',\ skew=' + str(round(stats.skew(values),3)) + '$')
plt.axis([1, 5, 0, .85])
plt.grid(True)

plt.show()
