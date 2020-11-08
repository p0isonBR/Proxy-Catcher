import re, requests

try:
    print('''De que site deseja pegar proxys?
[1] proxyscrape.com
[2] proxynova.com
''')
    try:
        site=int(input('Escolha uma opção: '))
        while(site > 2):
            print('Opção invalida')
            site=int(input('Escolha uma opção: '))
    except(ValueError):
        print('Selecione um valor numérico válido')
        site=int(input('Escolha uma opção: '))
        while(site > 2):
            print('Opção invalida')
            site=int(input('Escolha uma opção: '))
            
    print('''Escolha o tipo de proxy:
[1] HTTP/HTTPs
[2] Socks4
[3] Socks5
''')
    try:
        tipo=int(input('Escolha uma opção: '))
        while(tipo > 3):
            print('Opção invalida')
            tipo=int(input('Escolha uma opção: '))
    except(ValueError):
        print('Selecione um valor numérico válido')
        tipo=int(input('Escolha uma opção: '))
        while(tipo > 3):
            print('Opção invalida')
            tipo=int(input('Escolha uma opção: '))
    try:
        print('''Selecione o país:
[1] Brasil
[2] Todos os paises
''' )
        pais=int(input('Selecione o país: '))
        while(pais > 2):
            print('Opção invalida')
            pais=int(input('Selecione o país: '))
    except(ValueError):
        print('Selecione um valor numérico válido')
        pais=int(input('Selecione o país: '))
        while(pais > 2):
            print('Opção invalida')
            pais=int(input('Selecione o país: '))

    if site==1:
        lista=input('defina um nome para a lista: ')
        lista=lista+'.txt'
        print('Baixando lista de proxies...')
        if pais==1:
            if tipo==1:
                proxys=requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=BR&ssl=all&anonymity=all&simplified=true').text
                proxys=proxys.replace('\n', '')
                with open(lista, 'a+') as http:
                    http.write(proxys)
            elif tipo==2:
                proxys=requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=BR&simplified=true').text
                proxys=proxys.replace('\n', '')
                with open(lista, 'a+') as http:
                    http.write(proxys)
            elif tipo==3:
                print('Proxies Socks5 não disponiveis no Pais')
        elif pais==2:
            if tipo==1:
                proxys=requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&simplified=true').text
                proxys=proxys.replace('\n', '')
                with open(lista, 'a+') as http:
                    http.write(proxys)
            elif tipo==2:
                proxys=requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all&simplified=true').text
                proxys=proxys.replace('\n', '')
                with open(lista, 'a+') as http:
                    http.write(proxys)
            elif tipo==3:
                proxys=requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all')
                proxys=proxys.replace('\n', '')
                with open(lista, 'a+') as http:
                    http.write(proxys)
    elif site==2:
        print('Ainda nao disponivel')

    print(str(len(open(lista).readlines())))+' proxies salvas em '+lista)

except(KeyboardInterrupt):
    print('Interrompido pelo usuãrio')
    exit('Ctrl+C')
