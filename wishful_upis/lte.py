from .net import Network
from .radio import Radio
from .net_func import NetFun

__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Anatolij Zubow, Peter Ruckebusch, Domenico Garlisi"
__copyright__ = "Copyright (c) 2016, Technische Universitat Berlin, iMinds, CNIT"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de, peter.ruckebusch@intec.ugent.be"

'''Long Term Evolution (LTE) protocol family

The protocol-specific definition of the WiSHFUL radio control interface, UPI_R,
for configuration/monitoring of the lower layers of the network protocol stack
(lower MAC and PHY).

'''


class LteRadio(Radio):
    def configure_mimo_mode(self, mimo_mode):
        '''Configures the MIMO mode
        '''
        pass


class LteNet(Network):
    pass


class LteNetFun(NetFun):
    pass
