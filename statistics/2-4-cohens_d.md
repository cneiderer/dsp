[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

> > Compute the Cohen effect size for the difference in weight of first babies and others.\n 
`effectSize = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)`\n\n
Print Cohen effect size formatted and rounded to 5 decimal places.\n
`print('{:.5f}'.format(np.around(effectSize, 5)))`\n
`-0.08867`
