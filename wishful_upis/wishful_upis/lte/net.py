__author__ = "Francesco Giannone, Domenico Garlisi"
__copyright__ = "Copyright (c) 2017, Sant'Anna, CNIT"
__version__ = "0.1.0"
__email__ = "{francesco.giannone@santannapisa.it, domenico.garlisi@cnit.it}"

'''
The protocol-specific definition of the WiSHFUL network control interface, UPI_N, for configuration/monitoring of the higher
layers of the network protocol stack (upper MAC and higher).
LTE protocol family
'''



#********
#EPC Attribute
#********

LTE_EPC_MCC = Attribute(key='LTE_EPC_MCC', type=int, isReadOnly=False)  #: MME Mobile Country Code
LTE_EPC_MNC = Attribute(key='LTE_EPC_MNC', type=int, isReadOnly=False)  #: MME Mobile Network Code
LTE_EPC_OP = Attribute(key='LTE_EPC_OP', type=int, isReadOnly=False)  #: Configures global configuration parameters Global OP
LTE_EPC_AMF = Attribute(key='LTE_EPC_AMF', type=int, isReadOnly=False)  #: Configures global configuration parameters Global AMF

LTE_EPC_ENB_ADD = Attribute(key='LTE_EPC_ENB_ADD', type=int, isReadOnly=False)  #: adds a eNB to be served by the EPC (required: IP address)
LTE_EPC_ENB_DEL = Attribute(key='LTE_EPC_ENB_DEL', type=int, isReadOnly=False)  #: deletes an eNB
LTE_EPC_ENB_LIST = Attribute(key='LTE_EPC_ENB_LIST', type=int, isReadOnly=False)  #: get eNB list
LTE_EPC_SUBSCRIBER_ADD = Attribute(key='LTE_EPC_SUBSCRIBER_ADD', type=int, isReadOnly=False)  #: Add a single UE (required input: IMSI, Subscriber Group)
LTE_EPC_SUBSCRIBER_DEL = Attribute(key='LTE_EPC_SUBSCRIBER_DEL', type=int, isReadOnly=False)  #: deletes connection data for a single subscriber
LTE_EPC_SUBSCRIBER_LIST = Attribute(key='LTE_EPC_SUBSCRIBER_LIST', type=int, isReadOnly=False)  #: get UE list
LTE_EPC_SUBSCRIBER_GROUP_ADD = Attribute(key='LTE_EPC_SUBSCRIBER_GROUP_ADD', type=int, isReadOnly=False)  #: Adds a new subscriber profile (required input: Name, APN, , UL/DL AMBR)
LTE_EPC_SUBSCRIBER_GROUP_DEL = Attribute(key='LTE_EPC_SUBSCRIBER_GROUP_DEL', type=int, isReadOnly=False)  #: deletes a subscriber profile
LTE_EPC_SUBSCRIBER_GROUP_LIST = Attribute(key='LTE_EPC_SUBSCRIBER_GROUP_LIST', type=int, isReadOnly=False)  #: get subscriber profile list
LTE_EPC_APN_ADD = Attribute(key='LTE_EPC_APN_ADD', type=int, isReadOnly=False)  #: adds a new APN (required: Name, PGW address, DHCP pool, DNS server, UL/DL AMBR)
LTE_EPC_APN_DEL = Attribute(key='LTE_EPC_MNC', type=int, isReadOnly=False)  #: deletes an APN
LTE_EPC_APN_LIST = Attribute(key='LTE_EPC_APN_LIST', type=int, isReadOnly=False)  #: get APN list

LTE_EPC_RNTI = Attribute(key='LTE_EPC_RNTI', type=int, isReadOnly=False)  #:

LTE_EPC_HSS_ADDRESS = Attribute(key='LTE_EPC_HSS_ADDRESS', type=int, isReadOnly=False)  #: HSS address
LTE_EPC_HSS_DIAMETER_ADDRESS = Attribute(key='LTE_EPC_HSS_DIAMETER_ADDRESS', type=str, isReadOnly=False)  #: sets the configuration of the HSS (diameter bind IP address)

LTE_EPC_SGW_GTPU_IP_ADDRESS = Attribute(key='LTE_EPC_SGW_GTPU_IP_ADDRESS', type=str, isReadOnly=False)  #:sets the configuration params of the SGW (GTP-U and GTP-C bind addresses)
LTE_EPC_SGW_GTPC_IP_ADDRESS = Attribute(key='LTE_EPC_SGW_GTPC_IP_ADDRESS', type=str, isReadOnly=False)  #:sets the configuration params of the SGW (GTP-U and GTP-C bind addresses)

LTE_EPC_MME_NAME = Attribute(key='LTE_EPC_MME_NAME', type=str, isReadOnly=False)  #: sets the configuration of the MME "name"
LTE_EPC_MME_CODE = Attribute(key='LTE_EPC_MME_CODE', type=int, isReadOnly=False)  #: sets the configuration of the MME "code"
LTE_EPC_MME_GID = Attribute(key='LTE_EPC_MME_GID', type=int, isReadOnly=False)  #: sets the configuration of the MME "gid"
LTE_EPC_MME_GUMMEI = Attribute(key='LTE_EPC_MME_GUMMEI', type=str, isReadOnly=False)  #: sets the configuration of the MME "GUMMEI"
LTE_EPC_MME_MAX_ENB = Attribute(key='LTE_EPC_MME_MAX_ENB', type=int, isReadOnly=False)  #: number of eNB served by the same MME
LTE_EPC_MME_MAX_UE = Attribute(key='LTE_EPC_MME_MAX_UE', type=int, isReadOnly=False)  #: number of UE served by the same MME
LTE_EPC_MME_TAI_LIST = Attribute(key='LTE_EPC_MME_TAI_LIST', type=list, isReadOnly=False)  #: MME TAI list (TAI, MNC, MCC)
LTE_EPC_MME_GUMMEI_LIST = Attribute(key='LTE_EPC_MME_GUMMEI_LIST', type=list, isReadOnly=False)  #: MME GUMMEI LIST (MCC,MNC,MME_GID, MME_CODE)
LTE_EPC_MME_GTPC_ADDRESS = Attribute(key='LTE_EPC_MME_GTPC_ADDRESS', type=str, isReadOnly=False)  #: set the GTPC ADDRESS
LTE_EPC_MME_S1AP_ADDRESS = Attribute(key='LTE_EPC_MME_S1AP_ADDRESS', type=str, isReadOnly=False)  #: set the S1AP ADDRESS
LTE_EPC_MME_DIAMETER_ADDRESS = Attribute(key='LTE_EPC_MME_DIAMETER_ADDRESS', type=str, isReadOnly=False)  #: set the DIAMETER ADDRESS

LTE_EPC_PGW_GTPU_IP_ADDRESS = Attribute(key='LTE_EPC_PGW_GTPU_IP_ADDRESS', type=str, isReadOnly=False)  #:sets the configuration params of the PGW (GTP-U bind addresses)
LTE_EPC_PGW_GTPC_IP_ADDRESS = Attribute(key='LTE_EPC_PGW_GTPC_IP_ADDRESS', type=str, isReadOnly=False)  #:sets the configuration params of the PGW (GTP-C bind addresses)
LTE_EPC_PGW_DL_AMBR = Attribute(key='LTE_EPC_PGW_DL_AMBR', type=int, isReadOnly=False)  #: sets the configuration params of the PGW (DL AMBR)
LTE_EPC_PGW_UL_AMBR = Attribute(key='LTE_EPC_PGW_UL_AMBR', type=int, isReadOnly=False)  #: sets the configuration params of the PGW (UL AMBR)

LTE_EPC_RESTART = Attribute(key='LTE_EPC_RESTART', type=bool, isReadOnly=False)  #: Restarts the system
LTE_EPC_DETACH_UE = Attribute(key='LTE_EPC_DETACH_UE', type=str, isReadOnly=False)  #: Detaches a single UE (required input: IMSI)


#********
#ENB Attribute
#********

LTE_ENB_NM = Attribute(key='LTE_ENB_NM', type=int, isReadOnly=False)  #: eNB name
LTE_ENB_ID = Attribute(key='LTE_ENB_ID', type=int, isReadOnly=False)  #: eNB identifier
LTE_ENB_CT = Attribute(key='LTE_ENB_CT', type=int, isReadOnly=False)  #: eNB cell type (macro, pico, femto)
LTE_ENB_PLMN = Attribute(key='LTE_ENB_PLMN', type=int, isReadOnly=False)  #: eNB PLMN Code
LTE_ENB_TAC = Attribute(key='LTE_ENB_TAC', type=int, isReadOnly=False)  #: eNB Tracking Area Code
LTE_ENB_MME = Attribute(key='LTE_ENB_MME', type=int, isReadOnly=False)  #: MME address in the eNB config file
LTE_ENB_PGW = Attribute(key='LTE_ENB_PGW', type=int, isReadOnly=False)  #: PGW address in the eNB config file
LTE_ENB_SGW = Attribute(key='LTE_ENB_SGW', type=int, isReadOnly=False)  #: SGW address in the eNB config file
LTE_ENB_PHY_CELL_ID = Attribute(key='LTE_ENB_PHY_CELL_ID', type=int, isReadOnly=False) #: Cell identity
LTE_ENB_MCC = Attribute(key='LTE_ENB_MCC', type=int, isReadOnly=False)  #: eNB Mobile Country Code
LTE_ENB_MNC = Attribute(key='LTE_ENB_MNC', type=int, isReadOnly=False)  #: eNB Mobile Network Code

LTE_ENB_LOCAL_SCTP_PORT = Attribute(key='LTE_ENB_LOCAL_SCTP_PORT', type=int, isReadOnly=False)  #: SCTP port on the eNB to listen to S1 messages
LTE_ENB_EPC_SCTP_PORT = Attribute(key='LTE_ENB_EPC_SCTP_PORT', type=int, isReadOnly=False)  #: SCTP port for the remote EPC
LTE_ENB_MAX_ERAB = Attribute(key='LTE_ENB_MAX_ERAB', type=int, isReadOnly=False)  #: maximum RAB per UE
LTE_ENB_PUSCH_POWER_CONTROL_STATE = Attribute(key='LTE_ENB_PUSCH_POWER_CONTROL_STATE', type=bool, isReadOnly=False)  #: Enable/disable PUSCH Power control
LTE_ENB_PDCCH_POWER_CONTROL_STATE = Attribute(key='LTE_ENB_PDCCH_POWER_CONTROL_STATE', type=bool, isReadOnly=False)  #: Enable/disable PDCCH power control
LTE_ENB_SINR_PUCCH_POWER_CONTROL_STATE = Attribute(key='LTE_ENB_SINR_PUCCH_POWER_CONTROL_STATE', type=bool, isReadOnly=False)  #: enable/disable SINR based power control for PUCCH
LTE_ENB_HARQ_PUCCH_POWER_CONTROL_STATE = Attribute(key='LTE_ENB_HARQ_PUCCH_POWER_CONTROL_STATE', type=bool, isReadOnly=False)  #: enable/disable HARQ based power control for PUCCH
LTE_ENB_FREQUENCY_PUSCH_POWER_CONTROL_STATE = Attribute(key='LTE_ENB_FREQUENCY_PUSCH_POWER_CONTROL_STATE', type=bool, isReadOnly=False)  #: enable/disable frequency based PUSCH power control
LTE_ENB_PUCCH_TARGET_SINR = Attribute(key='LTE_ENB_PUCCH_TARGET_SINR', type=int, isReadOnly=False)  #: Set the SINR target for PUCCH power control
LTE_ENB_PUCCH_TARGET_BLER = Attribute(key='LTE_ENB_PUCCH_TARGET_BLER', type=int, isReadOnly=False)  #: set the BLER target for PUCCH power control
LTE_ENB_PDCH_POWER_OFFSET = Attribute(key='LTE_ENB_PDCH_POWER_OFFSET', type=int, isReadOnly=False)  #: PDSCH power offset
LTE_ENB_PSCH_POWER_OFFSET = Attribute(key='LTE_ENB_PSCH_POWER_OFFSET', type=int, isReadOnly=False)  #: PSCH power offset
LTE_ENB_SSCH_POWER_OFFSET = Attribute(key='LTE_ENB_SSCH_POWER_OFFSET', type=int, isReadOnly=False)  #: SSCH power offset
LTE_ENB_RACH_PREAMBLES = Attribute(key='LTE_ENB_RACH_PREAMBLES', type=int, isReadOnly=False)  #: Number of RA preambles
LTE_ENB_MCS_DL = Attribute(key='LTE_ENB_MCS_DL', type=int, isReadOnly=False)  #: MCS profile to be used for DL
LTE_ENB_MCS_UL = Attribute(key='LTE_ENB_MCS_UL', type=int, isReadOnly=False)  #: MCS profile to be used for UL
LTE_ENB_RADIO_STATE = Attribute(key='LTE_ENB_RADIO_STATE', type=bool, isReadOnly=False)  #: Set radio on/off
LTE_ENB_CQI_REPORT_STATE = Attribute(key='LTE_ENB_CQI_REPORT_STATE', type=bool, isReadOnly=False)  #: Enable/disable CQI reporting
LTE_ENB_UE_REPORT_STATE = Attribute(key='LTE_ENB_UE_REPORT_STATE', type=bool, isReadOnly=False)  #: Enable/Disable UE reporting
LTE_ENB_UE_INACTIVITY_TIMER = Attribute(key='LTE_ENB_UE_INACTIVITY_TIMER', type=int, isReadOnly=False)  #: UE inactivity timer
LTE_ENB_CIPHER_ALGORITHM_LIST = Attribute(key='LTE_ENB_CIPHER_ALGORITHM_LIST', type=list, isReadOnly=False)  #: List for the desired Ciphering algorithms

LTE_RCC_FRONTHAUL_IF_NAME_LOCAL = Attribute(key='LTE_RCC_FRONTHAUL_IF_NAME_LOCAL', type=int, isReadOnly=False)  #: Interface of the local fronthaul
LTE_RCC_FRONTHAUL_IP_ADDRESS_LOCAL = Attribute(key='LTE_RCC_FRONTHAUL_IP_ADDRESS_LOCAL', type=int, isReadOnly=False)  #: IP of the local fronthaul
LTE_RCC_FRONTHAUL_PORT_LOCAL = Attribute(key='LTE_RCC_FRONTHAUL_PORT_LOCAL', type=int, isReadOnly=False)  #: port of the local fronthaul
LTE_RCC_FRONTHAUL_IP_ADDRESS_REMOTE = Attribute(key='LTE_RCC_FRONTHAUL_IP_ADDRESS_REMOTE', type=int, isReadOnly=False)  #: IP of the remote fronthaul
LTE_RCC_FRONTHAUL_PORT_REMOTE = Attribute(key='LTE_RCC_FRONTHAUL_PORT_REMOTE', type=int, isReadOnly=False)  #: port of the remote fronthaul
LTE_RRU_FRONTHAUL_IF_NAME_LOCAL = Attribute(key='LTE_RRU_FRONTHAUL_IF_NAME_LOCAL', type=int, isReadOnly=False)  #: Interface of the local fronthaul
LTE_RRU_FRONTHAUL_IP_ADDRESS_LOCAL = Attribute(key='LTE_RRU_FRONTHAUL_IP_ADDRESS_LOCAL', type=int, isReadOnly=False)  #: IP of the local fronthaul
LTE_RRU_FRONTHAUL_PORT_LOCAL = Attribute(key='LTE_RRU_FRONTHAUL_PORT_LOCAL', type=int, isReadOnly=False)  #: port of the local fronthaul
LTE_RRU_FRONTHAUL_IP_ADDRESS_REMOTE = Attribute(key='LTE_RRU_FRONTHAUL_IP_ADDRESS_REMOTE', type=int, isReadOnly=False)  #: IP of the remote fronthaul
LTE_RRU_FRONTHAUL_PORT_REMOTE = Attribute(key='LTE_RRU_FRONTHAUL_PORT_REMOTE', type=int, isReadOnly=False)  #: port of the remote fronthaul

#********
#UE net Attribute
#********

LTE_UE_APN = Attribute(key='LTE_UE_APN', type=str, isReadOnly=False)  #: APN
LTE_UE_PLMN = Attribute(key='LTE_UE_PLMN', type=int, isReadOnly=False)  #: PLMNID


#********
#LTE UPI
#********

def MME_activation():
    '''Once set the MME parameters using the set_parameters(param_key_values_dict), MME_activation is to be used for running the MME

    Examples:
        .. code-block:: python

            >> controller.blocking(False).node(node).net.MME_activation()

    Args:
        controller:
        node: physical machine where the MME run

    Returns:
        0 = success, 1=fail, +1=error code
    '''
    return


def MME_deactivation():
    '''MME_deactivation is to be used for stopping the MME

    Examples:
        .. code-block:: python

            >> controller.blocking(False).node(node).net.MME_deactivation()

    Args:
        controller:
        node: physical machine where the MME run

    Returns:
        0 = success, 1=fail, +1=error code
    '''
    return


def HSS_activation():
    '''Once set the HSS parameters using the set_parameters(param_key_values_dict), HSS_activation is to be used for running the HSS

    Examples:
        .. code-block:: python

            >> controller.blocking(False).node(node).net.HSS_activation()

    Args:
        controller:
        node: physical machine where the HSS run

    Returns:
        0 = success, 1=fail, +1=error code
    '''
    return


def HSS_deactivation():
    '''HSS_deactivation is to be used for stopping the HSS

    Examples:
        .. code-block:: python

            >> controller.blocking(False).node(node).net.HSS_deactivation()

    Args:
        controller:
        node: physical machine where the HSS run

    Returns:
        0 = success, 1=fail, +1=error code
    '''
    return


def SPGW_activation():
    '''Once set the SPGW parameters using the set_parameters(param_key_values_dict), SPGW_activation is to be used for running the SPGW

    Examples:
        .. code-block:: python

            >> controller.blocking(False).node(node).net.SPGW_activation()

    Args:
        controller:
        node: physical machine where the SPGW run

    Returns:
        0 = success, 1=fail, +1=error code
    '''
    return


def SPGW_deactivation():
    '''SPGW_deactivation is to be used for stopping the SPGW

    Examples:
        .. code-block:: python

            >> controller.blocking(False).node(node).net.SPGW_deactivation()

    Args:
        controller:
        node: physical machine where the SPGW run

    Returns:
        0 = success, 1=fail, +1=error code
    '''
    return


def eNB_activation():
    '''Once set the eNB parameters using the set_parameters(param_key_values_dict), eNB_activation is to be used for running the eNB

    Examples:
        .. code-block:: python

            >> controller.blocking(False).node(node).net.eNB_activation()

    Args:
        controller:
        node: physical machine where the eNB run

    Returns:
        0 = success, 1=fail, +1=error code'''
    return


def eNB_deactivation():
    '''eNB_deactivation is to be used for stopping the eNB

    Examples:
        .. code-block:: python

            >> controller.blocking(False).node(node).net.eNB_deactivation()

    Args:
        controller:
        node: physical machine where the eNB run

    Returns:
        0 = success, 1=fail, +1=error code
    '''
    return


def RRU_activation():
    '''Once set the RRU parameters using the set_parameters(param_key_values_dict), RRU_activation is to be used for running the RRU

    Examples:
        .. code-block:: python

            >> controller.blocking(False).node(node).net.RRU_activation()

    Args:
        controller:
        node: physical machine where the RRU run

    Returns:
        0 = success, 1=fail, +1=error code'''
    return


def RRU_deactivation():
    '''RRU_deactivation is to be used for stopping the RRU

    Examples:
        .. code-block:: python

            >> controller.blocking(False).node(node).net.RRU_deactivation()

    Args:
        controller:
        node: physical machine where the RRU run

    Returns:
        0 = success, 1=fail, +1=error code
    '''
    return


def RCC_activation():
    '''Once set the RCC parameters using the set_parameters(param_key_values_dict), RCC_activation is to be used for running the RCC

    Examples:
        .. code-block:: python

            >> controller.blocking(False).node(node).net.RCC_activation()

    Args:
        controller:
        node: physical machine where the RCC run

    Returns:
        0 = success, 1=fail, +1=error code'''
    return


def RCC_deactivation():
    '''RCC_deactivation is to be used for stopping the RCC

    Examples:
        .. code-block:: python

            >> controller.blocking(False).node(node).net.RCC_deactivation()

    Args:
        controller:
        node: physical machine where the RCC run

    Returns:
        0 = success, 1=fail, +1=error code'''
    return


def UE_activation():
    '''UE_activation is to be used for running the UE

    Examples:
        .. code-block:: python

            >> controller.blocking(False).node(node).net.UE_activation()

    Args:
        controller:
        node: physical machine where the UE run

    Returns:
        0 = success, 1=fail, +1=error code'''
    return


def UE_deactivation():
    '''UE_deactivation is to be used for stopping the UE

    Examples:
        .. code-block:: python

            >> controller.blocking(False).node(node).net.UE_deactivation()

    Args:
        controller:
        node: physical machine where the UE run

    Returns:
        0 = success, 1=fail, +1=error code'''
    return


def UE_attach():
    '''UE_attach is to be used for attaching the UE to the MME

    Examples:
        .. code-block:: python

            >> controller.blocking(False).node(node).net.UE_attach()

    Args:
        controller:
        node: physical machine where the UE run

    Returns:
        0 = success, 1=fail, +1=error code'''
    return


def UE_detach():
    '''UE_detach is to be used for detaching the UE without stopping it

    Examples:
        .. code-block:: python

            >> controller.blocking(False).node(node).net.UE_detach()

    Args:
        controller:
        node: physical machine where the UE run

    Returns:
        0 = success, 1=fail, +1=error code'''
    return