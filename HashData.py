import hashlib

def HashData(data):
    hash_list = []
    hash = hashlib.sha256()
    hashed_data = hash.update(data)
    hash_value = hash.hexdigest()
    print(hash_value)
    return hash_value