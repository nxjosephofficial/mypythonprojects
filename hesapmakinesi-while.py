# Gelismis hesap makinesi [TR]
# Advanced calculator [EN]
while True:
    sayi1 = int(input("1.Sayiyi giriniz."))
    sayi2 = int(input("2.Sayiyi giriniz."))
    islemler = """
    1.topla (+)
    2.cikar (-)
    3.bol (/)
    4.carp (*)
    5.cikis (q)
    """
    print(islemler)
    islem_turu = input("Islem turunu seciniz.")
    
    if islem_turu == "1" or islem_turu == "topla" or islem_turu == "+":
        print(sayi1+sayi2)
    elif islem_turu == "2" or islem_turu == "cikar" or islem_turu == "-":
        print(sayi1-sayi2)
    elif islem_turu == "3" or islem_turu == "bol" or islem_turu == "/":
        print(sayi1/sayi2)
    elif islem_turu == "4" or islem_turu == "carp" or islem_turu == "*":
        print(sayi1*sayi2)
    elif islem_turu == "5" or islem_turu == "q" or islem_turu == "cikis":
        break
    else:
        print("Oops, bir seyler yanlis gitti.")
