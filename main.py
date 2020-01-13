import random
import webbrowser
import subprocess
import pyfiglet
import terminal_banner
a=pyfiglet.figlet_format("               J                  P                        T")
b=terminal_banner.Banner( a)
print("\033[1;32;40m",b)




print("\n\033[1;33;40mSelect one of the:\n")
#list1
list1={"1":"\033[1;33;40m1.Google","2":"2.Website You Wanna Open","3":"3.Payloads","4":"4.List Of Vulnerability" ,"5":"5.Bug Bounty Sites","6":"6.Search Videos On YouTube","7":"7.CTF-Sites","8":"8.Bug Bounty/Hacking Resources","9":"9.Pentesting/Hacking Tools"}
for key,value in list1.items():
    print(value)

print("\n\033[1;33;40mEnter one of the hai!!")
users=str(input("\n\033[1;33;40mWhat is your choice :\n>>"))

 #direct firefox open    
if users=="google" or users=="1" or users=="Goole" :

  
   

    subprocess.Popen(["/home/kiran/Documents/firefox/firefox" ,"www.google.com"])


#user input to open any sites  
if users=="site" or users=="2"or users=="url" :


    print("\033[1;32;40mWrite site url  fully haie\n")
    a=input()
    webbrowser.open(a)

#payloads

if users=="payloads" or users=="3" or users=="Payloads":
    print("Select one of the \n")
    #Pyalods of different ....
    list1={"1":"\033[1;32;40m1.XSS-Payloads","2":"\033[1;32;40m2.Command-injection"}#"3":"\033[1;32;40m3.RCE-payloads"
    for key,value in list1.items():
        print(value)
       
    input1=str(input("\n \033[1;33;40m  What is your choice :\n>>"))
    #xss payloads
    if input1==str("xss-payloads") or input1=="1" or input1==str("payloads") or input1==str("xsspayloads") or input1=="xss"or input1=="XSS-Payloads":
        
        print("Select one of the \n")
        #xss list
        list2={"1":"\033[1;32;40m1.direct-payloads","2":"\033[1;32;40m2.websites"}
        for key,value in list2.items():
            print(value)
        #xss direct payload in cmd portion
        print("\nenter one of the hai!!")
        input2=str(input("\n\033[1;33;40mWhat is your choice :\n"))
        if input2=="1" or input2=="payloads" or input2=="direct-payloads":
                f=open("xss-payloads.txt", "r")
                if f.mode == 'r':
                    contents =f.read()
                    print(contents)
        #list of xss websites 
        if input2=="2" or input2=="websites" or input2=="direct-web": 
                f1=open("xss-websites.txt", "r")    
                if f1.mode == 'r':
                    contents1 =f1.read()
                    print(contents1)


    #command injection

    if input1==str("cj") or input1=="2" or input1==str("command injection") or input1==str("command") or input1=="xss"or input1=="Command Injection":
        
        print("Select one of the \n")
        #command injection list
        list3={"1":"\033[1;32;40m1.direct-payloads","2":"\033[1;32;40m2.websites"}
        for key,value in list3.items():
            print(value)
        #command injection direct payload in cmd portion
        print("\nenter one of the hai!!")
        input3=str(input("\n\033[1;33;40mWhat is your choice :\n>>"))
        if input3=="1" or input3=="payloads" or input3=="direct-payloads":
                f=open("ci-payloads.txt", "r")
                if f.mode == 'r':
                    contents =f.read()
                    print(contents)
        #list of command injection websites 
        if input3=="2" or input3=="websites" or input3=="direct-web": 
                f1=open("ci-websites.txt", "r")    
                if f1.mode == 'r':
                    contents1 =f1.read()
                    print(contents1)




#List OF Vulnerability

if users=="4" or users=="List OF Vulnerability" or users=="list of vulnerability" or users=="vulerability":
    f=open("listofvuln.txt", "r")
    if f.mode == 'r':
        contents =f.read()
        print(contents)


#Bug Bounty Sites
if users=="5" or users=="Bug Bounty Sites" or users=="bug sites" or users=="bug bounty sites":
    f=open("bugsites.txt", "r")
    if f.mode == 'r':
        contents =f.read()
        print("\033[1;32;40m",contents)
    bug=input("\033[1;33;40m Wanna open this site?If yes,then type number according to each.\n>>")
    if bug=='1':
        webbrowser.open("https://www.hackerone.com/")
    if bug=='2':
        webbrowser.open("https://www.bugcrowd.com/")
    if bug=='3':
        webbrowser.open("https://safehats.com/")
    if bug=='4':
        webbrowser.open("https://www.intigriti.com/")
    if bug=='5':
        webbrowser.open("https://www.synack.com/")
    if bug=='6':
        webbrowser.open("https://www.yeswehack.com/")
    if bug=='7':
        webbrowser.open("https://cobalt.io/")   
    if bug=='8':
        webbrowser.open("https://www.zerocopter.com/")  
#searching videos on youtube
if users=="youtube" or users=="6"or users=="Youtube" or users=="YouTube"or users=="YOUTUBE" or users=="yt":
        user=input("What are you searching?\n>>")
        webbrowser.open_new_tab("https://www.youtube.com/results?search_query=" + user)


#CTF Sites
if users=="7" or users=="CTF Sites" or users=="ctf-sites" or users=="ctf" or users=="Ctf-Sites" or users=="CTF":
    f=open("ctf-sites.txt", "r")
    if f.mode == 'r':
        contents =f.read()
        print("\033[1;32;40m",contents)
        print(":\033[1;31;40m Most Recommend>>https://captf.com/practice-ctf/")
    bug=input("\033[1;33;40m Wanna open this site?If yes,then type number according to each.\n>>" )

    if bug=='1':
        webbrowser.open( "https://picoctf.com/")
    if bug=='2':
        webbrowser.open("https://overthewire.org/wargames/")
    if bug=='3':
        webbrowser.open("https://www.hackthebox.eu/")
    if bug=='4':
        webbrowser.open("https://ctf.hacker101.com/")
    if bug=='5':
        webbrowser.open("https://w3challs.com/")
    if bug=='6':
        webbrowser.open("http://hax.tor.hu/welcome/")
    if bug=='7':
        webbrowser.open("https://www.hackthissite.org/")   
    if bug=='8':
        webbrowser.open("https://www.vulnhub.com/") 
    if bug=='9':
        webbrowser.open("https://captf.com/practice-ctf/") 



        #CTF Sites
if users=="8" or users=="hacking" or users=="bug-bounty" or users=="resources" or users=="Bug Bounty/Hacking Resources":
    f=open("resources.txt", "r")
    if f.mode == 'r':
        contents =f.read()
        print("\033[1;32;40m",contents)
      
    bug=input("\033[1;33;40m Wanna open this site?If yes,then type number according to each.\n>>" )

    if bug=='1':
        webbrowser.open( "https://ctf101.org/")
    if bug=='2':
        webbrowser.open("hhttps://portswigger.net/web-security")
    if bug=='3':
        webbrowser.open("https://brutelogic.com.br/blog/")
    if bug=='4':
        webbrowser.open("https://medium.com/@ehsahil/getting-started-in-bug-bounty-7052da28445a")
    if bug=='5':
        webbrowser.open("https://www.shodan.io/?fbclid=IwAR3iNT-T2RkgH8Vb0BXOsNGvC7a63WB1Cm3Z0CQQxiOI08B12eW0jUBSz8M")
    if bug=='6':
        webbrowser.open("https://news.ycombinator.com/?fbclid=IwAR039sNf4pt8ObpohctSKRWCja2T34G_rE1sChjk23Y_2HA88NT-_aU5qbA")
    if bug=='7':
        webbrowser.open("https://www.cloudflare.com/learning/security/threats/owasp-top-10/")   
    if bug=='8':
        webbrowser.open("https://pentester.land/list-of-bug-bounty-writeups.html#bug-bounty-writeups-published-in-2019") 
    if bug=='9':
        webbrowser.open() 

if users=="9" or users=="tools" or users=="Pentesting/Hacking Tools" or users=="hacking tools" or users=="pentesting/hacking tools":
    f=open("tools.txt", "r")
    if f.mode == 'r':
        contents =f.read()
        print("\033[1;36;40m",contents)
      
