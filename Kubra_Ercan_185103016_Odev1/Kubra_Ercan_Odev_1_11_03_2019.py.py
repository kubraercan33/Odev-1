#!/usr/bin/env python
# coding: utf-8

# # GÜVERCİN YUVASI PRENSİBİ

# <p style='color:blue;'>Bilgisayar bilimleri de dahil olmak üzere pek çok matematik temelli bilim ve mühendislik alanında kullanılan oldukça basit bir umdedir.
# İsmini güvercin yuvalarından alan bu kaideye göre yuva sayısından fazla güvercin varsa ve bütün güvercinler bir yuvaya girecekse,en az
# bir yuvaya birden fazla güvercin girmek zorundadır.</p>

# <p style='color:blue;'>Bu durumu sembollerle göstermemiz gerekirse n tane yuva ve m tane güvercin için:
# m > n durumunda en az bir yuvada birden fazla güvercin bulunmalıdır.</p>

# ### ÖRNEK: 

# İskambil kartlarında 4 tip kart bulunur. Bunlar: Kupa, Karo, Sinek ve Maça'dır.
# 10 adet iskabil kartından kaç tanesi aynı tipte karttır?

# ### <span style='color:red;'>ÇÖZÜM:</span>

# <p>10 adet iskambil kartı 4 ayrı gruba ayrılacaktır. 
# Güvercin Yuvası Prensibine uyarlandığında güvercin sayısı iskambil sayısı ile; kart tipi sayısı ise yuva sayısı ile özdeştirilmiştir. 
# İskambil kart sayısı, kart tipi sayısına (yani 4'e) bölünür. Sonra bulunan değer yukarı yuvarlanır.
# 
# <i style='color:blue;'>math.ceil(Güvercin Sayısı / Yuva Sayısı) = math.ceil(İskambil Kartı Sayısı / İskambil Kart Tipi Sayısı)
# 
# math.ceil(10/4)=math.ceil(2.5)=3</i>
# </p>

# ## İskambil Kartı Örneği 

# In[ ]:


import math

def Sonuc(Iskambil_Kart_Sayisi): # Güvercin Yuvası Prensibi kuralı baz alındığında (güvercin/yuva sayısı)=(İskambil Kart Sayısı/Kart Tipi Sayısı) oranı yukarı yuvarlanmalıdır.
	
	sonuc = (math.ceil(int(Iskambil_Kart_Sayisi)/4.0))
 
	return sonuc


def SayiKontrol(GirilenDeger): #Girilen değerin kontrolü sağlanır. Negatif sayı yada harf girildiğinde uyarı çıkartılır. 
	deger = str(GirilenDeger)
	if not deger.isdigit(): #karakter kontrolü
		return False
	elif(int(deger) < 1) or (int(deger) > 52):  # 1-52 aralık kontrolü
		return False
	else:
		return True
 
    
while True:
	print("Lütfen 1 ile 52 aralığında bir sayi giriniz..")
	Iskambil_Kart_Sayisi = input("Kac adet iskambil karti ile islem yapmak istersiniz?: ")
	if SayiKontrol(Iskambil_Kart_Sayisi) == True:
		print("Aynı Tipte Kart Sayısı: En az %d adettir." % Sonuc(Iskambil_Kart_Sayisi))
	print("\n")


# In[ ]:





# In[ ]:




