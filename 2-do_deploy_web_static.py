#!/usr/bin/python3
"""Distributes an archive to web servers"""
from fabric import *
from os.path import exists
from datetime import datetime

env.hosts = ['100.25.163.190', '54.82.173.97']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not exists(archive_path):
        return False

    try:
        # Upload archive to /tmp/ directory of web server
        put(archive_path, '/tmp/')

        # Uncompress archive to folder on the web server
        archive_filename = archive_path.split('/')[-1]
        folder_name = archive_filename.split('.')[0]
        releases_path = '/data/web_static/releases/'
        run('mkdir -p {}{}/'.format(releases_path, folder_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(archive_filename,
            releases_path, folder_name))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Move extracted files to correct location
        run('mv {}{}/web_static/* {}{}/'.format(releases_path,
            folder_name, releases_path, folder_name))
        run('rm -rf {}{}/web_static'.format(releases_path, folder_name))

        # Delete the existing symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link to new version
        run('ln -s {}{}/ /data/web_static/current'.format(
            releases_path, folder_name))

        return True

    except Exception as e:
        print(e)
        return False
