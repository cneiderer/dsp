[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.

In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). 

What percentage of the U.S. male population is in this range? (Hint: use scipy.stats.norm.cdf)

>> ```python
>> import scipy.stats
>> ```
>>
>> Generate normal distribution from male stats
>> ```python
>> mu = 178
>> sigma = 7.7
>> dist = scipy.stats.norm(loc=mu, scale=sigma)
>> ```
>>
>> Convert height limits to cm
>> ```python
>> min_ht = (5 * 12 + 10) * 2.54 # 5'10"
>> max_ht = (6 * 12 + 1) * 2.54 # 6'1"
>> 
>> Compute percentage of population between height limits
>> ```python
>> pct = (dist.cdf(max_ht) - dist.cdf(min_ht)) * 100
>> print(('{:.2f}% is eligible to join Blue Man Group').format(pct))
>> ```
>> 34.27% of the male population is eligible to joing Blue Man Group.
