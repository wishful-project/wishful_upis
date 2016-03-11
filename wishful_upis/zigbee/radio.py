__author__ = "Piotr Gawlowicz, Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"

'''
    The protocol-specific definition of the WiSHFUL radio control interface, UPI_R, for configuration/monitoring of the
    lower layers of the network protocol stack (lower MAC and PHY).

    IEEE 802.15.4 protocol family
'''

def disable_carrier_sensing():
    '''
        Disables carrier sensing, i.e. no listen-before-talk.
    '''
    pass

