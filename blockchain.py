from block import Block

class Blockchain:

    def __init__(self):
        self.chain = []
        #genesi_block=Block(index, payload, previous_hash)
        genesis_block = Block(0,"Genesis Block","0000")
        genesis_block.mine_block(4)

        self.chain.append(genesis_block)

    def add_block(self, payload):

        index = len(self.chain)

        previous_hash = self.chain[-1].hash

        new_block = Block(index,payload,previous_hash)

        new_block.mine_block(4)
        self.chain.append(new_block)
        
    def validate_chain(self):

      for i in range(1, len(self.chain)):
        current_block = self.chain[i]
        previous_block = self.chain[i - 1]

        # Check if current block's hash is still correct
        if current_block.hash != current_block.calculate_hash():
            return False

        # Check if previous hash matches
        if current_block.previous_hash != previous_block.hash:
            return False

      return True