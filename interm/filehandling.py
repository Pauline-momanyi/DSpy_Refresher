#detect files
import os

print("Current directory:", os.getcwd()) #for some reason this leaves out the current dir thats why I have to add it before the file
file_path = "interm/test.txt" 
file_path1 = "interm/" 

if os.path.exists(file_path):
    print(f"{file_path} exists")
    if os.path.isfile(file_path):
        print(f"{file_path} is a file")
    elif os.path.isdir(file_path):
        print(f"{file_path} is a directory")
    
else:   
    print("Does not exist")
    
    
# WRITING FILES
#with - enclosure for file that closes it once we are done with that block
# file (you can use kwargs like file=file_path, mode="w")
# Mode: w - write whether it exists or not, x - write only when file doesnt exist, r - read, a - append

text_data = "I love python"
with open(file_path, "w") as file:
    file.write(text_data) #replaces the initial data
    print("Data written successfuly to file")
    
with open(file_path, "a") as file:
    file.write("\nYes I do")
    
try:
    with open(file_path, "x") as file:
        file.write(text_data)
        
except FileExistsError:
    print("File exists already!!!!")
    
    
# writing a list - we can only write str so we have to iterate
employees = ["Popo", "Pauline", "Nyaboke"]
new_file = "interm/employees.txt"

try: 
    with open(new_file, "w") as file:
        for employee in employees:
            file.write(employee+"\n")
    
except TypeError:
    print("write() argument must be str, not list!!!")
    

# json data
import json

json_filepath = "interm/employees.json"

n_employee = {
    "name":"Pauline",
    "age":28,
    "role":"project manager"
}

with open(json_filepath, "w") as file: 
    json.dump(n_employee, file)
    print("Json data was created")
