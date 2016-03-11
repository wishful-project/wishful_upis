__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de"

'''
    The protocol-specific definition of the WiSHFUL network control interface, UPI_N, for configuration/monitoring of the higher
    layers of the network protocol stack (upper MAC and higher).

    IEEE 802.11 protocol family
'''


''' Upper MAC layer '''
def connect_to_network(iface, **kwargs):
    '''
        Connects a given interface to some network, e.g. WiFi network identified by SSID.
    '''
    return


def add_device_to_blacklist(iface, device_mac_addr):
    '''
        Add the given device to the blacklist:
        - 802.11 AP: the device is a client and the result of blacklisting is that the client cannot associate with this node.
        - Other??
    '''
    return


def remove_device_from_blacklist(iface, device_mac_addr):
    '''
        Remove the given device from the blacklist:
        - 802.11 AP: the device is a client and the result of unblacklisting is that the client can associate with this node.
        - Other??
    '''
    return


def disconnect_device(iface, device_mac_addr):
    '''
        Disconnects the given device from this node:
        - 802.11 AP: send dissassociation request to client device
        - 802.11 adhoc: no meaning
        - Other?
    '''
    return


def register_new_device(iface, sta_mac_addr):
    '''
        Register the given device:
        - 802.11 AP: the device is associated with this AP.
        - Other??
    '''
    return


def get_info_of_connected_devices():
    '''
        Returns information about associated devices:
        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
    '''
    return


def get_inactivity_time_of_connected_devices():
    '''
        Returns information about associated devices - inactivity time:
        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
    '''
    return


def get_avg_sigpower_of_connected_devices():
    '''
        Returns information about associated devices - link signal power:
        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
    '''
    return


def trigger_channel_switch_in_device(iface, device_mac_addr, target_channel, serving_channel, **kwargs):
    '''
        Trigger a channel switch in the device connected to this node:
        - 802.11 AP: send channel switch announcement to client STA,
        - other??
    '''
    return
