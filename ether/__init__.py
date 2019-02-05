import sys
from ether._internal.loader.EtherLoader import EtherLoader

sys.meta_path.append(EtherLoader())