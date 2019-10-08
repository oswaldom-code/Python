
import urllib3


def app():
    
    http = urllib3.PoolManager() # creamos un objeto pool manager para manejar las conexiones

   # r = http.request('GET', 'http://httpbin.org/robots.txt') # devuelve un objeto HTTPResponse
    
    r = http.request('POST', 'http://httpbin.org/post', fields={'hello': 'world'})
    
    print(r.data)





if __name__ == '__main__':
    app()
    