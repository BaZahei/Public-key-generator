import blocksmith
import random


forNum = input("Need to generate number: ")
same_key = input("Fixed private key: ")

for i in range(int(forNum)):
    diff_key = "%04d" % random.randint(0, 9999)
    print(diff_key)
    print("Private key: " + same_key + str(diff_key))

    key = same_key + str(diff_key)

    address = blocksmith.EthereumWallet.generate_address(key)
    print("address: " + address)
