from fabric.api import *
from fabric.contrib.project import rsync_project

env['use_ssh_config'] = True
env['hosts'] = ['events@rosedu.org']
env['target_directory'] = 'public_html/web-workshops'


@task
def deploy():
    local('./manage.py freeze')
    rsync_project(env['target_directory'], 'build/', delete=True)
