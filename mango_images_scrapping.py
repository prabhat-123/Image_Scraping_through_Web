import requests
from bs4 import BeautifulSoup
import os
url = requests.get("https://www.google.com/search?sxsrf=ALeKk03LwNirYadlY3TcS2-3mRBLKnLdyQ:1589866686393&source=univ&tbm=isch&q=mango+images&sa=X&ved=2ahUKEwj3jNT4mr_pAhUm8HMBHd_mDdwQ7Al6BAgKEEk&biw=1366&bih=695")
soup = BeautifulSoup(url.content,'html.parser')
imagelocation = soup.find_all('img')
folder_name = "mango"
if os.path.exists(folder_name) is False:
    os.mkdir(folder_name)

for img in imagelocation:
    img_url = img.get('src')
    if img_url is not None and img_url.startswith('http'):
        response = requests.get(img_url)
        image_load = response.content

        
        with open("mango/"+str(imagelocation.index(img)) + ".jpg", "wb") as f:
            f.write(image_load)
        print("File are downloaded")