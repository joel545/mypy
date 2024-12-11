import requests
import bs4
import os
url="https://marketing-hsu01.web.app/fruit.html"
page=requests.get(url)
page.encoding="utf-8"
print(page) #reponse [200] , 請求成功
print(page.text)
soup=bs4.BeautifulSoup(page.text,"html.parser")
print (soup)
print(soup.prettify()) #如同字串，輸出到頁面元素
print("\n----title-----------------------")
title_tag=soup.title
print("網站標題(html 標籤):",title_tag)
print("網站標題(標籤名稱):",title_tag.name)
print("網站標題:",title_tag.text)
print("網站標題(標籤名稱):",title_tag.string)
print("\n----td-----------------------")
td_tag=soup.find_all("td")
print(td_tag)
print("\n----走訪 List td-----------------------")
for tag in td_tag:
    #print(tag)
    print(tag.contents)
    
print("\n----img-----------------------")
img_tag=soup.find_all("img")
print("\n----img,取得圖片的節點----------------")
for tag in img_tag:
    print(tag)
    
print("\n----img2-----------------------")
img2_tag=soup.find_all("img")
print("\n----img,取得圖片的節點之屬性,圖片來源src----------------")
for tag in img2_tag:
    print(tag.get("src"))  #取得屬性,圖片來源src
    
pos=url.rfind("/")
print(pos) #31
web=url[0:pos+1]
print(web)  #https://marketing-hsu01.web.app/fruit.html

print("\n----img3, full src-----------------------")
img3_tag=soup.find_all("img")
for tag in img3_tag:
    src=tag.get("src")
    fullsrc=web + src
    print(fullsrc)
    file=src[src.rfind("/")+1:]
    print(file)  #取得圖片來源full src
    
    if not os.path.exists("download_images"):
        os.mkdir("download_images")
    img=requests.get(fullsrc) #下載圖片
    with open("download_images/"+file,"wb") as file:  #開啟資料夾與圖片命名
        file.write(img._content) #寫入圖片以二進制位元碼