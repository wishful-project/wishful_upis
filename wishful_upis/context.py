from .upi import Upi

__author__ = "Piotr Gawlowicz, Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"

'''The WiSHFUL context control interface, UPI_C.

Used for getting/setting context information like the geo-location of a user
terminal.
'''

class Context(Upi):
	def get_node_position(self):
	    '''Returns the geo-location of a wireless node.
	    '''
	    pass
