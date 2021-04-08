# LinkedIn Jobs Scraping with Selenium Python

## Overview
* Create script to scrape the data about Jobs posted from [LinkedIn](https://www.linkedin.com/) automatically
* The automation build with 'Selenium' and 'Python'
* Do a simple Exploratory Data Analysis

## What I used
* **Python Version: 3.8** to create the script
* **Packages:** pandas, numpy, selenium
* **Jupyter Notebook** for the EDA

## Web Scraping
Scrape the information jobs posted from [LinkedIn](https://www.linkedin.com/) **WITHOUT LOGIN**. The number of jobs posting according to the the maximum results of jobs obtained by the keyword. So it allows you to scrape the all the number of jobs posting. Each of jobs will contain the following information:
* Company Name
* Job Posting Time (23 hours ago, 1 minute ago, etc)
* Number of applicants
* Seniority level (Entry level/Associate/Mid-senior level)
* Company industry
* Detail description (job desc, job req, benefit,etc)
* Employment type
* Job Function

## Data Cleaning
After scraping the data, I do simple EDA to cleaned it up to see early insights from the data itself
* Manipulated the `Job Posting Time` and `Number of Applicants` into possible format we can use for next purposes, like ploting or even modeling)
* Create new column that provided the information about when the jobs were posted (in a few days ago)

## My Early Insights
1. Surprisingly, with `data engineer` as the keyowrd and `indonesia` as the location for my search job, the result shows that the most frequently job title is `software engineering`. It happened due the search engine just searching with all possibilities from the keyword
2. For this search, the **Entry Level** position is on the high demand. Can be said that for this job title, it gives biggest chance to **fresher** to join the company<br>
![alt text](https://github.com/Jomen034/LinkedIn_Jobs_Scraping/blob/master/fig/Seniority%20Level.png "Seniority Level")
3. The recruiter is still actively hiring for this position. Most of jobs posted in recently time **(under 30 days ago)**<br>
![alt text](https://github.com/Jomen034/LinkedIn_Jobs_Scraping/blob/master/fig/The%20Time%20When%20The%20Jobs%20Posted.png "The Time When The Jobs Posted")
5. With the high demand, company also offered the candidates with the **Full-Time** position.<br>
![alt text](https://github.com/Jomen034/LinkedIn_Jobs_Scraping/blob/master/fig/Employment%20Type.png "Employment Type")

# About How to Run This Script
1. Make sure your set up is ready:
    * python has been installed on your PC
    * make sure you've installed the **selenium** along with your python. I used `pip install selenium` to install it 
    * chromedriver file is in the right path (you can download it [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
    * download the `config` and `LinkedInJobsScraping` file correctly
    * set the `config` file as your need to scrape jobs information
2. Open the `config` and `LinkedInJobsScraping` file in your python editor
3. Make sure the `config` file has been set up well
4. Run the `config` file

