[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> The shortest men that could be in the Blue Man Group are in the .4896 percentile and the tallest are at the .8323 percentile. The difference between the two is .3427, or 32.27% of the male population is qualified in height to join the Blue Man Group.

import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)

dist.mean(), dist.std()

shortest = 70*2.54
tallest = 73*2.54
print 'shortest', dist.cdf(shortest)*100, 'tallest', dist.cdf(tallest)*100
print 'percentage',(dist.cdf(tallest) - dist.cdf(shortest))*100