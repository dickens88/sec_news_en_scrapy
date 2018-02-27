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
- nltk
- numpy
- pymysql
- sklearn

## Database
Your need to prepare for a MySQL in advance. You can find the table creation SQL script in project folder named secnewsdb.sql. It contains two table which will be used to save articles and key words.
Remeber, you also need to modify pipelines.py. Add your database connection infomation into this py file, so that spdier will output all the data into this database you specified。

## Run Spider
In the scrapy root folder, eg. sec_news_en_scrapy. You can use scrapy command to list spdier .
```
scrapy list
```
![mark](http://oyy7pve7f.bkt.clouddn.com/blog/180227/b6l2HLhA7k.png)

And then you can shoose one of them to execute.
```
scrapy crawl en_news
```
## Result
You can use MySQL client to check the result.
![mark](http://oyy7pve7f.bkt.clouddn.com/blog/180227/iDDkcAFB4L.png)
