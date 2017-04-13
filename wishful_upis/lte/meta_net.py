"""The WiSHFUL net control interface, attributes.
Used for configuration/monitoring of the network
layers of the LTE technology
"""
__author__ = "Francesco Giannone, Domenico Garlisi"
__copyright__ = "Copyright (c) 2017, Sant'Anna, CNIT"
__version__ = "0.1.0"
__email__ = "{francesco.giannone@santannapisa.it, domenico.garlisi@cnit.it}"

from ..meta_models import ValueDoc, Attribute, Measurement, Event, Action

# ATTRIBUTES
MME_REALM = Attribute(key='MME_REALM', type=int, isReadOnly=False)  #:
MME_SERVED_ENB = Attribute(key='MME_SERVED_ENB', type=int, isReadOnly=False)  #:
MME_SERVED_UE = Attribute(key='MME_SERVED_UE', type=int, isReadOnly=False)  #:
MME_TAI_LIST = Attribute(key='MME_TAI_LIST', type=int, isReadOnly=False)  #:
MME_GUMMEI_LIST = Attribute(key='MME_GUMMEI_LIST', type=int, isReadOnly=False)  #:

ENB_NAME = Attribute(key='ENB_NAME', type=int, isReadOnly=False)  #:
ENB_ID = Attribute(key='ENB_ID', type=int, isReadOnly=False)  #:
ENB_CELL_TYPE = Attribute(key='ENB_CELL_TYPE', type=int, isReadOnly=False)  #:
ENB_TRACKING_AREA_CODE = Attribute(key='ENB_TRACKING_AREA_CODE', type=int, isReadOnly=False)  #:
ENB_MCC = Attribute(key='ENB_MCC', type=int, isReadOnly=False)  #:
ENB_MNC = Attribute(key='ENB_MNC', type=int, isReadOnly=False)  #:

RRU_NAME = Attribute(key='RRU_NAME', type=int, isReadOnly=False)  #:
RRU_ID = Attribute(key='RRU_ID', type=int, isReadOnly=False)  #:
RRU_CELL_TYPE = Attribute(key='ENB_CELL_TYPE', type=int, isReadOnly=False)  #:
RRU_TRACKING_AREA_CODE = Attribute(key='ENB_TRACKING_AREA_CODE', type=int, isReadOnly=False)  #:
RRU_MCC = Attribute(key='ENB_MCC', type=int, isReadOnly=False)  #:
RRU_MNC = Attribute(key='ENB_MNC', type=int, isReadOnly=False)  #:

RCC_NAME = Attribute(key='RRC_NAME', type=int, isReadOnly=False)  #:
RCC_ID = Attribute(key='RRC_ID', type=int, isReadOnly=False)  #:
RCC_CELL_TYPE = Attribute(key='ENB_CELL_TYPE', type=int, isReadOnly=False)  #:
RCC_TRACKING_AREA_CODE = Attribute(key='ENB_TRACKING_AREA_CODE', type=int, isReadOnly=False)  #:
RCC_MCC = Attribute(key='ENB_MCC', type=int, isReadOnly=False)  #:
RCC_MNC = Attribute(key='ENB_MNC', type=int, isReadOnly=False)  #:

SPLIT_LEVEL = Attribute(key='SPLIT_LEVEL', type=int, isReadOnly=False)  #:
FRONTHAUL_TRANSPORT_MODE = Attribute(key='FRONTHAUL_TRANSPORT_MODE', type=int, isReadOnly=False)  #:

mme_S1_name = Attribute(key='mme_S1_name', type=int, isReadOnly=False)  #:
mme_S1_addr = Attribute(key='mme_S1_addr', type=int, isReadOnly=False)  #:
mme_S11_name = Attribute(key='mme_S11_name', type=int, isReadOnly=False)  #:
mme_S11_addr = Attribute(key='mme_S11_addr', type=int, isReadOnly=False)  #:
mme_S11_port = Attribute(key='mme_S11_port', type=int, isReadOnly=False)  #:

sgw_S1U_S12_S4_name = Attribute(key='sgw_S1U_S12_S4_name', type=int, isReadOnly=False)  #:
sgw_S1U_S12_S4_addr = Attribute(key='sgw_S1U_S12_S4_addr', type=int, isReadOnly=False)  #:
sgw_S1U_S12_S4_port = Attribute(key='sgw_S1U_S12_S4_port', type=int, isReadOnly=False)  #:
sgw_S5_S8_name = Attribute(key='sgw_S5_S8_name', type=int, isReadOnly=False)  #:
sgw_S5_S8_addr = Attribute(key='sgw_S5_S8_addr', type=int, isReadOnly=False)  #:

pgw_S5_S8_name = Attribute(key='pgw_S5_S8_name_PGW', type=int, isReadOnly=False)  #:
pgw_SGi_name = Attribute(key='pgw_SGi_name', type=int, isReadOnly=False)  #:

ip_address_pool = Attribute(key='ip_address_pool', type=int, isReadOnly=False)  #:
default_DNS_addr = Attribute(key='default_DNS_addr', type=int, isReadOnly=False)  #:

enb_mme_addr = Attribute(key='enb_mme_addr', type=int, isReadOnly=False)  #:
enb_S1_name = Attribute(key='enb_S1_name', type=int, isReadOnly=False)  #:
enb_S1_addr = Attribute(key='enb_S1_addr', type=int, isReadOnly=False)  #:
enb_S1U_name = Attribute(key='enb_S1U_name', type=int, isReadOnly=False)  #:
enb_S1U_addr = Attribute(key='enb_S1U_addr', type=int, isReadOnly=False)  #:
enb_S1U_port = Attribute(key='enb_S1U_port', type=int, isReadOnly=False)  #:

rru_local_if_name = Attribute(key='rru_local_if_name', type=int, isReadOnly=False)  #:
rru_local_address = Attribute(key='rru_local_address', type=int, isReadOnly=False)  #:
rru_local_port = Attribute(key='rru_local_port', type=int, isReadOnly=False)  #:
rru_remote_address = Attribute(key='rru_remote_address', type=int, isReadOnly=False)  #:
rru_remote_port = Attribute(key='rru_remote_port', type=int, isReadOnly=False)  #:

rcc_mme_addr = Attribute(key='rcc_mme_addr', type=int, isReadOnly=False)  #:
rcc_S1_name = Attribute(key='rcc_S1_name', type=int, isReadOnly=False)  #:
rcc_S1_addr = Attribute(key='rcc_S1_addr', type=int, isReadOnly=False)  #:
rcc_S1U_name = Attribute(key='rcc_S1U_name', type=int, isReadOnly=False)  #:
rcc_S1U_addr = Attribute(key='rcc_S1U_addr', type=int, isReadOnly=False)  #:
rcc_S1U_port = Attribute(key='rcc_S1U_port', type=int, isReadOnly=False)  #:
rcc_local_if_name = Attribute(key='rcc_local_if_name', type=int, isReadOnly=False)  #:
rcc_local_address = Attribute(key='rcc_local_address', type=int, isReadOnly=False)  #:
rcc_local_port = Attribute(key='rcc_local_port', type=int, isReadOnly=False)  #:
rcc_remote_address = Attribute(key='rcc_remote_address', type=int, isReadOnly=False)  #:
rcc_remote_port = Attribute(key='rcc_remote_port', type=int, isReadOnly=False)  #:  # ATTRIBUTES

