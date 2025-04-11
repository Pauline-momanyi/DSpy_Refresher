# multithreading: perform multiple tasks concurrently. Good for I/O tasks, fetching data from APIs, threading - target=my_function. Good for things that you don't know when they will be completed

import threading 
import time

def walk_dog(dog_name):
    time.sleep(8)
    print(f"You walk Dog {dog_name}")
    
def trash_out():
    time.sleep(4)
    print("You take out trash")
    
def mail_out():
    time.sleep(2)
    print("You picked the mail")
    
# walk_dog()
# trash_out()
# mail_out()
# They will be executed in order cause they afre running on the Main thread.

task1 = threading.Thread(target = walk_dog, args=("Scooby",)) #has to be a tuple. Tuple of one you have to include comma, otherwise it will count each character
task1.start()
task2 = threading.Thread(target = trash_out)
task2.start()
task3 = threading.Thread(target = mail_out)
task3.start()
task1.join()
task2.join()
task3.join()
print("All tasks done!") #if we don't do the join, this will be executed first

