__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz}@tkn.tu-berlin.de"


def start_iperf_server(port):
    '''
        func desc
    '''
    pass


def stop_iperf_server(port):
    '''
        func desc
    '''
    pass

def start_iperf_client(destIp, port=5001):
    '''
        func desc
    '''
    pass


def stop_iperf_server(port):
    '''
        func desc
    '''
    pass

def get_info_of_associated_STAs():
    '''
        func desc
    '''
    return

def get_inactivity_time_of_associated_STAs():
    '''
        func desc
    '''
    return

def get_avg_sigpower_of_associated_STAs():
    '''
        func desc
    '''
    return

def connect_to_AP(iface, ssid):
    '''
        func desc
    '''
    return

def get_hw_addr(iface):
    '''
        func desc
    '''
    return

def get_iface_ip_addr(iface):
    '''
        func desc
    '''
    return

def gen_backlogged_80211_l2_bcast_traffic(iface, num_packets, ipPayloadSize, phyBroadcastMbps, ipdst, ipsrc, use_tcpreplay):
    '''
        func desc
    '''
    return

def gen_80211_l2_link_probing(iface, num_packets, pinter, ipdst, ipsrc):
    '''
        func desc
    '''
    return

def sniff_80211_l2_link_probing(iface, ipdst, ipsrc, sniff_timeout):
    '''
        func desc
    '''
    return

def set_ARP_entry(iface, mac_addr, ip_addr):
    '''
        func desc
    '''
    return

def change_routing(servingAP_ip_addr, targetAP_ip_addr, sta_ip_addr):
    '''
        func desc
    '''
    return

def transmit_disassociation_request_to_STA(iface, sta_mac_addr):
    '''
        func desc
    '''
    return

def send_CSA_beacon_to_STA(iface, bssid, sta_mac_addr, target_channel, serving_channel):
    '''
        func desc
    '''
    return

def add_STA_to_AP_blacklist(iface, sta_mac_addr):
    '''
        func desc
    '''
    return

def remove_STA_from_AP_blacklist(iface, sta_mac_addr):
    '''
        func desc
    '''
    return

def register_new_STA_in_AP(iface, sta_mac_addr):
    '''
        func desc
    '''
    return

