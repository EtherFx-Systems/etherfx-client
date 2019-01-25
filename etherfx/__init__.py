import sys
from etherfx.loader.EtherLoader import EtherLoader

sys.meta_path = [EtherLoader()]