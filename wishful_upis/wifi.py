from .net import Network
from .radio import Radio
from .net_func import NetFun

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
    The protocol-specific definition of WiSHFUL global control
    interface, UPI_G, for performing network-wide operations
    which go beyond just remote UPI_R/N calls

    IEEE 802.11 protocol family
'''


class WifiNetFun(NetFun):
    def perform_handover(self, interface, servingNode, targetNode, device_mac_addr, **kwargs):
        '''Performing an handover operation.

        Note: this is not supported on any wireless technology.

        - 802.11 - in infrastructure mode an STA can be handovered; not supported in 802.11 adhoc
        '''
        pass

    def is_associated_with(self, nodes, interface, device_mac_addr):
        '''Estimate the AP/BS with which a given device is associated.

        Note: this is not supported on any wireless technology.

        - enabled on 802.11 infrastructure mode
        '''
        pass
