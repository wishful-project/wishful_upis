from .net import Network
from .radio import Radio
from .net_func import NetFun

__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Anatolij Zubow, Peter Ruckebusch, Domenico Garlisi"
__copyright__ = "Copyright (c) 2016, Technische Universitat Berlin, iMinds, CNIT"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de, peter.ruckebusch@intec.ugent.be"

'''IEEE 802.15.4 protocol family

The protocol-specific definition of the WiSHFUL radio control interface, UPI_R,
for configuration/monitoring of the lower layers of the network protocol stack
(lower MAC and PHY).

'''


class LowpanRadio(Radio):

    PARAMETERS = [
        "IEEE802154_macMaxBE",
        "IEEE802154_macMaxCSMABackoffs",
        "IEEE802154_macMaxFrameRetries",
        "IEEE802154_macMinBE",
        "IEEE802154_macPANId",
        "IEEE802154_macShortAddress",
        "IEEE802154_macExtendedAddress",
        "IEEE802154_phyCurrentChannel",
        "IEEE802154_phyTXPower",
        "IEEE802154e_macHoppingSequenceLength",
        "IEEE802154e_macHoppingSequenceList",
        "IEEE802154e_macSlotframeSize",
        "IEEE802154e_macTimeslot",
        "IEEE802154e_macTsTimeslotLength",
        "TAISC_ACTIVERADIOPROGRAM",
        "IEEE802154_MACSTATS",
        "IEEE802154_event_macStats",
    ]

    def disable_carrier_sensing(self):
        '''
        Disables carrier sensing

        i.e. no listen-before-talk.
        '''
        pass

    def blacklist_channels():
        return


class LowpanNet(Network):
    pass


class LowpanNetFun(NetFun):
    pass
