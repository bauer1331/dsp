[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> The random.random() function appears to produce a uniform distribution of numbers between 0 and 1. This is shown by the CDF graph which produces a straight line with the slope of 1 or x=y. The PMF graph supports this with a graph that looks like a nearly solid block as the stepwise function reaches similar probabilities across the set of random numbers and creates stepwise lines for each of probabilites and 0, effectively shading in the area between the probabilities and 0.

![CDF Graph](https://github.com/bauer1331/dsp/blob/master/statistics/randomCdf.png)
![PMF Graph](https://github.com/bauer1331/dsp/blob/master/statistics/randomPMF.png)

import thinkstats2
import random

rand = []
for x in range (0, 1000):
    rand.append(random.random())

rand_cdf = thinkstats2.Cdf(rand)
thinkplot.Cdf(rand_cdf)
thinkplot.Show(xlabel='percentile rank', ylabel='CDF')

rand_pmf = thinkstats2.Pmf(rand)
thinkplot.Pmfs(rand_pmf)
thinkplot.Show(xlabel='probability', ylabel='PMF')

