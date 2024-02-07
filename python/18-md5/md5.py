############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Determine hash values using rockyou1000.txt
# OK - 1 Feb 2024

import hashlib

def hash_my_password(inputPass):
    hash = hashlib.md5(inputPass.encode("utf-8"))
    return hash.hexdigest()

def break_da_password(hashes: list[str]):
    rockyou = open('./rockyou1000.txt', 'r').readlines()
    for password in rockyou:
        hash = hash_my_password(password.strip())
        if hash in hashes:
            print(f'{password.strip()} = {hash}')

if __name__ == "__main__":
    hashes_to_crack = [
        '72dabe497516c268bc78ed8a0f3c2a73',
        'b40570d67e2051457ff8438906e62146',
        '9fab6755cd2e8817d3e73b0978ca54a6',
        'ab003765f3424bf8e2c8d1d69762d72c',
        '46f94c8de14fb36680850768ff1b7f2a'
    ]
    break_da_password(hashes_to_crack)
    #print(hash_my_password("ExamplePassword"))
