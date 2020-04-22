print("Silahkan pesan minuman Anda")
print("jumlah minimal Rp. 10.000")
uang= int(input("masukkan uang anda = Rp."))

        

        
def pesan(uang):
    menu_minuman=["1.Aqua = Rp.3000" , "2.Teh Pucuk = Rp.4000" , "3.Coca-cola = Rp.5000" , "4.Fanta = Rp.5000" , "5.Indomilk = Rp.6000" , "6.Pepsi = Rp.7000" , "7.Greensand = Rp.8000" , "8.Bintang = Rp.9000"]
    choise = 1
    while choise == 1:
        if uang > 0:
            print("pilih minuman anda :",*menu_minuman, sep= "\n")
            minuman=int(input("Tulis angka minuman : "))
            if minuman == 1:
                print("item = Aqua")
                uang = uang - 3000
                print("uang anda sekarang Rp." + str(uang))
               
            elif minuman == 2:
                print("item = Teh Pucuk")
                uang = uang - 4000
                print("uang anda sekarang Rp." + str(uang))
                
            elif minuman == 3:
                print("item = Coca-Cola")
                uang = uang - 5000
                print("uang anda sekarang Rp." + str(uang))
                
            elif minuman == 4:
                print("item = Fanta")
                uang = uang - 5000
                print("uang anda sekarang Rp." + str(uang))
            
            elif minuman == 5:
                print("item = Indomilk")
                uang = uang - 6000
                print("uang anda sekarang Rp." + str(uang))
                
            elif minuman == 6:
                print("item = Pepsi")
                uang = uang - 7000
                print("uang anda sekarang Rp." + str(uang))
                
            elif minuman == 7:
                print("item = Greensand")
                uang = uang - 8000
                print("uang anda sekarang Rp." + str(uang))
                
            elif minuman == 8:
                print("item = Bintang")
                uang = uang - 9000
                print("uang anda sekarang Rp." + str(uang))
                
            else:
                print("input salah !")
            
        else:
            print("Maaf budget anda tidak mencukupi ")
        print("")
        print("")
        print("Mau membeli tiket lagi?")
        print("")
        print("1. Ya")
        print("2. Tidak")
        print("")
        mengulang = int(input("Masukkan angka pilihan : "))
        print("")
        print("")
        print("")
        print("")
        if(mengulang > 1):
            print("terimakasih")
            break
        print("terimakasih")
       
    
