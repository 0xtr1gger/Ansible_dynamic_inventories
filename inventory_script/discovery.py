#!/usr/bin/env python3

import json   # formatting output
import docker # interacting with Docker API
import socket

def get_docker_containers():
    client = docker.from_env()
    containers = client.containers.list()
    inventory = {'_meta': {'hostvars': {}}}
    
    for container in containers:
        try:
            # get container's IP address
            container_ip = container.attrs['NetworkSettings']['Networks']['bridge']['IPAddress']
            inventory['all'] = inventory.get('all', {'hosts': []})
            inventory['all']['hosts'].append(container.name)
            inventory['_meta']['hostvars'][container.name] = {
				'ansible_host': container_ip,
				'container_id': container.id,
				'status': container.status,
				'ansible_user': 'ansible',
				'ansible_python_interpreter': '/usr/bin/python3.8'
            }
        except KeyError as e:
            print(f"Skipping container {container.name} due to error: {e}")
    
    return inventory

def main():
    # get the inventory file
    inventory = get_docker_containers()

    # convert the dictionary to JSON and output
    print(json.dumps(inventory, indent=4))

if __name__ == "__main__":
    main()