def write_file(file_name, file_content):
    file_name = str(file_name)
    if file_name[-4:] != ".txt":
        file_name += ".txt"
    
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    file_name = str(file_name)
    if file_name[-4:] != ".txt":
        file_name += ".txt"

    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(append_content)    

def read_file(file_name):
    file_name = str(file_name)
    if file_name[-4:] != ".txt":
        file_name += ".txt"

    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()     
