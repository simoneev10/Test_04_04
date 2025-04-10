# Esercizio 2
# Andare a creare un sistema ripetibile che si occupa di gestire la lunghezza delle stringhe e salvarle, 
# l'utente potrà continuare a inserire dati finché la stringa inserita e più lunga della precedente, 
# alla fine stamperà l'insieme delle stringhe date in input divise da virgole e quante stringhe ha inserito.

def lungstringhe():
    stringhe = []
    cont = 0
    # Controllo prima stringa (necessaria)
    if (primaStringa := input("Inserisci la prima stringa: ")):
        stringhe.append(primaStringa)
        cont += 1
    else:
        print("Devi inserire almeno una stringa!")
        return
    
    while True: #Gestione Gioco
        ultLunghezza = len(stringhe[-1])
        insStringa = input(f"Inserisci una stringa più lunga di {ultLunghezza} se vuoi andare avanti: ")
        
        if not insStringa: # Se non inserisci nulla esci
            break
        
        if len(insStringa) > ultLunghezza:# Controllo lunghezza e aggiunta
            stringhe.append(insStringa)
            cont += 1
        else:
            print("1nStringa non abbastanza lunga per continuare!")
            break
        
        print("\nLe stringhe inserite sono:")
        for i in range(len(stringhe)): # Scorro per poter stampare ed aggiungo anche una virgola tra le stringhe
            if i == len(stringhe) - 1:
                print(stringhe[i])
            else:
                print(stringhe[i] + ", ", end="")
        print(f"Hai inserito {cont} stringhe\n")

lungstringhe()