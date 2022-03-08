# xpath
基于上一篇[beautifulsoup](https://github.com/Kent-Griffith/Crawler_BeautifulSoup)模块，这一次学习用xpath模块写爬虫程序

**不同之处在于：**

>**使用User-Agent请求头随机更改和随机Referer自动更新避免相同User-Agent重复访问多次**

>**使用自动翻页，使得程序更加灵活**

>**以及更加使用的名字保存语法:grinning:	 :grinning:	:grinning:	:grinning:**

![image](https://user-images.githubusercontent.com/97998239/156747550-8f3bad92-362a-46de-bdea-af8d43c8314a.png)

`img_url = list('http:'+item for item in img_src)` 

遍历列表img_src，在每个成员前面加上http:并重新赋值给img_url

`for nurl,ntitle in zip(img_url,title):
save_img(nurl,ntitle,url)`

同时遍历两个列表

自动翻页函数，通过找到下一页的链接，从而让程序自己跳转下一页

![image](https://user-images.githubusercontent.com/97998239/156748219-4d348614-a91a-4c7f-86af-24712f4a4f25.png)


当程序报错时，由被try和except包裹的主程序代码便跳出循环，结束程序：


![image](https://user-images.githubusercontent.com/97998239/156748605-2876d8b1-4463-408c-9488-2a0dec4b0902.png)


