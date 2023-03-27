# import hashlib

# def MerkleHashData(hash_data):

#     data = list(hash_data)
#     first_hash_value = 0
#     second_hash_value = 1
#     new_list = []
#     list_of_hashes = []

#     while(len(data) != 0):
#         if(len(data) == 1):
#             new_list.append(data[0])
#             break
#         hash_value = data[first_hash_value] + data[second_hash_value]
#         byte_data = bytes(hash_value, 'utf-8')
#         hash = hashlib.sha256()
#         hash.update(byte_data)
#         hash_2 = hash.hexdigest()
#         data.pop(first_hash_value)
#         data.pop(first_hash_value)
#         new_list.append(hash_2)

#     if(len(new_list) != 1):
#         list_of_hashes.append(new_list)
#         MerkleHashData(new_list)
#     elif(len(new_list) == 1):
#         needed_value = str(new_list[0])
#         list_of_hashes.append(new_list)

#     print(list_of_hashes)
#     return new_list

import hashlib

def MerkleHashData(hash_data):
    if len(hash_data) == 1:
        return hashlib.sha256(hash_data[0].encode('utf-8')).hexdigest()

    new_list = []
    for i in range(0, len(hash_data), 2):
        if i+1 == len(hash_data):
            hash_value = hash_data[i] + hash_data[i]
        else:
            hash_value = hash_data[i] + hash_data[i+1]
        byte_data = bytes(hash_value, 'utf-8')
        hash = hashlib.sha256()
        hash.update(byte_data)
        new_list.append(hash.hexdigest())

    return MerkleHashData(new_list)
