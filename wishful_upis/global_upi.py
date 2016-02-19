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


def perform_soft_handover(srcAp, dstAp, station):
    '''
        func desc
    '''
    pass


def perform_hard_handover(srcAp, dstAp, station):
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

