===============================
Qiime 2 `Ley Lab`_ Quick Viewer
===============================

.. _Ley Lab: http://leylab.tuebingen.mpg.de/

.. image:: https://img.shields.io/pypi/v/qiime_2_ll_quick_viewer.svg
        :target: https://pypi.python.org/pypi/qiime_2_ll_quick_viewer

.. image:: https://img.shields.io/travis/leylabmpi/qiime_2_ll_quick_viewer.svg
        :target: https://travis-ci.org/leylabmpi/qiime_2_ll_quick_viewer

.. image:: https://pyup.io/repos/github/leylabmpi/qiime_2_ll_quick_viewer/shield.svg
     :target: https://pyup.io/repos/github/leylabmpi/qiime_2_ll_quick_viewer/
     :alt: Updates


This tool launches a simple web server to quickly visualize the contents locate into the ``data`` folder from
a `Qiime 2`_ visualization artifact, i.e. files produced by **Qiime 2** with extension ``*.qzv``.

.. _Qiime 2: https://qiime2.org/

* Free software: MIT license


Installation
------------

You can install this tool on a Python 3.5+ environment using either PIP

``pip install qiime_2_ll_quick_viewer``

or Conda

``conda install -c leylabmpi qiime_2_ll_quick_viewer``


Usage
-----

Given a **Qiime 2** visualization artifact e.g. ``demux.qzv`` you can run this command on your server:

``$ qiime_2_ll_quick_viewer --filename /full_path_to/demux.qzv``

By default, **qiime_2_ll_quick_viewer** will launch a web server on the port **8089** but you can change it for the one you want with the option ``--port XXXX``.
Then, you can for example open a SSH tunnel to the remote port opened on your server by **qiime_2_ll_quick_viewer** with this command:

``$ ssh -L 8089:localhost:8089 user@your_server``

Finally, open a browser and go to this address: `http://localhost:8089`_.

.. _http://localhost:8089: http://localhost:8089

Command options:

.. code-block:: bash

   -f, --filename TEXT  Full path to a Qiime2 visualization file (*.qzv). [required]
   -p, --port INTEGER   Port to launch the web server. [required]
   -h, --help           Show the help info and exit.


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

