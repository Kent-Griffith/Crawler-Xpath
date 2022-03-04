import requests
from lxml import etree
import random
import os


def pachong(url):
    version_id = random.randint(10, 100)
    os_id = ['Windows NT 10.0', 'Windows NT 6.1', 'linux 10.0']
    headers = {
        "User-Agent": "Mozilla/5.0 (" + random.choice(os_id) + " 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758." + str(version_id) + " Safari/537.36",
        "Referer": "http://www.4399dmw.com/donghua/"
    }
    # 使用了一个代理去爬取
    proxies = {"HTTP": "http://121.13.252.58:41564"}
    url = url
    # 发送网页请求，返回值用resp存储
    resp = requests.get(url=url, headers=headers, proxies=proxies)
    # 解码后就是网页源代码
    html_doc = resp.content.decode("utf-8")
    #用etree转化html_doc，转换为一个html的对象，此时etree的对象可以用xpath语法
    html = etree.HTML(html_doc)
    title=html.xpath("//p[@class='u-tt']/text()")
    pic=html.xpath('//div[@class="lst"]/a[@class="u-card"]/img/@data-src')
    # 将每个链接前面加上http:
    pic = list('http:' + item for item in pic)
    #print(title)
    page = html.xpath('//span[@class="cur"]/text()')
    print("0")
    mk_dir("第" + page[0] + "页")
    print("1")
    #print(pic)
    for opic,otitle in zip(pic,title):
        save_img(opic,otitle)
    pass

def mk_dir(path):
    # os.path.exists(name)判断是否存在路径
    # os.path.join(path, name)连接目录与文件名
    isExist = os.path.exists(os.path.join('E:\pachong2', path))
    if not isExist:
        print("mkdir" + path)
        # 在E:\pachong中创建文件夹
        os.mkdir(os.path.join('E:\pachong2', path))
        # 将路径转移到新建文件夹中，这样保存的图片就在这里
        os.chdir(os.path.join('E:\pachong2', path))
        return True
    else:
        print(path + " already exists")
        os.chdir(os.path.join('E:\pachong2', path))
        return False

def save_img(img_src,img_name):
    version_id = random.randint(10, 100)
    os_id = ['Windows NT 10.0', 'Windows NT 6.1', 'linux 10.0']
    headers = {
        "User-Agent": "Mozilla/5.0 (" + random.choice(os_id) + " 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758." + str(version_id) + " Safari/537.36",
        "Referer": "http://www.4399dmw.com/donghua/"
    }
    # 使用了一个代理去爬取
    proxies = {"HTTP": "http://121.13.252.58:41564"}
    try:
        #发送网页请求，得到都是图片的url地址
        img = requests.get(img_src,headers=headers,proxies=proxies)
        #给图片命名
        imgname = img_name+".jpg"
        #用追加的方式将图片以二进制写入
        with open(imgname,'ab') as f:
            f.write(img.content)
            print(imgname)
    except Exception as e:
           print(e)


#自动翻页
def find_next_page(url):
    version_id = random.randint(10, 100)
    os_id = ['Windows NT 10.0', 'Windows NT 6.1', 'linux 10.0']
    headers = {
        "User-Agent": "Mozilla/5.0 (" + random.choice(os_id) + " 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758." + str(version_id) + " Safari/537.36",
        "Referer": "http://www.4399dmw.com/donghua/"
    }
    # 使用了一个代理去爬取
    proxies = {"HTTP": "http://121.13.252.58:41564"}
    print("正在寻找下一页")
    # 发送网页请求，返回值用resp存储
    resp = requests.get(url=url, headers=headers, proxies=proxies)
    # 解码后就是网页源代码
    html_doc = resp.content.decode("utf-8")
    html = etree.HTML(html_doc)
    print(html)
    #找到下一页的地址
    next_page=html.xpath('//a[contains(text(),"下一页")]/@href')
    #etree导下来的东西都是list类型的
   # print(next_page)
    really_next_page = "http://www.4399dmw.com" + next_page[0]
    #print(really_next_page)
    return really_next_page


def main():
  url="https://www.4399dmw.com/search/dh-1-0-0-0-0-1-0/"

  while True:
      try:
          print("给爷爬"+url)
          pachong(url)
          url= find_next_page(url)
      except:
         break
  print("爬完了")
  pass

if __name__ == '__main__':
    main()
