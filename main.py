from block import Block

block = Block(
    1,
    "Lokesh pays Mansi ₹100",
    "0000"
)

print(block.index)
print(block.timestamp)
print(block.payload)
print(block.previous_hash)
print(block.nonce)