from .net import Network
from .radio import Radio
from .net_func import TriggerHandoverRequestEvent
from .net_func import NetFunEvent

__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de"


'''
The protocol-specific definition of the WiSHFUL radio control
interface, UPI_R, for configuration/monitoring of the
lower layers of the network protocol stack (lower MAC and PHY).

IEEE 802.11 protocol family
'''


class WifiRadio(Radio):

    def set_mac_access_parameters(self, iface, queueId, qParam):
        '''
        MAC access parameters in 802.11e: the configuration
        of the access categories
        '''
        pass

    def get_mac_access_parameters(self, queueId):
        '''
        MAC access parameters: in 802.11e:
        the configuration of the access categories
        '''
        pass

    def get_airtime_utilization(self):
        '''
        Returns the relative time the spectrum is empty.
        '''
        pass

    def perform_spectral_scanning(self, iface, freq_list, mode):
        '''
        Perform spectral scanning.

        Returns:
            Power value for each frequency bin.
        '''
        pass

    def set_channel(self, channel, iface):
        '''
        Set channel for given interface,
        i.e. center frequency of the primary band.

        Args:
            channel: channel to set
            iface: interface
        '''
        pass

    def get_channel(self, iface):
        '''
        Get channel of given interface,
        i.e. center frequency of the primary band.

        Args:
            iface: interface
        '''
        pass

    def set_modulation_rate(self, rate_Mbps):
        '''
        Set rate modulation
        '''
        pass

    def configure_radio_sensitivity(self, phy_dev, **kwargs):
        '''
        Configuring the receiving sensitivity of the IEEE 802.11 radio.
        '''
        pass

    ''' Per flow transmit power control '''

    def set_per_flow_tx_power(self, iface, flowId, txPower):
        """
        Sets for a flow identified by an 5-tuple
        (IP header) the transmit power to be used.
        """
        return

    def clean_per_flow_tx_power_table(self, iface):
        """
        Remove any entries in the transmit power table.
        """
        return

    def get_per_flow_tx_power(self, flowId):
        """
        Return the transmit power level used for the given flow.
        """
        return

    def get_per_flow_tx_power_table(self, iface):
        """
        Return the whole transmit power table.
        """
        return

    def install_mac_processor(self, interface, mac_profile):
        """
        Install new WiFi MAC Processor
        """
        return

    def update_mac_processor(self, interface, mac_profile):
        '''
        Update WiFi MAC Processor
        '''
        pass

    def uninstall_mac_processor(self, interface, mac_profile):
        '''
        Uninstall new WiFi MAC Processor
        '''
        pass

    '''
        Channel state information and spectrum scanning capabilities.
    '''

    def receive_csi(self, runt):
        '''
        Receives CSI samples from the ath9k driver.
        '''
        pass

    def scan_psd(self, runt):
        '''
        Receives PSD samples from the ath9k driver.
        '''
        pass

    def is_rf_blocked(self, iface):
        '''
        Returns information about rf blocks (Soft Block, Hard Block)
        '''
        pass


    def rf_unblock(self, iface):
        '''
        Turn off the softblock
        '''
        pass


    def set_power_management(self, iface, value):
        '''
        Sets power management
        '''


    def get_power_management(self, iface):
        '''
        Get power management
        '''


    def set_retry_short(self, iface, value):
        '''
        Sets retry short
        '''


    def get_retry_short(self, iface):
        '''
        Get retry short
        '''


    def set_retry_long(self, iface, value):
        '''
        Sets retry long
        '''


    def get_retry_long(self, iface):
        '''
        Get retry long
        '''


    def set_rts_threshold(self, iface, value):
        '''
        Sets RTS threshold
        '''


    def get_rts_threshold(self, iface):
        '''
        Get RTS threshold
        '''


    def set_fragmentation_threshold(self, iface, value):
        '''
        Sets framgmentation threshold
        '''


    def get_fragmentation_threshold(self, iface):
        '''
        Get framgmentation threshold
        '''


    def get_supported_modes(self, iface):
        '''
        Get supported WiFi modes
        '''


    def get_supported_swmodes(self, iface):
        '''
        Get supported WiFi software modes
        '''


    def get_rf_band_info(self, iface):
        '''
        Get info about supported RF bands
        '''


    def get_ciphers(self, iface):
        '''
        Get info about supported ciphers
        '''


    def get_supported_wifi_standards(self, iface):
        '''
        Get info about supported WiFi standards, i.e. 802.11a/n/g/ac/b
        '''


'''
    UPIs to add:
    ['new_interface', 'set_interface', 'new_key', 'start_ap', 'new_station', 'new_mpath', 'set_mesh_config',
    'set_bss', 'authenticate', 'associate', 'deauthenticate', 'disassociate', 'join_ibss', 'join_mesh',
    'remain_on_channel', 'set_tx_bitrate_mask', 'frame', 'frame_wait_cancel', 'set_wiphy_netns', 'set_channel',
    'set_wds_peer', 'tdls_mgmt', 'tdls_oper', 'probe_client', 'set_noack_map', 'register_beacons', 'start_p2p_device',
    'set_mcast_rate', 'connect', 'disconnect']
'''

"""
Base class for all MAC layers
"""
class AbstractMAC(object):
    def __init__(self):
        pass


"""
A hybrid TDMA CSMA MAC
"""
class HybridTDMACSMAMac(AbstractMAC):
    def __init__(self, no_slots_in_superframe, slot_duration_ns):
        super(HybridTDMACSMAMac, self).__init__()
        self.name = "hybridTDMACSMA"
        self.desc = "currently works only with patched ath9k"
        self.mNo_slots_in_superframe = no_slots_in_superframe
        self.mSlot_duration_ns = slot_duration_ns
        self.acs = []
        for ii in range(no_slots_in_superframe):
            self.acs.append(None)

    def getName(self):
        return self.name

    def getNumSlots(self):
        return self.mNo_slots_in_superframe

    def addAccessPolicy(self, slot_nr, ac):
        self.acs[slot_nr] = ac

    def getAccessPolicy(self, slot_nr):
        return self.acs[slot_nr]

    def getSlotDuration(self):
        return self.mSlot_duration_ns

    def printConfiguration(self):
        s = '['
        for ii in range(self.getNumSlots()):
            s = s + str(ii) + ': ' + self.getAccessPolicy(ii).printConfiguration() + "\n"
        s = s + ']'
        return s


"""
AccessPolicy for each slot
"""
class AccessPolicy(object):

    def __init__(self):
        self.entries = []

    def disableAll(self):
        self.entries = []

    def allowAll(self):
        self.entries = []
        self.entries.append(('FF:FF:FF:FF:FF:FF', 255))

    def addDestMacAndTosValues(self, dstHwAddr, *tosArgs):
        """add destination mac address and list of ToS fields
        :param dstHwAddr: destination mac address
        :param tosArgs: list of ToS values to be allowed here
        """

        tid_map = 0
        for ii in range(len(tosArgs)):
            # convert ToS into tid
            tos = tosArgs[ii]
            skb_prio = tos & 30 >> 1
            tid = skb_prio & 7
            tid_map = tid_map | 2**tid

        self.entries.append((dstHwAddr, tid_map))

    def getEntries(self):
        return self.entries

    def printConfiguration(self):
        s = ''
        for ii in range(len(self.entries)):
            s = str(self.entries[ii][0]) + "/" + str(self.entries[ii][1]) + "," + s
        return s


class EdcaQueueParameters(object):
    def __init__(self, aifs=1, cwmin=1, cwmax=1023, txop=0):
        self.setAifs(aifs)
        self.setCwMin(cwmin)
        self.setCwMax(cwmax)
        self.setTxOp(txop)
        pass

    def setAifs(self, value):
        if value < 0:
            value = 0
        if value > 255:
            value = 255

        self.mAifs = value
        pass

    def getAifs(self):
        return self.mAifs

    def setCwMin(self, value):
        if (value <= 1):
            value = 1
        if (1 < value <= 3):
            value = 3
        if (3 < value <= 7):
            value = 7
        if (7 < value <= 15):
            value = 15
        if (15 < value <= 31):
            value = 31
        if (31 < value <= 63):
            value = 63
        if (63 < value <= 127):
            value = 127
        if (127 < value <= 255):
            value = 255
        if (255 < value <= 511):
            value = 511
        if (511 < value):
            value = 1023

        self.mCwMin = value
        pass

    def getCwMin(self):
        return self.mCwMin

    def setCwMax(self, value):
        if (value <= 1):
            value = 1
        if (1 < value <= 3):
            value = 3
        if (3 < value <= 7):
            value = 7
        if (7 < value <= 15):
            value = 15
        if (15 < value <= 31):
            value = 31
        if (31 < value <= 63):
            value = 63
        if (63 < value <= 127):
            value = 127
        if (127 < value <= 255):
            value = 255
        if (255 < value <= 511):
            value = 511
        if (511 < value):
            value = 1023
        self.mCwMax = value
        pass

    def getCwMax(self):
        return self.mCwMax

    def setTxOp(self, value):
        if (value <= 0):
            value = 0
        if (value > 999):
            value = 999

        self.mTxOp = value
        pass

    def getTxOp(self):
        return self.mTxOp


'''
    The protocol-specific definition of the WiSHFUL network control interface,
    UPI_N, for configuration/monitoring of the higher
    layers of the network protocol stack (upper MAC and higher).

    IEEE 802.11 protocol family
'''


class WifiNet(Network):
    ''' Upper MAC layer '''

    def set_ap_conf(iface, config):
        '''
        Set hostapd configuration, provide functionality
        to setting Access Point station
        '''
        pass

    def start_ap(self):
        '''
        Start hostapd, provide functionality to run Access Point
        '''
        pass

    def stop_ap(self):
        '''
        Stop hostapd, provide functionality to stop Access Point
        '''
        pass

    def connect_to_network(self, iface, **kwargs):
        '''
        Connects a given interface to some network
        e.g. WiFi network identified by SSID.
        '''
        return

    def network_dump(iface):
        '''
        Return the connection information a given
        interface to some network
        '''
        return

    def add_device_to_blacklist(self, iface, device_mac_addr):
        '''
        Add the given device to the blacklist

        - 802.11 AP: the device is a client and the result of blacklisting
        is that the client cannot associate with this node.
        - Other??
        '''
        return

    def remove_device_from_blacklist(self, iface, device_mac_addr):
        '''
        Remove the given device from the blacklist

        - 802.11 AP: the device is a client and the result of unblacklisting
        is that the client can associate with this node.
        - Other??
        '''
        return

    def disconnect_device(self, iface, device_mac_addr):
        '''
        Disconnects the given device from this node

        - 802.11 AP: send dissassociation request to client device
        - 802.11 adhoc: no meaning
        - Other?
        '''
        return

    def register_new_device(self, iface, sta_mac_addr):
        '''
        Register the given device

        - 802.11 AP: the device is associated with this AP.
        - Other??
        '''
        return

    def trigger_channel_switch_in_device(self, iface,
                                         device_mac_addr, target_channel,
                                         serving_channel, **kwargs):
        '''
        Trigger a channel switch in the device connected to this node

        - 802.11 AP: send channel switch announcement to client STA,
        - other??
        '''
        return

    def get_info_of_connected_devices(self, iface):
        '''
        Returns information about associated devices

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_inactivity_time_of_connected_devices(self, iface):
        '''
        Returns information about associated devices - inactivity time

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_avg_sigpower_of_connected_devices(self, iface):
        '''
        Returns information about associated devices,
        i.e. link average signal power

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_sigpower_of_connected_devices(self, iface):
        '''
        Returns information about associated devices - link signal power

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_tx_retries_of_connected_devices(self, iface):
        '''
        Returns information about associated devices - tx retries

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_tx_packets_of_connected_devices(self, iface):
        '''
        Returns information about associated devices - tx packets

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_tx_failed_of_connected_devices(self, iface):
        '''
        Returns information about associated devices - tx failed

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_tx_bytes_of_connected_devices(self, iface):
        '''
        Returns information about associated devices - tx bytes

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_tx_bitrate_of_connected_devices(self, iface):
        '''
        Returns information about associated devices - tx bitrate

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_rx_bytes_of_connected_devices(self, iface):
        '''
        Returns information about associated devices - rx bytes

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_rx_packets_of_connected_devices(self, iface):
        '''
        Returns information about associated devices - rx packets

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_authorized_connected_device(self, iface):
        '''
        Returns information about associated devices - is authorized

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_authenticated_connected_device(self, iface):
        '''
        Returns information about associated devices - is authenticated

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_used_preamble_connected_device(self, iface):
        '''
        Returns information about associated devices - preamble used

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_mfp_connected_device(self, iface):
        '''
        Returns information about associated devices - MFP

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_wmm_wme_connected_device(self, iface):
        '''
        Returns information about associated devices - WMM/WME

        - 802.11 AP: info about the associated client devices of that AP.
        - Other??
        '''
        return

    def get_tdls_peer_connected_device(self, iface):
        '''
        Returns information about associated devices - TDLS peer

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
    Event to trigger a WiFi handover operation.
    Only supported in infrastructure mode.
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
    Event to find out the access point serving
    a particular client station. Only supported
    in infrastructure mode.
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
    Event containing information about whether two
    nodes are in carrier sensing range or not.
    '''
    def __init__(self, node1, node2, mon_dev, TAU, in_cs):
        super().__init__(node1, node2, mon_dev, TAU)
        self.in_cs = in_cs


class WiFiGetNodesInCSRangeRequestEvent(NetFunEvent):
    '''
    Event to check each nodes pairs whether it is
    in carrier sensing range or not.
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
    Event containing information about whether two
    nodes are in communication range or not.
    '''
    def __init__(self, node1, node2, mon_dev, MINPDR, in_comm):
        super().__init__(node1, node2, mon_dev, MINPDR)
        self.in_comm = in_comm


class WiFiGetNodesInCommRangeRequestEvent(NetFunEvent):
    '''
    Event to check each nodes pairs whether it is
    in communication range or not.
    '''
    def __init__(self, mon_dev, MINPDR):
        super().__init__()
        self.mon_dev = mon_dev
        self.TAU = MINPDR
