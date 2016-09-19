from .upi import Upi
from .upi import EventBase

__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"

'''
Events for performing network-wide operations which go beyond just remote
UPI_R/N calls. Example are estimating the nodes in carrier sensing range, performing handover operation, ....
'''

# Generic functionality which should be supported by most of the platforms.

class NetFunEvent(EventBase):
    def __init__(self):
        super().__init__()
        pass

'''
    Handover operation
'''

class TriggerHandoverRequestEvent(NetFunEvent):
    '''
    Event to trigger a handover operation.
    '''
    def __init__(self, sta_id, serving_node, target_node, gateway):
        super().__init__()
        self.sta_id = sta_id
        self.serving_node = serving_node
        self.targetAP_node = target_node
        self.gateway = gateway


class TriggerHandoverReplyEvent(NetFunEvent):
    '''
    Reply send after triggering handover operation.
    '''
    def __init__(self, success):
        super().__init__()
        self.success = success