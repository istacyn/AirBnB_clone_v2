#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
from os.path import exists


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    if not exists('versions'):
        local('mkdir -p versions')
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        file_name = "web_static_{}.tgz".format(timestamp)
        local("tar -czvf versions/{} web_static".format(file_name))
        archive_path = 'versions/{}'.format(file_name)
    if exists(archive_path):
        return archive_path
    else:
        return None
