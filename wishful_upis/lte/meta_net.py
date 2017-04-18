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
MME_SERVED_ENB = Attribute(key='MME_SERVED_ENB', type=int, isReadOnly=False)  #: number of eNB served by the same MME
MME_SERVED_UE = Attribute(key='MME_SERVED_UE', type=int, isReadOnly=False)  #: number of UE served by the same MME
MME_TAI_LIST = Attribute(key='MME_TAI_LIST', type=int, isReadOnly=False)  #: MME TAI list (TAI, MNC, MCC)
MME_GUMMEI_LIST = Attribute(key='MME_GUMMEI_LIST', type=int, isReadOnly=False) #: MME GUMMEI LIST (MCC,MNC,MME_GID, MME_CODE)

ENB_NAME = Attribute(key='ENB_NAME', type=int, isReadOnly=False)  #: name of the eNB
ENB_ID = Attribute(key='ENB_ID', type=int, isReadOnly=False)  #: identification number of the eNB
ENB_CELL_TYPE = Attribute(key='ENB_CELL_TYPE', type=int, isReadOnly=False)  #: eNB cell type (macro, small)
ENB_TRACKING_AREA_CODE = Attribute(key='ENB_TRACKING_AREA_CODE', type=int, isReadOnly=False)  #: eNB Tracking Area Code
ENB_MCC = Attribute(key='ENB_MCC', type=int, isReadOnly=False)  #: eNB Mobile Country Code
ENB_MNC = Attribute(key='ENB_MNC', type=int, isReadOnly=False)  #: eNB Mobile Network Code

RRU_NAME = Attribute(key='RRU_NAME', type=int, isReadOnly=False)  #: name of the RRU
RRU_ID = Attribute(key='RRU_ID', type=int, isReadOnly=False)  #: identification number of the RRU
RRU_CELL_TYPE = Attribute(key='ENB_CELL_TYPE', type=int, isReadOnly=False)  #: RRU cell type (macro, small)
RRU_TRACKING_AREA_CODE = Attribute(key='ENB_TRACKING_AREA_CODE', type=int, isReadOnly=False) #: RRU Tracking Area Code
RRU_MCC = Attribute(key='ENB_MCC', type=int, isReadOnly=False)  #: RRU Mobile Country Code
RRU_MNC = Attribute(key='ENB_MNC', type=int, isReadOnly=False)  #: RRU Mobile Network Code

RCC_NAME = Attribute(key='RRC_NAME', type=int, isReadOnly=False)  #: name of the RCC
RCC_ID = Attribute(key='RRC_ID', type=int, isReadOnly=False)  #: identification number of the RCC
RCC_CELL_TYPE = Attribute(key='ENB_CELL_TYPE', type=int, isReadOnly=False)  #: RCC cell type (macro, small)
RCC_TRACKING_AREA_CODE = Attribute(key='ENB_TRACKING_AREA_CODE', type=int, isReadOnly=False)  #: RRU Tracking Area Code
RCC_MCC = Attribute(key='ENB_MCC', type=int, isReadOnly=False)  #: RCC Mobile Country Code
RCC_MNC = Attribute(key='ENB_MNC', type=int, isReadOnly=False)  #: RCC Mobile Network Code

SPLIT_LEVEL = Attribute(key='SPLIT_LEVEL', type=int, isReadOnly=False)  #: point where the lte protocol stack is splitted
FRONTHAUL_TRANSPORT_MODE = Attribute(key='FRONTHAUL_TRANSPORT_MODE', type=int, isReadOnly=False) #: Fronthaul link transport mode(UDP or RAW are the possible options)'''

mme_S1_name = Attribute(key='mme_S1_name', type=int, isReadOnly=False)  #: S1 interface name of MME
mme_S1_addr = Attribute(key='mme_S1_addr', type=int, isReadOnly=False)  #: S1 interface address of MME
mme_S11_name = Attribute(key='mme_S11_name', type=int, isReadOnly=False)  #: S11 interface name of MME
mme_S11_addr = Attribute(key='mme_S11_addr', type=int, isReadOnly=False)  #: S11 interface address of MME
mme_S11_port = Attribute(key='mme_S11_port', type=int, isReadOnly=False)  #: S11 interface port of MME

sgw_s11_name = Attribute(key='sgw_S1_name', type=int, isReadOnly=False)  #: S11 interface name of S-GW
sgw_s11_addr = Attribute(key='sgw_S1_addr', type=int, isReadOnly=False)  #: S11 interface addr of S-GW
sgw_S1U_S12_S4_name = Attribute(key='sgw_S1U_S12_S4_name', type=int, isReadOnly=False) #: S1-U,S12,S4 interface name of S-GW
sgw_S1U_S12_S4_addr = Attribute(key='sgw_S1U_S12_S4_addr', type=int, isReadOnly=False) #: S1-U,S12,S4 interface addr of S-GW
sgw_S1U_S12_S4_port = Attribute(key='sgw_S1U_S12_S4_port', type=int, isReadOnly=False) #: S1-U,S12,S4 interface port of S-GW
sgw_S5_S8_name = Attribute(key='sgw_S5_S8_name', type=int, isReadOnly=False)  #: S5, S8 interface name of S-GW
sgw_S5_S8_addr = Attribute(key='sgw_S5_S8_addr', type=int, isReadOnly=False)  #: S5, S8 interface addr of S-GW

pgw_S5_S8_name = Attribute(key='pgw_S5_S8_name_PGW', type=int, isReadOnly=False)  #: S5, S8 interface name of P-GW
pgw_SGi_name = Attribute(key='pgw_SGi_name', type=int, isReadOnly=False)  #: SGi interface name of P-GW

ip_address_pool = Attribute(key='ip_address_pool', type=int, isReadOnly=False)  #: pool of IP addressess. The MME will assign at the UE one address from the such pool
default_DNS_addr = Attribute(key='default_DNS_addr', type=int, isReadOnly=False)  #: default DNS IP address

enb_mme_addr = Attribute(key='enb_mme_addr', type=int, isReadOnly=False)  #:the MME address in the eNB config file (used by the eNB for reaching the MME)
enb_S1_name = Attribute(key='enb_S1_name', type=int, isReadOnly=False)  #: S1-C interface name of the eNB
enb_S1_addr = Attribute(key='enb_S1_addr', type=int, isReadOnly=False)  #: S1-C interface address of the eNB
enb_S1U_name = Attribute(key='enb_S1U_name', type=int, isReadOnly=False)  #: S1-U interface name of the eNB
enb_S1U_addr = Attribute(key='enb_S1U_addr', type=int, isReadOnly=False)  #: S1-U interface address of the eNB
enb_S1U_port = Attribute(key='enb_S1U_port', type=int, isReadOnly=False)  #: S1-U interface port of the eNB

rru_local_if_name = Attribute(key='rru_local_if_name', type=int, isReadOnly=False)  #: interface name of the RRU where the RCC is connected
rru_local_address = Attribute(key='rru_local_address', type=int, isReadOnly=False)  #: interface address of the RRU where the RCC is connected
rru_local_port = Attribute(key='rru_local_port', type=int, isReadOnly=False)  #: interface port of the RRU where the RCC is connected
rru_remote_address = Attribute(key='rru_remote_address', type=int, isReadOnly=False)  #: interface name of the RCC
rru_remote_port = Attribute(key='rru_remote_port', type=int, isReadOnly=False)  #: interface port of the RCC

rcc_mme_addr = Attribute(key='rcc_mme_addr', type=int, isReadOnly=False)  #: the MME address in the RCC config file (used by the eNB for reaching the MME)
rcc_S1_name = Attribute(key='rcc_S1_name', type=int, isReadOnly=False)  #:S1-C interface name of the RCC
rcc_S1_addr = Attribute(key='rcc_S1_addr', type=int, isReadOnly=False)  #:S1-C interface address of the RCC
rcc_S1U_name = Attribute(key='rcc_S1U_name', type=int, isReadOnly=False)  #: S1-U interface name of the RCC
rcc_S1U_addr = Attribute(key='rcc_S1U_addr', type=int, isReadOnly=False)  #: S1-U interface address of the RCC
rcc_S1U_port = Attribute(key='rcc_S1U_port', type=int, isReadOnly=False)  #: S1-U interface port of the RCC
rcc_local_if_name = Attribute(key='rcc_local_if_name', type=int, isReadOnly=False)  #: interface name of the RCC where the RRU is connected
rcc_local_address = Attribute(key='rcc_local_address', type=int, isReadOnly=False)  #: interface address of the RCC where the RRU is connected
rcc_local_port = Attribute(key='rcc_local_port', type=int, isReadOnly=False)  #:interface port of the RCC where the RRU is connected
rcc_remote_address = Attribute(key='rcc_remote_address', type=int, isReadOnly=False)  #: interface name of the RRU
rcc_remote_port = Attribute(key='rcc_remote_port', type=int, isReadOnly=False)  #: interface name of the RRU
