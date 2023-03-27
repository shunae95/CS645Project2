import os
import time
from HashData import HashData
from MerkleHashData import MerkleHashData
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def ReadFiles():

    def signHash(hash):
        byte_data = bytes(hash, 'utf-8')
        signature = private_key.sign(byte_data, padding.PSS(mgf=padding.MGF1(hashes.SHA256()),salt_length=padding.PSS.MAX_LENGTH),hashes.SHA256())
        hex = signature.hex()
        return hex

    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    root_directories = []
    needed_directories = []
    files_in_directory = []
    hash_data = []
    h0 = '0000000000000000000000000000000000000000000000000000000000000000'
    overall_hash = [h0]

    for root, dir, files in os.walk(".", topdown=True):
        for directories in dir:
            root_directories.append(directories)

            if(directories.startswith("Day")):
                needed_directories.append(directories)
    
    inorder_days = sorted(needed_directories)
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

        day_hash = MerkleHashData(hash_data)
        print(day_hash)
        overall_hash.append(day_hash)
        count = count + 1
        combined_hash = [day_hash, overall_hash[count-1]]
        needed_hash = MerkleHashData(combined_hash)
        signedHash = signHash(needed_hash)
        time_of_day = time.time()
        print(time_of_day)
        print("Hash of Day " + str(count) + ": " + needed_hash)
        sign_list = [time_of_day, signedHash]
        print("The time and hash of Day " + str(count) + " is: " + str(sign_list))
        in_order_files = []
        files_in_directory = []
    
    print(overall_hash)
    return hash_data


if __name__ == "__main__":
    ReadFiles()
