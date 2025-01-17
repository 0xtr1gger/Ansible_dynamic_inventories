apt-get update
apt-get install -y openssh-server # install ssh
service ssh start                 # start SSH daemon
apt-get install -y python3        # install python3
apt-get install -y sudo           # install sudo

# create a runtime directory for sshd
mkdir -p /var/run/sshd

# set up a dedicated user for Ansible automation
useradd -m ansible -s /bin/bash
echo "ansible:ansible" | chpasswd
echo "ansible ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# create an SSH directory in /home/ansible
mkdir /home/ansible/.ssh