# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 02:01:57 2021

@author: jomen
"""

import LinkedinJobsScraping as scraper
import pandas as pd

keyword = "data engineer"
location = "indonesia"
path = "C:/Users/jomen/Documents/self_project/LinkedIn_Jobs_Scraping/chromedriver.exe"

df = scraper.get_jobs(keyword, location, path)

df.to_csv("linkedin_scraper_full(2).csv", index=False)