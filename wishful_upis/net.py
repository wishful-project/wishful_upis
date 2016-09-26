from .upi import Upi
from .upi import EventBase

__author__ = "Piotr Gawlowicz, Anatolij Zubow, Mikolaj Chwalisz"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow, chwalisz}@tkn.tu-berlin.de"

'''
    The WiSHFUL network control interface, UPI_N, for configuration/monitoring of the higher
    layers of the network protocol stack (upper MAC and higher).
'''

# Generic API to control the higher layers, i.e. key-value configuration.

class Network(Upi):
    def set_parameter_higher_layer(self, **kwargs):
        """Set the parameter on higher layers of protocol stack (higher MAC and above)

        Args:
           param_key_value: key and value of this parameter
        """
        return


    def get_parameter_higher_layer(self, **kwargs):
        """Get the parameter on higher layers of protocol stack (higher MAC and above)

        Args:
           param_key: the parameter identified by this key.

        Returns:
           the parameter value
        """
        return

    ''' App layer - set-up of packet flows '''

    def install_application(self, app_desc):
        '''
        Install application in node. Possible applications are IperfClient and IperfServer.
        '''
        return

    ''' Network layer - routing, networking, etc. '''

    def get_ifaces(self):
        '''Returns list of interface names, e.g. ['lo', 'ens33', 'lxcbr0', 'ovs-system'].
        '''
        return


    def get_iface_hw_addr(self, iface):
        '''Returns the hardware address (MAC address) of a given interface.
        '''
        return


    def get_iface_ip_addr(self, iface):
        '''Returns the IP address of a given interface.
        '''
        return


    def set_ARP_entry(self, iface, mac_addr, ip_addr):
        '''Manipulates the entries in the ARP cache.
        '''
        return


    def change_routing(self, current_gw_ip_addr, new_gw_ip_addr, device_ip_addr):
        '''Controls the routing.
        '''
        return


    ''' Upper MAC layer - injection and sniffing of layer2 traffic '''

    def gen_layer2_traffic(self, iface, num_packets, pinter, max_phy_broadcast_rate_mbps=None, **kwargs):
        '''Inject layer2 traffic into network device.
        '''
        return


    def inject_frame(self, iface, frame, is_layer_2_packet, tx_count=1, pkt_interval=1):
        '''Inject L2/L3 frame injection into the protocol stack
        '''
        return


    def sniff_layer2_traffic(self, iface, sniff_timeout, **kwargs):
        '''Layer-2 packet sniffing from network device.
        '''
        return


    ''' Controlling network emulation (netem), i.e. emulation of variable delay, loss, duplication and re-ordering. '''

    def set_netem_profile(self, iface, profile):
        """Func Desc
        """
        return


    def update_netem_profile(self, iface, profile):
        """Func Desc
        """
        return


    def remove_netem_profile(self, iface):
        """Func Desc
        """
        return


    def set_per_link_netem_profile(self, iface, dstIpAddr, profile):
        """Func Desc
        """
        return


    def update_per_link_netem_profile(self, iface, dstIpAddr, profile):
        """Func Desc
        """
        return


    def remove_per_link_netem_profile(self, iface, dstIpAddr):
        """Func Desc
        """
        return


    ''' Controlling queuing disciplines '''

    def install_egress_scheduler(self, iface, scheduler):
        """Func Desc
        """
        return


    def remove_egress_scheduler(self, iface):
        """Func Desc
        """
        return


    ''' Network filter tables '''

    def clear_nf_tables(self, table="ALL", chain="ALL"):
        """Func Desc
        """
        return

    def get_nf_table(self, tableName):
        """Func Desc
        """
        return

    ''' Packet marking - IP ToS '''

    def set_pkt_marking(self, flowId, markId=None, table="mangle", chain="POSTROUTING"):
        """Func Desc
        """
        return


    def del_pkt_marking(self, flowId, markId=None, table="mangle", chain="POSTROUTING"):
        """Func Desc
        """
        return

    ''' Packet mangling - IP ToS '''

    def set_ip_tos(self, flowId, tos, table="mangle", chain="POSTROUTING"):
        """Func Desc
        """
        return


    def del_ip_tos(self, flowId, tos, table="mangle", chain="POSTROUTING"):
        """Func Desc
        """
        return


"""
Application classes:
 (1) iperf

 TODO: move me to app.py
"""

class Application(object):
    def __init__(self):
        # do not include logging here, beacuse this cannot be pickled
        self.startTime = 0
        self.type = None
        self.resultReportInterval = None
        self.port = 5001
        self.protocol = "TCP"
        self.tcpWindow = None

        self.results = []
        self.newResult = False

    def setStartTime(self, value):
        self.startTime = value

    def setProtocol(self, protocol):
        self.protocol = protocol

    def setPort(self, port):
        self.port = port

    def collectResults(self, result):
        self.results.append(result)
        self.newResult = True

    def isNewResult(self):
        return self.newResult

    def getResult(self):
        retValue = self.results[0]
        del self.results[0]
        return retValue

class ServerApplication(Application):
    def __init__(self):
        super(ServerApplication, self).__init__()
        self.type = "Server"
        self.bind = None

    def setBind(self, bind):
        self.bind = bind


class ClientApplication(Application):
    def __init__(self):
        super(ClientApplication, self).__init__()
        self.type = "Client"
        self.destination = None
        self.udpBandwidth = "1M"
        self.dualtest = False
        self.dataToSend = None
        self.transmissionTime = None
        self.frameLen = None

    def setDestination(self, dest):
        self.destination = dest

    def setBandwidth(self, band):
        self.udpBandwidth = band

    def setDualTest(self, value):
        self.dualtest = value

    def setDataSize(self, value):
        self.dataToSend = value

    def setTransmissionTime(self, value):
        self.transmissionTime = value

    def setFrameLen(self, value):
        self.frameLen = value


class RawperfClientApplication(Application):
    def __init__(self):
        super(RawperfClientApplication, self).__init__()
        self.type = "RawperfClient"
        self.destination = None
        self.udpBandwidth = "1M"
        self.dualtest = False
        self.dataToSend = None
        self.transmissionTime = None
        self.frameLen = None
        self.waitTime = 1

    def setWaitTime(self, value):
        self.waitTime = value

    def setDestination(self, dest):
        self.destination = dest
        pass
    def setBandwidth(self, band):
        self.udpBandwidth = band

    def setDualTest(self, value):
        self.dualtest = value

    def setDataSize(self, value):
        self.dataToSend = value

    def setTransmissionTime(self, value):
        self.transmissionTime = value

    def setFrameLen(self, value):
        self.frameLen = value


'''
    List of events
'''
class NetEvent(EventBase):
    def __init__(self):
        super().__init__()
        pass

