[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

In games like hockey and soccer, the time between goals is roughly exponential. So you could estimate a team’s goal-scoring rate by observing the number of goals they score in a game. This estimation process is a little different from sampling the time between goals, so let’s see how it works.

Write a function that takes a goal-scoring rate, lam, in goals per game, and simulates a game by generating the time between goals until the total time exceeds 1 game, then returns the number of goals scored.

Write another function that simulates many games, stores the estimates of lam, then computes their mean error and RMSE.

Is this way of making an estimate biased? Plot the sampling distribution of the estimates and the 90% confidence interval. What is the standard error? What happens to sampling error for increasing values of lam?

>> Single Game Simulation
>> 
>> ```python
>> def single_game_sim(lam, game_len=90):
>>     '''Simulates a game by taking a goal-scoring rate and generating the time between goals 
>>        until the total time exceeds one game, then returns the number of goals scored.'''
>> 
>>     # DO SOMETHING
>> 
>>     return goals_scored
>> ```
>>
>> Many Game Simulation:
>>
>> ```python
>> def multi_game_sim(num_games, lam, game_len=90):
>>     '''Simulates many games, stores the estimates of lam, then computes mean error and RMSE.'''
>>
>>     goals_per_game = []
>>     for n in range(num_games):
>>         # simulate single game
>>         goals_per_game.append(single_game_sim(lam))
>>
>>    # compute mean error
>>    mean_error = 
>>    # compute RMSE
>>    rmse =
>>
>> ```
>>
>> Distribution of Estimates:
>> ```python
>>
>> ```
>>
>> Standard Error:
>> ```python
>>
>> ```
>>
>> As lam increases, sampling error XXX.
