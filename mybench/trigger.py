import requests
import json
import click

@click.command()
@click.option('--trigger-config', type=str, default='./trigger-config.json')
@click.option('--function-config', type=str, default='./function-config.json')
@click.option('--function', type=str)
def cli(trigger_config, function_config, function):
    with open(trigger_config) as f:
        trig_config = json.load(f)

    if function:
        trig_config['function'] = function

    function_name = trig_config['function']
    with open(function_config) as f:
        func_config = json.load(f)[function_name]

    print('[Json Sent]')
    print(func_config['post-json'])

    r = requests.post(trig_config['url'], json=func_config['post-json'])
    if r.status_code == 200:
        print('[Json Reply]')
        print(json.dumps(r.json(), indent=4))
    else:
        print(r.text)
        

if __name__ == '__main__':
    cli()