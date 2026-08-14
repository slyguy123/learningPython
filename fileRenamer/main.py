
###### a tool to rename sequences of files 

import os

def create_test_files(directory):
    i = 0
    while i<6:
        file = open(os.path.join(directory, f"file_{i}.txt"), 'w')
        file.write(f"This is the context of the file_{i}.txt")
        file.close()
        i += 1

def clear_test_files(directory):
    for file in os.listdir(directory):
        os.remove(os.path.join(directory, file))       

def rename_files(directory, prefix="file", padding=4, start_index=0, extension=".txt"):
    files = os.listdir(directory)
    files.sort()
    for i, file in enumerate(files):
        new_name = f"{prefix}_{start_index + i:0{padding}d}{extension}"
        os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
        print(f"Renamed {file} to {new_name}")
    

if __name__ == "__main__":
    directory = os.getcwd()+"/fileRenamer/testing_files"
    clear_test_files(directory)
    #create_test_files(directory)
    #rename_files(directory,prefix="renamed_file", padding=4, start_index=0, extension=".txt")
    

        

