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

def gendoc():
    """ Generates sphinx html documentation for IoTPy """
    with cd("./docs"):
        local("make html")

def graphs():
    """ Generate hierarchy class library graphs """
    local("pyreverse -Ak -o png -p IoTPy IoTPy")

def upload():
    """ Uploads iotpy/ to carambola:/tmp/iotpy/ """
    local("tar -czf /tmp/iotpy.tar.gz IoTPy examples")
    put("/tmp/iotpy.tar.gz", "/tmp/")
    with cd("/tmp"):
        run("tar -zxf iotpy.tar.gz")

def upload_test():
    """ Uploads to carambola:/tmp/iotpy and run tests """
    pass

def test_pyflakes():
        local("echo 'PYFLAKES --------' > pyflakes.log")
        local("pyflakes IoTPy >> pyflakes.log")

def test_pep8():
        local("echo 'PEP8 --------' > pep8.log")
        local("pep8 IoTPy --show-source --show-pep8 --statistics --count >> pep8.log")