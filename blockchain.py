from block import Block


class Blockchain:

    def __init__(self):
        self.chain = []
        #genesi_block=Block(index, payload, previous_hash)
        genesis_block = Block(0,"Genesis Block","0000")

        self.chain.append(genesis_block)

    def add_block(self, payload):

        index = len(self.chain)

        previous_hash = self.chain[-1].hash

        new_block = Block(index,payload,previous_hash)

        self.chain.append(new_block)