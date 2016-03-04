__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de"

'''
    The WiSHFUL network control interface, UPI_N, for configuration/monitoring of the higher
    layers of the network protocol stack (upper MAC and higher).
'''


'''
    App layer
'''

def create_packetflow_sink(port):
    '''
        Start IPerf server (TCP/IP)
    '''
    pass


def destroy_packetflow_sink():
    '''
        Stop IPerf server.
    '''
    pass


def start_packetflow(dest_ip, port = 5001):
    '''
        Start IPerf client.
    '''
    pass


def stop_packetflow():
    '''
        Stop IPerf client.
    '''
    pass

'''
    Net layer
'''

def get_iface_hw_addr(iface):
    '''
        func desc
    '''
    return

def get_iface_ip_addr(iface):
    '''
        func desc
    '''
    return

def set_ARP_entry(iface, mac_addr, ip_addr):
    '''
        func desc
    '''
    return

def change_routing(current_gw_ip_addr, new_gw_ip_addr, device_ip_addr):
    '''
        func desc
    '''
    return

def connect_to_network(iface, **kwargs):
    '''
        func desc
    '''
    return

'''
    Upper MAC layer
'''

def gen_layer2_traffic(iface, num_packets, pinter, max_phy_broadcast_rate_mbps=None, **kwargs):
    '''
        Inject layer2 traffic into network device.
    '''
    return

def sniff_layer2_traffic(iface, sniff_timeout, **kwargs):
    '''
        Packet sniffing from network device.
    '''
    return


def inject_frame(iface, frame, is_layer_2_packet, tx_count=1, pkt_interval=1):
    '''
        Inject L2/L3 frame injection into the protocol stack
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
