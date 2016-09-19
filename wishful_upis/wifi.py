from .net import Network
from .radio import Radio
from .net_func import NetFun
from .net_func import TriggerHandoverRequestEvent
from .net_func import NetFunEvent

__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de"


'''
    The protocol-specific definition of the WiSHFUL radio control interface, UPI_R, for configuration/monitoring of the
    lower layers of the network protocol stack (lower MAC and PHY).

    IEEE 802.11 protocol family
'''

class WifiRadio(Radio):

    def set_mac_access_parameters(self, queueId, qParam):
        '''MAC access parameters in 802.11e: the configuration of the access categories
        '''
        pass

    def get_mac_access_parameters(self, queueId):
        '''MAC access parameters: in 802.11e: the configuration of the access categories
        '''
        pass


    def get_airtime_utilization(self):
        '''Returns the relative time the spectrum is empty.
        '''
        pass

    def perform_spectral_scanning(self, iface, freq_list, mode):
        '''Perform spectral scanning.

        Returns:
            Power value for each frequency bin.
        '''
        pass

    def set_channel(self, channel):
        '''Set channel, i.e. center frequency of the primary band.

        Args:
            channel: channel to set
        '''
        pass

    def get_channel(self):
        '''Get channel, i.e. center frequency of the primary band.
        '''
        pass

    def configure_radio_sensitivity(self, phy_dev, **kwargs):
        '''Configuring the receiving sensitivity of the IEEE 802.11 radio.
        '''
        pass

    ''' Per flow transmit power control '''

    def set_per_flow_tx_power(self, flowId, txPower):
        """Sets for a flow identified by an 5-tuple (IP header) the transmit power to be used.
        """
        return

    def clean_per_flow_tx_power_table(self):
        """Remove any entries in the transmit power table.
        """
        return

    def get_per_flow_tx_power(self, flowId):
        """Return the transmit power level used for the given flow.
        """
        return

    def get_per_flow_tx_power_table(self):
        """Return the whole transmit power table.
        """
        return

    def install_mac_processor(self, interface, mac_profile):
        """Install new WiFi MAC Processor
        """
        return

    def update_mac_processor(self, interface, mac_profile):
        '''func desc
        '''
        pass

    def uninstall_mac_processor(self, interface, mac_profile):
        '''func desc
        '''
        pass

    '''
        Channel state information and spectrum scanning capabilities.
    '''

    def receive_csi(self, runt):
        '''Receives CSI samples from the ath9k driver.
        '''
        pass

    def scan_psd(self, runt):
        '''Receives PSD samples from the ath9k driver.
        '''
        pass
'''
    The protocol-specific definition of the WiSHFUL network control interface,
    UPI_N, for configuration/monitoring of the higher
    layers of the network protocol stack (upper MAC and higher).

    IEEE 802.11 protocol family
'''


class WifiNet(Network):
    ''' Upper MAC layer '''

    def connect_to_network(self, iface, **kwargs):
        '''Connects a given interface to some network

        e.g. WiFi network identified by SSID.
        '''
        return

    def add_device_to_blacklist(self, iface, device_mac_addr):
        '''Add the given device to the blacklist

        - 802.11 AP: the device is a client and the result of blacklisting
        is that the client cannot associate with this node.
        - Other??
        '''
        return

    def remove_device_from_blacklist(self, iface, device_mac_addr):
        '''Remove the given device from the blacklist

        - 802.11 AP: the device is a client and the result of unblacklisting
        is that the client can associate with this node.
        - Other??
        '''
        return

    def disconnect_device(self, iface, device_mac_addr):
        '''Disconnects the given device from this node

        - 802.11 AP: send dissassociation request to client device
        - 802.11 adhoc: no meaning
        - Other?
        '''
        return

    def register_new_device(self, iface, sta_mac_addr):
        '''Register the given device

        - 802.11 AP: the device is associated with this AP.
        - Other??
        '''
        return

    def trigger_channel_switch_in_device(self, iface, device_mac_addr, target_channel, serving_channel, **kwargs):
        '''Trigger a channel switch in the device connected to this node

        - 802.11 AP: send channel switch announcement to client STA,
        - other??
        '''
        return

    def get_info_of_connected_devices(self):
        '''Returns information about associated devices

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_inactivity_time_of_connected_devices(self):
        '''Returns information about associated devices - inactivity time

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_avg_sigpower_of_connected_devices(self):
        '''Returns information about associated devices - link average signal power

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_sigpower_of_connected_devices(self):
        '''Returns information about associated devices - link signal power

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_tx_retries_of_connected_devices(self):
        '''Returns information about associated devices - tx retries

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_tx_packets_of_connected_devices(self):
        '''Returns information about associated devices - tx packets

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_tx_failed_of_connected_devices(self):
        '''Returns information about associated devices - tx failed

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_tx_bytes_of_connected_devices(self):
        '''Returns information about associated devices - tx bytes

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_tx_bitrate_of_connected_devices(self):
        '''Returns information about associated devices - tx bitrate

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_rx_bytes_of_connected_devices(self):
        '''Returns information about associated devices - rx bytes

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_rx_packets_of_connected_devices(self):
        '''Returns information about associated devices - rx packets

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_authorized_connected_device(self):
        '''Returns information about associated devices - is authorized

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_authenticated_connected_device(self):
        '''Returns information about associated devices - is authenticated

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_used_preamble_connected_device(self):
        '''Returns information about associated devices - preamble used

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_mfp_connected_device(self):
        '''Returns information about associated devices - MFP

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_wmm_wme_connected_device(self):
        '''Returns information about associated devices - WMM/WME

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_tdls_peer_connected_device(self):
        '''Returns information about associated devices - TDLS peer

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return


'''
    The protocol-specific global events for performing network-wide operations
    which go beyond just remote UPI_R/N calls

    IEEE 802.11 protocol family
'''

class WiFiTriggerHandoverRequestEvent(TriggerHandoverRequestEvent):
    '''
    Event to trigger a WiFi handover operation. Only supported in infrastructure mode.
    '''
    def __init__(self, sta_mac_addr, sta_ip, wlan_iface, wlan_inject_iface, network_bssid, serving_AP, serving_AP_ip,
                 serving_channel, target_AP, target_AP_ip, target_channel, gateway, ho_scheme):
        super().__init__(sta_mac_addr, serving_AP, target_AP, gateway)
        self.sta_ip = sta_ip
        self.wlan_iface = wlan_iface
        self.wlan_inject_iface = wlan_inject_iface
        self.network_bssid = network_bssid
        self.servingAP_ip = serving_AP_ip
        self.servingChannel = serving_channel
        self.targetAP_ip = target_AP_ip
        self.targetChannel = target_channel
        self.ho_scheme = ho_scheme

class WiFiGetServingAPRequestEvent(NetFunEvent):
    '''
    Event to find out the access point serving a particular client station. Only supported in infrastructure mode.
    '''
    def __init__(self, sta_mac_addr, wifi_intf):
        super().__init__()
        self.sta_mac_addr = sta_mac_addr
        self.wifi_intf = wifi_intf

class WiFiGetServingAPReplyEvent(WiFiGetServingAPRequestEvent):
    '''
    Event containing the UUID of the AP serving the client station.
    '''
    def __init__(self, sta_mac_addr, wifi_intf, ap_uuid):
        super().__init__(sta_mac_addr, wifi_intf)
        self.ap_uuid = ap_uuid

class WiFiTestTwoNodesInCSRangeRequestEvent(NetFunEvent):
    '''
    Event to test whether two nodes are in carrier sensing range or not.
    '''
    def __init__(self, node1, node2, mon_dev, TAU):
        super().__init__()
        self.node1 = node1
        self.node2 = node2
        self.mon_dev = mon_dev
        self.TAU = TAU

class WiFiTestTwoNodesInCSRangeReplyEvent(WiFiTestTwoNodesInCSRangeRequestEvent):
    '''
    Event containing information about whether two nodes are in carrier sensing range or not.
    '''
    def __init__(self, node1, node2, mon_dev, TAU, in_cs):
        super().__init__(node1, node2, mon_dev, TAU)
        self.in_cs = in_cs


class WiFiGetNodesInCSRangeRequestEvent(NetFunEvent):
    '''
    Event to check each nodes pairs whether it is in carrier sensing range or not.
    '''
    def __init__(self, mon_dev, TAU):
        super().__init__()
        self.mon_dev = mon_dev
        self.TAU = TAU


class WiFiTestTwoNodesInCommRangeRequestEvent(NetFunEvent):
    '''
    Event to test whether two nodes are in communication range or not.
    '''
    def __init__(self, node1, node2, mon_dev, MINPDR):
        super().__init__()
        self.node1 = node1
        self.node2 = node2
        self.mon_dev = mon_dev
        self.MINPDR = MINPDR

class WiFiTestTwoNodesInCommRangeReplyEvent(WiFiTestTwoNodesInCommRangeRequestEvent):
    '''
    Event containing information about whether two nodes are in communication range or not.
    '''
    def __init__(self, node1, node2, mon_dev, MINPDR, in_comm):
        super().__init__(node1, node2, mon_dev, MINPDR)
        self.in_comm = in_comm


class WiFiGetNodesInCommRangeRequestEvent(NetFunEvent):
    '''
    Event to check each nodes pairs whether it is in communication range or not.
    '''
    def __init__(self, mon_dev, MINPDR):
        super().__init__()
        self.mon_dev = mon_dev
        self.TAU = MINPDR
