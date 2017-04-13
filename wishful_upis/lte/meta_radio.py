"""The WiSHFUL radio control interface, attributes.
Used for configuration/monitoring of the radio
layers of the LTE technology
"""
__author__ = "Francesco Giannone, Domenico Garlisi"
__copyright__ = "Copyright (c) 2017, Sant'Anna, CNIT"
__version__ = "0.1.0"
__email__ = "{francesco.giannone@santannapisa.it, domenico.garlisi@cnit.it}"

from ..meta_models import ValueDoc, Attribute, Measurement, Event, Action

# ATTRIBUTES
PUCCH_nom = Attribute(key='PUCCH_nom', type=int, isReadOnly=False)  #:
PUSCH_nom = Attribute(key='PUSCH_nom', type=int, isReadOnly=False)  #:
RX_GAIN = Attribute(key='RX_GAIN', type=int, isReadOnly=False)  #:
TX_GAIN = Attribute(key='TX_GAIN', type=int, isReadOnly=False)  #:
TX_BANDWIDTH = Attribute(key='TX_BANDWIDTH', type=int, isReadOnly=False)  #:
TX_CHANNEL = Attribute(key='TX_CHANNEL', type=int, isReadOnly=False)  #:
TX_MODE = Attribute(key='TX_MODE', type=int, isReadOnly=False)  #:
UL_FREQ_OFFSET = Attribute(key='UL_FREQ_OFFSET', type=int, isReadOnly=False)  #:
