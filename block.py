from datetime import datetime
import hashlib
class Block:

    def __init__(self, index, payload, previous_hash):
        self.index = index
        self.timestamp = str(datetime.now())
        self.payload = payload
        self.previous_hash = previous_hash
        self.nonce = 0