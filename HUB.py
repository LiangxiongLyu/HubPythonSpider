import urllib
import urllib2
import cookielib
import re


class HUB:
    def __init__(self):
        self.cookies = cookielib.CookieJar()
        self.handler=urllib2.HTTPCookieProcessor(self.cookies)
        self.opener = urllib2.build_opener(self.handler)
        self.url1='https://pass.hust.edu.cn/cas/login?service=http%3A%2F%2Fhubs.hust.edu.cn%2Fhustpass.action'
        self.url2='https://pass.hust.edu.cn/cas/login?service=http%3A%2F%2Fhubs.hust.edu.cn%2Fhustpass.action'
        self.url3='http://hub.hust.edu.cn/hustpass.action'
        self.url4='http://hubs.hust.edu.cn/hublogin.action'
        self.postData1=urllib.urlencode({})
        self.postData2=urllib.urlencode({
            'username':'56ff07f249594f8e7ec6f9101ff4a2fc2287f81293dd5e400c23cb19805136d35f46598bf8f1b13932b62f1f4ed25e1bb65ad5fd663a56c4312becbb69a0da32d37314b3097ef5d15944997f4bb0d98a7b34607939f694e54e7169d23b997fce95d625bec5414eb263c09d0a79c58ddd6628552952e2f7ef53ec037d66ff8222',
            'password':'1fb8cd2ca5b1ceb208d3d52210dcb3d3ae990c35ad3dce7da43ce51f0b50c7be011e87d510db09fd6fd640d58ed7022838014716a821dc828d27bc190cdea2c6f84d165b551dd3bb6b732e17f7af6781dce6d210d2b2e2711a6c4eca086919313d9e52edbd11ef041e22f2e182f3779b8eb2785f825b4d269634c3af85bec800',
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
    hub=HUB()
    hub.start()
    w=raw_input('Press any key to end......')

except urllib2.URLError,e:
    if hasattr(e,'code'):
        print e.code
    if hasattr(e,'reason'):
        print e.reason
