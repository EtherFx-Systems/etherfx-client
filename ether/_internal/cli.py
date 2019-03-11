import click
import yaml
import os
from click_default_group import DefaultGroup
from functools import lru_cache

class EtherConfig(yaml.YAMLObject):
    yaml_tag = u'!EtherConfig'
    def __init__(self, host, port):
        self.host = host
        self.port = port
    def __repr__(self):
        return f'Cluster Host at: {self.host}:{self.port}'

@click.group(cls=DefaultGroup, default='init', default_if_no_args=True)
def cli():
    pass

@cli.command()
@click.option('--host', prompt='Cluster host IP Address')
@click.option('--port', prompt='Cluster host port')
def init(host, port):
    with open('.ether.yml', 'w') as optfile:
        yaml.dump(EtherConfig(host=host, port=port), optfile)

@lru_cache
def get_config():
    if os.path.isfile('.ether.yml'):
        with open('.ether.yml', 'r') as optfile:
            return yaml.load(optfile)
    else:
        cli()
        return get_config()

if __name__ == '__main__':
    cli()