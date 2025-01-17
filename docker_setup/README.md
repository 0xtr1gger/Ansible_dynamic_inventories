This directory holds the files necessary to build an image for an Ubuntu-based container to serve as an Ansible node.

Here are the commands to build the container and turn it into an Ansible node:

1. Build the image:

```bash
docker build -t ansible_node_image .
```

2. Run the container:

```bash
docker run -d --name ansible_node_one ansible_node_image /bin/bash
```

3. Generate SSH keys on your host machine:

```bash
ssh-keygen -t rsa -b 4096
```

4. Copy the keys into the container:

```bash
docker exec -it ansible_node_one bash -c "echo $(cat ~/.ssh/id_r  
sa.pub) >> /home/ansible/.ssh/authorized_keys"
```

5. Find the IP address of the running container:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ansible_node_one
```

Output:

```bash
172.17.0.2
```

6. Check SSH connectivtiy:

```bash
ssh ansible@172.17.0.2
```

7. Create an inventory to manage the container with Ansible. You can find how to do that in this repository.

