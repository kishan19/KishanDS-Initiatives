# THIS REPO IS A WORK IN PROGRESS. 

## Use cases related to Cricket

- Who has spent the most time at the top of the international cricket rankings

This is possible thanks to datewise rankings released by the ICC http://www.relianceiccrankings.com/datespecific/test/?stattype=batting&day=18&month=02&year=2019 on their datespecific website. 

The first step is to compile all the URLs for the particular year. Then, process the URLs one by one, to find out which player has spent the most number of days in the time between the two spots.

Then a function is used to preprocess a few data inside pandas. This is processed as a dataframe which can be used for query purposes or integrated as part of a chatbot.

#### DRS Analysis

- ODI, Test, T20I success indices
- Umpire metrics
- Neat frontend for application
- Automated data pipelines for extraction of Match notes data
- Dashboard with key metrics of referrals

Dashboard for automated ODI, TEST and T20 analysis


Data:
- Capture keeper (done)
- Capture captain of team (done)


Edge cases

- Retired out affecting active partnership (done)
- Extras of same ball in over commentary (done)
- Ordering innings list (done)
- Capturing change of keeper during particular event  (manual override based on aware events)
- If there are 3 innings, then reverse keeper order and captain order- in terms of count (manual override now for <=3 innings in test)


### Commentary references

1. https://github.com/nishant-mor/Commentary-Parser/blob/master/comment.py
2. https://www.espncricinfo.com/story/_/id/21898685/m
3. https://stackoverflow.com/questions/5314241/difference-between-consecutive-elements-in-list


#### Some useful references:

https://elitedatascience.com/python-web-scraping-libraries 





