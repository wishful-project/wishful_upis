from . import net
from . import radio
from . import mgmt
from . import net_func
from . import context

from . import lte
from . import wifi
from . import zigbee

# everything to the buttom is only for backward compatilibity,
# to be removed in future
from .tools import copy_functions_from_class_to_module
from .tools import copy_functions_from_subclasses_to_module
from .tools import add_module_to_module

add_module_to_module(net, wifi)
add_module_to_module(radio, wifi)
add_module_to_module(net_func, wifi)

add_module_to_module(net, lte)
add_module_to_module(radio, lte)
add_module_to_module(net_func, lte)

add_module_to_module(net, zigbee)
add_module_to_module(radio, zigbee)
add_module_to_module(net_func, zigbee)

copy_functions_from_class_to_module(net)
copy_functions_from_class_to_module(radio)
copy_functions_from_class_to_module(mgmt)
copy_functions_from_class_to_module(net_func)
copy_functions_from_class_to_module(context)

copy_functions_from_class_to_module(lte)
copy_functions_from_class_to_module(wifi)
copy_functions_from_class_to_module(zigbee)

copy_functions_from_subclasses_to_module(radio, radio.Radio)
copy_functions_from_subclasses_to_module(net, net.Network)

