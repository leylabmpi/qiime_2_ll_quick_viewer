Qiime 2 [Ley Lab](http://leylab.tuebingen.mpg.de/) Quick Viewer
=======================

[![image](https://img.shields.io/pypi/v/qiime_2_ll_quick_viewer.svg)](https://pypi.python.org/pypi/qiime_2_ll_quick_viewer)

[![image](https://img.shields.io/travis/leylabmpi/qiime_2_ll_quick_viewer.svg)](https://travis-ci.org/leylabmpi/qiime_2_ll_quick_viewer)

[![Updates](https://pyup.io/repos/github/leylabmpi/qiime_2_ll_quick_viewer/shield.svg)](https://pyup.io/repos/github/leylabmpi/qiime_2_ll_quick_viewer/)

This tool launches a simple web server to quickly visualize the contents
locate into the `data` folder from a [Qiime 2](https://qiime2.org/)
visualization artifact, i.e. files produced by **Qiime 2** with
extension `*.qzv`.

-   Free software: MIT license

Installation
============

You can install this tool on a Python 3.6 environment using this
command:

`pip install qiime_2_ll_quick_viewer`

Usage
=====

Given a **Qiime 2** visualization artifact e.g. `demux.qzv` you can run
this command on your server:

`$ qiime_2_ll_quick_viewer --filename /full_path_to/demux.qzv`

By default, **qiime\_2\_ll\_quick\_viewer** will launch a web server on
the port **8089** but you can change it for the one you want with the
option `--port XXXX`. Then, you can for example open a SSH tunnel to the
remote port opened on your server by **qiime\_2\_ll\_quick\_viewer**
with this command:

`$ ssh -L 8089:localhost:8089 user@your_server`

Finally, open a browser and go to this address: http://localhost:8089\_.

Command options:

:   

    -f, --filename TEXT Full path to a Qiime2 visualization file (\*.qzv).

    :   \[required\]

    -p, --port INTEGER Port to launch the web server. \[required\] -h,
    --help Show the help info and exit.

Credits
=======

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.
