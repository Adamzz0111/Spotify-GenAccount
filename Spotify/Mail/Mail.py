import platform
import random
import string
import threading
import time
from os import system

import requests

if platform.system() == "Windows":  # checking OS
    title = "windows"
else:
    title = "linux"


def randomName(size=10, chars=string.ascii_letters + string.digits):
    return "".join(random.choice(chars) for i in range(size))


def randomPassword(size=14, chars=string.ascii_letters + string.digits):
    return "".join(random.choice(chars) for i in range(size))


global maxi
global created

created = 0
errors = 0


class proxy:
    def update(self):
        while True:

            data = ""
            urls = [
                "https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&ssl=yes"
            ]
            for url in urls:
                data += requests.get(url).text
                self.splited += data.split("\r\n")  # scraping and splitting proxies
            time.sleep(600)

    def get_proxy(self):
        random1 = random.choice(self.splited)  # choose a random proxie
        return random1

    def FormatProxy(self):
        proxyOutput = {"https": "socks4://" + self.get_proxy()}
        return proxyOutput

    def __init__(self):
        self.splited = []
        threading.Thread(target=self.update).start()
        time.sleep(3)


proxy1 = proxy()


def creator():
    global maxi
    global created
    global errors
    while maxi > created:
        if title == "windows":
            system(
                "title "
                + f""
            )

        s = requests.session()

        email = randomName()
        password = ("PandaLegit#1")

        data = {
            "displayname": "Panda is legit",
            "creation_point": "https://login.app.spotify.com?utm_source=spotify&utm_medium=desktop-win32&utm_campaign=organic",
            "birth_month": "12",
            "email": email + "@mail.com",
            "password": password,
            "creation_flow": "desktop",
            "platform": "desktop",
            "birth_year": "1991",
            "iagree": "1",
            "key": "4c7a36d5260abca4af282779720cf631",
            "birth_day": "19",
            "gender": "female",
            "password_repeat": password,
            "referrer": "",
        }

        try:

            r = s.post(
                "https://spclient.wg.spotify.com/signup/public/v1/account/",
                data=data,
                proxies=proxy1.FormatProxy(),
            )
            if '{"status":1,"' in r.text:
                open("Mail-hits.txt", "a+").write(email + "@mail.com:" + password + " Config by Panda.xyz \n")
                created += 1
                if title == "windows":
                    system(
                        "title "
                        + f"Cuentas Creadas : {created}/{maxi} Errors:{errors}"
                    )
            else:
                errors += 1
        except:
            pass


maxi = int(input("Cuantas cuentas quieres crear?\n"))

maxthreads = int(input("Cuantos hilos/ms ?\n"))
num = 0

while num < maxthreads:
    num += 1
    threading.Thread(target=creator).start()  # Start Checking Thread