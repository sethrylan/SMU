#!/usr/bin/env python
import csv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as stats
from array import array

values = array('f', [])
for row in csv.reader(open('C:/school/emis7300/term paper/work/avg_rating_per_customer.csv','rb')):
    values.append(float(row[0]))

mu, sigma, numbins = np.mean(values), np.std(values), 100
print 'size=\t' + str(values.buffer_info()[1])
print 'mu=\t' + str(mu)
print 'sigma=\t' + str(sigma)


normed_data=(values-mu)/sigma
print 'kstest:', 
print(stats.kstest(normed_data,'norm'))
print 'anderson-darling:',
print(stats.anderson(normed_data,'norm'))
print 'shapiro-wilk',
print(stats.shapiro(values))
#print 'custom anderson:',
#print adstatistic(values)


#normalizedfunc = np.vectorize(lambda x, y: x/y)
#values = normalizedfunc(values, numbins)

#how to normalize to value other than 1
#x = np.random.random(100)
#normed_value = 1
#hist, bins = np.histogram(x, bins=20, density=True)
#widths = np.diff(bins)
#hist *= normed_value
#plt.bar(bins[:-1], hist, widths)
#plt.show()

# the histogram of the data
n, bins, patches = plt.hist(values, numbins, normed=True, facecolor='blue', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=1)

#pdfy, pdfx = statistics.pdf(values)
#cdfx, cdfy = statistics.cdfp(values)
#pdfl = plt.plot(bins, pdfy, 'g--', linewidth=1)

plt.xlabel('Average Rating')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Average\ Rating\ By\ Customer:}\ n=' + str(values.buffer_info()[1]) + ',\ \mu=' + str(round(mu,3)) + ',\ \sigma=' + str(round(sigma, 3)) + '$' + '\n$\mathrm{}kurtosis=' + str(round(stats.kurtosis(values),3)) + ',\ skew=' + str(round(stats.skew(values),3)) + '$')
plt.axis([1, 5, 0, 1.0])
plt.grid(True)

plt.show()
