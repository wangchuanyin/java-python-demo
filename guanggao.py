'''
Created on Apr 11, 2018

@author: Charlie.Wang
'''
import urllib.request,socket,sys
# def visit_guanggao(args):
#     print("your request user agent is "+my_user_agent)
 
if __name__ == '__main__':
    timeout =5
    socket.setdefaulttimeout(timeout)
   # print("your argument is {}".format(sys.argv[1]))
   # my_user_agent = sys.argv[1]
    try:
        url="http://wm.lrswl.com/page/?s=270987"
        req = urllib.request.Request(url)  
        req.add_header('Referer', 'http://www.baidu.com')  
        response = urllib.request.urlopen(req) 
        html = response.read()
        print("html==> {}".format(html))
    except urllib.error.HTTPError as e:
        print("HTTPError")  
        print(e.code)
        print(e.read().decode("utf8"))
    except urllib.error.URLError as e2:
        print("URLError")  
        print('We failed to reach a server.')
        print('Reason: ', e2.reason)
    else:
        print("good!")
        print(response.read().decode("utf8"))
