[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

### Code:
>> pmf = thinkstats2.Pmf(resp['numkdhh'], label='Actual')
>> biased_pmf = BiasPmf(pmf, label='Observed')
>> thinkplot.Pmfs([pmf, biased_pmf])
>> thinkplot.Config(xlabel='No. Children per Household', ylabel='PMF')

>> print('Actual mean', pmf.Mean())
>> print('Observed mean', biased_pmf.Mean())
Actual mean 1.024205155043831
Observed mean 2.403679100664282

### Response
The actual mean of 1.02 is below the observed mean of 2.40 because, for a survey taken by asking the children, children in big families would overrrepresent their families and
families with no children would not be represented at all.  
