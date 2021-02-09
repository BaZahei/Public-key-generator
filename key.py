# the library is form https://github.com/Destiner/blocksmith, Thinks the author.
import blocksmith
import random


forNum = input("Need to generate number: ")
same_key = input("Fixed private key: ")

for i in range(int(forNum)):
    diff_key = "%04d" % random.randint(0, 9999)
    print("Private key: " + same_key + str(diff_key))
    generate_address(same_key, diff_key)



# @same_key The same part of the private key.
# @diff_key The random part of the private key.
# for this function, it will generate a ETH address from the given private key.
def generate_address(frist_key, last_key):
    key = frist_key + last_key
    address = blocksmith.EthereumWallet.generate_address(key)
    print("address: " + address)
