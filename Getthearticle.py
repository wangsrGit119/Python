# coding=gbk  
import urllib.request
import re

url = "https://xiaoshuo.sogou.com/list/6632040968"
urlpre="https://xiaoshuo.sogou.com"
# decode 解码  encode编码
data = urllib.request.urlopen(url).read().decode('UTF-8', 'ignore')
data.encode('UTF-8')
#获取小说的名字
title=re.findall(r'<title>.*?_(.*?)-.*?</title>', data,re.S)[0]
print(title)
#新建一个文件存放数据
fb=open('%s.txt' % title,'w',encoding='utf-8')
# 得到所有的章节
resulttext = re.findall(r'<ul class="chapter clear" pbflag="章节列表">(.*?)</ul>', data, re.S)[0]
# 得到每个章节的url和title
chapter_info_list = re.findall(r'href=\"(.*?)\" target=\"_blank\"><span>(.*?)<', resulttext, re.S)
for chapter_info in chapter_info_list:
 chapter_uri,chapter_title=chapter_info
 chapter_url=urlpre+chapter_uri
 
 #下载章节内容
 chapter_html=urllib.request.urlopen(chapter_url).read().decode('UTF-8', 'ignore')
 
 chapter_text=re.findall(r'<div id="contentWp" style="display:none">(.*?)</div>', chapter_html, re.S)[0]
 
 chapter_text=chapter_text.replace(' ','')
 chapter_text=chapter_text.replace('\r\n','')
 chapter_text=chapter_text.replace('&rdquo;','')
 chapter_text=chapter_text.replace('</p>','')
 chapter_text=chapter_text.replace('<p>','')
 chapter_text=chapter_text.replace('&hellip;','')
 chapter_text=chapter_text.replace('&ldquo;','')
 
 
 #写入数据
 fb.write(chapter_title)
 fb.write(chapter_text)
 fb.write('\n')
 fb.write('\r\n')
 print(chapter_title,chapter_text)


