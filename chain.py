import time
import hashlib
import socket




class Block(object):

    def __init__(self, index, prevHash, timestamp, data):

        """ A Class to represent a single block in the blockchain 
        Args:
            index: int
            prevHash: string
            timestamp: long
            data : string
            hashVal: string
        """
        
        self.index = index
        self.time = timestamp # should be in unix millis
        self.data = data
        self.prevHash = prevHash
        self.hashValue = self.calculateHash()


    def calculateHash(self):
        return hashlib.sha256(str(self.index) + self.prevHash + str(self.time) + self.data).hexdigest()

class Chain(object):

    """ The class for actually managing the overall block chain. Responsible for the interface to control the blockchain, as well as send out websocket updates to all
    connected to the network
    """
    
    def __init__(self): 
        self.blockChain = [self.createGenesis()]
        self.connections = [] # maintains the socket connections, which yields the number of people on your blockchain

        # TODO: Actually run the chain 


    def createGenesis(self):
        """ Creates the genesis block for a new blochain """
        
        # TODO: Don't hardcode the initial hash
        return Block(0, '0', int(time.time()), "Genesis", "18a99095f5a68fe43b51068a4b30e0d18687933f3bd2f52d2e0a7a37536256b7")
    
    def isValidBlock(self, block):

        """ A validator function for the entire block, and checks whether it is valid for it to be added 
        returns:
        Bool
        """

        latestBlock = self.blockChain[-1]
        if latestBlock.index + 1 != block.index:
            return False
        elif latestBlock.hashValue != block.prevHash:
            return False
        elif block.calculateHash() != block.hashValue:
            return False
        else:
            return True

        
    def createBlock(self, data):

        """ Creates a block, but does not append it to the blockchain. 
        WARNING: data is not validated. It is expecting a string, please be nice <3
        """
        
        latest = self.blockChain[-1]
        timestamp = int(time.time())
        prevHash = latest.hashValue
        
        block = Block(latest.index + 1, prevHash, timestamp, data)

    def addBlock(self, block):

        """ Validates a block and then appends it to the blockchain """
        
        if self.isValidBlock(block):
            self.blockChain.append(block)
            
        
    
    def history(self):
        """ Returns an iterator to look over the history of this blockchain """
        
        for val in self.blockChain:
            yield val
