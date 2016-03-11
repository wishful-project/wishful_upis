from lte.net import *
from wifi.net import *
from zigbee.net import *


__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de"

'''
    The WiSHFUL network control interface, UPI_N, for configuration/monitoring of the higher
    layers of the network protocol stack (upper MAC and higher).
'''

''' Generic API to control the higher layers, i.e. key-value configuration. '''

def set_parameter_higher_layer(**kwargs):
    """Set the parameter on higher layers of protocol stack (higher MAC and above)
    :param param_key_value: key and value of this parameter
    """
    return


def get_parameter_higher_layer(**kwargs):
    """Get the parameter on higher layers of protocol stack (higher MAC and above)
    :param param_key: the parameter identified by this key.
    :return the parameter value
    """
    return

''' App layer - set-up of packet flows '''

def create_packetflow_sink(port):
    '''
        Start IPerf server (TCP/IP)
    '''
    return


def destroy_packetflow_sink():
    '''
        Stop IPerf server.
    '''
    return


def start_packetflow(dest_ip, port = 5001):
    '''
        Start IPerf client.
    '''
    return


def stop_packetflow():
    '''
        Stop IPerf client.
    '''
    return


''' Net layer '''

def get_iface_hw_addr(iface):
    '''
        Returns the hardware address (MAC address) of a given interface.
    '''
    return


def get_iface_ip_addr(iface):
    '''
        Returns the IP address of a given interface.
    '''
    return


def set_ARP_entry(iface, mac_addr, ip_addr):
    '''
        Manipulates the entries in the ARP cache.
    '''
    return


def change_routing(current_gw_ip_addr, new_gw_ip_addr, device_ip_addr):
    '''
        Controlles the routing.
    '''
    return


''' Upper MAC layer - injection and sniffing of layer2 traffic '''

def gen_layer2_traffic(iface, num_packets, pinter, max_phy_broadcast_rate_mbps=None, **kwargs):
    '''
        Inject layer2 traffic into network device.
    '''
    return


def inject_frame(iface, frame, is_layer_2_packet, tx_count=1, pkt_interval=1):
    '''
        Inject L2/L3 frame injection into the protocol stack
    '''
    return


def sniff_layer2_traffic(iface, sniff_timeout, **kwargs):
    '''
        Layer-2 packet sniffing from network device.
    '''
    return


''' Controlling network emulation (netem), i.e. emulation of variable delay, loss, duplication and re-ordering. '''

def set_netem_profile(iface, profile):
    """
    Func Desc
    """
    return


def update_netem_profile(profileId, profile):
    """
    Func Desc
    """
    return


def remove_netem_profile(profileId):
    """
    Func Desc
    """
    return


def set_per_link_netem_profile(iface, dstAddr, profile):
    """
    Func Desc
    """
    return


def update_per_link_netem_profile(profileId, profile):
    """
    Func Desc
    """
    return


def remove_per_link_netem_profile(profileId):
    """
    Func Desc
    """
    return


''' Controlling queuing disciplines '''

def install_egress_scheduler(iface, scheduler):
    """
    Func Desc
    """
    return


def remove_egress_scheduler(schedulerId):
    """
    Func Desc
    """
    return


''' Network filter tables '''

def clear_nf_tables():
    """
    Func Desc
    """
    return

def get_nf_table(tableName):
    """
    Func Desc
    """
    return

''' Packet marking - IP ToS '''

def set_pkt_marking(flowId, mark):
    """
    Func Desc
    """
    return


def del_pkt_marking(flowId):
    """
    Func Desc
    """
    return

''' Packet mangling - IP ToS '''

def set_ip_tos(flowId, tos):
    """
    Func Desc
    """
    return


def del_ip_tos(flowId):
    """
    Func Desc
    """
    return