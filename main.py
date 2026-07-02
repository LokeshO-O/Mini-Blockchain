from blockchain import Blockchain

my_chain = Blockchain()

my_chain.add_block("Lokesh pays Mansi ₹100")
my_chain.add_block("Mansi pays DecodeLabs ₹50")
my_chain.add_block("DecodeLabs rewards Lokesh ₹25")

for block in my_chain.chain:
    print("-" * 50)
    print("Index:", block.index)
    print("Payload:", block.payload)
    print("Nonce:", block.nonce)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)

print("-" * 50)
print("Is blockchain valid?", my_chain.validate_chain())



## -------------------------
# Tampering Test (Uncomment to test)
# -------------------------

# my_chain.chain[2].payload = "Lokesh pays Hacker ₹1000000"
# print("After Tampering:")
# print("Is blockchain valid?", my_chain.validate_chain())