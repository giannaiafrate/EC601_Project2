# EC601_Project2
Project 2 is on analyzing twitter feeds

The first phase is testing out the twitter API and understanding how to pull various data.
The second phase is testing out the Google NLP API. 

My original user story was pulling tweets from a certain time frame on the TV show, Big Brother, which had its finale last week.
I wanted to see if, based on what people tweeted, I could accurately figure out who America's Favorite Houseguest is and compare it to the actual results.
However, the standard track does not allow for archive tweets and start/end dates.

My final user story is gathering MLB data and performing a sentiment analysis on data pulled for each team to see which teams have the best feedback, and if it lines up to the current MLB rankings (i.e., the teams playing the best have the happiest fan base). 

To perform this, I used Twitter API and pulled 2 sets of data 2 times for each team:
1. Data with the team name in a tweet
2. Data with the MLB 2021 team Hashtag

I performed this twice at two different periods of time to get a large group of data.

I then performed a sentiment analysis on each tweet and stored the results in a csv file. The analysis is averaged across each team and the teams are sorted from best sentiment score to worst. 
