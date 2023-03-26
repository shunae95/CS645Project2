import hashlib

def MerkleHashData(hash_data):

    data = list(hash_data)
    first_hash_value = 0
    second_hash_value = 1
    new_list = []
    new_list.clear()

    while(len(data) != 0):
        if(len(data) == 0):
            print(data)
            print(new_list)
            break
        if(len(data) == 1):
            new_list.append(data[0])
            print(data)
            print(new_list)
            break
        hash_value = data[first_hash_value] + data[second_hash_value]
        byte_data = bytes(hash_value, 'utf-8')
        hash = hashlib.sha256()
        hash.update(byte_data)
        hash_2 = hash.hexdigest()
        data.pop(first_hash_value)
        data.pop(first_hash_value)
        new_list.append(hash_2)

        print(data)
        print(new_list)

    if(len(new_list) > 1):
        MerkleHashData(new_list)

    final_value = new_list
    return final_value