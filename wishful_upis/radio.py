from .lte.radio import *
from .wifi.radio import *
from .zigbee.radio import *


__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de"

'''
    The WiSHFUL radio control interface, UPI_R, for configuration/monitoring of the lower
    layers of the network protocol stack (lower MAC and PHY).
    Note, here all generic functions are defined, i.e. those which can be supported by any wireless networking node (IEEE 802.11, LTE, ZigBee).
    All protocol-dependent functions are defined in separate folder, e.g. wifi/ or lte/
'''

''' Generic API to control the lower layers, i.e. key-value configuration. '''

def set_parameter_lower_layer(**kwargs):
    """ The UPI_R interface is able to configure the radio behavior thanks to the abstraction of the hardware
    platform and radio programs in terms of Radio Capabilities. A subset of radio capabilities are the parameter.
    Parameters correspond to the configuration registers of the hardware platform and to the variables used in
    the radio programs. This function (re)set the value(s) of the Parameters Radio Capabilities specified in
    the dictionary argument. The list of available parameters is defined as attributes of the UPI_R class,
    you can use the UPI_RN.getRadioInfo function to find the platform supported parameters.
    :param myargs: list of parameters and values to set, in term of a dictionary data type (list of key: value) in which keys is the interface ('interface') to specify network interface to be uses and the desired UPI_R attribute, and value is the value to set. An example of argument dictionary data type is {UPI_RN.CSMA_CW : 15, UPI_RN.CSMA_CW_MIN : 15, UPI_RN.CSMA_CW_MAX : 15}.
    :return result: return 0 if the parameter setting call was successfully performed, 1 partial success, 2 error.
    :example:
        >> args = {'interface' : 'wlan0', UPI_RN.CSMA_CW : 15, UPI_RN.CSMA_CW_MIN : 15, UPI_RN.CSMA_CW_MAX : 15}\n
        >> result = UPI_RN.setParameterLowerLayer(args)\n
        >> print result\n
        [0, 0, 0]\n
    """
    return


def get_parameter_lower_layer(**kwargs):
    """ The UPI_R interface is able to configure the radio behavior thanks to the abstraction of the hardware
    platform and radio programs in terms of Radio Capabilities. A subset of radio capabilities are the parameters.
    Parameters correspond to the configuration registers of the hardware platform and to the variables used in the
    radio programs.
    This function get the value(s) of the Parameters Radio Capabilities specified in the dictionary argument.
    The available parameters are defined as attributes of the UPI_R clas, you can use the UPI_RN.getRadioInfo function
    to find the platform supported parameters.
    :param myargs: list of parameters, in term of a dictionary data type (list of key: value) in which:the key is 'parameters' and the value is a list of UPI_R attributes for parameters, the key in 'interface' specify network interface to be uses. An argument dictionary example is {'interface' : 'wlan0', 'PARAMETERS' : [UPI_RN.CSMA_CW, UPI_RN.CSMA_CW_MIN, UPI_RN.CSMA_CW_MAX]}.
    :return result: list of parameters and values, in term of a dictionary data type (list of key: value) in which the key is the UPI_R class attribute, and value is the current setting of the attribute. An example of argument dictionary data type is {UPI_RN.CSMA_CW : 15, UPI_RN.CSMA_CW_MIN : 15, UPI_RN.CSMA_CW_MAX : 15}.
    :example:
        >> args = {'interface' : 'wlan0', 'parameters' : [UPI_RN.CSMA_CW] }\n
        >> result = UPI_RN.getParameterLowerLayer(args)\n
        >> print result\n
        {UPI_RN.CSMA_CW : 15}\n
    """
    return


def get_monitor(**kwargs):
    """ The UPI_R interface is able to get the radio measurements thanks to the abstraction of the hardware
    platform and radio programs in terms of Radio Capabilities. A subset of radio capabilities are the low-level
    measurements. The low-level measurements are continuously monitored by the hardware platform and by the
    radio programs. The measurement capabilities can be used to get information and statistics about the state of
    the physical links or the internal state of the node.
    This function get the value(s) of the Measurements Radio Capabilities specified in the dictionary
    argument. The list of available measurements are defined as attribute of the UPI_R class, you can use the
    UPI_RN.getRadioInfo function to find the platform supported measurements.
    :param myargs: list of parameters, in term of a dictionary data type (list of key: value) in which: the key is 'measurements' and the value is a list of UPI_R attributes for measurements, the key in 'interface' specify network interface to be uses. An example of argument dictionary is {"measurements" : [UPI_RN.NUM_FREEZING_COUNT, UPI_RN.TX_ACTIVITY]}.
    :return result: list of parameters and values, in term of a dictionary data type (list of key: value) in which the key are the UPI_R attributes for measurements, and value is the reading of the measurement. An example of argument dictionary data type is {UPI_RN.NUM_FREEZING_COUNT : 150, UPI_RN.TX_ACTIVITY : 45670}.
    :example:
        >> args = {'interface' : 'wlan0', 'measurements' : [UPI_RN.NUM_FREEZING_COUNT] }\n
        >> result = UPI_RN.getMonitor(args)\n
        >> print result\n
        {UPI_RN.NUM_FREEZING_COUNT : 150}\n
    """
    return

''' Activation and deactivation of radio programs. '''

def set_active(**kwargs):
    """ This function activates the passed radio program, one the platform. When executed, this function stops the
    current radio program and enables the execution of the radio program specified in the parameter
    radioProgramName. Two additional parameters can be used, one of these is required.The path of the radio program
    description is required. The optionally parameter specify the index, in order to associate an index to the radio
    program.
    :param myargs: a dictionary data type (key: value) where the keys are: The key 'interface' specify the network interface to use. The key 'radio_program_name'specify the name of radio program. The key 'path' in which the value specify the path of radio program description, and 'position' in which the value specify the radio program index associated.
    :return result:  return 0 if the parameter setting call was successfully performed, 1 partial success, 2 error.
    :example:
        >> args = {'interface' : 'wlan0', 'radio_program_name' : 'CSMA', 'path': './radio_program/csma.txt'} \n
        >> result = UPI_RN.setActive(args) \n
        >> print result
        0
    """
    return


def set_inactive(**kwargs):
    """ When executed, this function stops the radio program specified in the parameter radio_program_name.
    :param myargs: a dictionary data type (key: value) where the keys are: The key "interface" specify the network interface to use and the key 'radio_program_name' in which the value specify the name of radio program,
    :return result:  return 0 if the parameter setting call was successfully performed, 1 partial success, 2 error.
    :example:
        >> args = {'interface' : 'wlan0', 'radio_program_name' : 'CSMA'} \n
        >> result = UPI_RN.setInactive(args) \n
        >> print result \n
        0 \n
    """
    return


def get_active(**kwargs):
    """ Each radio program is associated with a name and an index. When executed, this function return the index of the radio program active.
    :param myargs: a dictionary data type (key: value) where the keys are: The key "interface" specify the network interface to use.
    :return result: the index of the active radio program.
    :example:
        >> args = {'interface' : 'wlan0'} \n
        >> result = UPI_RN.getActive(args) \n
        >> print result \n
        2 \n
    """
    return

''' Transmission of radio waveform (no MAC) '''

def play_waveform(iface, freq, power_lvl, **kwargs):
    '''
        Starts transmitting a radio waveform (just PHY, no MAC).
    '''
    pass


def stop_waveform(iface, **kwargs):
    '''
        Stops transmitting a radio waveform.
    '''
    pass


def set_power(power_dBm):
    '''
        func desc
        todo: rename in txpower
    '''
    pass


def get_power():
    '''
        func desc
        todo: rename in txpower
    '''
    pass


def get_rssi():
    '''
        Piotr: please comment!
    '''
    pass


def get_noise():
    '''
        Returns the noise floor measured by the wireless driver.
    '''
    pass

def receive_csi(runt):
    '''
        Receives CSI samples from the ath9k driver.
    '''
    pass
