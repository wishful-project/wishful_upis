__author__ = "Francesco Giannone, Domenico Garlisi"
__copyright__ = "Copyright (c) 2017, Sant'Anna, CNIT"
__version__ = "0.1.0"
__email__ = "{francesco.giannone@santannapisa.it, domenico.garlisi@cnit.it}"

'''
The protocol-specific definition of the WiSHFUL network control interface, UPI_N, for configuration/monitoring of the higher
layers of the network protocol stack (upper MAC and higher).
LTE protocol family
'''


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