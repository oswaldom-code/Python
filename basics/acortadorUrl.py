import requests

'''
  parameters: website: string that contains a website 
  
  return: return a string with the website encoding 
  
  dependences: module requests
'''
def getShortUrl(website):
    shortUrl=requests.get("http://tinyurl.com/api-create.php?url="+website);
    return shortUrl.content.decode("utf-8")



print("Ejemplo de como acortar un url")
website="https://www.google.com.mx/"
url=getShortUrl(website)
print("la url acortada es ",url)