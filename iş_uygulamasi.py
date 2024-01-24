import socket  # internet bağlantımızı kontrol etmekte kullanağımız kütüphane
import time # pomodoro programımızd akullancagız
import tkinter as tk  # pencere işlerinde kullanacağımız kütüphane
from tkinter import * # tkinter kutuphanesındekı tum modullerı ımport etmek ıcın kullanıyoruz
import requests  # url üzerinden veri çekmek için kullanacağımız kütüphane
from bs4 import BeautifulSoup # html.parser için kullandık
from PIL import ImageTk, Image # arkaplanımız için resim oluşturma işlemlerimizde kullanıyoruz
import datetime # tarih ve saati menumuzde goruntulemek ıcın kullancagız

# shift+f10 = HIZLI ÇALIŞTIRMA KISAYOL TUŞU
# ctrl+F = Arama yapmamızı saglayan kısayol tuşu

def dovizbutonu_click():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #socket.socket(socket.AF_INET, socket.SOCK_STREAM) komutuyla bir soket oluşturulur. AF_INET parametresi, IPv4 adresleme kullanılacağını belirtir. SOCK_STREAM ise TCP bağlantısı oluşturmak için kullanılır.
        s.connect(("www.google.com", 80)) # googleın 80 numaralı portuna bir ping atıyoruz
        s.close() # oluşturulan soketi kapatıyoruz
        print('Bağlanılıyor')
    except Exception: # hata/çalışmaması durumunda :
        print("Lütfen Internet Bağlantınızı Kontrol Ediniz")
        time.sleep(3)
        exit()

    hedef_sitesi = "https://kur.doviz.com/"
    hedef = requests.get(hedef_sitesi) # requests modülünü kullanarak belirtilen URL'den (hedef_sitesi değişkeninde tutulan) veri getirmek için bir istek yapar.
    ana_data = BeautifulSoup(hedef.content,"html.parser")  # html kodlarını ayıklayacagımzı ıcın html parser parametresini yazıyoruz
    dovizdata = ana_data.find("span", {"data-socket-key": "gram-altin"}).text  # veri span etiketi altında bunu belirtiyoruz
    dovizdata1 = ana_data.find("span", {"data-socket-key": "USD"}).text  # site url'i içerisinde veriler arasındaki tek değişken data-socket değeri bunu kullanacağız
    dovizdata2 = ana_data.find("span", {"data-socket-key": "EUR"}).text  # .text parametresi ile bir metin belgesi çektiğimizi belirtiyoruz
    dovizdata3 = ana_data.find("span", {"data-socket-key": "GBP"}).text
    dovizdata4 = ana_data.find("span", {"data-socket-key": "XU100"}).text
    dovizdata5 = ana_data.find("span", {"data-socket-key": "bitcoin"}).text


    # Döviz TEMA:
    # Bunlar temada kullanabılecegım guzel renkler "light steel blue" / "spring green" /
    doviz_pencere_rengi = "white"
    doviz_pencere_baslik_rengi = "white"
    doviz_pencere_baslik_yazi_tipi = "arial 15 bold"
    doviz_isim_rengi = "white"
    doviz_isim_yazi_tipi = "arial 12 bold"
    doviz_fiyat_rengi = "white"  # tüm tema renklerimi tek bir değişkende topladım degıstırmenın kolay olması için
    doviz_fiyat_yazi_tipi = "arial 12 bold"


    pencere_doviz = Toplevel()  # pencere_doviz oluşturdum
    pencere_doviz.geometry("310x270")  # bu pencerenin boyutlarını ayarladım
    pencere_doviz.resizable(False, False)  # döviz penceremizin boyutlarını kilitledik
    pencere_doviz.iconbitmap(r"resimler/gold_icon.ico")
    pencere_doviz.title("Döviz")  # pencere_doviz başlığımız
    pencere_doviz.configure(background=doviz_pencere_rengi)  # pencere_doviz rengimiz


    döviz_cerceve_resmi = tk.PhotoImage(file=r"resimler\döviz_arkaplan_resmi.png")
    pencere_arkaplan = tk.Label(pencere_doviz, image=döviz_cerceve_resmi)
    pencere_arkaplan.place(x=0, y=0, relwidth=1, relheight=1)
    pencere_arkaplan.pack()



    gramaltin = tk.Label(pencere_doviz, text="Gram Altın", font=doviz_isim_yazi_tipi, bg=doviz_isim_rengi)
    gramaltin.pack()  # frame oluşturduk
    gramaltin.place(x=30, y=45)
    altin_degeri = tk.Label(pencere_doviz, text=dovizdata, font=doviz_fiyat_yazi_tipi, bg=doviz_fiyat_rengi)
    altin_degeri.pack()
    altin_degeri.place(x=30, y=65)

    dolar = tk.Label(pencere_doviz, text="Dolar", font=doviz_isim_yazi_tipi, bg=doviz_isim_rengi)
    dolar.pack()
    dolar.place(x=215, y=45)
    dolar_degeri = tk.Label(pencere_doviz, text=dovizdata1, font=doviz_fiyat_yazi_tipi, bg=doviz_fiyat_rengi)
    dolar_degeri.pack()
    dolar_degeri.place(x=215, y=65)

    euro = tk.Label(pencere_doviz, text="Euro", font=doviz_isim_yazi_tipi, bg=doviz_isim_rengi)
    euro.pack()
    euro.place(x=30, y=115)
    euro_degeri = tk.Label(pencere_doviz, text=dovizdata2, font=doviz_fiyat_yazi_tipi, bg=doviz_fiyat_rengi)
    euro_degeri.pack()
    euro_degeri.place(x=30, y=135)

    sterlin = tk.Label(pencere_doviz, text="Sterlin", font=doviz_isim_yazi_tipi, bg=doviz_isim_rengi)
    sterlin.pack()
    sterlin.place(x=215, y=115)
    sterlin_degeri = tk.Label(pencere_doviz, text=dovizdata3, font=doviz_fiyat_yazi_tipi, bg=doviz_fiyat_rengi)
    sterlin_degeri.pack()
    sterlin_degeri.place(x=215, y=135)

    bist = tk.Label(pencere_doviz, text="Bist 100", font=doviz_isim_yazi_tipi, bg=doviz_isim_rengi)
    bist.pack()
    bist.place(x=30, y=185)
    bist_degeri = tk.Label(pencere_doviz, text=dovizdata4, font=doviz_fiyat_yazi_tipi, bg=doviz_fiyat_rengi)
    bist_degeri.pack()
    bist_degeri.place(x=30, y=205)

    bitcoin = tk.Label(pencere_doviz, text="Bitcoin", font=doviz_isim_yazi_tipi, bg=doviz_isim_rengi)
    bitcoin.pack()
    bitcoin.place(x=215, y=185)
    bitcoin_degeri = tk.Label(pencere_doviz, text=dovizdata5, font=doviz_fiyat_yazi_tipi, bg=doviz_fiyat_rengi)
    bitcoin_degeri.pack()
    bitcoin_degeri.place(x=215, y=205)

    pencere_doviz.mainloop()


def borsabutonu_click():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("www.google.com", 80))
        s.close()
        print('Bağlanılıyor')
    except Exception:
        print("Lütfen Internet Bağlantınızı Kontrol Ediniz")
        time.sleep(3)
        exit()

    hedef_site1 = "https://bigpara.hurriyet.com.tr/borsa/canli-borsa/"
    hedef1 = requests.get(hedef_site1)
    taramadegiskeni = BeautifulSoup(hedef1.content, "html.parser")
    borsadata = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_AEFES"}).text
    borsadata1 = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_ASELS"}).text
    borsadata2 = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_AKBNK"}).text
    borsadata3 = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_SKBNK"}).text
    borsadata4 = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_SISE"}).text
    borsadata5 = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_THYAO"}).text
    borsadata6 = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_VESTL"}).text
    borsadata7 = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_ULKER"}).text
    borsadata8 = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_AYGAZ"}).text
    borsadata9 = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_ALGYO"}).text
    borsadata10 = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_AKSEN"}).text
    borsadata11 = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_AFYON"}).text
    borsadata12 = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_CCOLA"}).text
    borsadata13 = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_PGSUS"}).text
    borsadata14 = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_SAHOL"}).text
    borsadata15 = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_SASA"}).text
    borsadata16 = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_ODAS"}).text
    borsadata17 = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_MGROS"}).text
    borsadata18 = taramadegiskeni.find("li", {"id": "h_td_fiyat_id_TKNSA"}).text

    #BORSA TEMA:
    #Bunlar temada kullanabılecegım guzel renkler "light steel blue" / "spring green" /
    borsa_pencere_rengi = "white"
    borsa_pencere_baslik_rengi = "white"
    borsa_pencere_baslik_yazi_tipi = "arial 15 bold"
    borsa_hisse_isim_rengi = "white"
    borsa_hisse_isim_yazi_tipi = "arial 12 bold"
    borsa_fiyat_rengi = "white"
    borsa_fiyat_yazi_tipi = "arial 12 bold"



    pencere_borsa = Toplevel()  # pencere_doviz oluşturdum
    pencere_borsa.geometry("854x480")  # bu pencerenin boyutlarını ayarladım
    pencere_borsa.resizable(False, False)  # borsa penceremizin boyutlarını kilitledik
    pencere_borsa.title("Borsa")  # pencere_doviz başlığımız
    pencere_borsa.iconbitmap(r"resimler/bitcoin_icon.ico")
    pencere_borsa.configure(background=borsa_pencere_rengi)  # pencere_doviz rengimiz

    borsa_cerceve_resmi = tk.PhotoImage(file=r"resimler\borsa_arkaplan_resmi.png")
    pencere_arkaplan = tk.Label(pencere_borsa, image=borsa_cerceve_resmi)
    pencere_arkaplan.place(x=0, y=0, relwidth=1, relheight=1)
    pencere_arkaplan.pack()



    anadoluefes = tk.Label(pencere_borsa, text="ANADOLU EFES (AEFES)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    anadoluefes.pack()  # frame oluşturduk
    anadoluefes.place(x=30, y=75)
    anadoluefes_degeri = tk.Label(pencere_borsa, text=borsadata, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    anadoluefes_degeri.pack()
    anadoluefes_degeri.place(x=30, y=95)

    aselsan = tk.Label(pencere_borsa, text="ASELSAN (ASELS)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    aselsan.pack()
    aselsan.place(x=300, y=75)
    aselsan_degeri = tk.Label(pencere_borsa, text=borsadata1, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    aselsan_degeri.pack()
    aselsan_degeri.place(x=300, y=95)

    akbank = tk.Label(pencere_borsa, text="AKBANK (AKBNK)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    akbank.pack()
    akbank.place(x=570, y=75)
    akbank_degeri = tk.Label(pencere_borsa, text=borsadata2, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    akbank_degeri.pack()
    akbank_degeri.place(x=570, y=95)

    sekerbank = tk.Label(pencere_borsa, text="SEKERBANK (SKBNK)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    sekerbank.pack()
    sekerbank.place(x=30, y=130)
    sekerbank_degeri = tk.Label(pencere_borsa, text=borsadata3, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    sekerbank_degeri.pack()
    sekerbank_degeri.place(x=30, y=150)

    sisecam = tk.Label(pencere_borsa, text="SİSE CAM (SISE)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    sisecam.pack()
    sisecam.place(x=300, y=130)
    sisecam_degeri = tk.Label(pencere_borsa, text=borsadata4, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    sisecam_degeri.pack()
    sisecam_degeri.place(x=300, y=150)

    thy = tk.Label(pencere_borsa, text="TURK HAVA YOLLARI (THYAO)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    thy.pack()
    thy.place(x=570, y=130)
    thy_degeri = tk.Label(pencere_borsa, text=borsadata5, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    thy_degeri.pack()
    thy_degeri.place(x=570, y=150)

    vestel = tk.Label(pencere_borsa, text="VESTEL (VESTL)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    vestel.pack()  # frame oluşturduk
    vestel.place(x=30, y=185)
    vestel_degeri = tk.Label(pencere_borsa, text=borsadata6, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    vestel_degeri.pack()
    vestel_degeri.place(x=30, y=205)

    ulker = tk.Label(pencere_borsa, text="ULKER BISKUVI (ULKER)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    ulker.pack()
    ulker.place(x=300, y=185)
    ulker_degeri = tk.Label(pencere_borsa, text=borsadata7, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    ulker_degeri.pack()
    ulker_degeri.place(x=300, y=205)

    aygaz = tk.Label(pencere_borsa, text="AYGAZ (AYGAZ)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    aygaz.pack()
    aygaz.place(x=570, y=185)
    aygaz_degeri = tk.Label(pencere_borsa, text=borsadata8, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    aygaz_degeri.pack()
    aygaz_degeri.place(x=570, y=205)

    vestel = tk.Label(pencere_borsa, text="ALARKO GMYAO (ALGYO)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    vestel.pack()
    vestel.place(x=30, y=240)
    vestel_degeri = tk.Label(pencere_borsa, text=borsadata9, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    vestel_degeri.pack()
    vestel_degeri.place(x=30, y=260)

    aksaenerji = tk.Label(pencere_borsa, text="AKSA ENERJİ (AKSEN)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    aksaenerji.pack()
    aksaenerji.place(x=30, y=240)
    aksaenerji_degeri = tk.Label(pencere_borsa, text=borsadata10, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    aksaenerji_degeri.pack()
    aksaenerji_degeri.place(x=30, y=260)

    afyon = tk.Label(pencere_borsa, text="AFYON CIMENTO (AFYON)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    afyon.pack()
    afyon.place(x=300, y=240)
    afyon_degeri = tk.Label(pencere_borsa, text=borsadata11, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    afyon_degeri.pack()
    afyon_degeri.place(x=300, y=260)

    kola = tk.Label(pencere_borsa, text="COCA COLA ICECEK (CCOLA)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    kola.pack()
    kola.place(x=570, y=240)
    kola_degeri = tk.Label(pencere_borsa, text=borsadata12, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    kola_degeri.pack()
    kola_degeri.place(x=570, y=260)

    pegasus = tk.Label(pencere_borsa, text="PEGASUS (PGSUS)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    pegasus.pack()
    pegasus.place(x=30, y=295)
    pegasus_degeri = tk.Label(pencere_borsa, text=borsadata13, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    pegasus_degeri.pack()
    pegasus_degeri.place(x=30, y=315)

    sabanci = tk.Label(pencere_borsa, text="SABANCI HOLDING (SAHOL)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    sabanci.pack()
    sabanci.place(x=300, y=295)
    sabanci_degeri = tk.Label(pencere_borsa, text=borsadata14, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    sabanci_degeri.pack()
    sabanci_degeri.place(x=300, y=315)

    sasapol = tk.Label(pencere_borsa, text="SASA POLYESTER (SASA)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    sasapol.pack()
    sasapol.place(x=570, y=295)
    sasapol_degeri = tk.Label(pencere_borsa, text=borsadata15, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    sasapol_degeri.pack()
    sasapol_degeri.place(x=570, y=315)

    odaselektrik = tk.Label(pencere_borsa, text="ODAS ELEKTRIK (ODAS)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    odaselektrik.pack()
    odaselektrik.place(x=30, y=350)
    odaselektrik_degeri = tk.Label(pencere_borsa, text=borsadata16, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    odaselektrik_degeri.pack()
    odaselektrik_degeri.place(x=30, y=370)

    migrosticaret = tk.Label(pencere_borsa, text="MIGROS TICARET (MGROS)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    migrosticaret.pack()
    migrosticaret.place(x=300, y=350)
    migrosticaret_degeri = tk.Label(pencere_borsa, text=borsadata17, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    migrosticaret_degeri.pack()
    migrosticaret_degeri.place(x=300, y=370)

    teknosa = tk.Label(pencere_borsa, text="TEKNOSA TICARET (TKNSA)", font=borsa_hisse_isim_yazi_tipi, bg=borsa_hisse_isim_rengi)
    teknosa.pack()
    teknosa.place(x=570, y=350)
    teknosa_degeri = tk.Label(pencere_borsa, text=borsadata18, font=borsa_fiyat_yazi_tipi, bg=borsa_fiyat_rengi)
    teknosa_degeri.pack()
    teknosa_degeri.place(x=570, y=370)

    pencere_borsa.mainloop()


def haberbutonu_click():
    import feedparser
    import webview

    def default_color_button():
        btn_son_dakika.configure(bg="white")
        btn_dunya_haberleri.configure(bg="white")
        btn_ekonomi_haberleri.configure(bg="white")
        btn_saglık_haberleri.configure(bg="white")
        btn_spor_haberleri.configure(bg="white")
        btn_gundem.configure(bg="white")
        btn_egıtım.configure(bg="white")

    def clear_frame():
        for widget in fr_haberler.winfo_children():
            widget.destroy()

    def open_url(event):
        webview.create_window(event.widget.cget("text"), event.widget.cget("text"))
        webview.start()

    def son_dakika_command():
        default_color_button()
        btn_son_dakika.configure(bg="blue")
        clear_frame()
        url = "https://www.ntv.com.tr/son-dakika.rss"
        haberler = feedparser.parse(url)
        for haber in haberler.entries:
            Label(fr_haberler, text=haber.title, anchor='w', font=('Helveticabold', 14)).pack(side=TOP, fill="x")
            lbl_link = Label(fr_haberler, text=haber.link, anchor='w', font=('Helveticabold', 14), fg="blue",cursor="hand2")
            lbl_link.pack(side=TOP, fill="x")
            lbl_link.bind("<Button-1>", open_url)
            Label(fr_haberler, text="-", anchor='c', bg="light steel blue", cursor="hand2").pack(side=TOP, fill="x")

    def dunya_haberleri_command():
        default_color_button()
        btn_dunya_haberleri.configure(bg="red")
        clear_frame()
        url = "https://www.ntv.com.tr/dunya.rss"
        haberler = feedparser.parse(url)
        for haber in haberler.entries:
            Label(fr_haberler, text=haber.title, anchor='w', font=('Helveticabold', 14)).pack(side=TOP, fill="x")
            lbl_link = Label(fr_haberler, text=haber.link, anchor='w', font=('Helveticabold', 14), fg="blue",cursor="hand2")
            lbl_link.pack(side=TOP, fill="x")
            lbl_link.bind("<Button-1>", open_url)
            Label(fr_haberler, text="-", anchor='c', bg="light steel blue", cursor="hand2").pack(side=TOP, fill="x")


    def ekonomi_haberleri_command():
        default_color_button()
        btn_ekonomi_haberleri.configure(bg="orange")
        clear_frame()
        url = "https://www.ntv.com.tr/ekonomi.rss"
        haberler = feedparser.parse(url)
        for haber in haberler.entries:
            Label(fr_haberler, text=haber.title, anchor='w', font=('Helveticabold', 14)).pack(side=TOP, fill="x")
            lbl_link = Label(fr_haberler, text=haber.link, anchor='w', font=('Helveticabold', 14), fg="blue",cursor="hand2")
            lbl_link.pack(side=TOP, fill="x")
            lbl_link.bind("<Button-1>", open_url)
            Label(fr_haberler, text="-", anchor='c', bg="light steel blue", cursor="hand2").pack(side=TOP, fill="x")

    def saglik_haberleri_command():
        default_color_button()
        btn_saglık_haberleri.configure(bg="purple")
        clear_frame()
        url = "https://www.ntv.com.tr/saglik.rss"
        haberler = feedparser.parse(url)
        for haber in haberler.entries:
            Label(fr_haberler, text=haber.title, anchor='w', font=('Helveticabold', 14)).pack(side=TOP, fill="x")
            lbl_link = Label(fr_haberler, text=haber.link, anchor='w', font=('Helveticabold', 14), fg="blue",cursor="hand2")
            lbl_link.pack(side=TOP, fill="x")
            lbl_link.bind("<Button-1>", open_url)
            Label(fr_haberler, text="-", anchor='c', bg="light steel blue", cursor="hand2").pack(side=TOP, fill="x")

    def spor_haberleri_command():
        default_color_button()
        btn_spor_haberleri.configure(bg="brown")
        clear_frame()
        url = "https://www.ntv.com.tr/spor.rss"
        haberler = feedparser.parse(url)
        for haber in haberler.entries:
            Label(fr_haberler, text=haber.title, anchor='w', font=('Helveticabold', 14)).pack(side=TOP, fill="x")
            lbl_link = Label(fr_haberler, text=haber.link, anchor='w', font=('Helveticabold', 14), fg="blue",cursor="hand2")
            lbl_link.pack(side=TOP, fill="x")
            lbl_link.bind("<Button-1>", open_url)
            Label(fr_haberler, text="-", anchor='c', bg="light steel blue", cursor="hand2").pack(side=TOP, fill="x")

    def gundem_command():
        default_color_button()
        btn_gundem.configure(bg="yellow")
        clear_frame()
        url = "https://www.ntv.com.tr/gundem.rss"
        haberler = feedparser.parse(url)
        for haber in haberler.entries:
            Label(fr_haberler, text=haber.title, anchor='w', font=('Helveticabold', 14)).pack(side=TOP, fill="x")
            lbl_link = Label(fr_haberler, text=haber.link, anchor='w', font=('Helveticabold', 14), fg="blue",cursor="hand2")
            lbl_link.pack(side=TOP, fill="x")
            lbl_link.bind("<Button-1>", open_url)
            Label(fr_haberler, text="-", anchor='c', bg="light steel blue", cursor="hand2").pack(side=TOP, fill="x")

    def egitim_command():
        default_color_button()
        btn_egıtım.configure(bg="green")
        clear_frame()
        url = "https://www.ntv.com.tr/egitim.rss"
        haberler = feedparser.parse(url)
        for haber in haberler.entries:
            Label(fr_haberler, text=haber.title, anchor='w', font=('Helveticabold', 14)).pack(side=TOP, fill="x")
            lbl_link = Label(fr_haberler, text=haber.link, anchor='w', font=('Helveticabold', 14), fg="blue",cursor="hand2")
            lbl_link.pack(side=TOP, fill="x")
            lbl_link.bind("<Button-1>", open_url)
            Label(fr_haberler, text="-", anchor='c', bg="light steel blue", cursor="hand2").pack(side=TOP, fill="x")

    window = Tk()
    window.title("Haber Programı  ")
    window.geometry("1000x600")
    window.configure(bg="light steel blue")
    window.iconbitmap(r"resimler/haber_icon.ico")

    fr_haberler = Frame(window, height=600)
    fr_buttons = Frame(window, relief=RAISED, bg="black", bd=20)

    btn_son_dakika = Button(fr_buttons, text="Son Dakika", font=('Helveticabold', 14), bg="white",command=son_dakika_command)
    btn_dunya_haberleri = Button(fr_buttons, text="Dünya Haberleri", font=('Helveticabold', 14), bg="white",command=dunya_haberleri_command)
    btn_ekonomi_haberleri = Button(fr_buttons, text="Ekonomi haberleri", font=('Helveticabold', 14), bg="white",command=ekonomi_haberleri_command)
    btn_saglık_haberleri = Button(fr_buttons, text="Sağlık Haberleri", font=('Helveticabold', 14), bg="white",command=saglik_haberleri_command)
    btn_spor_haberleri = Button(fr_buttons, text="Spor Haberleri", font=('Helveticabold', 14), bg="white",command=spor_haberleri_command)
    btn_gundem = Button(fr_buttons, text="Gündem", font=('Helveticabold', 14), bg="white", command=gundem_command)
    btn_egıtım = Button(fr_buttons, text="Eğitim", font=('Helveticabold', 14), bg="white", command=egitim_command)

    btn_son_dakika.grid(row=0, column=0, sticky="ew", padx=4, pady=8)
    btn_dunya_haberleri.grid(row=2, column=0, sticky="ew", padx=4, pady=8)
    btn_ekonomi_haberleri.grid(row=5, column=0, sticky="ew", padx=4, pady=8)
    btn_saglık_haberleri.grid(row=3, column=0, sticky="ew", padx=4, pady=8)
    btn_spor_haberleri.grid(row=4, column=0, sticky="ew", padx=4, pady=8)
    btn_gundem.grid(row=1, column=0, sticky="ew", padx=4, pady=8)
    btn_egıtım.grid(row=6, column=0, sticky="ew", padx=4, pady=8)

    fr_buttons.grid(row=0, column=0, sticky="ns")
    fr_haberler.grid(row=0, column=1, sticky="nsew")

    window.mainloop()


def pomodorobutonu_click():
    def start_pomodoro():
        minutes = int(work_entry.get())  # çalışma oturumunun başlatılması
        countdown(minutes * 60)  # Çalışma süresi gir

    def start_break():
        countdown(5 * 60)  # 5 dakikalık mola süresi

    def start_long_break():  # 15 dakikalık mola süresi
        countdown(15 * 60)

    def countdown(seconds):  # fonksiyonun geri sayımını yönetir
        global is_running
        is_running = True  # doğru olduğu ve seconds değişkeni sıfır olmadığı sürece çalışmaya devam eder. değişkeni başlatır
        while seconds and is_running:  # çalışır durumda kalmasını sağlar
            minute, second = divmod(seconds,60)  # zamanlayıcıda görüntülenmek üzere kullanılan toplam saniyeleri dakikaya dönüştürür
            zamanlayici_cerceve.config(text=f'{minute:02d}:{second:02d}')  # görüntülenen metni güncellemek için kullanılır
            root.update()
            time.sleep(1)
            seconds -= 1

    def stop_continue_timer():
        global is_running
        if is_running:
            is_running = False
            stop_continue_button.config(text="Devam Et")
        else:
            minutes = int(zamanlayici_cerceve["text"].split(":")[0])  # zamanın dakika kısmını belirtir.
            seconds = int(zamanlayici_cerceve["text"].split(":")[1])
            total_seconds = minutes * 60 + seconds  # toplam süreyi saniye cinsinden açıklar
            countdown(total_seconds)
            stop_continue_button.config(text="Çalışmayı Durdur")

    def add_task():
        task = task_entry.get()
        not_listesi.insert(tk.END, task)  # öğe ekleyebilmek için kullanılır
        task_entry.delete(0, tk.END)  # temizleme

    def delete_task():
        selected_task = not_listesi.curselection()  # seçilen öğe dizinini alır
        not_listesi.delete(selected_task)

    root = tk.Toplevel()
    root.title("Pomodoro Uygulaması")
    root.iconbitmap(r"resimler\pomodoro_icon.ico")
    root.geometry("550x650")
    root.resizable(False, False)

    # canvas=tk.Canvas(root,width=450, height=700,bg="white")
    # canvas.pack()
    # background_image=tk.PhotoImage(file="ağaç.jpg")
    # canvas.create_image(0,0,anchor=tk.NW,image=background_image)

    # Arka Plan Resmi
    # background_image=ImageTk.PhotoImage(Image.open("ağaç.jpg"))
    # background_label=tk.Label(root,image=background_image)
    # background_label.place(x=0, y=0, relwidth=1, relheight=1)

    pomodoro_arkaplan_resmi = ImageTk.PhotoImage(file=r"resimler/agac.png")
    pomodoro_arkaplan_cerceve = tk.Label(root, image=pomodoro_arkaplan_resmi, bg="light steel blue")
    pomodoro_arkaplan_resmi.image = pomodoro_arkaplan_resmi
    pomodoro_arkaplan_cerceve.place(x=0, y=0, relwidth=1, relheight=1)

    timer_frame = tk.Frame(root, background="light steel blue")
    timer_frame.pack(pady=40)
    timer_frame.configure(relief=tk.SOLID, bd=0)

    zamanlayici_cerceve = tk.Label(timer_frame, font=('Arial', 48), text='00:00', bg="white")
    zamanlayici_cerceve.pack()

    work_frame = tk.Frame(root)
    work_frame.pack(pady=10)

    work_label = tk.Label(work_frame, text="Çalışma Süresini Giriniz: ")
    work_label.pack(side=tk.LEFT)

    work_entry = tk.Entry(work_frame, width=10)
    work_entry.pack(side=tk.LEFT)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    start_button = tk.Button(button_frame, text="Çalışmaya Başla", foreground="white", background="red",font="Times 12 bold", command=start_pomodoro)
    start_button.pack(side=tk.LEFT, padx=0)

    stop_continue_button = tk.Button(button_frame, text="Çalışmayı Durdur", foreground="white", background="red",font="Times 12 bold", command=stop_continue_timer)
    stop_continue_button.pack(side=tk.LEFT, padx=0)

    break_frame = tk.Frame(root)
    break_frame.pack(pady=0)

    break_button = tk.Button(break_frame, text="Kısa Mola Vermek İçin Tıkla", foreground="white", background="green",font="Times 12 bold", command=start_break)
    break_button.pack(side=tk.LEFT, padx=0)

    long_break_button = tk.Button(break_frame, text="Uzun Mola Vermek İçin Tıkla", foreground="white",background="green", font="Times 12 bold", command=start_long_break)
    long_break_button.pack(side=tk.LEFT, padx=0)

    task_frame = tk.Frame(root)
    task_frame.pack(pady=10)

    task_label = tk.Label(task_frame, text="NOTLAR: ", font="Times 20 bold")
    task_label.pack()

    not_listesi = tk.Listbox(task_frame, width=50)
    not_listesi.pack(pady=10)

    task_entry = tk.Entry(task_frame, width=35)
    task_entry.pack()

    button_frame2 = tk.Frame(root)
    button_frame2.pack(pady=10)

    add_button = tk.Button(button_frame2, text="Ekle", font="Times 12 bold", foreground="white", background="#2488FF",command=add_task)
    add_button.pack(side=tk.LEFT, padx=0)

    delete_button = tk.Button(button_frame2, text="Sil", font="Times 12 bold", foreground="white", background="#2488FF",command=delete_task)
    delete_button.pack(side=tk.LEFT, padx=0)

def open_url():
    import webbrowser
    # Tarayıcıyı açmak, belirli bir URL'yi tarayıcıda göstermek için bu kutuphaneyı kullanıyoruz
    webbrowser.open("https://www.youtube.com/watch?v=GyyvKNsXig4") # url'yi görüntülememizi sağlar


def hava_durumu_click():
    import tkinter


    hava_durumu_url = "http://api.openweathermap.org/data/2.5/weather"
    api_numarasi = "48fa1272d9f1a6912367ba9b34ede792"
    hava_durumu_icon_url = "https://openweathermap.org/img/wn/{}@2x.png"

    # TEMALAR

    havadurumu_font = "Arial Black bold"
    hava_durumu_icerik_arkaplan_rengi = "light blue"

    # json= metin belgesi biçimi (txt,docx gibi)

    def alinan_sehir(sehir):
        parametrelerimiz = {'q': sehir, 'appid': api_numarasi, 'lang': 'TR'}  # parametrelerimiz için bir sözlük oluşturduk
        parametre_verilerimiz = requests.get(hava_durumu_url,params=parametrelerimiz).json()  # parametrelerimiz üzerinden sitemizden verilerimizi json biçiminde çekiyoruz (requests.get = istekte bulunmak)
        # json biçiminde almamızın sebebi alınan değerlerin parçalanabilmesii için

        if parametre_verilerimiz:
            sehir = parametre_verilerimiz['name'].capitalize()  # şehir ismi verisini capitalize yani büyük harf parametresi ile sehir degıskenıne atıyoruz
            ulke = parametre_verilerimiz['sys']['country']  # data degıskenımız uzerınden sys sınıfından country uzerındekı ülke billgisini ulke degıskenıne atıyoruz
            hava_durumu_sicaklik = int(parametre_verilerimiz['main']['temp'] - 273.15)  # Main sınıfından temp değerindeki Kelvin verisini Celcius değerine çeviriyoruz hava_durumu_sicaklik degıskenıne atıyoruz
            hava_durumu_icon = parametre_verilerimiz['weather'][0]['icon']  # weather sınıfından 0'ıncı index üzerinden icon yani hava durumu resimlerimizi hava_durumu_icon değişkenine atıyoruz
            hava_durumu_aciklama = parametre_verilerimiz['weather'][0]['description']  # weather sınıfından 0'ıncı index üzerinden description yani hava durumu açıklamamızı hava_durumu_aciklama değişkenine atıyoruz
            return (sehir, ulke, hava_durumu_sicaklik, hava_durumu_icon,hava_durumu_aciklama)  # 'return'fonksiyonun içerisinde ki değeri çağırmamızı sağlayan komuttur.

    def hava_durumu_programi():

        hava_durumu = alinan_sehir(girilen_sehir.get()) # alinan sehir fonksiyonumuzu metin barımızda almış olduğumuz şehir bilgisi ile çalıştırıyoruz

        if hava_durumu:
            sehir_ismi_ulke_cerceve['text'] = (hava_durumu[0], hava_durumu[1])  # alinan_sehir fonksiyonumuzdan 0'ıncı ve 1'inci indexteki verileri (şehir,ülke) çerçevemize ekliyoruz
            sicaklik_cerceve['text'] = '{}°C'.format(hava_durumu[2])  # alinan_sehir fonksiyonumuzdan 2'inci indexteki veriyi (sıcaklık) çerçevemize ekliyoruz format parametresini kullanarak
            hava_durumu_aciklama_cerceve['text'] = hava_durumu[4]  # alinan_sehir fonksiyonumuzdan 4'üncü indexteki veriyi (hava durumu bilgisini) çerçevemize ekliyoruz
            hava_durumu_iconlari = ImageTk.PhotoImage(Image.open(requests.get(hava_durumu_icon_url.format(hava_durumu[3]), stream=TRUE).raw))
            # hava durumu iconlaırmızı ; hava durumu icon urlimiz uzerinden alıyoruz stream true sürekli görüntülememizi sağlıyor raw ise resim biçimimiz (png, jpeg, raw resim biçimleridir)
            hava_durumu_ikonlari_cerceve.configure(image=hava_durumu_iconlari, font=(havadurumu_font, 16)) # hava durumu ikonlaırımzı için bir çerçeve olusturudk ve iconlarımızı çerçevemizde kullandık
            hava_durumu_ikonlari_cerceve.image = hava_durumu_iconlari # İkonlarımızın görselini çerçeveye atanır. Bu atama, çerçevenin görüntüsünü veya içeriğini güncellemek için kullanılabilir.

    hava_durumu_programi_ana_pencere = Toplevel() # Toplevel() ile tkinter kutuphanemizi kullanarak bir pencere oluşturuyoruz
    hava_durumu_programi_ana_pencere.geometry("640x550") # pencere boyutumuz
    hava_durumu_programi_ana_pencere.title("Hava Durumu") #pencere başlığımız
    hava_durumu_programi_ana_pencere.iconbitmap(r"resimler/bulut_icon.ico") #penceremize simge ekledık # pencere ikonumuz
    hava_durumu_arkaplan_resmi = tkinter.PhotoImage(file=r"resimler\havadurumuarkaplan_resmi.png") #pencere arkaplan resmimimizin değişkeni
    hava_durumu_programi_ana_cerceve = tkinter.Label(hava_durumu_programi_ana_pencere, image=hava_durumu_arkaplan_resmi)  # pencere arkaplan resmimizi arkaplan çerçevemizde oluşturup goruntuluyoruz
    hava_durumu_programi_ana_cerceve.place(x=0, y=0)

    hava_durumu_programi_ana_pencere.resizable(False, False)  # pencere boyutumuzu kilitliyoruz
    girilen_sehir = Entry(hava_durumu_programi_ana_pencere, justify='center', font=(havadurumu_font, 16), bg="white") # kullanıcıdan şehir girdisi almak için kullandığımız metin barı (widget çeşidi)
    girilen_sehir.pack(fill=BOTH, ipady=5, padx=150, pady=10) # metin barımızın içinin doluluğunun x ve y biçiminde şeklinde ayarlıyoruz
    # ipady değeri metin barımızın içine yazılan yazının yükseklikte ne kadar boşluk bırakılacağını belirtir
    # padx değeri metin barımızın penceremizde sağ ve soldan ne kadar boşlukt mesafede kalacağını belirtir
    # pady değeri metin barımızın üst ve alt kısımdan ne kadar boşluk mesafede kalacağını belirtir

    hava_durumu_arama_butonu = Button(hava_durumu_programi_ana_pencere, text="Arama", font=(havadurumu_font, 16),command=hava_durumu_programi, bg="light grey")
    # hava_durumu_programi fonksiyonumuzu çalıştıracak bir buton oluşturuyoruz
    hava_durumu_arama_butonu.pack(fill=BOTH, ipady=5, padx=250)

    hava_durumu_programi_ana_pencere.bind("<Return>", lambda event: hava_durumu_programi())
    # return yani enter tuşuna basıldığında hava_durumu_programi fonksiyonunu çalıştırır
    # lambda bir anonim (isimsiz) fonksiyon oluşturmak için kullanılan bir Python ifadesidir. Genellikle kısa ve tek seferlik kullanımlar için tercih edilir.
    # bind parametresini bir tuş karşılıgında eylem gerceklestırmek ıcın kullanıyoruz

    hava_durumu_ikonlari_cerceve = Label(hava_durumu_programi_ana_pencere, bg=hava_durumu_icerik_arkaplan_rengi)
    hava_durumu_ikonlari_cerceve.pack()

    sehir_ismi_ulke_cerceve = Label(hava_durumu_programi_ana_pencere, font=(havadurumu_font, 30),bg=hava_durumu_icerik_arkaplan_rengi)
    sehir_ismi_ulke_cerceve.pack()

    sicaklik_cerceve = Label(hava_durumu_programi_ana_pencere, font=(havadurumu_font, 30, "bold"),bg=hava_durumu_icerik_arkaplan_rengi)
    sicaklik_cerceve.pack()

    hava_durumu_aciklama_cerceve = Label(hava_durumu_programi_ana_pencere, font=(havadurumu_font, 25),bg=hava_durumu_icerik_arkaplan_rengi)
    hava_durumu_aciklama_cerceve.pack()

    yt_icon = ImageTk.PhotoImage(file=r"resimler/yt_logo.png")

    opsiyonel_butonu = tk.Button(hava_durumu_programi_ana_pencere ,text="Opsiyonel :)  ",font="arial 16 bold",command=open_url,image=yt_icon, compound=LEFT )
    opsiyonel_butonu.pack()
    opsiyonel_butonu.place(x=245,y=425)




    hava_durumu_programi_ana_pencere.mainloop()


def isimler_butonu_click():
    import tkinter as tk

    def update_text():
        current_name = names.pop(0)
        label.config(text=current_name)
        names.append(current_name)
        window.after(2000, update_text)

    window = tk.Tk()
    window.title("Yapımcılar")
    window.geometry("890x110")
    window.iconbitmap(r"resimler\kullanici_resmi.ico")
    window.resizable(False, False)

    window_background = tk.Label(window, bg="light steel blue")
    window_background.pack()
    window_background.place(x=0, y=0, relwidth=1, relheight=1)

    names = ["Yağız Murat ÇULLU", "Kerim Emre ÇOBAN", "İlaydanur GÜNAY", "Beyza FIRAT", "Ahmet ÇAKIRCAN"]

    label = tk.Label(window, text="", font="arial 70 bold", bg="light steel blue", fg="black")
    label.pack()

    update_text()
    window.mainloop()


def tarih_saat():
    zaman = datetime.datetime.now() # datetime modülünün içindeki datetime sınıfının now() adlı fonksiyonu, bize içindeki bulunduğumuz andaki tarih, saat ve zaman bilgilerini verir.
    tarih = zaman.strftime("%Y-%m-%d %H:%M:%S") #strftime() fonksiyonu, size tarih ve zaman bilgilerini ihtiyaçlarınız doğrultusunda biçimlendirme imkanı sunar.
    tarih_saat_cerceve.config(text=tarih)
    ana_pencere.after(1000, tarih_saat) # her saniye güncelle

    # %a:hafta gününün kısaltılmış adı
    # %A:hafta gününün tam adı
    # %b:ayın kısaltılmış adı
    # %B:ayın tam adı
    # %c:tam tarih, saat ve zaman bilgisi
    # %d:sayı değerli bir karakter dizisi olarak gün
    # %j:belli bir tarihin, yılın kaçıncı gününe denk geldiğini gösteren 1-366 arası bir sayı
    # %m:sayı değerli bir karakter dizisi olarak ay
    # %U:belli bir tarihin yılın kaçıncı haftasına geldiğini gösteren 0-53 arası bir sayı
    # %y:yılın son iki rakamı
    # %Y:yılın dört haneli tam hali
    # %x:tam tarih bilgisi
    # %X:tam saat bilgisi


if __name__ == '__main__':
    # shift+f10 = HIZLI ÇALIŞTIRMA KISAYOL TUŞU
    # ctrl+F = Arama yapmamızı saglayan kısayol tuşu
    # Ana pencereyi oluşturma

    ana_menu_buton_rengi = "light grey"

    ana_pencere = tk.Tk()
    ana_pencere.title("Hack Heroes İş Uygulaması")
    ana_pencere.geometry("854x480")
    ana_pencere.iconbitmap(r"resimler\ana_pencere_icon.ico")
    ana_pencere.resizable(False, False)  # çerçeve boyutunu kilitliyoruz
    arka_plan_resmi = tk.PhotoImage(file=r"resimler\pencereresmi.png")


    pencere_arkaplan_cerceve = tk.Label(ana_pencere, image=arka_plan_resmi)
    pencere_arkaplan_cerceve.place(x=0, y=0, relwidth=1, relheight=1)


    tarih_saat_cerceve = Label(ana_pencere, text="", fg="black", bg="white", font=("arial bold", 8))
    tarih_saat_cerceve.pack(side="bottom", anchor="center") # merkezde gostermek ıcın anchor=center dıyoruz
    tarih_saat()


    altin_resmi = PhotoImage(file=r'resimler\gold_icon.gif')  # döviz işlemi butonu ıcın bır resım kullandırttım
    kaltin_resmi = altin_resmi.subsample(2,2)  # bu resmı belirli oranda kuculttum (dovız ıslemı ıcın kullandıgım resmi)

    # Butonları oluşturma
    doviz_butonu = tk.Button(ana_pencere, text=" Döviz İşlemleri           ", command=dovizbutonu_click, image=kaltin_resmi, compound=LEFT, bg=ana_menu_buton_rengi)
    doviz_butonu.configure(border=5)
    doviz_butonu.pack()
    doviz_butonu.place(x=100, y=100)


    bitcoin_resmi = PhotoImage(file=r'resimler\bitcoin_icon.gif')  # borsa işlemi butonu ıcın bır resım kullandırttım
    kbitcoin_resmi = bitcoin_resmi.subsample(2, 2)  # bu resmı belirli oranda kuculttum (borsa ıslemı ıcın kullandıgım resmi)

    borsa_butonu = tk.Button(ana_pencere, text="  Borsa İşlemleri          ", command=borsabutonu_click,image=kbitcoin_resmi,compound=LEFT, bg=ana_menu_buton_rengi)
    borsa_butonu.configure(border=5)
    borsa_butonu.pack()
    borsa_butonu.place(x=600, y=100)

    gazete_resmi = PhotoImage(file=r'resimler\haber_icon.gif')  # borsa işlemi butonu ıcın bır resım kullandırttım
    kgazete_resmi = gazete_resmi.subsample(2, 2)  # bu resmı belirli oranda kuculttum (borsa ıslemı ıcın kullandıgım resmi)

    haber_butonu = tk.Button(ana_pencere, text="Gündemden Haberler", command=haberbutonu_click, image=kgazete_resmi,compound=LEFT,bg=ana_menu_buton_rengi)
    haber_butonu.configure(border=5,)
    haber_butonu.pack()
    haber_butonu.place(x=100, y=300)

    pomodoro_resmi = PhotoImage(file=r'resimler\pomodoro_icon.gif')  # hava durumu işlemi butonu ıcın bır resım kullandırttım
    kpomodoro_resmi = pomodoro_resmi.subsample(2,2)  # bu resmı belirli oranda kuculttum (borsa ıslemı ıcın kullandıgım resmi)

    pomodoro_butonu = tk.Button(ana_pencere, text=" Pomodoro                  ", command=pomodorobutonu_click,image=kpomodoro_resmi,compound=LEFT, bg=ana_menu_buton_rengi)
    pomodoro_butonu.configure(border=5)
    pomodoro_butonu.pack()
    pomodoro_butonu.place(x=600, y=300)


    bulut_resmi = PhotoImage(
        file=r'resimler\bulut_icon.gif')  # hava durumu işlemi butonu ıcın bır resım kullandırttım
    kbulut_resmi = bulut_resmi.subsample(2,2)  # bu resmı belirli oranda kuculttum (borsa ıslemı ıcın kullandıgım resmi)

    hava_durumu_butonu = tk.Button(ana_pencere, text=" Hava Durumu            ", command=hava_durumu_click, image=kbulut_resmi,compound=LEFT,bg=ana_menu_buton_rengi)
    hava_durumu_butonu.configure(border=5)
    hava_durumu_butonu.pack()
    hava_durumu_butonu.place(x=350, y=100)



    isimler_buton_resmi = PhotoImage( file=r'resimler\kullanici_resmi.gif')
    isimler_butonu = tk.Button(ana_pencere, text=" Emeği Geçenler           ", command=isimler_butonu_click,image=isimler_buton_resmi, compound=LEFT, bg=ana_menu_buton_rengi)
    isimler_butonu.configure(border=5)
    isimler_butonu.pack()
    isimler_butonu.place(x=350, y=300)
    # Pencereyi çalıştırma
    ana_pencere.mainloop()