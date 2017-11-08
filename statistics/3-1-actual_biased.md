[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)  
  
Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.  

Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household.  
  
Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household.  
  
Plot the actual and biased distributions, and compute their means. (As a starting place, you can use chap03ex.ipynb)
  
>> Load data  
>> ```python
>> resp = nsfg.ReadFemResp()
>> ```
>>
>> Construct distribution  
>> ```python
>> pmf = thinkstats2.Pmf(resp.numkdhh, label='numkdhh')
>> ```
>>
>> Plot pmf as bars and steps  
>> ```python 
>> # Bar Chart
>> thinkplot.PrePlot(2, cols=2)
>> thinkplot.Hist(pmf)
>> thinkplot.Config(xlabel='Number of Children < 18', ylabel='PMF')
>> # Step Function
>> thinkplot.PrePlot(2)
>> thinkplot.SubPlot(2)
>> thinkplot.Pmf(pmf)
>> thinkplot.Config(xlabel='Number of Children < 18', ylabel='PMF')
>> ```
>>
>> Compute biased distribution  
>> ```python
>>  biased_pmf = BiasPmf(pmf, label='biased')
>> ```
>> 
>> Plot actual and biased distributions  
>> ```python
>> pmf.label = 'actual
>> thinkplot.PrePlot(2)
>> thinkplot.Pmfs([pmf, biased_pmf])
>> thinkplot.Config(xlabel='Num Kid < 18', ylabel='PMF')
>> ```
>> 
>> Compute actual and biased means  
>> ```python
>> print('Actual mean:', pmf.Mean())
>> print('Biased mean:', biased_pmf.Mean())
>> ```
>> Actual mean: 1.02420515504  
>> Observed mean: 2.40367910066  

