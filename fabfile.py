from fabric.api import run, env, local, sudo, prefix
from contextlib import contextmanager


def live():
    env.hosts = ['54.202.70.27']
    env.user = 'ubuntu'
    env.cwd = '/home/ubuntu'
    env.project = 'vkposts'


def deploy():
    # sudo("git pull")
    pass


def initial():
    # setup_directories()
    clone_repo()
    install_virtualenv()
    install_requirements()
    # create_nginx_config_symblink()
    # activate_uwsgi_ini()


def create_nginx_config_symblink():
    sudo('cp %s/%s/nginx_vkposts /etc/nginx/sites-avaiable/' %(env.cwd, env.project))
    sudo('ln -s /etc/nginx/sites-avaiable/nginx_vkposts /etc/nginx/sites-enabled/' %(env.cwd, env.project))


def activate_uwsgi_ini():
    sudo('uwsgi --ini %s/%s/vkposts.ini' % (env.cwd, env.project))


# not working
def setup_directories():
    sudo('mkdir -p %s' % env.cwd)


def clone_repo():
    sudo('git clone https://github.com/andreyavramchikov/vkposts.git')


@contextmanager
def source_env():
    """Actives embedded virtual env"""
    with prefix('source env/bin/activate'):
        yield


def install_requirements():
    """Installs requirements.txt packages using pip"""
    with source_env():
        sudo('pip install -r vkposts/requirements.txt')


def install_virtualenv():
    """
    Setup a fresh virtualenv.
    """
    sudo('virtualenv %s/env --no-site-packages;' % env.cwd)


def setup():
    sudo('apt-get -y update')
    sudo('apt-get -y upgrade')
    sudo('apt-get -y install python-dev')
    sudo('apt-get -y install python-virtualenv')
    sudo('apt-get -y install libmysqlclient-dev')
    sudo('apt-get install -y git')
    sudo('apt-get install -y build-essential python')
    sudo('apt install -y uwsgi')
    sudo('apt install -y python-pip')
    sudo('apt-get install -y nginx')

# FOR UBUNTU 16.04
# export LC_ALL="en_US.UTF-8"
# export LC_CTYPE="en_US.UTF-8"
