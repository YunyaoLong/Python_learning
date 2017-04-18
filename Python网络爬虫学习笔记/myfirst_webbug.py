
# coding: utf-8

# In[2]:

import requests 
artibody_url = 'http://news.sina.com.cn/o/2017-04-18/doc-ifyeimzx6745829.shtml'
artibody_res = requests.get(artibody_url)
artibody_res.encoding = 'utf-8'
print(artibody_res.text)


# In[34]:

from bs4 import BeautifulSoup
artibody_soup = BeautifulSoup(artibody_res.text, 'html.parser')
artibody_div = artibody_soup.select('#artibody p')[1:-2]
print(artibody_div)


# In[25]:

article = []
for p in artibody_div:
    article.append(p.text.strip())
print(article)


# In[30]:

' '.join(article)


# In[35]:

' '.join([p.text.strip() for p in artibody_soup.select('#artibody p')[1:-2]])


# In[43]:

artibody_editor = artibody_soup.select('.article-editor')[0].text.lstrip('责任编辑：')
print(artibody_editor)


# In[6]:

artibody_title = artibody_soup.select('title')[0].text
print(artibody_title)


# In[8]:

artibody_p = artibody_div.select('p')[0].contents
print(artibody_p)


# In[10]:

artibody_time = artibody_soup.select('.time-source')[0].contents[0].strip()
from datetime import datetime
dt = datetime.strptime(artibody_time, '%Y年%m月%d日%H:%M')
print(dt.strftime('%Y-%m-%d %H:%M'))


# In[12]:

artibody_from = artibody_soup.select('.time-source span a')[0].text
print(artibody_from)


# In[50]:

artibody_commentCount = artibody_soup.select('.page-tool-i')
print(artibody_commentCount)


# In[56]:

comment_url = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fyeimzx6745829&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
comment_res = requests.get(comment_url)
comment_res.encoding = 'utf-8'
print(comment_res.text)


# In[63]:

import json
jd = json.loads(comment_res.text.strip('var data='))
jd['result']['count']['total']


# In[88]:

#artibody_url.split('/')[-1].rstrip('.shtml')
# newsid=comos-fyeimzx6745829
#news_id = artibody_url.split('/')[-1].lstrip('doc-i').rstrip('.shtml')
import re
news_id = re.search('doc-i(.*).shtml', artibody_url).group(1)


# In[90]:

form_comment_url = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
form_comment_url.format(news_id)


# In[5]:

import re
artibody_url = 'http://news.sina.com.cn/o/2017-04-18/doc-ifyeimzx6745829.shtml'
def getCommentCounts(news_url):
    news_id = re.search('doc-i(.*).shtml', news_url).group(1)
    comments = requests.get(form_comment_url.format(news_id))
    jd = json.loads(comments.text.lstrip('var data='))
    return jd['result']['count']['total']


# In[101]:

getCommentCounts(artibody_url)


# In[7]:

import requests
from bs4 import BeautifulSoup
import re
import json
from datetime import datetime
form_comment_url = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
def getNewsDetail(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    result['title'] = soup.select('title')[0].text
    result['newssource'] = soup.select('p')[0].contents[0].strip()
    artibody_time = soup.select('.time-source')[0].contents[0].strip()
    result['dt'] = datetime.strptime(artibody_time, '%Y年%m月%d日%H:%M')
    result['article'] = ' '.join([p.text.strip() for p in soup.select('#artibody p')[1:-2]])
    result['editor'] = soup.select('.article-editor')[0].text.lstrip('责任编辑：')
    result['comments'] = getCommentCounts(newsurl)
    return result


# In[8]:

# artibody_url = 'http://news.sina.com.cn/o/2017-04-18/doc-ifyeimzx6745829.shtml'
getNewsDetail(artibody_url)

