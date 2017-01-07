[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> Finding summary statistics on the number of kids per household for this actual vs. biased sample focuses on a difference between the bases assumed to highlight a missing data problem, and disproportional probability in sampling. For example, the biased sample "surveys" kids and determines how many siblings each of them has. As pointed out in the book this eliminates all households without kids. This is where the biased sample is sampling from the incorrect base, it is focusing on kids instead of households. It assumes all households have kids or that only households that have kids are relevant, overlooking households without kids. Furthermore, each additional child in a household increases the likelihood that a child from that household will get chosen for the sample and increasing the number of siblings sampled, creating a biased sample. Combined, the observed sample comes out with a mean of 1.02 kids per household compared to the biased sample with a mean of 2.40, doubling the mean. 

![PMF Graph](https://github.com/bauer1331/dsp/blob/master/statistics/biasedVsUnbiased.png)

import numpy as np
import thinkstats2
import thinkplot
import nsfg

dfkids = nsfg.ReadFemResp()

pmf_num_kids = thinkstats2.Pmf(dfkids.numkdhh, label='Observed')
print ('mean', pmf_num_kids.Mean())
#('mean', 1.0242051550438309)

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    
    for x, p in pmf.Items():
        new_pmf.Mult(x,x)
        
    new_pmf.Normalize()
    return new_pmf

biased_num_kids = BiasPmf(pmf_num_kids, label='Biased')
print ('mean', biased_num_kids.Mean())
#('mean', 2.4036791006642821)

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf_num_kids, biased_num_kids])
thinkplot.Show(xlabel='Number of Kids', ylabel='PMF')
print('mean', biased_num_kids.Mean())
