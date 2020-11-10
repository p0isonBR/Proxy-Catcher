import re, os, time, requests

R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

os.system('git pull && clear')

print(f'''{C}
                            /+osyhhhhhhyys++/
                         +oydddhhhhyyhhhhdddhy+/
                      /+yddhyyyys.josue.syyhddhs/
                     +hddyyssssssssssssssssssyyhdds/
                   /sddhyyyyyyssssssssssssssyyyyyhmh+
                  /hmdhhddddddhhhyyyyyyhhhhdddddhhhddo
                 /hmmdhs+/ //+osyhhhhhhysso+////ohddmdo
                /hmmmy{B}.           `````          `{C}smddd+
                smddm/{B}     `````          `````   {C}mdhmh/
               +ddydm+{B}  -/osyyyys+.    ./syyyyso/-{C}mdydms
               ymhyhmh{B}.yyo/ -- +hdo  /dho -- /oyh.{C}ymdyymd/
              /dmyyymd{B}.  ``.-   ./   -/.-   .``  `{C}dmhsydmo
              smdysymd{B}   shdhyydy      sdyyhddy   {C}dmyyshmy
              dmysshmy{B}                            {C}smhssymd/
             /dmyssymd{B}                            {C}hmhsyymm/
             /dmyssyhms{B}                          /{C}mdysyymm/
             /dmyssyydm/{B}  sh       hh/     -hy  .{C}dmyssyymm/
              dmhssssydd/{B} -hdhysshdysdhssyhdd  -{C}hmhyssyymd/
              ymhssssyyddo{B}``. //+/.` ./+// -` /{C}ddhysssyhmh
              +mdysssssyhdh{B} `     `/+`      -{C}sddysssssydmo
               ymhysssssyyddh/{B}`   `dm.   ` {C}sddhysssssyhmh/
               /hmhysssssyyyhdds{B} ..dm . {C}ohddhyyssssyyhmd+
                /yddhyssssssyyhhddhddddddhyyssssssyydmh+
               /+sdmmdhhyyyysssyyyyyyyyyysssyyyyyhddmdyo+/
           /+shdddhhyhhddddddhhhhhhhhhhhhhhdddddddhyyhhdddyo/
         /shddhyyysssssyyyyhhhhhhhhhhhhhhhhhhyyyyyssssyyyhdddy+
        /hmhyyssssssssssssssssssssssssssssssssssssssssssssyyhddo
        /dmhyyyyyssssssssssssssssssssssssssssssssssssssyyyyyydms
         +yhddddddhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyhhhhhdddddddhs/
           //++oossyyhhhhhhhdddddddddddddddddhhhhhhyyssoo++///
                       ///////+++++++++++++//////
     ██████╗  ██████╗ ██╗███████╗ ██████╗ ███╗   ██╗██████╗ ██████╗
     ██╔══██╗██╔═══██╗██║██╔════╝██╔═══██╗████╗  ██║██╔══██╗██╔══██╗
     ██████╔╝██║   ██║██║███████╗██║   ██║██╔██╗ ██║██████╔╝██████╔╝
     ██╔═══╝ ██║   ██║██║╚════██║██║   ██║██║╚██╗██║██╔══██╗██╔══██╗
     ██║     ╚██████╔╝██║███████║╚██████╔╝██║ ╚████║██████╔╝██║  ██║
     ╚═╝      ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝
     {RT}{B}*t.me/p0isonBR*{RT}'''); time.sleep(3)

os.system('clear')

print(f'''{G}*By PoisonBR
{B}█████╗ █████╗  █████╗ ██╗  ██╗██╗   ██╗{C} ████╗ ████╗ ██████╗ ████╗██╗ ██╗█████╗█████╗ 
{B}██╔═██╗██╔═██╗██╔══██╗╚██╗██╔╝╚██╗ ██╔╝{C}██╔══╝██╔═██╗╚═██╔═╝██╔══╝██║ ██║██╔══╝██╔═██╗
{B}█████╔╝█████╔╝██║  ██║ ╚███╔╝  ╚████╔╝ {C}██║   ██████║  ██║  ██║   ██████║█████╗█████╔╝
{B}██╔══╝ ██╔═██╗██║  ██║ ██╔██╗   ╚██╔╝  {C}██║   ██╔═██║  ██║  ██║   ██╔═██║██╔══╝██╔═██╗
{B}██║    ██║ ██║╚█████╔╝██╔╝ ██╗   ██║   {C}╚████╗██║ ██║  ██║  ╚████╗██║ ██║█████╗██║ ██║
{B}╚═╝    ╚═╝ ╚═╝ ╚════╝ ╚═╝  ╚═╝   ╚═╝   {C} ╚═══╝╚═╝ ╚═╝  ╚═╝   ╚═══╝╚═╝ ╚═╝╚════╝╚═╝ ╚═╝
''')
try:
    print(f'''{C}[{G}!{C}] Escolha o tipo de proxy:
    
[{G}1{C}] HTTP/HTTPs
[{G}2{C}] Socks4
[{G}3{C}] Socks5
''')
    try:
        tipo=int(input(f'{C}[{G}+{C}] Escolha uma opção: {B}'))
        while(tipo > 3):
            print(f'{C}[{R}-{C}] Opção invalida.')
            tipo=int(input(f'{C}[{G}+{C}] Escolha uma opção: {B}'))
    except(ValueError):
        print(f'{C}[{R}-{C}] Selecione um valor numérico válido!')
        tipo=int(input('Escolha uma opção: '))
        while(tipo > 3):
            print(f'{C}[{R}-{C}] Opção invalida.')
            tipo=int(input(f'{C}[{G}+{C}] Escolha uma opção: {B}'))
    try:
        print(f'''
{C}[{G}!{C}] Selecione o país:

[{G}1{C}] Brasil
[{G}2{C}] Todos os paises
''' )
        pais=int(input(f'{C}[{G}+{C}] Selecione o país: {B}'))
        while(pais > 2):
            print(f'{C}[{R}-{C}] Opção invalida.')
            pais=int(input(f'{C}[{G}+{C}] Selecione o país: {B}'))
    except(ValueError):
        print(f'{C}[{R}-{C}] Selecione um valor numérico válido')
        pais=int(input(f'{C}[{G}+{C}] Selecione o país: {B}'))
        while(pais > 2):
            print(f'{C}[{R}-{C}] Opção invalida.')
            pais=int(input(f'{C}[{G}+{C}] Selecione o país: {B}'))

    lista=input(f'\n{C}[{G}+{C}] defina um nome para a lista: {B}')
    lista=lista+'.txt'
    print(f'{C}[{G}!{C}] Baixando lista de proxies...{C}')
    if pais==1:
        if tipo==1:
            proxys=requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=BR&ssl=all&anonymity=all&simplified=true').text
            proxys=proxys.replace('\n', '')
            with open(lista, 'a+') as http:
                http.write(proxys)
        elif tipo==2:
            proxys=requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=BR&simplified=true').text
            proxys=proxys.replace('\n', '')
            with open(lista, 'a+') as socks4:
                socks4.write(proxys)
        elif tipo==3:
            print(f'{C}[{R}!{C}] Proxies Socks5 não disponiveis no Pais')
    elif pais==2:
        if tipo==1:
            proxys=requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&simplified=true').text
            proxys=proxys.replace('\n', '')
            with open(lista, 'a+') as http:
                http.write(proxys)
        elif tipo==2:
            proxys=requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all&simplified=true').text
            proxys=proxys.replace('\n', '')
            with open(lista, 'a+') as socks4:
                socks4.write(proxys)
        elif tipo==3:
            proxys=requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all').text
            proxys=proxys.replace('\n', '')
            with open(lista, 'a+') as socks5:
                socks5.write(proxys)
                
    print(str(len(open(lista).readlines()))+' proxies salvas em '+B+lista+C)

except(KeyboardInterrupt):
    print(f'\n{C}[{R}!{C}] Interrompido pelo usuãrio!')
    exit(f'{R}Ctrl+C pressionado{C}')
