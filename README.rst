=======================
Qiime 2 LL Quick Viewer
=======================


.. image:: https://img.shields.io/pypi/v/qiime_2_ll_quick_viewer.svg
        :target: https://pypi.python.org/pypi/qiime_2_ll_quick_viewer

.. image:: https://img.shields.io/travis/gluque/qiime_2_ll_quick_viewer.svg
        :target: https://travis-ci.org/gluque/qiime_2_ll_quick_viewer

.. image:: https://readthedocs.org/projects/qiime-2-ll-quick-viewer/badge/?version=latest
        :target: https://qiime-2-ll-quick-viewer.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/gluque/qiime_2_ll_quick_viewer/shield.svg
     :target: https://pyup.io/repos/github/gluque/qiime_2_ll_quick_viewer/
     :alt: Updates


This tool launches a simple web server to quicly visualize the contents locate into the **``data``** folder from
a [Qiime 2](https://qiime2.org/) visualization artifact i.e. files produced by **Qiime 2** with extension ``\*.qzv``.

* Free software: MIT license
* Documentation: https://qiime-2-ll-quick-viewer.readthedocs.io.


Installation
------------

You can install this tool on a Python 3.6 environment using this command:

``pip install qiime_2_ll_quick_viewer``


Usage
--------

Given a **Qiime 2** visualization artifact e.g. ``demux.qzv`` you can run this command on your server:

``qiime_2_ll_quick_viewer --filename /full_path_to/demux.qzv``

By default, **qiime_2_ll_quick_viewer** will launch a web server on the port **8089** but you can change it for the one you want with the option `--port XXXX`.
Then, you can for example open a SSH tunnel to the remote port opened on your server by **qiime_2_ll_quick_viewer** with this command:

``$ ssh -L 8089:localhost:8089 user@your_server``

Finally, open a browser and go to this address: [http://localhost:8089](http://localhost:8089).


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

