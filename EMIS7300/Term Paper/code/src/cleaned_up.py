

#!/usr/bin/env python
import csv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as stats
from array import array

values = array('f', [])
for row in csv.reader(open('avg_ratings.csv','rb')):
    values.append(float(row[0]))

mu, sigma, numbins = np.mean(values), np.std(values), 100
normed_data=(values-mu)/sigma
print(stats.kstest(normed_data,'norm'))

# histogram of the data
n, bins, patches = plt.hist(values, numbins, normed=True,\
                            facecolor='blue', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=1)

...

plt.show()


