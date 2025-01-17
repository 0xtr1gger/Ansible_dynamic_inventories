# base image
FROM ubuntu:20.04 

# copying setup script
COPY ./setup.sh /usr/bin/setup.sh

# assigning execute permissions to the script and then execute the script
RUN chmod +x /usr/bin/setup.sh && /usr/bin/setup.sh

EXPOSE 22

# start SSH service
CMD ["/usr/sbin/sshd", "-D"]