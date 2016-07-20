__author__ = "Piotr Gawlowicz, Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"

'''Long Term Evolution (LTE) protocol family

The protocol-specific definition of the WiSHFUL radio control interface, UPI_R,
for configuration/monitoring of the lower layers of the network protocol stack
(lower MAC and PHY).

'''
class LteRadio(object):
	def configure_mimo_mode(self, mimo_mode):
	    '''Configures the MIMO mode
	    '''
	    pass
