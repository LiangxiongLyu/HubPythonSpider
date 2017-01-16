import urllib
import urllib2
import cookielib
import re


##Used for RSA encrypt password and username, this part I've ignored in this script, I just used the Chrome to find out the final code Form posts,
##which is easy to achieve. Later I will write a Tool class for RSA en/decrypt, which is a some kind of big work, and modify this script to its best.
def RSAencrypt(str):
    pass
    return str

class HUB:
    def __init__(self,username,password):
        self.__username=username
        self.__password=password
        self.cookies = cookielib.CookieJar()
        self.handler=urllib2.HTTPCookieProcessor(self.cookies)
        self.opener = urllib2.build_opener(self.handler)
        self.url1='https://pass.hust.edu.cn/cas/login?service=http%3A%2F%2Fhubs.hust.edu.cn%2Fhustpass.action'
        self.url2='https://pass.hust.edu.cn/cas/login?service=http%3A%2F%2Fhubs.hust.edu.cn%2Fhustpass.action'
        self.url3='http://hub.hust.edu.cn/hustpass.action'
        self.url4='http://hubs.hust.edu.cn/hublogin.action'
        self.postData1=urllib.urlencode({})
        self.postData2=urllib.urlencode({
            'username':RSAencrypt(username),
            'password':RSAencrypt(password),
            'code':'code',
            'lt':'LT-NeusoftAlwaysValidTicket',
            'execution':'e1s1',
            '_eventId':'submit' 
            })
        self.postData3=urllib.urlencode({})
        self.postData4=urllib.urlencode({})
        self.headers1={
            }
        self.headers2={
            }
        self.headers3={}
        self.headers4={
            'Host': 'hubs.hust.edu.cn',
            'Connection': 'keep-alive',
            'Content-Length': '258',
            'Cache-Control': 'max-age=0',
            'Origin': 'http://hub.hust.edu.cn',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Content-Type':'application/x-www-form-urlencoded',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer':'http://hub.hust.edu.cn/hustpass.action',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8'
        }

    def linkIn(self,url,data='',headers={}):
        #for cookie in self.cookies:
        #    print cookie.name,cookie.value
        request=urllib2.Request(url,data,headers)
        responce=self.opener.open(request)
        return responce
    def getContent(self,url,data='',headers={}):
        responce=self.linkIn(url,data,headers)
        content=responce.read().decode('utf-8')
        return content
    def getInfo(self,content):
        pattern=re.compile('<input.*?name="(.*?)".*?value="(.*?)"')
        result=pattern.findall(content)
        Dict={}
        for item in result:
            Dict[item[0]]=item[1]
        return Dict
    def start(self):
        
        self.linkIn(self.url1,self.postData1,self.headers1)
        #self.getContent(self.url1,self.postData1,self.headers1)
        #self.linkIn(self.url2,self.postData2,self.headers2)
        print self.getContent(self.url2,self.postData2,self.headers2)

        #content3=self.getContent(self.url3,self.postData3,self.headers3)
        #self.postData4=urllib.urlencode(self.getInfo(content3))
        #self.linkIn(self.url4,self.postData4,self.headers4)
        #self.getContent(self.url4,self.postData4,self.headers4)



try:
    hub=HUB('XXXXXXX',
            'XXXXXXXXXXXXXX')
    hub.start()
    w=raw_input('Press any key to end......')

except urllib2.URLError,e:
    if hasattr(e,'code'):
        print e.code
    if hasattr(e,'reason'):
        print e.reason
