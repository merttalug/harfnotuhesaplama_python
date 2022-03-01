vize1=int(input("Lütfen 1. vize notunuzu giriniz: "))
vize2=int(input("Lütfen 2. vize notunuzu giriniz: "))
final_=int(input("Lütfen final notunuzu giriniz: "))



"""
90-100---->AA
80-90----->BA
70-80------>BB
60-70------->CB
50-60------->CC
40-50-------->DC
<40---------->Başarısız !


"""
if (vize1 >=0 and vize1 <=100) and (vize2>=0 and vize2<=100) and (final_ >=0 and final_ <=100):
    ortalama = (vize1 * 0.3) + (vize2 * 0.3) + (final_ * 0.4)


    print("Ortalamanız: {}".format(ortalama))


    if ortalama <=100 and ortalama >=90:
         print("AA ile dersi geçtiniz.")
    elif ortalama < 90 and ortalama >=80:
        print("BA ile dersi geçtiniz.")
    elif ortalama < 80 and ortalama >=70:
        print("BB ile dersi geçtiniz.")
    elif ortalama <70 and ortalama >=60:
        print("CB ile dersi geçtiniz")
    elif ortalama <60 and ortalama >=50:
        print("CC ile dersi geçtiniz.")
    elif ortalama <50 and ortalama >=50:
        print("DC ile dersi şartlı geçtiniz.")
    else:
        print("Dersten başarısız oldunuz.")
else:
    print("Geçersiz bir not girdiniz. ")
