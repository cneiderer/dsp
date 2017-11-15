[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

In games like hockey and soccer, the time between goals is roughly exponential. So you could estimate a team’s goal-scoring rate by observing the number of goals they score in a game. This estimation process is a little different from sampling the time between goals, so let’s see how it works.

Write a function that takes a goal-scoring rate, lam, in goals per game, and simulates a game by generating the time between goals until the total time exceeds 1 game, then returns the number of goals scored.

Write another function that simulates many games, stores the estimates of lam, then computes their mean error and RMSE.

Is this way of making an estimate biased? Plot the sampling distribution of the estimates and the 90% confidence interval. What is the standard error? What happens to sampling error for increasing values of lam?

>> Single Game Simulation
>> ```python
>> def SimulateGame(lam):
>>     """
>>     Simulates a game and returns the estimated goal-scoring rate.
>>     lam: actual goal scoring rate in goals per game
>>     """
>>     goals = 0
>>     t = 0
>>     while True:
>>         time_between_goals = random.expovariate(lam)
>>         t += time_between_goals
>>         if t > 1:
>>             break
>>         goals += 1
>> 
>>     # estimated goal-scoring rate is the actual number of goals scored
>>     L = goals
>>     return L
>> ```
>>
>> Many Game Simulation
>> ```python
>> def SimulateManyGames(lam=2, n=1000):
>>     """
>>     Simulates many games and returns the RMSE and the mean error.
>>     lam: actual goal scoring rate in goals per game
>>     n:   number of games to simulate
>>     """
>>     goals_est = []
>>     for game in range(n):
>>         goals_est.append(SimulateGame(lam))
>>      
>>     return (goals_est, RMSE(goals_est, lam), MeanError(goals_est, lam))
>> ```
>>
>> Is this estimator unbiased?
>> ```python
>> num_games = [10, 100, 1000, 10**4, 10**5, 10**6, 10**7]
>> for n in num_games:
>>     print('n={}:'.format(n), SimulateManyGames(n=n)[1:])  
>> ```
>> n=10: (1.3038404810405297, 0.29999999999999999)  
>> n=100: (1.3638181696985856, -0.059999999999999998)  
>> n=1000: (1.451895313030523, -0.0060000000000000001)   
>> n=10000: (1.4193308282426618, 0.0011000000000000001)  
>> n=100000: (1.4136795959481059, 0.0020699999999999998)  
>> n=1000000: (1.4143383612134686, 0.00026699999999999998)  
>> n=10000000: (1.4138155466679521, -0.00056999999999999998)  
>>
>> The mean error is small and decreases with n; therefore, this estimator appears to be unbiased.
>>
>> Plot Goals Distribution
>> ```python
>> estimates, rmse, me = SimulateManyGames() 
>> pmf = thinkstats2.Pmf(estimates)
>> thinkplot.Hist(pmf)
>> thinkplot.Config(xlabel='Goals Scored', ylabel='PMF')
>> ```
>>
>> INSERT IMAGE HERE
>>
>> Calculate Standard Error
>> ```python
>> print('RMSE:', RMSE(estimates, lam))
>> print('Mean Error:', MeanError(estimates, lam))
>> ```
>> RMSE: 1.41337999137  
>> Mean Error: 0.000381
