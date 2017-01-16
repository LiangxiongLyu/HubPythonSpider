import urllib
import urllib2
import cookielib
import re
#声明一个CookieJar对象实例来保存cookie
cookies = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookies)
#通过handler来构建opener
opener = urllib2.build_opener(handler)


try:
    
    #访问登录界面
    url1='https://pass.hust.edu.cn/cas/login?service=http%3A%2F%2Fhubs.hust.edu.cn%2Fhustpass.action'
    req1=urllib2.Request(url1)
    res1=opener.open(req1)

    ####表单提交地址
    url2='https://pass.hust.edu.cn/cas/login?service=http%3A%2F%2Fhubs.hust.edu.cn%2Fhustpass.action'
    post2={
        'username':'56ff07f249594f8e7ec6f9101ff4a2fc2287f81293dd5e400c23cb19805136d35f46598bf8f1b13932b62f1f4ed25e1bb65ad5fd663a56c4312becbb69a0da32d37314b3097ef5d15944997f4bb0d98a7b34607939f694e54e7169d23b997fce95d625bec5414eb263c09d0a79c58ddd6628552952e2f7ef53ec037d66ff8222',
        'password':'1fb8cd2ca5b1ceb208d3d52210dcb3d3ae990c35ad3dce7da43ce51f0b50c7be011e87d510db09fd6fd640d58ed7022838014716a821dc828d27bc190cdea2c6f84d165b551dd3bb6b732e17f7af6781dce6d210d2b2e2711a6c4eca086919313d9e52edbd11ef041e22f2e182f3779b8eb2785f825b4d269634c3af85bec800',
        'code':'code',
        'lt':'LT-NeusoftAlwaysValidTicket',
        'execution':'e1s1',
        '_eventId':'submit' 
        }
    postData2=urllib.urlencode(post2)
    headers2={
        ##为空，可以直接访问到hub系统
        }
    req2=urllib2.Request(url2,postData2,headers2)
    res2=opener.open(req2)
    print res2.read().decode('utf-8')


    ###这个地址使用Fiddler捕捉到过，但是后来一直没有了，本以为是通过这个中转地址访问的HUB系统，但是后来一直没有捕捉到
    ###不过下面的代码还可以访问到这个地址的代码？？Excuse me？？
    #url3='http://hub.hust.edu.cn/hustpass.action'
    #req3=urllib2.Request(url3)
    #res3=opener.open(req3)
    #content3=res3.read().decode('utf-8')
    #print content3
    ###定义从上述的页面取得表单参数的函数
    #def getInfo(content):
    #    pattern=re.compile('<input.*?name="(.*?)".*?value="(.*?)"')
    #    result=pattern.findall(content)
    #    Dict={}
    #    for item in result:
    #        Dict[item[0]]=item[1]
    #    return Dict
    ###上述地址自动跳转地址
    #url4='http://hubs.hust.edu.cn/hublogin.action'
    #post4=getInfo(content3)
    ##print post4
    #postData4=urllib.urlencode(post4)
    #headers4={
    #    'Host': 'hubs.hust.edu.cn',
    #    'Connection': 'keep-alive',
    #    'Content-Length': '258',
    #    'Cache-Control': 'max-age=0',
    #    'Origin': 'http://hub.hust.edu.cn',
    #    'Upgrade-Insecure-Requests': '1',
    #    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #    'Content-Type':'application/x-www-form-urlencoded',
    #    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #    'Referer':'http://hub.hust.edu.cn/hustpass.action',
    #    'Accept-Encoding':'gzip, deflate',
    #    'Accept-Language':'zh-CN,zh;q=0.8'
    #}
    #req4=urllib2.Request(url4,postData4,headers4)
    #res4=opener.open(req4)
    #print res4.read()

except urllib2.URLError,e:
    print e.code
