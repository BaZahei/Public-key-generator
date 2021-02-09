import blocksmith
import random


forNum = input("生成个数：")
same_key = input("固定私钥，请输入与例子相同的长度“7077da4a47f6c85a21fe6c6cf1285c0fa06915871744ab1e5a5b79469057”：")

for i in range(int(forNum)):
    # diff_key = random.randint(0,1000000000000)
    diff_key = "%04d" % random.randint(0, 9999)
    print(diff_key)
    print("私钥是：" + same_key + str(diff_key))

    key = same_key + str(diff_key)

    address = blocksmith.EthereumWallet.generate_address(key)
    print("地址是：" + address)
# 0x1269645a46a3e86c1a3c3de8447092d90f6f04ed

# checksum_address = blocksmith.EthereumWallet.checksum_address(address)
# print(checksum_address)
# # 0x1269645a46A3e86c1a3C3De8447092D90f6F04ED