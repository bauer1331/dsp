[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> The total weight comparison between first born and other order born children showed that the mean of first born children was lighter, by 0.12 pounds than the mean of children born in another order. The effect size of this difference produced a Cohen's D of -0.0887. This is a rather small effect size, which makes common sense as teh difference between the two means was 0.124 pounds. However, in comparison to pregnancy length the difference in means were .078 weeks, or 13 hours, and the Cohen's D effect size 0.0289, the effect of birth weight is about three times larger than pregnancy length. 


import numpy as np
import math
import nsfg

def ReadFemPreg(dct_file='2002FemPreg.dct',
               dat_file='2002FemFreg.dat.gz'):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    CleanFemFreg(df)
    return df

def CleanFemPreg(df):
    df.agepreg /= 100.0
    
    na_vals = [97, 98, 99]
    df.birthwgt_lb.replace(na_vals, np.nan, inplace=True)
    df.birthwgt_oz.replace(na_vals, np.nan, inplace=True)
    
    df['totalwgt_lb'] = df.birthwgt_lb + df.birthgwt_oz / 16.0

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

if firsts.totalwgt_lb.mean() > others.totalwgt_lb.mean():
    x = 'First babies heavier'
else:
    if firsts.totalwgt_lb.mean() == others.totalwgt_lb.mean():
        x = 'First and other babies equal'
    else: x = 'First babies lighter'
    print x
print firsts.totalwgt_lb.mean() - others.totalwgt_lb.mean()

print CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

print CohenEffectSize(firsts.prglngth, others.prglngth)
print firsts.prglngth.mean() - others.prglngth.mean()
