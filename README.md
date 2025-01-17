# Lab: Ansible dynamic inventories with Docker coontainers

This repository contains files used to setup a lab to practice working with dynamic Ansible inventories using Docker containers. In this lab, I created both a Python script for my own dynamic inventory, and a a configuration file to utilize an exsiting inventory plugin, `community.docker.docker_containers`.

The description of the full setup process and everything that i did is available in my Medium, as a story:

- [Mastering Ansible Inventories - Part 2: Dynamic Inventories](<link>)

If you don't have a Medium subscription, use my friend link that I provide at the beginning of the article to read the story for free.

The tree of this repository:

```bash
tree -L 3
```

```bash
.
├── docker_setup
│   ├── Dockerfile
│   ├── README.md
│   └── setup.sh
├── inventory_plugin
│   ├── dynamic_inventory.docker.yaml
│   └── README.md
├── inventory_script
│   ├── discovery.py
│   └── README.md
├── README.md
└── screenshots
    ├── # ...
    └── # screenshots
```

