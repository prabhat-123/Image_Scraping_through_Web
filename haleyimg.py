from bs4 import BeautifulSoup
import requests
import os
url=requests.get("https://auto.ndtv.com/harley-davidson-bikes/dealers")
soup=BeautifulSoup(url.content,'html.parser')
imagelocation=soup.find_all('img')
folder_name = "harley"
if os.path.exists(folder_name) is False:
    os.mkdir(folder_name)

for img in imagelocation:
    img_url=img.get('data-src')
    if img_url is not None:
        response=requests.get(img_url)
        image_load=response.content

        with open("harley/"+str(imagelocation.index(img)) + ".jpg", "wb") as f:
            f.write(image_load)
        print("File are downloaded")


