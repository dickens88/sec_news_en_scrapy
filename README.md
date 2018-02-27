# sec_news_en_scrapy

# Introduction
This Python Spider is base on Scrapy framework. It's main founction is use spider to crawl several high-quality cyber security news web site and save all the information into database(MySQL).After that, we can use some sample ML algorithm package to analyze these data and find out the useful key words from all these articles. 

# Process
- Use Scrapy to go to the Security News website to crawl the title and content of the article
- Separate the content of the article into individual words
- Use TF-IDF algorithm to extract keywords
- Save the keywords to the database

# How to
##  Install Scrapy
Install scrapy is really sample, you can visit [Scrapy Guide](https://doc.scrapy.org/en/latest/intro/install.html) to get some details. But before you do this, make sure you have already installed Python3 on your computer. 

## Dependent packages

## Database

## Run Spider
