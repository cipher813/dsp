[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

### Code
>> r =np.random.random(1000)

>> width = 0.4 / 1000
>> pmf = thinkstats2.Pmf(r, label='Random Number Generated')
>> thinkplot.Hist(pmf,width=width)
>> thinkplot.Config(xlabel='Random Number Generated', ylabel='PMF')

>> thinkplot.Pmf(pmf)
>> thinkplot.Config(xlabel='RNG', ylabel='Pmf')

>> cdf = thinkstats2.Cdf(r, label='Random Number Generated')
>> thinkplot.Cdf(cdf)
>> thinkplot.Config(xlabel='Random Number Generated', ylabel='CDF', loc='upper left')

### Response

The PMF data appears uniformly distributed. The data is relatively evenly spread out throughout the range, but using this chart alone it is difficult to tell whether the information is indeed uniformly distributed. A potential issue is that the numbers are continous vs discrete (such as an integer), so in theory all 1000 numbers are different.

Per the CDF, it is clear that the distribution is uniform.
