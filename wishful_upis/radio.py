__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de"


def set_channel(channel):
    '''
    Set channel, i.e. center frequency
    ch - channel to set
    '''
    pass

def get_channel():
    '''
        func desc
    '''
    pass

def set_power(power):
    '''
        func desc
        todo: rename in transmit_power
    '''
    pass

def get_power():
    '''
        func desc
        todo: rename in transmit_power
    '''
    pass

def get_noise():
    '''
        func desc
    '''
    pass

def get_rssi():
    '''
        func desc
        todo: specify the link!!!
    '''
    pass


def inject_frame(frame):
    '''
        func desc
    '''
    pass

'''
    MAC layer
'''

def install_mac_processor(interface, mac_profile):
    '''
        func desc
    '''
    pass

def update_mac_processor(interface, mac_profile):
    '''
        func desc
    '''
    pass

def uninstall_mac_processor(interface, mac_profile):
    '''
        func desc
    '''
    pass

def set_edca_parameters(queueId, qParam):
    '''
        func desc
        todo: this is against unification: edca is specific to 802.11; try to generalize
    '''
    pass


def get_edca_parameters(queueId):
    '''
        func desc
        todo: this is against unification: edca is specific to 802.11; try to generalize
    '''
    pass

'''
    PHY layer
'''

def perform_spectral_scanning(iface, freq_list, mode):
    '''
        Perform spectral scanning. Returns a power value for each frequency bin.
    '''
    pass


def get_airtime_utilization():
    '''
        Returns the relative time the spectrum is empty.
    '''
    pass


def play_waveform(iface, freq, power_lvl, **kwargs):
    '''
        Starts transmitting a specified waveform (just PHY, no MAC).
    '''
    pass


def stop_waveform(iface, **kwargs):
    '''
        Stops transmitting a specified waveform.
    '''
    pass