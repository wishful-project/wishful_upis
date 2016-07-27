"""The WiSHFUL radio control interface, UPI_R.
Used for configuration/monitoring of the lower
layers of the network protocol stack (lower MAC and PHY).

Note, the functions can be supported by WMP platform.

"""
__author__ = "Domenico Garlisi"
__copyright__ = "Copyright (c) 2016, CNIT"
__version__ = "0.1.0"
__email__ = "{domenico.garlisi@cnit.it}"

"""
UPI_M
"""
def install_execution_engine(myargs):
    """The architectures of the nodes present in the testbed define an execution environment or execution engine
    able to run radio programs defined in a high-level programming language. This management function install an
    execution environment on a node. If the execution engine is implemented on the microcode wireless card, the
    function the copy and able the correct microcode.

    :param myargs:list of parameters, in term of a dictionary data type (list of key: value) in which: the key is 'execution_engine' and the value is the path of the execution engine file(s).
    :return result: return 0 if the parameter setting call was successfully performed, 1 partial success, 2 error.

    example:
        >> args = {'execution_engine' : ['runtime/connectors/wmp_linux/execution_engine/wmp'] } \n
        >> result = UPI_M.installExecutionEngine(args) \n
        >> print result \n
        0 \n
    """
    return

def init_test(myargs):
    """This function is a management function used to setup the nodes before the experiment, the function can
    performs different action.They are i) restart the driver module, ii) creates infrastructure BSS, the node
    is used such Access Point, iii) associate node to infrastructure BSS. The different action are addressing the
    key 'operation' in the dictionary data type of arguments.

    :param myargs: list of parameters, in term of a dictionary data type (list of key: value) in which: The key "interface" specify the network interface to use. The key 'operaiton' is used to specify the action, the supported value for the key 'operation' are 'module', used to restart the module, 'create-network', used to create the IBSS, and 'association' used to associate the node to the IBSS. The key 'ssid' is used to define the essid of the IBSS. The key 'ip_address' is used to define the ip address of the wireless interface.
    :return result: return 0 if the parameter setting call was successfully performed, 1 partial success, 2 error.

    example :
        >> args ={'interface' : 'wlan0', 'operation' : ['create-network'], 'ssid' : ['MyNetwork'], 'ip_address' : ['192.168.1.1'] } ] \n
        >> result = UPI_M.initTest(args) \n
        >> print result \n
        0 \n
    """
    return

def get_iface_ip_addr(iface):
    '''Returns the IP address of a given interface.
    '''
    return
