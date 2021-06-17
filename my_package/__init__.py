print(f'Importing {__name__}')

# Both ways to import (also with relative path)
# import my_package.subpackage_1 # - A bit messy, since to access subpackage_1.value 
#   code: my_package.my_package.subpackage_1.module_1.value is needed
from my_package import subpackage_1
from . import subpackage_2
from .subpackage_3 import *