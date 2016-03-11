__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de"

'''
    The protocol-specific definition of the WiSHFUL radio control interface, UPI_R, for configuration/monitoring of the
    lower layers of the network protocol stack (lower MAC and PHY).

    IEEE 802.11 protocol family
'''

'''
    MAC layer
'''

def set_mac_access_parameters(queueId, qParam):
    '''
        MAC access parameters in 802.11e: the configuration of the access categories
    '''
    pass


def get_mac_access_parameters(queueId):
    '''
        MAC access parameters: in 802.11e: the configuration of the access categories
    '''
    pass


'''
    PHY layer
'''


def get_airtime_utilization():
    '''
        Returns the relative time the spectrum is empty.
    '''
    pass


def perform_spectral_scanning(iface, freq_list, mode):
    '''
        Perform spectral scanning. Returns a power value for each frequency bin.
    '''
    pass


def set_channel(channel):
    '''
        Set channel, i.e. center frequency of the primary band.
        ch - channel to set
    '''
    pass


def get_channel():
    '''
        Get channel, i.e. center frequency of the primary band.
    '''
    pass


def get_noise():
    '''
        Returns the noise floor measured by the wireless driver.
    '''
    pass


def configure_radio_sensitivity(phy_dev, **kwargs):
    '''
        Configuring the receiving sensitivity of the IEEE 802.11 radio.
    '''
    pass


''' Per flow transmit power control '''

def set_per_flow_tx_power(flowId, txPower):
    """
        Sets for a flow identified by an 5-tuple (IP header) the transmit power to be used.
    """
    return


def clean_per_flow_tx_power_table():
    """
        Remove any entries in the transmit power table.
    """
    return


def get_per_flow_tx_power(flowId):
    """
        Return the transmit power level used for the given flow.
    """
    return


def get_per_flow_tx_power_table():
    """
        Return the whole transmit power table.
    """
    return








