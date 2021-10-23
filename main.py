from termcolor import colored

def createNew():
    global saldo
    num = int(input("Ange din ny kontonummer> "))
    if num in dict.keys():
        print(colored("Felmeddelande: Den kontonummer redan taget!", "red"))
    else:
        saldo = int(input("Ange din saldo: "))
        dict[num] = saldo

def showAccountMeny():
    global num
    print("")
    print(f"***KONTOMENY**** - konto: {num}")
    print("1. Ta ut pengar")
    print("2. Sätt in pengar")
    print("3. Visa saldo")
    print("4. Avsluta")   

def accountMeny():
    global saldo, num
    print(colored(f"Välkomma til din konto! {num}", "green"))
    while True:
        showAccountMeny()
        numb = int(input("Vad ska du göra med din konto?"))
        if numb == 3:
            print(f"Din saldo är: {saldo} kr")
        elif numb == 2:
            putin = int(input("Hur många SEK ska du sätt in din konto: "))
            saldo = saldo + putin
            print(f"OK! Du har satt in {putin} kr")
        elif numb == 1:
            getout = int(input("Hur många SEK ska du ta ut från din konto: "))
            if getout <= saldo:
                saldo = saldo - getout
                print(f"OK! Du har ta ut {getout} kr")
            else:
                print(colored(f"Felmeddelande: Det finns mindre pengar på ditt konto än {getout} kr!", "red"))
                    
        elif numb == 4:
            break
        
def manage():   
        global saldo, num
        num = int(input("Ange din kontonummer> "))
        if num not in dict.keys():
            print(colored("Felmeddelande: Den kontonummer finns inte!", "red"))
        else:
            accountMeny()

def showHuvudMeny():
    print("****HUVUDMENY****")
    print("1. Skapa konto")
    print("2. Administrera konto")
    print("3. Avsluta")
    print("")

dict = {}
while True:
    showHuvudMeny()
    val = int(input("Ange huvudmenyval> "))
    if val == 3:
        break
    elif val == 1:
        createNew()
    elif val == 2:
        manage()