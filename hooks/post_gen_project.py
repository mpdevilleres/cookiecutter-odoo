#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.use_lets_encrypt }}' == 'y':
        import os, subprocess

        dhparam = os.path.join(PROJECT_DIRECTORY, 'compose', 'nginx', 'dhparams.pem')
        if not os.path.isfile(dhparam):
            subprocess.call(['openssl', 'dhparam', '-out', dhparam, '1024'])

