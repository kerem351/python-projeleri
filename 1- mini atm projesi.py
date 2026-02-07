kullancilar={
    'kerem':{'sifre':'123','bakiye':160},
    'berivan':{'sifre':'6057','bakiye':2000},
    'mizgin':{'sifre':'1946','bakiye':100000},
}


username=input('kullanıcı adınızı giriniz')

if  username in kullancilar:

    hak=3
    while hak>0:
        sifre=input('şifrenizi giriniz')
        if sifre==kullancilar[username]['sifre']:
            print('heseba giriş yapıldı')
            break
        else:
            print('sifre yanliş')
            hak=hak-1
    if hak==0:
        print('kartınız bloke olmuştur hayırlı uğurlu olsun')
    else:
        

        print('''
        (1)bakiye görüntüle
        (2)para çek
        (3)para yatırma
        (4)çıkış

        ''')

        secim=input('seçiminizi yapınız:')

        if secim=='1':
            bakiye=kullancilar[username]['bakiye']
            print(bakiye)
        elif secim=='2':
            miktar=(input("Ne kadar para çekmek istiyorsun:"))
            bakiye=kullancilar[username]['bakiye']
            if miktar<=bakiye:
                bakiye=bakiye-miktar
                print(f'kalan bakiyeniz:',bakiye)

            else:
                print('bakiyeniz yetrli değil')
        elif secim=='3': 
            bakiye=kullancilar[username]['bakiye']
            miktar=int(input('kaç para yatıracaksınız:'))
            bakiye=bakiye+miktar

            print('toplam bakiyeniz',bakiye)

      
                    
        

        