from lib.web_server import wsClient, wsServer

import threading

serv_p = None

def startProgram(values):
    serv = wsServer('localhost', '8765', values)
    # client = wsClient('localhost', '8765')
    
    global serv_p
    # serv_p = mp.Process(target=serv.run_server)
    serv_p = threading.Thread(target=serv.run_server)
    serv_p.daemon = True
    # client_p = mp.Process(target=client.run_server)
    
    serv_p.start()
    # client_p.start()
    
def stopProgram():
    pass
