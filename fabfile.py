from fabric.api import run, local, cd, put, env

"""
USE:

fab upload

ISSUES:
fabric && dropbear sftp
http://wiki.openwrt.org/doc/howto/sftp.server
http://wiki.openwrt.org/inbox/replacingdropbearbyopensshserver
"""

env.use_ssh_config = True
env.shell = "/bin/ash -l -c"

# Set default hosts
if not env.hosts:
    env.hosts = ["user@hostnameorip"]

def upload():
    """ Uploads iotpy/ to carambola:/tmp/iotpy/ """
    local("tar -czf /tmp/iotpy.tar.gz IoTPy examples")
    put("/tmp/iotpy.tar.gz", "/tmp/")
    with cd("/tmp"):
        run("tar -zxf iotpy.tar.gz")

def upload_test():
    """ Uploads to carambola:/tmp/iotpy and run tests """
    pass

def tests():
    """ Run tests """
    pass