#!/usr/bin/python3
"""Create a folder if not exists and create a tgz
file with the local command execution with fabric"""

from datetime import datetime
from fabric.api import local, hide


def do_pack():
    """Create the folder and the tgz"""
    try:
        with hide('running'):
            local("mkdir -p ./versions")

        date = datetime.now()
        adt = date.strftime("%Y%m%d%H%M%S")

        command = "tar -cvzf versions/web_static_{}.tgz web_static".format(adt)
        path = "versions/web_static_{}.tgz".format(adt)
        message = "Packing web_static to {}".format(path)

        print(message)
        local(command)

        with hide('running'):
            size = local('wc -c < {}'.format(path), capture=True)

        f_msg = "web_static packed: {} -> {}Bytes".format(path, size)

        with hide('running'):
            local("chmod 664 {}".format(path))

        print(f_msg)

        return path
    except:
        return None
