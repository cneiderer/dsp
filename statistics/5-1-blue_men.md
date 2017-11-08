[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.

In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). 

What percentage of the U.S. male population is in this range? (Hint: use scipy.stats.norm.cdf)

>> ```python
>> # Convert height limits to cm
>> min_ht = (5 * 12 + 10) * 2.54 # 5'10"
>> max_ht = (6 * 12 + 1) * 2.54 # 6'1"
>> 
>> # Compute percentage of population between height limits
>> pct = (dist.cdf(max_ht) - dist.cdf(min_ht)) * 100
>> print(('{:.2f}%').format(pct))
>> ```
>> 34.27%
