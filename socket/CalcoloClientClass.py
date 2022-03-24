import socket 
from threading import Thread
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225
class Client():
    """
    Questa classe rappresenta una persona che opera come client
    """
    def connessione_server(self,address,port):
        """
        Metodo per stabilire la connessione con il server
        """
        sock_service = socket.socket()
        sock_service.connect((address, port))
        print("Connesso a " + str((address, port)))
        return sock_service

    def invia_comandi(self,sock_service):
        """
        Metodo per inviare le richieste di servizio e ricevere le risposte
        """
        while True:
            try:
                n1 = input("Inserisci il primo numero: ")
                n2 = input("Inserisci il secondo numero: ")
                oper = input("Inserisci l'operazione da effettuare(piu/ meno/ per / diviso): ")
                dati=f"{oper};{n1};{n2}"
            except EOFError:
                print("\nOKay. Exit")
                break 
            if not dati:
                print("Non puoi inviare una stringa vuota!")
                continue 
            if dati == '0':
                print("Chiudo la connessione con il server!")
                sock_service.close()
                break

            dati = dati.encode()
            sock_service.sendall(dati)
            dati = sock_service.recv(2048)
            if not dati: 
                print("Server non risponde. Exit")
                break 
            dati = dati.decode()
            print("Ricevuto dal server:")
            print(dati + '\n') 


c1=Client()
sock_serv=c1.connessione_server(SERVER_ADDRESS,SERVER_PORT)
c1.invia_comandi(sock_serv)