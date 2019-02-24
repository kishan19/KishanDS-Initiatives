# THIS REPO IS A WORK IN PROGRESS. 

## Use cases related to Cricket

- Who has spent the most time at the top of the international cricket rankings

This is possible thanks to datewise rankings released by the ICC http://www.relianceiccrankings.com/datespecific/test/?stattype=batting&day=18&month=02&year=2019 on their datespecific website. 

The first step is to compile all the URLs for the particular year. Then, process the URLs one by one, to find out which player has spent the most number of days in the time between the two spots.

Then a function is used to preprocess a few data inside pandas. This is processed as a dataframe which can be used for query purposes or integrated as part of a chatbot.

#### Who uses DRS the most as a batsman? And who has had the highest success rate so far in 2018?

Trying to unearth a few associated questions

- Are captains the most frequent users? 
- Who took the most successful reviews in 2018?

The first step is to scrape through commentary texts, but we need a scalable approach to do this. Scraping a page one by one will have to be configured. 


For the future....

#### ODIs in 2018: Who got the most runs in the first 10 balls they faced? 



#### Tests in 2018: Who got the most wickets in a single session? 


#### Some useful references:

https://elitedatascience.com/python-web-scraping-libraries 





