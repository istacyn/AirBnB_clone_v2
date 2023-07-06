#!/usr/bin/python3
"""Distributes an archive to web servers"""
from fabric.api import env, run, put
from os.path import exists
from datetime import datetime

env.hosts = ['100.25.163.190', '54.82.173.97']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    try:
        if not (exists(archive_path)):
            return False

        # Upload archive to /tmp/ directory of web server
        put(archive_path, '/tmp/')

        # Create a target directory
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/\
                releases/web_static_{}/'.format(timestamp))

        # Uncompress archive to folder on the web server
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
                /data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))

        # Delete the archive from the web server
        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        # Move extracted files to correct location
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
                /data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))
        run('sudo rm -rf /data/web_static/releases/\
                web_static_{}/web_static'.format(timestamp))

        # Delete the existing symbolic link
        run('sudo rm -rf /data/web_static/current')

        # Create a new symbolic link to new version
        run('sudo ln -s /data/web_static/releases/\
                web_static_{}/ /data/web_static/current'.format(timestamp))

    except Exception as e:
        print(e)
        return False

    return True
