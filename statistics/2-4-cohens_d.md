[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)  
  
Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?  
  
>> Compute the Cohen effect size for the difference in pregnancy length for first babies and others.  
>> ```python
>> lenEffect = CohenEffectSize(firsts.prglngth, others.prglngth)
>> print('{:.10f}'.format(lenEffect))
>> ```
>> 0.0288790447
>>
>> Compute the Cohen effect size for the difference in birth weight for first babies and others.  
>> ```python
>> wgtEffect = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
>> print('{:.10f}'.format(wgtEffect))
>> -0.0886729271
>> ```
>>
>> Compare the effect sizes.  
>> ```python
>> effectDiff = np.abs(wghEffect) - np.abs(lenEffect)
>> print('{:.10f}'.format(effectDiff))
>> ```
>> 0.0597938824
>>
>> Birth order has a greater effect on birth weight than on pregnancy length.
>>
