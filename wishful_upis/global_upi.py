__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


def transaction_begin():
    '''
        func desc
    '''
    pass


def transaction_abort():
    '''
        func desc
    '''
    pass


def transaction_commit():
    '''
        func desc
    '''
    pass


def perform_soft_handover(wifi_intf, wlan_inject_iface, sta_mac_addr, sta_ip_addr,
                          servingAP, servingAP_ip_addr, servingAP_channel, servingAP_bssid,
                          targetAP, targetAP_ip_addr, targetAP_channel, gateway):
    '''
        func desc
    '''
    pass


def perform_hard_handover(wifi_intf, wlan_inject_iface, sta_mac_addr, sta_ip_addr,
                          servingAP, servingAP_ip_addr, servingAP_channel, servingAP_bssid,
                          targetAP, targetAP_ip_addr, targetAP_channel, gateway):
    '''
        func desc
    '''
    pass

def get_servingAP(nodes, wifi_intf, sta_mac_addr):
    '''
    Estimates the AP which serves the given STA. Note: if an STA is associated with multiple APs the one with the
    smallest inactivity time is returned.
    '''
    pass


def estimate_nodes_in_carrier_sensing_range(nodes, iface, channel, TAU):
    """
    Estimate which nodes are in carrier sensing range using UPIs.
    For a network with N nodes all combinations are evaluated, i.e. N over 2.
    Note: make sure ptpd is running: sudo /etc/init.d/ptp-daemon
    @return a list of triples (node1, node2, True/False) True/False if nodes are in carrier sensing range
    """
    pass

def is_in_carrier_sensing_range(node1, node2, mon_dev, TAU, rfCh):
    """
    Estimate whether two nodes are in carrier sensing range or not using UPIs.
    """
    pass

def estimate_nodes_in_communication_range(self, nodes, iface, channel, MINPDR):
    """
    Estimate which nodes are in communication range using UPIs.
    For a network with N nodes all combinations are evaluated, i.e. N over 2.
    Note: make sure ptpd is running: sudo /etc/init.d/ptp-daemon
    @return a list of triples (node1, node2, True/False) True/False if nodes are in communication range
    """

def is_in_communication_range(node1, node2, mon_dev, MINPDR, rfCh):
    """
    Estimate whether two nodes are in communication range or not using UPIs.
    """
    pass

