from .upi import Upi
from .upi import EventBase

__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Anatolij Zubow, Peter Ruckebusch, Domenico Garlisi"
__copyright__ = "Copyright (c) 2016, Technische Universitat Berlin, iMinds, CNIT"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de, peter.ruckebusch@intec.ugent.be"

'''
    The WiSHFUL network control interface, UPI_N, for configuration/monitoring of the higher
    layers of the network protocol stack (upper MAC and higher).
'''


# Generic API to control the higher layers, i.e. key-value configuration.
class Network(Upi):
    def set_parameters(self, iface, param_key_values_dict):
        """ The UPI_N interface is able to configure the protocol (routing, transport, application) behavior by changing parameters.
        Parameters correspond to the  variables used in the protocols.
        This function (re)set the value(s) of the parameters specified in the dictionary argument.
        The list of available parameters supported by all platforms/OS are defined in this module.
        Parameters specific to a subgroup of platforms/OS are defined in the corresponding submodules.
        A list of supported parameters can be dynamically obtained using the get_info function on each module.

        Examples:
            .. code-block:: python

                >> param_key_values = {ROUTING_MAX_TTL : 5}
                >> result = control_engine.net.set_parameters(param_key_values)
                >> print result
                {ROUTING_MAX_TTL : 0}

        Args:
            param_key_values_dict (dict): dictionary containing the key (string) value (any) pairs for each parameter.
                An example is {CSMA_CW : 15, CSMA_CW_MIN : 15, CSMA_CW_MAX : 15}

        Returns:
            dict: A dictionary containing key (string name) error (0 = success, 1=fail, +1=error code) pairs for each parameter.
        """
        return

    def get_parameters(self, iface, param_key_list):
        """ Get the parameter on higher layers of protocol stack (higher MAC and above)

        Args:
           param_key: the parameter identified by this key.

        Returns:
           the parameter value
        """
        return

    def get_measurements(self, iface, measurement_key_list):
        """

        Examples:
            .. code-block:: python

                >> measurement_keys = [NUM_FREEZING_COUNT]
                >> result = control_engine.net.iface("wlan0").get_measurements(measurement_keys)
                >> print result
                {UPI_RN.NUM_FREEZING_COUNT : 150}

        Args:
            measurement_key_list (list): list of requested measurements, an example of is [NUM_FREEZING_COUNT, TX_ACTIVITY].

        Returns:
            dict: A dictionary containing key (string name) and values of the requested measurements.
        """
        return

    def get_measurements_periodic(self, iface, measurement_key_list, collect_period, report_period, num_iterations, report_callback):
        """

        Examples:
            .. code-block:: python

                >> def my_cb(report):
                >>     for key in report.keys():
                >>         for measurement in report[key]:
                >>             print measurement
                >> measurement_keys = [NUM_FREEZING_COUNT, TX_ACTIVITY]
                >> result = control_engine.radio.iface("wlan0").get_measurements_periodic(measurement_keys,1000000,5000000,10,my_cb)
                >> print result
                {UPI_RN.NUM_FREEZING_COUNT : 150}

        Args:
            measurement_key_list (list): list of measurement keys. The keys are measurement names defined in this module.
            collect_period (int): defines the time between two consecutive measurement readings, in microsecond.
            report_period (int): defines the time between two consecutive reports to the control program, in microseconds.
            num_iterations (int): defines how many times the measurement collection has to be repeated.
            report_callback (function): the local callback that is invoked every report period.

        Returns:
            int: error code, 0 if success, 1 otherwise.
        """
        return

    def subscribe_events(self, iface, event_key_list, event_callback, event_duration):
        """

        Examples:
            .. code-block:: python

                >> event_keys = ["MAC_RX_EVENT","MAC_COLLISION_EVENT"]
                >> result = control_engine.radio.iface("wlan0").subscribe_events(event_keys, event_cb, 60)
                >> print result
                {"MAC_RX_EVENT" : 0, "MAC_COLLISION_EVENT":0}

        Args:
            event_key_list (list): List of events which should be monitored.
            event_callback (Callable): Callback called every time an event is posted.
            event_duration (int): Duration (in seconds) for which the event listener(s) should be active (0 = infinite)

        Returns:
            dict: A dictionary containing an error code for each event.
        """
        return

    def get_network_info(self, iface):
        return

    ''' App layer - set-up of packet flows '''

    def start_application(self, iface, application_id):
        return

    def stop_application(self, iface, application_id):
        return

    def create_packetflow_sink(self, port):
        '''Start IPerf server (TCP/IP)
        '''
        return

    def destroy_packetflow_sink(self):
        '''Stop IPerf server.
        '''
        return

    def start_packetflow(self, dest_ip, port=5001):
        '''Start IPerf client.
        '''
        return

    def stop_packetflow(self):
        '''Stop IPerf client.
        '''
        return

    # Net layer

    def get_iface_hw_addr(self, iface):
        '''Returns the hardware address (MAC address) of a given interface.
        '''
        return

    def get_iface_ip_addr(self, iface):
        '''Returns the IP address of a given interface.
        '''
        return

    def set_ip_address(self, iface, ip_address):
        '''Set ip address of the station
        '''
        pass

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


class NetEvent(EventBase):
    def __init__(self):
        super().__init__()
        pass
