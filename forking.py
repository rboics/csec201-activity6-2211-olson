import os
import subprocess
"""
# Press the green button in the gutter to run the script.
# Use this version on Linux or Mac
# Comment out if you are using Windows
if __name__ == '__main__':
    print(f"Main is running - {os.getpid()}")
    print(f"Main's parent is {os.getppid()}")
    result = os.fork()
    if result == 0: #Remember, result returns pid of the child to the parent
# 1. Use the subprocess library to run a Linux command to show the current user account
# 2. Use the subprocess library to run the Linux command 'ps -ef' to show the currently active Windows processes
        print(f"Child is running - {os.getpid()}")
        print(f"Child's parent is {os.getppid()}")
    else:
        print(f"Main is running is {os.getpid()}")
        print(f"Main's child is {result}")

# Uncomment the section below if you are using Windows and comment out the section above
"""
import multiprocessing

def child():
# 1. Use the subprocess library to run a Windows command to show the current user account
# 2. Use the subprocess library to run the Windows command tasklist to show the currently active Windows processes
    print(f"Child is running - {os.getpid()}")
    print(f"Child's parent is {os.getppid()}")

if __name__ == '__main__':
    print(f"Main's PID is {os.getpid()}")
    print(f"Main's parent is {os.getppid()}")
        
    p1 = multiprocessing.Process(target=child)
    p1.start()
    print(f"Main is running is {os.getpid()}")
    print(f"Main's child is {result}")
    p1.join()
