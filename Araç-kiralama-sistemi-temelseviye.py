

class Arac: 
    def __init__(self,marka,model,yakit,gunluk_fiyat) : 
        ### Araç bilgilerini kapüslleme işlemi yapılıyor ###
        self.marka = marka
        self.model = model
        self.yakit = yakit
        self.gunluk_fiyat = gunluk_fiyat
        

    def kiralama_bilgisi(self) : 
        ### Kiralama bilgilerini yazdıran methodu ####
        print(f"Marka: {self.marka}\nModel: {self.model}\nYakıt Türü: {self.yakit}\nGünlük Rent: {self.gunluk_fiyat}")

    def kiralama_bedeli(self) : 
        #### Kiralama bedeli hesaplanıyor ####
        gun = int(input("Kiralama Süresi(Gün)"))    ## Kullanıcıdan araç kiralama süresi bilgisi alınıyor
        return self.gunluk_fiyat*gun

class Araba(Arac):    
    def __init__(self,marka,model,yakit,gunluk_fiyat,kapi_sayisi): 
        super().__init__(marka,model,yakit,gunluk_fiyat)   ### Ata sınıftan özellikler çekiliyor
        self.kapi_sayisi = kapi_sayisi

    def kiralama_bilgisi(self) : 
        super().kiralama_bilgisi()
        print(f"Kapı Sayısı: {self.kapi_sayisi}")
        print()
class Motosiklet(Arac): 
    def __init__(self,marka,model,yakit,gunluk_fiyat,motor_hacmi): 
        super().__init__(marka,model,yakit,gunluk_fiyat)
        self.motor_hacmi = motor_hacmi

    def kiralama_bilgisi(self) : 
        super().kiralama_bilgisi()

        ### motor gücüne bağlı olarak kask kullanım zorunluluğu değerlendiriliyor.
        if self.motor_hacmi > 50 :  
            print(f"Motorunuz {self.motor_hacmi} cc hacmindedir. Kask kullanmanız zorunludur.")
        else : 
            print(f"Motorunuz {self.motor_hacmi} cc hacmindedir. Kask kullanmak zorunda değilsiniz.")
        print()
class Kamyonet(Arac): 
    def __init__(self,marka,model,yakit,gunluk_fiyat,yuk_kapasitesi): 
        super().__init__(marka,model,yakit,gunluk_fiyat)
        self.yuk_kapasitesi = yuk_kapasitesi

    def kiralama_bilgisi(self) : 
        super().kiralama_bilgisi()
        print(f"Yük Kapasitesi: {self.yuk_kapasitesi}")
        print()


araba1 = Araba("Citroen","C4x","Benzin",1000,4)
motosiklet1 = Motosiklet("Honda","NC750","Benzin",500,750)
motosiklet2 = Motosiklet("Kuba","City","Benzin",200,39)
kamyonet = Kamyonet("Ford","Transit","Benzin",2500,5000)

print(araba1.kiralama_bedeli())
print(kamyonet.kiralama_bedeli())