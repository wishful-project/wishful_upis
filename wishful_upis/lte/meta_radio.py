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
PUCCH_nom_enb = Attribute(key='PUCCH_nom_enb', type=int, isReadOnly=False)  #: power of the PUCCH channel for the eNB
PUSCH_nom_enb = Attribute(key='PUSCH_nom_enb', type=int, isReadOnly=False)  #: power of the PUSCH channel for the eNB
RX_GAIN_enb = Attribute(key='RX_GAIN_enb', type=int, isReadOnly=False)  #: RX gain for the eNB
TX_GAIN_enb = Attribute(key='TX_GAIN_enb', type=int, isReadOnly=False)  #: TX gain for the eNB
TX_BANDWIDTH_enb = Attribute(key='TX_BANDWIDTH_enb', type=int, isReadOnly=False)  #: transmission signal bandwidth for the eNB
TX_CHANNEL_enb = Attribute(key='TX_CHANNEL_enb', type=int, isReadOnly=False)  #: downlink transmission channel for the eNB
TX_MODE_enb = Attribute(key='TX_MODE_enb', type=int, isReadOnly=False)  #: transmission mode (FDD or TDD) for the eNB
UL_FREQ_OFFSET_enb = Attribute(key='UL_FREQ_OFFSET_enb', type=int, isReadOnly=False)  #: offset from the downlink transmission channel (uplink transmission channel)for the eNB

PUCCH_nom_rcc = Attribute(key='PUCCH_nom_rcc', type=int, isReadOnly=False)  #: power of the PUCCH channel for the RCC
PUSCH_nom_rcc = Attribute(key='PUSCH_nom_rcc', type=int, isReadOnly=False)  #: power of the PUSCH channel for the RCC
RX_GAIN_rcc = Attribute(key='RX_GAIN_rcc', type=int, isReadOnly=False)  #: RX gain for the RCC
TX_GAIN_rcc = Attribute(key='TX_GAIN_rcc', type=int, isReadOnly=False)  #: TX gain for the RCC
TX_BANDWIDTH_rcc = Attribute(key='TX_BANDWIDTH_rcc', type=int, isReadOnly=False)  #: transmission signal bandwidth for the RCC
TX_CHANNEL_rcc = Attribute(key='TX_CHANNEL_rcc', type=int, isReadOnly=False)  #: downlink transmission channel for the RCC
TX_MODE_rcc = Attribute(key='TX_MODE_rcc', type=int, isReadOnly=False)  #: transmission mode (FDD or TDD) for the RCC
UL_FREQ_OFFSET_rcc = Attribute(key='UL_FREQ_OFFSET_rcc', type=int, isReadOnly=False)  #: offset from the downlink transmission channel (uplink transmission channel)for the RCC

PUCCH_nom_rru = Attribute(key='PUCCH_nom_rru', type=int, isReadOnly=False)  #: power of the PUCCH channel for the RRU
PUSCH_nom_rru = Attribute(key='PUSCH_nom_rru', type=int, isReadOnly=False)  #: power of the PUSCH channel for the RRU
RX_GAIN_rru = Attribute(key='RX_GAIN_rru', type=int, isReadOnly=False)  #: RX gain for the RRU
TX_GAIN_rru = Attribute(key='TX_GAIN_rru', type=int, isReadOnly=False)  #: TX gain for the RRU
TX_BANDWIDTH_rru = Attribute(key='TX_BANDWIDTH_rru', type=int, isReadOnly=False)  #: transmission signal bandwidth for the RRU
TX_CHANNEL_rru = Attribute(key='TX_CHANNEL_rru', type=int, isReadOnly=False)  #: downlink transmission channel for the RRU
TX_MODE_rru = Attribute(key='TX_MODE_rru', type=int, isReadOnly=False)  #: transmission mode (FDD or TDD) for the RRU
UL_FREQ_OFFSET_rru = Attribute(key='UL_FREQ_OFFSET_rru', type=int, isReadOnly=False)  #: offset from the downlink transmission channel (uplink transmission channel)for the RRU
