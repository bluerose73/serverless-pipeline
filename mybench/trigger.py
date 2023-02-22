import requests
import json
import click

@click.command()
@click.option('--trigger-config', type=str, default='./trigger-config.json')
@click.option('--function-config', type=str, default='./function-config.json')
def cli(trigger_config, function_config):
    with open(trigger_config) as f:
        trig_config = json.load(f)
    function_name = trig_config['function']
    with open(function_config) as f:
        func_config = json.load(f)[function_name]

    r = requests.post(trig_config['url'], json=func_config['post-json'])
    print('[Json Reply]')
    print(json.dumps(r.json(), indent=4))

if __name__ == '__main__':
    cli()