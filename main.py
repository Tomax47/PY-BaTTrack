import time
import urllib3
import json
from colorama import *

Try = 3
line = (Fore.GREEN+"________________________________________________________________")
skey = (Style.BRIGHT+Fore.GREEN+"$ ")
while True:

    usn = (Fore.YELLOW+"USERNAME : ")
    passwd = (Fore.YELLOW+"PASSCODE : ")
    username = input (usn+Fore.BLACK+"")
    passcode = input (passwd+Fore.BLACK+"")
    user_name = "bat"
    pass_code = "47"

    if (passcode == pass_code) and (username == user_name) :
        print(skey+"Tool is running....")
        for i in range(10,0,-1):
            print(".")
            time.sleep(1)
        while True:
            print (line)
            print(" ")
            command = input (skey+Fore.YELLOW+" ")
            if command == "bat -t":
                print (" ")
                ip = input ("put the targeted ip address : ")
                http = urllib3.PoolManager()
                res = http.request("GET","http://ip-api.com/json/"+ip)
                data = json.loads(res.data)

                if (len(ip)==0):
                    print (Fore.RED+"STATUS : FAIL")

                elif (data['status'] == "success") :
                    print("")
                    print (Fore.GREEN+"STATUS : "+Fore.GREEN+data['status'])
                    print("")
                    print(Fore.YELLOW + "COUNTRY : " + Fore.CYAN + data['country'])
                    print(Fore.YELLOW + "COUNTRY-CODE : " + Fore.CYAN + data['countryCode'])
                    print(Fore.YELLOW + "REGION : " + Fore.CYAN + data['region'])
                    print(Fore.YELLOW + "REGION-NAME : " + Fore.CYAN + data['regionName'])
                    print(Fore.YELLOW + "CITY : " + Fore.CYAN + data['city'])
                    print(Fore.YELLOW + "ZIP : " + Fore.CYAN + data['zip'])
                    print(Fore.YELLOW + "LATITUDE : " + Fore.CYAN + str(data['lat']))
                    print(Fore.YELLOW + "LONGITUDE : " + Fore.CYAN + str(data['lon']))
                    print(Fore.YELLOW + "TIME-ZONE : " + Fore.CYAN + data['timezone'])
                    print(Fore.YELLOW + "ISP : " + Fore.CYAN + data['isp'])
                    print(Fore.YELLOW + "ORG : " + Fore.CYAN + data['org'])
                    print(Fore.YELLOW + "AS : " + Fore.CYAN + data['as'])
                    print("")

                else :
                    print (Fore.RED+"STATUS : FAIL")

            elif command == "bat -m":
                print(" ")
                http = urllib3.PoolManager()
                res = http.request("GET", "http://ip-api.com/json/")
                data = json.loads(res.data)

                if (data['status'] == "success"):
                    print("")
                    print(Fore.GREEN+"STATUS : " + Fore.GREEN + data['status'])
                    print("")
                    print(Fore.YELLOW + "Ip-Address : " + Fore.CYAN + data['query'])
                    print(Fore.YELLOW + "COUNTRY : " + Fore.CYAN + data['country'])
                    print(Fore.YELLOW + "COUNTRY-CODE : " + Fore.CYAN + data['countryCode'])
                    print(Fore.YELLOW + "REGION : " + Fore.CYAN + data['region'])
                    print(Fore.YELLOW + "REGION-NAME : " + Fore.CYAN + data['regionName'])
                    print(Fore.YELLOW + "CITY : " + Fore.CYAN + data['city'])
                    print(Fore.YELLOW + "ZIP : " + Fore.CYAN + data['zip'])
                    print(Fore.YELLOW + "LATITUDE : " + Fore.CYAN + str(data['lat']))
                    print(Fore.YELLOW + "LONGITUDE : " + Fore.CYAN + str(data['lon']))
                    print(Fore.YELLOW + "TIME-ZONE : " + Fore.CYAN + data['timezone'])
                    print(Fore.YELLOW + "ISP : " + Fore.CYAN + data['isp'])
                    print(Fore.YELLOW + "ORG : " + Fore.CYAN + data['org'])
                    print(Fore.YELLOW + "AS : " + Fore.CYAN + data['as'])
                    print("")

                else:
                    print(Fore.RED+Style.BRIGHT+ "STATUS : "+ data['status'])

            if command == "bat -passwd":

                passwd = (Fore.YELLOW + "PASSCODE : ")
                passcode = input(passwd + Fore.BLACK + "")
                pass_code = "47"

                if (passcode == pass_code):
                    print("")
                    new_pass = input (skey+Fore.YELLOW+"Enter the new passcode : ")
                    new_pass2 = input (skey+Fore.YELLOW+"Re-enter the passcode : ")
                    if new_pass == new_pass2:
                        print("")
                        pass_code = new_pass
                    else:
                        print("")
                        print(Fore.RED+"PASSCODES DON'T MATCH!")
                        print("")


            elif command == ("bat -h"):
                print("")
                print(Fore.MAGENTA+"To run any of the tool's commands type 'bat' followed by :")
                print("")
                print(Fore.YELLOW+"-t               to trace an IP-Address")
                print("-m               to trace your own IP-Address")

            else:
                print("")
                print(Fore.RED+"INVALID INPUT!")
                print("")

    else:
        Try = Try - 1

    if Try == 0:
        break
