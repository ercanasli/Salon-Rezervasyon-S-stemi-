#ASLI CENNET ERCAN 170421040
#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Koltuk:#Salonda bulanacak koltuğu ve özelliklerini bir sınıf yardımıyla oluşturdum.  
    def __init__(self, kategori):
        self.kategori = kategori#Burada koltuğun hangi kategoriye ait olduğu bildirilir.
        self.rezerve = False #Koltuğun rezerve olup olmadığını boolean bir değişken ile belirledim.


# In[2]:


import sys
class Salon:
    def __init__(self):
        #Aşağıda bizden istenen 20 sıra ve her sırada 20 koltuk olan salonu oluşturdum.
        self.koltuklar = [[Koltuk(0) for j in range(20)] for i in range(20)]
        #İlk 10 sıradaki koltukların kategorilerini belirler.
        for i in range(10):
            for j in range(0,5):
                self.koltuklar[i][j] = Koltuk(2)
            for j in range(5,15):
                self.koltuklar[i][j] = Koltuk(1)
            for j in range(15,20):
                self.koltuklar[i][j] = Koltuk(2)
        #Sonraki 10 sıradaki koltukların kategorilerini belirler.
        for i in range(10,20):
            for j in range(0,5):
                self.koltuklar[i][j] = Koltuk(4)
            for j in range(5,15):
                self.koltuklar[i][j] = Koltuk(3)
            for j in range(15,20):
                self.koltuklar[i][j] = Koltuk(4)
        #Kategori bilet fiyatlarını ve kullanıcının max alabileceği bilet sayısını bize örnekte verilen dosyayı
        #oluşturdum ve oradan okuyarak değişkenlere atanır.("indirim.txt") 
        self.fiyat = {}
        self.max_alinabilir_bilet = 0
        f = open("C:\\Users\\user\\Desktop\\indirim.txt")
        lines = f.readlines()
        self.max_alinabilir_bilet = int(lines[0][2:])
        for i in range(4):
            self.fiyat[i+1] = int(lines[i+1].split("-")[1])
        f.close()
        self.toplam_ciro=[]
    #Ana_menu fonksiyonu ile burada yapılabilecek işlemlerle alakalı kullanıcıya bilgi verilir.Yapılan seçimi geri döndürür.
    def ana_menu(self):
        print("****************")
        print("****Ana Menü****")
        print("****************")
        print("1-Rezervasyon İşlemi")
        print("2-Salonu Yazdır")
        print("3-Yeni Etkinlik")
        print("4-Toplam Ciro")
        print("0-Çıkış")
        self.sec = input("Seçiminizi yapınız: ")
        return self.sec
    #main fonk. ile ana_menü'de yapılmış seçimi işleme alır.
    def main(self):
        secim = self.ana_menu()
        if secim == "1":
            self.rezervasyon_menü()#rezervasyon işleminde gerekli bilgileri almak için fonksiyona yönlendirir.
            self.main()#işlem sonrası ana_menü'ye geri döner.   
        elif secim == "2":
            self.salon_göster()#salonun rezerve durumunu göstermek için fonk. yönlendirir.
            self.main()    
        elif  secim == "3":
            self.salon_sifirla()
            print("Yeni Etkinlik Oluşturuldu")
            self.main()   
        elif secim == "4":
            self.Toplam_Ciro()
            self.main()   
        elif secim == "0":
            print("Program sonlandı.")
            sys.exit()
        else:
            print("Lütfen geçerli bir seçim yapınız.")
            self.main() 
    #Etkinlikte salonun rezerve durumunu hakkında bilgi vermek için fonk. oluşturdum 
    def salon_göster(self):
        #Salonda bulunan koltukları döngü içine alır.
        for sira in self.koltuklar:
            #Sırada bulanan koltukların doluluklarını kontrol eden ve string bir değişkene dolu ise "X" boş ise "-" ekleyen döngü
            koltuk_string = ""
            for koltuk in sira:
                if koltuk.rezerve:
                    koltuk_string += "X"
                else:
                    koltuk_string += "-"
            #Her sırayı döngüden çıkınca yazdırır.
            print(koltuk_string)
    #Yeni etkinlik için salon rezervasyonunu sıfırlayan fonksiyon.
    def salon_sifirla(self):
        for satir in self.koltuklar:
            for koltuk in satir:
                koltuk.rezerve = False
        self.toplam_ciro=[]#Etkinlik yenilendiği için ciroyu sıfırlar.
    #rezervasyon_menü fonksiyonundan alınan değişkenler ile rezerve işlemi yapılan fonksiyon.
    def rezervasyon_yap(self, kategori, bilet_sayisi):
        if bilet_sayisi > self.max_alinabilir_bilet:#Girilen bilet sayısı max alınabilir bilet sayısını aşarsa
            #hata mesajı verip ana_menüye döner. 
            print("Maximum bilet adedini geçtiniz!")
            return

        bos_koltuk = 0
        #kategorideki güncel boş koltuk sayısını hesaplar
        for satir in self.koltuklar:
            for koltuk in satir:
                if koltuk.kategori == kategori and not koltuk.rezerve:
                    bos_koltuk += 1
        
        if bos_koltuk < bilet_sayisi:#Girilen bilet sayısın boş koltuk sayısını geçerse bilgi verip geri döner.
            print("Bu kategoride yeterli boş koltuk bulunmamaktadır.")
            return
        else:##Girilen bilet sayısın boş koltuk sayısını geçmezse rezerve işlemi gerçekleştirilir.
            sayac = 0
            toplam_tutar = 0
            rezerve_koltuklar=[]
            if kategori in [1,3]:#kategori 1 ya da 3 ise aşağıdaki gibi rezerve işlemi gerçekleştirir.
                koltuk_num =5
                satir_baslangic = 10 if kategori == 3 else 0
                for i in range(satir_baslangic, satir_baslangic+10):#kategorideki koltukları baştan başlayarak gezer.
                    for j in range(koltuk_num, koltuk_num+10):
                        if not self.koltuklar[i][j].rezerve:#Koltuk rezerve durumunu kontrol eder.
                            self.koltuklar[i][j].rezerve = True #rezerve değilse rezerve eder.
                            numara=(i+1,j+1)
                            rezerve_koltuklar.append(numara)#rezervasyon yaptığı koltukları bi listeye ekler 
                            sayac += 1
                            toplam_tutar += self.fiyat[kategori]
                        if sayac == bilet_sayisi:#kullanıcının istediği kadar koltuk rezervasyonu yapınca ayrılır.
                            break
                    if sayac == bilet_sayisi:
                        break
            if kategori in [2,4]:#kategori 2 ya da 4 ise aşağıdaki gibi rezerve işlemi gerçekleştirir.
                satir_baslangic = 0 if kategori == 2 else 10
                for i in range(satir_baslangic,satir_baslangic+10):
                    for j in range(5,0,-1):#2. ve 4. kategori için 5ten başlayarak 1e doğru rezervasyon yapar.
                        if not self.koltuklar[i][j-1].rezerve:
                            self.koltuklar[i][j-1].rezerve = True
                            numara=(i+1,j)
                            rezerve_koltuklar.append(numara)
                            sayac += 1
                            toplam_tutar += self.fiyat[kategori]
                        if sayac == bilet_sayisi:
                            break
                    if sayac == bilet_sayisi:
                        break
                    for j in range(15, 20):#İlk 5 koltuktan sonra 16dan devam eder.
                        if not self.koltuklar[i][j].rezerve:
                            self.koltuklar[i][j].rezerve = True
                            numara=(i+1,j+1)
                            rezerve_koltuklar.append(numara)
                            sayac += 1
                            toplam_tutar += self.fiyat[kategori]
                        if sayac == bilet_sayisi:
                            break
                    if sayac == bilet_sayisi:
                        break
        yapilan_indirim=0
        net_tutar=0
        f = open("C:\\Users\\user\\Desktop\\indirim.txt")#indirim tarifelerini okumak için dosyayı tekrar açar.
        lines = f.readlines()
        for line in lines[5:]:#indirim tarifelerini okur.
            parts = line.split("-")
            k = int(parts[0])
            min_bilet = int(parts[1])
            max_bilet = int(parts[2])if parts[2] != "M" else self.max_alinabilir_bilet
            indirim = int(parts[3])
           #indirim tarifelerini gezerek uygulanacak indirim varsa uygular ve döngüden ayrılır.
            if k==kategori and min_bilet<=bilet_sayisi<=max_bilet:
                yapilan_indirim=(toplam_tutar * indirim / 100)
                net_tutar=toplam_tutar-yapilan_indirim
                break
            else:
                yapilan_indirim=0
                net_tutar=toplam_tutar
        a=(kategori,net_tutar)
        self.toplam_ciro.append(a)#toplam ciro listesine kategoriyi ve net tutarı ekler.
        print("Rezervasyon işlemi başarıyla gerçekleştirildi. Rezerve edilen koltuklar (Sıra-Koltuk): ",end=" ")
        for koltuk in rezerve_koltuklar:
            print(str(koltuk[0])+"-"+str(koltuk[1])+",",end=" ")
        print("\nToplam Tutar: {} TL".format(toplam_tutar))
        print("Yapılan indirim: {} TL".format(yapilan_indirim))
        print("Net Tutar: {} TL".format(net_tutar))
    #Rezervasyon işleminde gerekli bilgileri alır,kontrol eder ve rezervasyon_yap fonk. çağırır.(Kategori-bilet sayısı)   
    def rezervasyon_menü(self):
        kategori = int(input("Kategori seçiniz (1-4 arası): "))
        if kategori not in range(1,5):#belirtilen kategori aralığına girmezse uyarı verip tekrar girmesini ister.
            print("HATALI TUŞLAMA")
            self.rezervasyon_menü()
        bilet_sayisi = int(input("Bilet adedini giriniz: "))
        self.rezervasyon_yap(kategori, bilet_sayisi)
    #toplam_ciro listesi ile her kategorinin cirosunu ayrı ayrı hesaplar sonra toplam ciroyu hesaplar ve
    #bunların hepsinin bilgisini ekrana yazdırır.
    def Toplam_Ciro(self):
        kategori1=0
        kategori2=0
        kategori3=0
        kategori4=0
        for satir in self.toplam_ciro:
            if satir[0]==1:
                kategori1+=satir[1]
            elif satir[0]==2:
                kategori2+=satir[1]
            elif satir[0]==3:
                kategori3+=satir[1]
            elif satir[0]==4:
                kategori4+=satir[1]       
        print("1.Kategoriden elde edilen tutar: {}".format(kategori1))
        print("2.Kategoriden elde edilen tutar: {}".format(kategori2))
        print("3.Kategoriden elde edilen tutar: {}".format(kategori3))
        print("4.Kategoriden elde edilen tutar: {}".format(kategori4))
        toplam=kategori1+kategori2+kategori3+kategori4
        print("Toplam ciro : {}".format(toplam))


# In[3]:


a=Salon()
a.main()





