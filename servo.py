import tornado
from chain import Block, Chain




class ChainServo(object):

    """ A web server that interfaces between the local blockchain, and other blockchains on the network, as well as providing some control through http """

    

    def __init__(self, port=3431):
        """ Creates handlers for p2p networking as well as http requests """
        
        self.blockChain = Chain()
        self.sockets = []
        # send out the request to get the chain
        class P2PHandler(tornado.websocket.WebSocketHandler):


            # 
            def on_message(self, message):
                self.blockChain

    def run(self):
        



