# Python网络爬虫学习

**龙云尧个人博客，转载请注明出处**

_初步了解网络爬虫的工具使用和代码编写_

学习地址见[`网易云课堂《Python网络实战》`](http://study.163.com/course/courseMain.htm?courseId=1003285002)

## 前言

**工具**

1.Python编辑工具

实验中使用到的Python工具为[`Anaconda`](https://www.continuum.io/downloads/)，工具的安装参照[`Anaconda使用总结`](http://python.jobbole.com/86236/)（Linux下）以及[`Python科学计算的瑞士军刀——Anaconda 安装与配置`](http://blog.csdn.net/u012675539/article/details/46974217)（windows下）相关教程。

在视频教学过程中，讲师也会有一点安装指导。

初学过程中推荐使用`Jupyter notebook`工具在浏览器中编辑，这样可以每次只执行几行函数，而不用一次从头到尾执行完毕。调试完成以后，可以在`Spyder`中一次运行。

`Jupyter notebook`工具中，ctrl+enter表示执行当前cell的代码，alt+enter表示新建一个cell，其他的在本次实验中用不到。

2.辅助工具

使用`Chrome`辅助元素选择。需要对Chrome的`开发者模式`有较多的使用经验。

不过在视频中，讲师会反复示范怎么使用Chrome的开发者模式，所以使用起来不必太担心。

**知识储备**

1.语法

基本的Python语法知识可以参照[Python 基础语法](http://www.runoob.com/python/python-basic-syntax.html)（**推荐**）和[Python基本语法，python入门到精通[二]](http://www.cnblogs.com/toutou/p/4774284.html)（页面很low）

**注：[runoob.com](http://www.runoob.com/python)是一个好网站**

在语法和知识结构上，Python的概念和C++/Java这类面向对象型语言很相似，比如类似的对象概念.

比如类似于数组的列表(List)，类似于map的字典(dictdict)。其他部分自行体会.

因为本次教学课程中，实验较为简单，所以我其实也只是对Python有一个基本的了解。

2.工具使用

BeautifulSoap的使用教程参见[`Python爬虫利器二之Beautiful Soup的用法`](http://cuiqingcai.com/1319.html)

在本次实验中，网络爬虫需要对爬取的网页进行解析，故而不可避免的需要使用到html的相关知识。不过难度不大，一边实验一边回忆都已经足够了。

在实验中使用了BeautifulSoup工具能够很方便的将抓取的网页解析成一个文档树。然后我们就可以对这个文档树进行select，选择出特定的标签，进而分析出我们想要的信息。

举个例子：

```python
import requests # 导入工具包
artibody_url = 'http://news.sina.com.cn/o/2017-04-18/doc-ifyeimzx6745829.shtml'
artibody_res = requests.get(artibody_url) # 模仿浏览器，使用get方法获取url指向的网页资源
artibody_res.encoding = 'utf-8' # 设置编码，否则抓取的文档会出现乱码


from bs4 import BeautifulSoup # 从bs4中导入BeautifulSoap包
artibody_soup = BeautifulSoup(artibody_res.text, 'html.parser') # 将抓取的网页扔进BeautifulSoap生成一个文档树
artibody_div = artibody_soup.select('#artibody p')[1:-2] # 使用select方法获取想要的内容
# select中内容的使用和css的选择器类似，id使用'#xxx'， 类使用'.xxx'，普通标签使用'p'，另外还可以有子代选择器'body div #artibody p'
```

3.**本篇博客系个人学习所总结的知识，如果有什么概念或者其他错误，欢迎喷。但是不小心对你们造成误导，那就概不负责了2333**

##正题

### 课程知识总结

将这个部分写在最前面，是为了在课程开始之前就对整个课程的目的，以及coding过程中，每一步的目的有所了解。避免盲目跟着打代码，而不知道整个项目目的。

本课程实现了从网易新闻网页中抓取新闻信息，封装成结构化数据的过程。

课程一共18讲，每一讲2-10分钟不等，一般为5分钟。
* 第1-3讲，为课程入门，大致介绍课程目的，对Python编写网络爬虫进行初步介绍。
* 第4讲，实现模拟浏览器，使用get方法获取网页信息的方法。
* 第5-6讲，介绍BeautifulSoap，介绍基本使用方法
* 第7-16讲，利用BeautifulSoap构造的文档树剖析整个网页，并且通过网页一步一步获取"title"(标题), "newssource"(原标题), "date"(发稿时间), "article"(新闻主题), "article"(编辑), "comments"(评论数)。
* 第17讲，函数封装指导
* 第18讲，将前17章中所实现的功能封装成一个函数，最终实现输入一个网页，返回一个封装好的结构化数据。

### 代码解释

**1.requests获取网页信息**

```python
# 导入requests包
import requests 
artibody_url = 'http://news.sina.com.cn/o/2017-04-18/doc-ifyeimzx6745829.shtml'
# 模仿浏览器发送一个get请求，获取链接指向的网页，将获取的数据存进artibody_res
artibody_res = requests.get(artibody_url)
# 设置编码，以免乱码
artibody_res.encoding = 'utf-8'
# 打印text
print(artibody_res.text)
```

**2.利用BeautifulSoap将网页装进文档树**

```python
# 从bs4中导入BeautifulSoup数据
from bs4 import BeautifulSoup
# 选择解析器为Python标准库(html.parser)，如果不设置就会有warnning
artibody_soup = BeautifulSoup(artibody_res.text, 'html.parser')
# 调用BeautifulSoap中的select方法进行，[1:-2]表示选择从第1个元素到倒数第二个元素（Python从0开始计数）
artibody_div = artibody_soup.select('#artibody p')[1:-2]
print(artibody_div)
```

**3.获取文本信息**

strip函数的使用可以参考[python strip()函数 介绍](http://www.jb51.net/article/37287.htm)

```python
# 构建一个List，用于存放文本
article = []
# for循环，记得for语句最后有一个':'（注，Python没有括号，而是以缩进代替）
for p in artibody_div:
    # 调用append方法，将text一个一个加入list，调用strip()是为了去掉空白字符
    article.append(p.text.strip())
print(article)
```

**4.文本合并**

```python
# 调用join方法，两article中的元素全部合并，原本List中不同的元素之间使用' '隔开，换成'\n'也可
#只不过Juphter Notebook会直接将'\n'显示出来而已
' '.join(article)
```

**5.一行实现文本合并**

```python
# 不用解释了吧
' '.join([p.text.strip() for p in artibody_soup.select('#artibody p')[1:-2]])
```

**6.编辑提取**

```python
# 调用lstrip左切除
artibody_editor = artibody_soup.select('.article-editor')[0].text.lstrip('责任编辑：')
print(artibody_editor)
```

**7.title获取**

```python
artibody_title = artibody_soup.select('title')[0].text
print(artibody_title)
```

**8.引用获取**

contents的使用请继续参照开头提到的文章[`Python爬虫利器二之Beautiful Soup的用法`](http://cuiqingcai.com/1319.html)

```python
# 在较为复杂的层级结构中，调用contents获得其子节点
artibody_p = artibody_div.select('p')[0].contents[0].strip()
print(artibody_p)
```

**9.日期获取**

关于datetime的使用，参见[python 常用 time, datetime处理](http://www.cnblogs.com/snow-backup/p/5063665.html)。

（其实只要只要strptime和strftime的用法，在本次实验就足够了。）

```python
artibody_time = artibody_soup.select('.time-source')[0].contents[0].strip()
from datetime import datetime
# 使用datetime进行日期获取，strptime表示将str转换成时间
dt = datetime.strptime(artibody_time, '%Y年%m月%d日%H:%M')
# strftime表示将时间转换成文字
print(dt.strftime('%Y-%m-%d %H:%M'))
```

**10.来源获取**

```python
# 不解释
artibody_from = artibody_soup.select('.time-source span a')[0].text
print(artibody_from)
```

**11.评论数获取**

在课程中，最难抓的也就是这货了。因为使用的是js从后台获取数据，所以不能直接从静态网页抓取。

下面代码就展示了，明明使用了正确的定位，但是抓取不到数值的情况。

```
artibody_commentCount = artibody_soup.select('.page-tool-i')
print(artibody_commentCount)
```

结果如下：

```
[<span class="page-tool-i page-tool-s" title="分享">
<a href="javascript:;" id="shareArticleButton" onclick="_S_uaTrack('index_news_content', 'other_click');">分享</a>
</span>, <span class="page-tool-i page-tool-c page-tool-share" title="评论">
<span id="commentCount1"></span>
<a href="javascript:;" suda-uatrack="key=index_news_content&amp;value=comment_click"></a>
</span>, <span class="page-tool-i page-tool-s" title="分享">
<a href="javascript:;" id="shareArticleButton2" onclick="_S_uaTrack('index_news_content', 'other_roll_click');">分享</a>
</span>, <span class="page-tool-i page-tool-c page-tool-share" id="pageToolShare" title="评论">
<a href="javascript:;" suda-uatrack="key=index_news_content&amp;value=comment_roll_click"></a>
<span id="commentCount1M"></span>
</span>]
```

只有span标签，而没有任何a标签。

所以我们只能从仿照js抓取数据了。不要问我那个老师是怎么知道是哪个js文件的= =，我也觉得很神奇。

抓取过程中可以用一点小技巧。

在网页加载过程中盯着评论数。

![未加载出来](https://cloud.githubusercontent.com/assets/18045191/25130907/7cd4cf38-2476-11e7-82fe-2faad44f5885.PNG)

在评论加载出来之后，立即停止Chrome中开发者模式下控制台的监控。这样从后向前找会轻松一点（虽然还是需要寻找很久）。

![加载出来](https://cloud.githubusercontent.com/assets/18045191/25130906/7cc85c44-2476-11e7-8132-f0b72b7a09e4.PNG)

寻找的过程中好好利用控制台的preview功能。

![preview功能](https://cloud.githubusercontent.com/assets/18045191/25130889/6f905068-2476-11e7-80d6-39ef6e4b2e4b.png)

抓取过程中，代码如下。

```python
comment_url = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fyeimzx6745829&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
comment_res = requests.get(comment_url)
comment_res.encoding = 'utf-8'
print(comment_res.text)
```

然后你就能够抓到如下结果

```
var data={"result": {"status": {"msg": "", "code": 0}, "count": {"qreply": 10065, "total": 10756, "show": 200}, "replydict": ...中间省去真·1w字..., "agree": "251", "channel": "gn", "uid": "5121097321"}]}}
```

将js返回的这一段数据，使用json存放起来。

json的基本操作参见[python解析json](http://www.cnblogs.com/kaituorensheng/p/3877382.html)

```python
import json
jd = json.loads(comment_res.text.strip('var data='))
# 获取jd下'result'标签中‘count'标签中’total‘内容
jd['result']['count']['total']
```

到这里评论数的获取就结束了，有点麻烦们也有点蛋疼。

**12.获取newsid**

这一步获取newsid能够让我们在后面实现批量导入。

关于正则表示式的使用，参见[Python正则表达式](http://www.runoob.com/python/python-reg-expressions.html)。

```python
# 有两种实现方法，第一种，先split，然后去头去尾提取出来就是了
#artibody_url.split('/')[-1].rstrip('.shtml')
# newsid=comos-fyeimzx6745829
#news_id = artibody_url.split('/')[-1].lstrip('doc-i').rstrip('.shtml')
#另一种是使用正则表达式
# group(1)表示匹配的字符串， group(0)会将整个字符串返回回来
import re
news_id = re.search('doc-i(.*).shtml', artibody_url).group(1)
```

**13.使用newsid**

```python
# 将newsis填入form_comment_url的括号内
form_comment_url = 'http://comment5.news.sina.com.cn/page/info?version=1&\
format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
form_comment_url.format(news_id)
```

**14.封装函数**

封装函数之后，我们就能够实现，传入一个新闻的网址，就获取这个新闻的评论数的功能了。

```python
import re
artibody_url = 'http://news.sina.com.cn/o/2017-04-18/doc-ifyeimzx6745829.shtml'
def getCommentCounts(news_url):
    news_id = re.search('doc-i(.*).shtml', news_url).group(1)
    comments = requests.get(form_comment_url.format(news_id))
    jd = json.loads(comments.text.lstrip('var data='))
    return jd['result']['count']['total']
```

**15.整体封装**

前面步骤全部走了一遍之后，我们就可以将它们封装起来，称为一个函数了。

通过这一步，我们可以就可以把`news.sina.com.cn/china`中所有的href获取下来，然后逐一传入这个函数，就能够得到每一条新闻的结构化数据了。剩下的任务就是看我们怎么使用咯。

```python
import requests
from bs4 import BeautifulSoup
import re
import json
from datetime import datetime
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
```

整个`Python网络爬虫实战`课程到这里也就结束了。`丘祐玮`讲师讲课比较细致，整个课程浅显易懂，对于有JS基础或者java基础或者C++基础或者Matlab基础的人来说，应该不难。