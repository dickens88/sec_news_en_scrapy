# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import nltk
import numpy as np
import pymysql
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer


def db_handle():
    conn = pymysql.connect(
        host="80.158.2.192",
        user="root",
        passwd="Charlesliu@2017abc",
        charset="utf8",
        db='secnews',
        port=3306)
    return conn


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = []
    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    return stems


def save_key_word(item):
    tfidf = TfidfVectorizer(token_pattern="(?u)\\b[\\w-]+\\b", stop_words='english')
    tfidf.fit_transform([item['title'][0]])
    indices = np.argsort(tfidf.idf_)[::-1]
    features = tfidf.get_feature_names()
    top_n = 20
    words = [features[i] for i in indices[:top_n]]
    word_map = dict(zip(words, indices[:top_n]))
    # print(item['content'])
    # print(top_features)

    conn = db_handle()
    cursor = conn.cursor()
    sql = "insert ignore into t_security_en_news_words(title, `key`, val) values (%s,%s,%s)"
    try:
        for k in word_map:
            if len(k) <= 2:
                continue
            cursor.execute(sql, (item['title'][0], k, int(word_map[k])*3))
        cursor.connection.commit()
    except BaseException as e:
        print("存储错误", e, "<<<<<<原因在这里")
        conn.rollback()


def save_article(item):
    conn = db_handle()
    cursor = conn.cursor()
    sql = "insert ignore into t_security_en_news_article(title, content, uri, src) values (%s,%s,%s,%s)"
    try:
        cursor.execute(sql, (item['title'][0], item['content'], item['uri'], item['src']))
        cursor.connection.commit()
    except BaseException as e:
        print("存储错误", e, "<<<<<<原因在这里")
        conn.rollback()


class TutorialPipeline(object):
    def process_item(self, item, spider):
        save_key_word(item)
        save_article(item)
        return item
