from selenium import webdriver
import bs4 as bs
import chromedriver_autoinstaller as ca
import requests



''' Normal Weapons '''

url = "https://mirror.gbf-wiki.com/index.php?%C9%F0%B4%EFSSR"
path = ca.install()
driver = webdriver.Chrome(path)
driver.get(url)
content = driver.page_source
soup = bs.BeautifulSoup(content, features="html.parser")

div = soup.find_all('div', attrs={'class':'ie5'}, limit=3)[-1]
tbody = div.find('tbody')
weapons_list = tbody.findAll('tr')

for weapon_source in weapons_list:
    tds = weapon_source.find_all('td')
    image_title = tds[0].find('a')['title']
    if image_title is not None:
        if "." in image_title:
            index = image_title.index(".")
            id = image_title[0:index]
            #Normal Image URL
            #image_url = "http://game-a.granbluefantasy.jp/assets/img_mid/sp/assets/weapon/m/" + str(id) + ".jpg"
            #Main Image URL
            image_url = "http://game-a.granbluefantasy.jp/assets/img_mid/sp/assets/weapon/ls/" + str(id) + ".jpg"
            response = requests.get(image_url)
            file = open("C:\\Users\\Ken\\Desktop\\GBF_Weapons\\Main_Image\\"+str(id)+".png", "wb")
            file.write(response.content)
            file.close()

print("done")


''' Special Weapons'''
url = "https://mirror.gbf-wiki.com/index.php?%C9%F0%B4%EFSSR%2F%C6%C3%BC%EC%C9%F0%B4%EF"
path = ca.install()
driver = webdriver.Chrome(path)
driver.get(url)
content = driver.page_source
soup = bs.BeautifulSoup(content, features="html.parser")

div = soup.find_all('div', attrs={'class':'ie5'}, limit=2)[-1]
tbody = div.find('tbody')
weapons_list = tbody.findAll('tr')

print(len(weapons_list))
for weapon_source in weapons_list:
    tds = weapon_source.find_all('td')
    image_href = tds[0].find('a')
    if image_href:
        image_title = image_href['title']
    if image_title is not None:
        if "." in image_title:
            index = image_title.index(".")
            id = image_title[0:index]
            if "_note" in id:
                id = id[0: id.index("_note")]
            #Normal Image URL
            #image_url = "http://game-a.granbluefantasy.jp/assets/img_mid/sp/assets/weapon/m/" + str(id) + ".jpg"
            #Main Image URL
            image_url = "http://game-a.granbluefantasy.jp/assets/img_mid/sp/assets/weapon/ls/" + str(id) + ".jpg"
            response = requests.get(image_url)
            file = open("C:\\Users\\Ken\\Desktop\\GBF_Weapons\\Main_Image\\"+str(id)+".png", "wb")
            file.write(response.content)
            file.close()
print("done")


