from . import net
from . import radio
from . import mgmt
from . import net_func
from . import context

from . import lte
from . import wifi
from . import zigbee

from .tools import copy_functions_to_module

copy_functions_to_module(net)
copy_functions_to_module(radio)
copy_functions_to_module(mgmt)
copy_functions_to_module(net_func)
copy_functions_to_module(context)

copy_functions_to_module(lte)
copy_functions_to_module(wifi)
copy_functions_to_module(zigbee)
