import sys
from ether._internal.loader.EtherLoader import EtherLoader
from ether._internal.cli import get_config
conf = get_config()
sys.meta_path.append(EtherLoader())