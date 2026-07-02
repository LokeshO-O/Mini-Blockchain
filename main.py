from blockchain import Blockchain

my_chain = Blockchain()

my_chain.add_block("Lokesh pays Mansi ₹100")
my_chain.add_block("Mansi pays DecodeLabs ₹50")
my_chain.add_block("DecodeLabs rewards Lokesh ₹25")

for block in my_chain.chain:
    print("---------------------------")
    print("Index:", block.index)
    print("Payload:", block.payload)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)