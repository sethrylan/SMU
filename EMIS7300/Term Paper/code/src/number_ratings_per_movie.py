#!/usr/bin/env python
import csv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import lognorm, rayleigh, norm
from array import array



values = array('l', [])
for row in csv.reader(open('C:/school/emis7300/term paper/work/num_ratings_per_movie.csv','rb')):
    if values.buffer_info()[1] % 1000 == 0:
        print values.buffer_info()[1]
#    if values.buffer_info()[1] >= 5000:
#        break
    values.append(long(row[0]))

mu, sigma, numbins = np.mean(values), np.std(values), 12000
print 'size=\t' + str(values.buffer_info()[1])
print 'mu=\t' + str(mu)
print 'sigma=\t' + str(sigma)
print 'median=\t' + str(np.median(values, axis=0))
#print stats.skew(values)

# the histogram of the data
n, bins, patches = plt.hist(values, numbins, normed=True, facecolor='cyan', alpha=0.75)
#doesn't appear to be lognormal
shape, loc, scale = stats.lognorm.fit(values, floc=0)
print np.log(scale), shape  # mu, sigma, 4.57364532995 1.3159903533
dist=lognorm(shape,loc=np.log(scale)) #sigma, mu
l = plt.plot(bins, dist.pdf(bins), 'b--', linewidth=1)

#let's try rayleigh
#samp = rayleigh.rvs(loc=5,scale=2,size=150) # samples generation
param = rayleigh.fit(values) # distribution fitting
#x = linspace(5,13,100)
# fitted distribution
pdf_fitted = rayleigh.pdf(bins,loc=param[0],scale=param[1])
print param
# original distribution
pdf = rayleigh.pdf(bins,loc=5,scale=2)
#title('Rayleigh distribution')
#plot(x,pdf_fitted,'g-',x,pdf,'b-')
#hist(samp,normed=1,alpha=.3)
#show()

normed_data=(values-mu)/sigma
print 'kstest:',
print(stats.kstest(normed_data,'norm'))
print 'anderson-darling:',
print(stats.anderson(normed_data,'norm'))
print 'shapiro-wilk',
print(stats.shapiro(values))

l = plt.plot(bins, pdf_fitted, 'r--', linewidth=1)

plt.xlabel('# of Ratings')
plt.ylabel('Probability')
plt.title(r'$\mathrm{\#\ Ratings\ Per\ Movie:}\ n=' + str(values.buffer_info()[1]) + ',\ \mu=' + str(round(mu,3)) + ',\ median=' + str(np.median(values, axis=0)) + '$' )
plt.axis([1, 15000, 0, .0043])
plt.grid(True)

plt.show()
