# -*- coding: utf-8 -*-
"""
@author: bsbilal
"""

from bs4 import BeautifulSoup #html parcalama icin gerekli kutuphane
import requests #internete baglanmak icin gerekli kutuphane

#baglanirken tarayicidan baglaniyormus gibi cikma
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',}

#Hafta Girisi
haftaNo = input("Haftayi girin(ornek 9): ")
try:
       print(str(haftaNo))
       page=requests.get("https://www.tff.org/Default.aspx?pageID=198&hafta="+str(haftaNo)+"#grpctl00_MPane_m_198_935_ctnr_m_198_935", headers=headers)
       soupTff = BeautifulSoup(page.content,"html.parser")#html parcalanmasi
       soupTarih=soupTff.find_all("td",{"align":"left"})#Tarihlerin alinmasi
       soupSkor= soupTff.find_all("td",{"align":"center"})#skorarin alinmasi
       soupTakimlar= soupTff.find_all("td",{"style":"width: 30%;"})#takimlarin alinmasi
       scorer=43 #skorlar 43. tdden sonra basliyor
       for x in range(0,18,2):
              print(soupTarih[x+1].text)
              skor=soupSkor[scorer].text.strip()
              print(soupTakimlar[x].text.strip()+ " |" + soupSkor[scorer].text.strip() +" |"+ soupTakimlar[x+1].text.strip())
              scorer+=1
except:
    print("Veriler Alinamadi")

