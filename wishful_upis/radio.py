"""The WiSHFUL radio control interface, UPI_R.
Used for configuration/monitoring of the lower
layers of the network protocol stack (lower MAC and PHY).

Note, here all generic functions are defined, i.e. those which can be
supported by any wireless networking node (IEEE 802.11, LTE, ZigBee).

All protocol-dependent functions are defined in separate folder,
e.g. ``wifi/``, ``lowpan/`` or ``lte/``.
"""
from .lte.radio import *
from .wifi.radio import *
from .lowpan.radio import *


__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Anatolij Zubow, Peter Ruckebusch, Domenico Garlisi"
__copyright__ = "Copyright (c) 2016, Technische Universitat Berlin, iMinds, CNIT"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de, peter.ruckebusch@intec.ugent.be, "

PARAMETERS = [
    "TX_POWER",
    "RX_CHANNEL"
]



# Generic API to control the lower layers, i.e. key-value configuration.
def set_parameters(param_key_values_dict):
    """The UPI_R interface is able to configure the radio and MAC behavior by changing parameters.
    Parameters correspond to the configuration registers of the hardware platform and to the variables used in
    the radio programs. This function (re)set the value(s) of the parameters specified in
    the dictionary argument. The list of available parameters supported by all platforms are defined in this module.
    Parameters specific to a subgroup of platforms are defined in the corresponding submodules.
    A list of supported parameters can be dynamically obtained using the get_radio_info function.

    Examples:
        .. code-block:: python

            >> param_key_values = {CSMA_CW : 15, UPI_RN.CSMA_CW_MIN : 15, UPI_RN.CSMA_CW_MAX : 15}
            >> result = control_engine.radio.iface("wlan0").set_parameters(param_key_values)
            >> print result
            {CSMA_CW : 0, CSMA_CW_MIN : 0, CSMA_CW_MAX : 0}

    Args:
        param_key_values_dict (dict): dictionary containing the key (string) value (any) pairs for each parameter.
            An example is {CSMA_CW : 15, CSMA_CW_MIN : 15, CSMA_CW_MAX : 15}

    Returns:
        dict: A dictionary containing key (string name) error (0 = success, 1=fail, +1=error code) pairs for each parameter.
    """
    return


def get_parameters(param_key_list):
    """The UPI_R interface is able to obtain the current radio and MAC configuration by getting parameter values.
    Parameters correspond to the configuration registers of the hardware platform and to the variables used in the
    radio programs. This function get(s) the value(s) of the parameters specified in the list argument.
    The list of available parameters supported by all platforms are defined in this module.
    Parameters specific to a subgroup of platforms are defined in the corresponding submodules.
    A list of supported parameters can be dynamically obtained using the get_radio_info function.

    Examples:
        .. code-block:: python

            >> param_keys = [CSMA_CW,CSMA_CWMIN]
            >> result = control_engine.radio.iface("wlan0").get_parameters(param_keys)
            >> print result
            {CSMA_CW : 15, CSMA_CWMIN : 15}

    Args:
        param_key_list (list): list of parameter names, an example is [UPI_RN.CSMA_CW, UPI_RN.CSMA_CW_MIN, UPI_RN.CSMA_CW_MAX].

    Returns:
        dict: A dictionary containing key (string name) and values of the requested parameters.
     """
    return


def get_measurements(measurement_key_list):
    """The UPI_R interface is able to get the radio measurements in a pull based manner.
    The low-level measurements are continuously monitored by the hardware platform and by the radio programs.
    They can be used to get information and statistics about the state of the physical links or the internal state of the node.
    This function gets the measurements specified in the list argument and returns a dictionary with their values.
    The list of available measurements supported by all platforms are defined in this module.
    Measurements specific to a subgroup of platforms are defined in the corresponding submodules.
    A list of supported measurements can be dynamically obtained using the get_radio_info function.

    Examples:
        .. code-block:: python

            >> measurement_keys = [NUM_FREEZING_COUNT]
            >> result = control_engine.radio.iface("wlan0").get_measurements(measurement_keys)
            >> print result
            {UPI_RN.NUM_FREEZING_COUNT : 150}

    Args:
        measurement_key_list (list): list of requested measurements, an example of is [NUM_FREEZING_COUNT, TX_ACTIVITY].

    Returns:
        dict: A dictionary containing key (string name) and values of the requested measurements.
    """
    return


def get_measurements_periodic(measurement_key_list, collect_period, report_period, num_iterations, report_callback):
    """The UPI_R interface is able to get the radio measurements in a pull based manner periodically.
    This function works similarly to  get_measurements, it gets the value(s) specified in the list argument and returns a dictionary with their values, but in cycling mode.
    The function gets the measurements every collect_period and stores them on node memory. Every report_period all measurements are reported to the controller.
    This operation is performed a number of times specified by num_iterations. A callback function is used to receive the measurements results.
    The list of available measurements supported by all platforms are defined in this module. Measurements specific to a subgroup of platforms are defined in the corresponding submodules.
    A list of supported measurements can be dynamically obtained using the get_radio_info function.

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


def subscribe_events(event_key_list, event_callback, event_duration):
    """The UPI_R interface is able to monitor the radio and mac behavior asynchronously through events.
    This function subscribes an event listener for one or more events for the specified event duration (0 = infinite).
    The event callback is called each time on of the event is posted.
    The list of available events supported by all platforms are defined in this module.
    Events specific to a subgroup of platforms are defined in the corresponding submodules.
    A list of supported events can be dynamically obtained using the get_radio_info function.

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

# Activation and deactivation of radio programs.


def activate_radio_program(name):
    """This function activates the specified radio program.
    When executed, this function stops the current radio program and enables the execution of the radio program specified in the parameter name.

    Examples:
        .. code-block:: python

           >> result = control_engine.radio.iface("wlan0").activate_radio_program("CSMA")
           >> print result
           0

    Args:
        name (str): String identifier of the radio program (e.g. CSMA, TDMA, TSCH)

    Returns:
        int: - 0 if the parameter setting call was successfully performed
            - 1 partial success
            - 2 error.
    """
    return


def deactivate_radio_program(name):
    """When executed, this function stops the radio program specified in the parameter radio_program_name.

    Examples:
        .. code-block:: python

            >> result = control_engine.radio.iface("wlan0").deactivate_radio_program("CSMA")
           >> print result
           0

    Args:
        name (str): String identifier of the radio program (e.g. CSMA, TDMA, TSCH)

    Returns:
        int:
            - 0 if the parameter setting call was successfully performed
            - 1 partial success
            - 2 error.
    """
    return


def get_running_radio_program():
    """Returns active radio program.

    Each radio program is associated with a name and an index. When executed,
    this function return the index of the radio program active.

    Examples:
        .. code-block:: python

            >> args = {'interface' : 'wlan0'}
            >> result = UPI_RN.getActive(args)
            >> print result
            2

    Args:
        myargs:
            a dictionary data type (key: value) where the keys are:
            The key "interface" specify the network interface to use.

    Returns:
        the index of the active radio program
    """
    return

''' Transmission of radio waveform (no MAC) '''


def play_waveform(iface, freq, power_lvl, **kwargs):
    '''Starts transmitting a radio waveform (just PHY, no MAC).
    '''
    pass


def stop_waveform(iface, **kwargs):
    '''Stops transmitting a radio waveform.
    '''
    pass

#to rename when will be updated the wifi module
#def set_tx_power(power_dBm):
def set_power(power_dBm):
    '''func desc

    Args:
        power_dBm (TYPE): Description
    '''
    pass

#to rename when will be updated the wifi module
#def get_tx_power():
def get_power():
    '''func desc
    '''
    pass

def get_noise():
    '''Returns the noise floor measured by the wireless driver.
    '''
    pass


def start_csi_measurements(callback):
    '''Receives channel state information. (amplitude + phase)
    '''
    pass


def stop_csi_measurements():
    '''Receives channel state information. (amplitude + phase)
    '''
    pass


def get_radio_platforms():
    """ Gets available NIC on board and type of supported platforms. The information elements used by the UPI_R
    interface, to manage parameters, measurements and radio program, are organized into data structures,
    which provide information on the platform type and radio capabilities.
    When executed, this function return information about available interfaces on node, the name or the identifier
    of the interface and the supported platform type.

    :return current_NIC_list: a list of pair value, the first value is the interface identifier and the second is the supported platforms.

    example:
        >> current_NIC_list = RadioPlatform_t()
        >> current_NIC_list_string = UPI_RN.getRadioPlatforms()
        >> current_NIC_list.platform_info =  current_NIC_list_string[0]
        >> current_NIC_list.platform =  current_NIC_list_string[1]
    """
    return


def get_radio_info(radio_id):
    """Gets the radio capabilities of a given network card RadioPlatform_t in terms of supported measurement and supported
    parameter and list of supported radio program. The information elements used by the UPI_R interface, to manage
    parameters, measurements and radio program, are organized into data structures, which provide information
    on the platform type and radio capabilities. When executed, this function return information about available
    radio capabilities (measurements and parameters) of each interface (RadioPlatform_t) on the available radio programs
    (radio_prg_t) available for transmissions over the radio interface.

    :param radio_id: network interfaces to use
    :return result: return a list in term of a dictionary data type (list of key: value). in which are present the key showed below:
            'radio_info' --> a list of pair value, the first value is the interface identifier and the second is the supported platforms.
            'monitor_list' --> a list of supported measurements between the attribute of the class UPI_R
            'param_list' --> a list of supported Parameters between the attribute of the class UPI_R
            'exec_engine_list_name' --> a list of supported execution environment name
            'exec_engine_list_pointer' --> a list of supported execution environment path
            'radio_prg_list_name'--> a list of supported radio program name
            'radio_prg_list_pointer' --> a list of supported radio program path

    example:
            >> interface = 'wlan0'\n
            >> current_platform_info = radio_info_t()\n
            >> param_key = {'platform' : 'wmp'}\n
            >> current_platform_info_str = UPI_RN.getRadioInfo(interface, param_key)\n
            >> current_platform_info.platform_info.platform_id = current_platform_info_str['radio_info'][0]\n
            >> current_platform_info.platform_info.platform = current_platform_info_str['radio_info'][1]\n
            >> current_platform_info.monitor_list = current_platform_info_str['monitor_list']\n
            >> current_platform_info.param_list = current_platform_info_str['param_list']\n
            >> current_platform_info.execution_engine_list_name = current_platform_info_str['exec_engine_list_name']\n
            >> current_platform_info.execution_engine_list_pointer = current_platform_info_str['exec_engine_list_pointer']\n
            >> current_platform_info.radio_program_list_name = current_platform_info_str['radio_prg_list_name']\n
            >> current_platform_info.radio_program_list_path = current_platform_info_str['radio_prg_list_pointer']\n
    """
    return


def set_rxchannel(freq_Hz, bandwidth):
    '''func desc
    '''
    pass


def get_rxchannel():
    '''func desc
    '''
    pass


def set_txchannel(freq_Hz, bandwidth):
    '''func desc
    '''
    pass


def get_txchannel():
    '''func desc
    '''
    pass


def get_hwaddr():
    '''func desc
    '''
    pass