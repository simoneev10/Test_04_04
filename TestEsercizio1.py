# Esercizio 1:
# Crea un sistema ripetibile che si occupi di dividere su tre possibili liste i tipi basilari di dato che riceve in entrata. 
# Deve poter stampare una lista singola o tutte.  Si deve ripetere X volte definite all'inizio dall'utente

# Creo liste per contenere i dato
listaInteri = []
listaBool = []
listaStringhe = []

def tipodato(scelta):
    for i in range(scelta):# Applico controlli per ogni tipologia di dato chiesto nella domanda e lo aggiungo alla propria lista
        inserimento = input("Inserisci un dato: ")
        if inserimento.lstrip('-').isdigit():
            listaInteri.append(int(inserimento))
        elif inserimento.lower() == "true": # Accetto anche True e false con lettera picccola
            listaBool.append(True)
        elif inserimento.lower() == "false":
            listaBool.append(False)
        else:
            listaStringhe.append(inserimento)

    while True: # Menu
        print("Cosa vuoi stampare?\n1) Interi\n2) Stringhe\n3) Booleani\n4) Tutte le liste \n5) Esci")
        scelta = input("Scegli un'opzione (1-5): ")

        if scelta == '1':
            print("\nInteri:", listaInteri)
        elif scelta == '2':
            print("\nStringhe:", listaStringhe)
        elif scelta == '3':
            print("\nBooleani:", listaBool)
        elif scelta == '4':
            print("\nTutte le liste:")
            print("Interi:", listaInteri)
            print("Stringhe:", listaStringhe)
            print("Booleani:", listaBool)
        elif scelta == '5':
            break
        else:
            print("Scelta non valida. Riprova.")
    
scelta = int(input("Quanti dati vuoi inserire?: "))
tipodato(scelta)    
