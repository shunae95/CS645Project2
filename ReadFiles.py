import os
import hashlib
from HashData import HashData
from MerkleHashData import MerkleHashData

def ReadFiles():
    root_directories = []
    needed_directories = []
    files_in_directory = []
    hash_data = []
    h0 = '0000000000000000000000000000000000000000000000000000000000000000'
    hashes = [h0]

    for root, dir, files in os.walk(".", topdown=True):
        for directories in dir:
            root_directories.append(directories)

            if(directories.startswith("Day")):
                needed_directories.append(directories)
    
    inorder_days = sorted(needed_directories)
        
    print(root_directories)
    print(needed_directories)
    print(inorder_days)
    count = 0
    
    for day in inorder_days:
        file = "./" + inorder_days[count] 
        
        entries = os.listdir(file)
        for entry in entries:
            files_in_directory.append(entry)

        in_order_files = sorted(files_in_directory)

        for files in in_order_files:
            new_file = open(file + "/" + files, "rb")
            data = new_file.read()

            hash_file = HashData(data)
            hash_data.append(hash_file)
            new_file.close()
            print(files)

        print(hash_data)
        day_hash = MerkleHashData(hash_data)
        print(day_hash)
        returned_day_hash = data = list(day_hash)
        hashes.append(returned_day_hash)
        count = count + 1
        in_order_files = []
        files_in_directory = []
    
    overall_hash = MerkleHashData(hashes)
    return hash_data


if __name__ == "__main__":
    ReadFiles()
