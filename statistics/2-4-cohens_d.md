[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

> > Compute the Cohen effect size for the difference in weight of first babies and others. 
`effectSize = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)`
Print rounded and formatted Cohen effect size.
`'{:.5f}'.format(np.around(effectSize, 5))`
`'-0.08867'`
