# EC601_Project2
_Please note that project 3 unittest is located at https://github.com/giannaiafrate/EC601_Project3_

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

Guidance to the files in the folder:
1. EC601_Project2_Iafrate.pptx: Powerpoint documentation of project goals, description, method, results, and conclusion
2. MLB_SentimentResults.xlsx: The Excel sheet with the results and comparison is listed in 
3. mlb_search.py: Python file for pulling tweets
4. mlb_predict.py: Python file for performing Google sentiment analysis
5. Project2_Phase2a.docx: User stories
6. MLB_SentimentResults/: Folder containing all sentiment results for each team
7. MLB_Tweets/: Folder containing all tweets per team
8. TutorialFolder/: All python files used when running tutorials and understanding the tools
