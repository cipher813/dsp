[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

### Code
>> cm = 2.54
>> min_cm = 70*cm
>> max_cm = 74*cm
>> print("Men between {} and {} centimeters are eligible to join BMG.".format(min_cm,max_cm))
>> min_sig = mu - min_cm
>> max_sig = max_cm - mu
>> print("This equates to min and max sigmas of {} and {}, respectively.".format(min_sig, max_sig))
>> pop_above_min = dist.cdf(mu+min_sig)
>> pop_above_max = dist.cdf(mu-max_sig)
>> bmg_eligible = pop_above_min - pop_above_max
>> print("A total of {}% of the male population is eligible to join BMG.".format(bmg_eligible))

Men between 177.8 and 187.96 centimeters are eligible to join BMG.
This equates to min and max sigmas of 0.19999999999998863 and 9.960000000000008, respectively.
A total of 0.41244300229842557% of the male population is eligible to join BMG.

### Response
41.2% of the U.S. male population is eligible to join BMG.  
