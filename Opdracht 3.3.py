print("Welkom bij MacDonalds")

bedankt_hier_opeten = ("Bedankt voor uw bestelling en eet smakelijk in ons restaurant.")
bedankt_meenemen = ("bedankt voor uw bestelling, goede reis en eet smakelijk.")

waar_opeten = input("Wilt u uw eten hier opeten of meenemen?: ").lower()

if waar_opeten == "hier opeten":
    print("Hier Opeten")
    burgers_drankjes = input("Wilt u een burger of een drankje?: ").lower()
    if burgers_drankjes == "burger":
        print("burger")
        keuze_burgers = input("Welke burger wilt u hebben? [Hamburger, Cheese burger, Big Mac, Quarter Pounder]: ").lower()
        if keuze_burgers == "hamburger":
            print("Hamburger")
            print(bedankt_hier_opeten)
        elif keuze_burgers == "cheese burger":
            print("Cheese burger")
            print(bedankt_hier_opeten)
        elif keuze_burgers == "big mac":
            print("Big Mac")
            print(bedankt_hier_opeten)
        elif keuze_burgers == "quarter pounder":
            kaas = input("Wilt u met of zonder kaas?: ").lower()
            if kaas == "met":
                print("Quarter Pounder met kaas")
                print(bedankt_hier_opeten)
            elif kaas == "zonder":
                print("Quarter Pounder zonder kaas")
                print(bedankt_hier_opeten)
            else:
                print("Abort, unknown input")
        else:
            print("Abort, unknown input")



    elif burgers_drankjes == "drankje":
        print("drankje")
        warm_koud = input("Wilt u een warm of koud drankje? [Warm/Koud]: ").lower()
        if warm_koud == "warm":
            warme_drankje = input("Welk warm drankje wilt u? [Koffie, Cappucino, Chocolademelk]: ").lower()
            if warme_drankje == "koffie":
                print("Koffie")
                print(bedankt_hier_opeten)
            elif warme_drankje == "cappucino":
                print("Cappucino")
                print(bedankt_hier_opeten)
            elif warme_drankje == "chocolademelk":
                print("Chocolademelk")
                print(bedankt_hier_opeten)
            else:
                print("Abort, unknown input")
        elif warm_koud == "koud":
            koud_drankje = input("Welk koud drankje wilt u? [Coca Cola, Cola Zero, 7-UP, Fanta, Fristi]: ").lower()
            if koud_drankje == "coca cola":
                print("Coca Cola")
                print(bedankt_hier_opeten)
            elif koud_drankje == "cola zero":
                print("Cola Zero")
                print(bedankt_hier_opeten)
            elif koud_drankje == "7-up":
                print("7-up")
                print(bedankt_hier_opeten)
            elif koud_drankje == "fristi":
                print("Fristi")
                print(bedankt_hier_opeten)
            else:
                print("Abort, unknown input")
        else:
            print("Abort, unknown input")
    else:
        print("Abort, unknown input")








elif waar_opeten == "meenemen":
    print("meenemen")
    burgers_drankjes = input("Wilt u een burger of een drankje?: ").lower()
    if burgers_drankjes == "burger":
        print("burger")
        keuze_burgers = input(
            "Welke burger wilt u hebben? [Hamburger, Cheese burger, Big Mac, Quarter Pounder]: ").lower()
        if keuze_burgers == "hamburger":
            print("Hamburger")
            print(bedankt_meenemen)
        elif keuze_burgers == "cheese burger":
            print("Cheese burger")
            print(bedankt_meenemen)
        elif keuze_burgers == "big mac":
            print("Big Mac")
            print(bedankt_meenemen)
        elif keuze_burgers == "quarter pounder":
            kaas = input("Wilt u met of zonder kaas?: ").lower()
            if kaas == "met":
                print("Quarter Pounder met kaas")
                print(bedankt_meenemen)
            elif kaas == "zonder":
                print("Quarter Pounder zonder kaas")
                print(bedankt_meenemen)
            else:
                print("Abort, unknown input")
        else:
            print("Abort, unknown input")



    elif burgers_drankjes == "drankje":
        print("drankje")
        warm_koud = input("Wilt u een warm of koud drankje? [Warm/Koud]: ").lower()
        if warm_koud == "warm":
            warme_drankje = input("Welk warm drankje wilt u? [Koffie, Cappucino, Chocolademelk]: ").lower()
            if warme_drankje == "koffie":
                print("Koffie")
                print(bedankt_meenemen)
            elif warme_drankje == "cappucino":
                print("Cappucino")
                print(bedankt_meenemen)
            elif warme_drankje == "chocolademelk":
                print("Chocolademelk")
                print(bedankt_meenemen)
            else:
                print("Abort, unknown input")
        elif warm_koud == "koud":
            koud_drankje = input("Welk koud drankje wilt u? [Coca Cola, Cola Zero, 7-UP, Fanta, Fristi]: ").lower()
            if koud_drankje == "coca cola":
                print("Coca Cola")
                print(bedankt_meenemen)
            elif koud_drankje == "cola zero":
                print("Cola Zero")
                print(bedankt_meenemen)
            elif koud_drankje == "7-up":
                print("7-up")
                print(bedankt_meenemen)
            elif koud_drankje == "fristi":
                print("Fristi")
                print(bedankt_meenemen)
            else:
                print("Abort, unknown input")
        else:
            print("Abort, unknown input")
    else:
        print("Abort, unknown input")
else:
    print("Abort, unknown imput")



