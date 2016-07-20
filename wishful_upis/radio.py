from .lte.radio import *
from .wifi.radio import *
from .zigbee.radio import *


__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de"

'''The WiSHFUL radio control interface, UPI_R.

Used for configuration/monitoring of the lower
layers of the network protocol stack (lower MAC and PHY).

Note, here all generic functions are defined, i.e. those which can be
supported by any wireless networking node (IEEE 802.11, LTE, ZigBee).

All protocol-dependent functions are defined in separate folder,
e.g. ``wifi/`` or ``lte/``.
'''

class Radio(object):
    def set_parameter_lower_layer(self, **kwargs):
        """The UPI_R interface is able to configure the radio behavior.

        Thanks to the abstraction of the hardware
        platform and radio programs in terms of Radio Capabilities. A subset of radio capabilities are the parameter.
        Parameters correspond to the configuration registers of the hardware platform and to the variables used in
        the radio programs. This function (re)set the value(s) of the Parameters Radio Capabilities specified in
        the dictionary argument. The list of available parameters is defined as attributes of the UPI_R class,
        you can use the UPI_RN.getRadioInfo function to find the platform supported parameters.

        Examples:
            .. code-block:: python

                >> args = {'interface' : 'wlan0', UPI_RN.CSMA_CW : 15, UPI_RN.CSMA_CW_MIN : 15, UPI_RN.CSMA_CW_MAX : 15}
                >> result = UPI_RN.setParameterLowerLayer(args)
                >> print result
                [0, 0, 0]

        Args:
            myargs:
                list of parameters and values to set, in term of a dictionary
                data type (list of key: value) in which keys is the `interface` to
                specify network interface to be uses and the desired UPI_R attribute,
                and value is the value to set. An example of argument dictionary data
                type is ``{UPI_RN.CSMA_CW : 15, UPI_RN.CSMA_CW_MIN : 15,
                UPI_RN.CSMA_CW_MAX : 15}``.

        Returns:
            0 if the parameter setting call was successfully performed, 1 partial success, 2 error.
        """
        return


    def get_parameter_lower_layer(self, **kwargs):
        """The UPI_R interface is able to configure the radio behavior.

        Thanks to the abstraction of the hardware
        platform and radio programs in terms of Radio Capabilities. A subset of radio capabilities are the parameters.
        Parameters correspond to the configuration registers of the hardware platform and to the variables used in the
        radio programs.
        This function get the value(s) of the Parameters Radio Capabilities specified in the dictionary argument.
        The available parameters are defined as attributes of the UPI_R clas, you can use the UPI_RN.getRadioInfo function
        to find the platform supported parameters.

        Examples:
            .. code-block:: python

                >> args = {'interface' : 'wlan0', 'parameters' : [UPI_RN.CSMA_CW] }
                >> result = UPI_RN.getParameterLowerLayer(args)
                >> print result
                {UPI_RN.CSMA_CW : 15}

        Args:
            myargs:
                list of parameters, in term of a dictionary data type (list of
                key: value) in which: the key is `parameters` and the value is a list
                of UPI_R attributes for parameters, the key in `interface` specify
                network interface to be uses. An argument dictionary example is
                ``{'interface' : 'wlan0', 'PARAMETERS' :
                [UPI_RN.CSMA_CW, UPI_RN.CSMA_CW_MIN, UPI_RN.CSMA_CW_MAX]}``.

        Returns:
            list of parameters and values:
                in term of a dictionary data type (list
                of key: value) in which the key is the UPI_R class attribute, and value
                is the current setting of the attribute. An example of argument
                dictionary data type is
                ``{UPI_RN.CSMA_CW : 15, UPI_RN.CSMA_CW_MIN : 15, UPI_RN.CSMA_CW_MAX : 15}``.
        """
        return


    def get_monitor(self, **kwargs):
        """The UPI_R interface is able to get the radio measurements.

        Thanks to the abstraction of the hardware platform and radio programs in
        terms of Radio Capabilities. A subset of radio capabilities are the
        low-level measurements. The low-level measurements are continuously
        monitored by the hardware platform and by the radio programs.
        The measurement capabilities can be used to get information and statistics
        about the state of the physical links or the internal state of the node.

        This function get the value(s) of the Measurements Radio Capabilities specified in the dictionary
        argument. The list of available measurements are defined as attribute of the UPI_R class, you can use the
        UPI_RN.getRadioInfo function to find the platform supported measurements.

        Examples:
            .. code-block:: python

                >> args = {'interface' : 'wlan0', 'measurements' : [UPI_RN.NUM_FREEZING_COUNT] }
                >> result = UPI_RN.getMonitor(args)
                >> print result
                {UPI_RN.NUM_FREEZING_COUNT : 150}

        Args:
            myargs:
                list of parameters, in term of a dictionary data type (list of
                key: value) in which: the key is `measurements` and the value is a list
                of UPI_R attributes for measurements, the key in `interface` specify
                network interface to be uses. An example of argument dictionary is
                ``{"measurements" : [UPI_RN.NUM_FREEZING_COUNT, UPI_RN.TX_ACTIVITY]}``.

        Returns:
            list of parameters and values:
                in term of a dictionary data type (list
                of key: value) in which the key are the UPI_R attributes for
                measurements, and value is the reading of the measurement.
                An example of argument dictionary data type is
                ``{UPI_RN.NUM_FREEZING_COUNT : 150, UPI_RN.TX_ACTIVITY : 45670}``.
        """
        return

    # Activation and deactivation of radio programs.

    def set_active(self, **kwargs):
        """This function activates the passed radio program, one the platform. When executed, this function stops the
        current radio program and enables the execution of the radio program specified in the parameter
        radioProgramName. Two additional parameters can be used, one of these is required.The path of the radio program
        description is required. The optionally parameter specify the index, in order to associate an index to the radio
        program.

        Examples:
            .. code-block:: python

               >> args = {'interface' : 'wlan0', 'radio_program_name' : 'CSMA', 'path': './radio_program/csma.txt'}
               >> result = UPI_RN.setActive(args)
               >> print result
               0

        Args:
            myargs: a dictionary data type (key: value) where the keys are: The key 'interface' specify the network interface to use. The key 'radio_program_name'specify the name of radio program. The key 'path' in which the value specify the path of radio program description, and 'position' in which the value specify the radio program index associated.

        Returns:
            int:
                - 0 if the parameter setting call was successfully performed
                - 1 partial success
                - 2 error.
        """
        return


    def set_inactive(self, **kwargs):
        """When executed, this function stops the radio program specified in the parameter radio_program_name.

        Examples:
            .. code-block:: python

                >> args = {'interface' : 'wlan0', 'radio_program_name' : 'CSMA'}
                >> result = UPI_RN.setInactive(args)
                >> print result
                0

        Args:
            myargs: a dictionary data type (key: value) where the keys are: The key "interface" specify the network interface to use and the key 'radio_program_name' in which the value specify the name of radio program,

        Returns:
            int:
                - 0 if the parameter setting call was successfully performed
                - 1 partial success
                - 2 error.
        """
        return


    def get_active(self, **kwargs):
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


    def add_program(self, **kwargs):
        """Adds a new radio program to the nodes repository """
        return


    def remove_program(self, **kwargs):
        """Remove radio program from nodes repository """
        return


    def merge_programs(self, **kwargs):
        """Merge the set of radio programs """
        return

    def switch_program(self, target_program_name, **kwargs):
        """Switch from one to another radio program """
        return


    ''' Transmission of radio waveform (no MAC) '''

    def play_waveform(self, iface, freq, power_lvl, **kwargs):
        '''Starts transmitting a radio waveform (just PHY, no MAC).
        '''
        pass


    def stop_waveform(self, iface, **kwargs):
        '''Stops transmitting a radio waveform.
        '''
        pass


    def set_power(self, power_dBm):
        '''func desc

        todo: rename in txpower
        '''
        pass


    def get_power(self):
        '''func desc

        todo: rename in txpower
        '''
        pass


    def get_rssi(self):
        '''

        '''
        pass


    def get_noise(self):
        '''Returns the noise floor measured by the wireless driver.
        '''
        pass


    def receive_csi(self):
        '''Receives CSI samples from the ath9k driver.
        '''
        pass


    def scand_start(self, iface='wlan0', mode='background', ival=1):
        '''Reconfigure ath9k spectral scan daemon.
        '''
        pass


    def scand_stop(self):
        '''Reconfigure ath9k spectral scan daemon.
        '''
        pass


    def scand_reconf(self, iface='wlan0', mode='background', ival=1):
        '''Reconfigure ath9k spectral scan daemon.
        '''
        pass


    def scand_read(self):
        '''Receives PSD samples from the ath9k driver.
        '''
        pass

    @property
    #@attribute
    def channel(self):
        """
        Description
        """
        pass

    #@function
    def switch_on(self):
        """
        Description
        """
        pass

    #@event
    def event_packet_loss(self):
        """
        Description:
        descriptor = node.iface(0).callback(cb1).wifi.event_packet_loss()
        descriptor.subscribe(duration=10)
        descriptor.unsubscribe()
        """
        pass

    #@service
    def service_spectral_scan(self, sampling_rate, frequency_range):
        """
        Description: generate functions
        id = start_spectral_scan(sampling_rate, frequency_range),
        stop_spectral_scan(id),

        CALLING EXAMPLE:
        descriptor = node.iface(0).wifi.service_spectral_scan()
        descritor.start(duration = 10)
        descriptor.stop()
        duration in context
        """
        pass
