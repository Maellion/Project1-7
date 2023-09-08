def loop1():
    wifi_str = input("Welke wifi wilt u gebruiken? [4G, 5G, Wifi open] ").lower()

    if wifi_str == "4g":
        print("U bent verbonden met 4G")

    elif wifi_str == "5g":
        print("U bent verbonden met 5G")

    elif wifi_str == "wifi open":
        print("U heeft voor de Wifi open gekozen, wij wijzen u erop dat de data door de eigenaar van dit netwerk is te lezen.")
        loop2()

    else:
        print("Kies een geldige optie")
        loop1()

def loop2():
    open_wifi_str = input("Weet U zeker dat u wilt verbinden met Wifi open? [Ja/Nee] ").lower()

    if open_wifi_str == "ja":
        print("U bent verbonden met Wifi open")

    elif open_wifi_str == "nee":
        print("U bent niet verbonden")

    else:
        print("Kies een geldige optie")
        loop2()

loop1()