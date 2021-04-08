# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 09:16:49 2021

@author: jomen
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

def get_jobs(keywords, locations, path):
    
    """Intialization the set up and parameters"""
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    url = "https://www.linkedin.com/jobs/search?position=1&pageNum=0"
    driver.get(url)
    driver.maximize_window()
    
    jobs = []
    
    keyword = driver.find_element_by_name("keywords")
    keyword.send_keys(keywords)
    
    location = driver.find_element_by_name("location")
    location.clear()
    location.send_keys(locations)
    location.send_keys(Keys.RETURN)
    
    
    """Find the maximum number of jobs found from the search"""
    
    total_results = driver.find_element_by_class_name("results-context-header__job-count")
    total_results_int = int(total_results.text)
    print("Total jobs found for this search: ", total_results_int)
    time.sleep(2)
    
    
    """Scroll down the page until the last page. The reason I put n=0 is beacuse start looping for scrolling down until
    meet the button to see more jobs."""
    
    n = 0
    for i in range(n, 7):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        print('Button is not ready, continue scrolling...')
    
    time.sleep(2)
    print('Button is ready, click it, and continue scrolling...')
    driver.find_element_by_xpath('//*[@id="main-content"]/div/section[2]/button').click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    
    scrolling_successfully = False
    while not scrolling_successfully:
        try:
            driver.find_element_by_class_name('infinite-scroller__show-more-button.infinite-scroller__show-more-button--visible')#('See more jobs')#('//*[@id="main-content"]/div/section[2]/button')
            
            try:
                print('Button again, click & continue scrolling...')
                driver.find_element_by_class_name('infinite-scroller__show-more-button.infinite-scroller__show-more-button--visible').click()
                if driver.find_element_by_xpath('//*[@id="main-content"]/div/section[2]/div[3]').isDisplayed():
                    print("SCROLLING DONE")
                    break
            except:
                pass
            
            time.sleep(2)
        
        except NoSuchElementException:
            try:
                driver.find_element_by_xpath('//*[@id="main-content"]/div/section[2]/div[3]')
                print('\nSCROLLING DONE')
                scrolling_successfully = True
            except:
                pass
     
    print("You've viewed all jobs for this search")
    print("Back to top page")
    driver.execute_script("window.scroll(0, 0);")
    print("It's time to extract your data")
    
    
    """Start the scraping"""
    
    while len(jobs) < total_results_int:
        time.sleep(2)
        job_buttons = driver.find_elements_by_class_name('result-card__full-card-link')
        
        for job_button in job_buttons:
            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(total_results_int)))
            if len(jobs) >= total_results_int:
                print("SCRAPING DATA IS DONE")
                driver.close()
                break
            
            hover = ActionChains(driver).move_to_element(job_button)
            hover.perform()
            try:
                job_button.click()   
            except ElementClickInterceptedException:
                time.sleep(2)
                job_button = driver.find_element_by_class_name('result-card__full-card-link')
                job_button.click() 
                
            time.sleep(1)
            collected_successfully = False
            
            while not collected_successfully:
                try:
                    job_title = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/section/div[2]/section[1]/div[1]/div[1]/a/h2'))
                        )
                    company = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/section/div[2]/section[1]/div[1]/div[1]/h3[1]/span[1]'))
                        )
                    job_posting_time = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/section/div[2]/section[1]/div[1]/div[1]/h3[2]/span'))
                        )
                    
                    try:
                        no_of_applicants = driver.find_element_by_xpath('//*[@id="main-content"]/section/div[2]/section[1]/div[1]/div[1]/h3[2]/span[2]').text
                    except NoSuchElementException:
                        #no_of_applicants1 = -1
                        try:
                            no_of_applicants = driver.find_element_by_xpath('//*[@id="main-content"]/section/div[2]/section[1]/div[1]/div[1]/h3[2]/figure/figcaption').text
                        except:
                            no_of_applicants = -1
                    
                    '''try:
                        no_of_applicants2 = driver.find_element_by_xpath('//*[@id="main-content"]/section/div[2]/section[1]/div[1]/div[1]/h3[2]/figure/figcaption').text

                    except:
                        no_of_applicants2 = -1'''
                   
                    
                    try:
                        seniority_level = driver.find_element_by_xpath("//*[@id='main-content']/section/div[2]/section[2]/ul/li[1]/span").text
                    except:
                        seniority_level = -1
                        
                    try:
                        job_function = driver.find_element_by_xpath('//*[@id="main-content"]/section/div[2]/section[2]/ul/li[3]/span').text
                    except:
                        job_function = -1
                    
                    try:
                        company_industry = driver.find_element_by_xpath('//*[@id="main-content"]/section/div[2]/section[2]/ul/li[4]/span').text
                    except:
                        company_industry = -1
                    
                    time.sleep(2)
                        
                    try:
                        show_more_button = driver.find_element_by_xpath('//*[@id="main-content"]/section/div[2]/section[2]/div/section/button[1]')
                        #show_more_button = WebDriverWait(driver, 10).until(
                        #    EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/section/div[2]/section[2]/div/section/button[1]'))
                        #    )
                        try:
                            show_more_button.click()
                        except:
                            pass
                        
                        try:   
                            detail_desc = driver.find_element_by_xpath('//*[@id="main-content"]/section/div[2]/section[2]/div/section/div').text
                        except NoSuchElementException:
                            detail_desc = -1
                    
                    except NoSuchElementException:
                        #detail_desc = -1
                        try:
                            time.sleep(5)
                            sm_button = driver.find_element_by_xpath('//*[@id="main-content"]/section/div[2]/section[3]/div/section/button[1]')
                            #sm_button = WebDriverWait(driver, 10).until(
                            #    EC.presence_of_element_located((By.XPATH,'//*[@id="main-content"]/section/div[2]/section[3]/div/section/button[1]'))
                            #    )
                            try:
                                sm_button.click()
                            except:
                                pass
                            
                            try:
                                detail_desc = driver.find_element_by_xpath('//*[@id="main-content"]/section/div[2]/section[3]/div/section/div').text
                            except NoSuchElementException:
                                detail_desc = -1
                                
                        except NoSuchElementException:
                            detail_desc = driver.find_element_by_xpath('//*[@id="main-content"]/section/div[2]/section[2]/div/section/div').text
                        
                        except ElementClickInterceptedException:
                            detail_desc = -1
                        
                        except StaleElementReferenceException:
                            detail_desc = -1
                    
                    try:
                        employment_type = driver.find_element_by_xpath('//*[@id="main-content"]/section/div[2]/section[2]/ul/li[2]/span').text
                        #WebDriverWait(driver, 10).until(
                        #EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/section/div[2]/section[2]/ul/li[2]/span'))
                        #)
                    except:
                        employment_type = -1
                        
                    collected_successfully = True
                
                except:
                    time.sleep(2)
                    
                try:
                    jobs.append({
                        "Job Title": job_title.text,
                        "Company": company.text,
                        "Posted Date": job_posting_time.text,
                        #"Applicants1": no_of_applicants1,
                        "Number of Applicants": no_of_applicants,
                        "Seniority Level": seniority_level,
                        "Job Function": job_function,
                        "Company Industry": company_industry,
                        "Detail Desc": detail_desc,
                        "Employment Type": employment_type
                        })
                    time.sleep(1)
                except StaleElementReferenceException:
                    continue
    
    return pd.DataFrame(jobs)

