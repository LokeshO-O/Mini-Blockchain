from block import Block

block = Block(
    1,
    "Lokesh pays Mansi ₹100",
    "0000"
)

print("Index:", block.index)
print("Payload:", block.payload)
print("Hash:", block.hash)