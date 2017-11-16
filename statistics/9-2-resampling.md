[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

In Section 9.3, we simulated the null hypothesis by permutation; that is, we treated the observed values as if they represented the entire population, and randomly assigned the members of the population to the two groups.
An alternative is to use the sample to estimate the distribution for the population, then draw a random sample from that distribution. This process is called resampling. There are several ways to implement resampling, but one of the simplest is to draw a sample with replacement from the observed values, as in Section 9.10.

Write a class named DiffMeansResample that inherits from DiffMeansPermute and overrides RunModel to implement resampling, rather than permutation.

Use this model to test the differences in pregnancy length and birth weight. How much does the model affect the results?

>> Define DiffMeansResample Class
>> ```python
>> class DiffMeansResample(DiffMeansPermute):
>>
>>     def RunModel(self):
>>         group1 = np.random.choice(self.pool, self.n, replace=True)
>>         group2 = np.random.choice(self.pool, self.m, replace=True)
>>        
>>         return group1, group2
>>```
>>
>> Test the differences in pregancy length between first-born and other babies.
>> ```python
>> data = firsts.prglngth.values, others.prglngth.values
>> ht = DiffMeansResample(data)
>> p_value = ht.PValue()
>> print('DiffMeansResample Pregnancy Length:')
>> if p_value == 0: 
>>     p_value = '< 0.001'
>> print('p-value =', p_value)
>> print('actual =', ht.actual)
>> print('ts max =', ht.MaxTestStat())
>> ```
>> DiffMeansResample Pregnancy Length:  
>> p-value = 0.173  
>> actual = 0.0780372667775  
>> ts max = 0.206175715361  
>>
>> Test the differences in birth weight between first-born and other babies.
>> ```python
>> data = firsts.totalwgt_lb.dropna().values, others.totalwgt_lb.dropna().values
>> ht = DiffMeansResample(data)
>> p_value = ht.PValue()
>> print('DiffMeansResample Birth Weight:')
>> if p_value == 0: 
>>     p_value = '< 0.001'
>> print('p-value =', p_value)
>> print('actual =', ht.actual)
>> print('ts max =', ht.MaxTestStat())
>> ```
>> DiffMeansResample Birth Weight:  
>> p-value = < 0.001  
>> actual = 0.124761184535  
>> ts max = 0.0925545575887  
>>
>> In this case, model selection between permutation and resampling minimally effects the results.
>>
