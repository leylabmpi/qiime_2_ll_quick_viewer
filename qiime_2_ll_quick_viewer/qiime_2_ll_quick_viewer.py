# -*- coding: utf-8 -*-

"""Main module."""
import http.server
import socketserver
import os
import zipfile
import tempfile
import click
import random


def launch_server(filename, port):
    tmp_dir = tempfile.gettempdir()
    rand_fn = ''.join([random.choice('0123456789ABCDEF') for x in range(8)])
    tmp_dir = os.path.join(tmp_dir, rand_fn)

    with zipfile.ZipFile(filename, 'r') as zip_ref:
        contents = zip_ref.namelist()
        index_html = [x for x in contents if x.endswith('index.html')][0]
        web_dir = os.path.join(tmp_dir, os.path.dirname(index_html))
        zip_ref.extractall(tmp_dir)

    os.chdir(web_dir)
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)
    click.echo("Qiime 2 Ley Lab Viewer at port %s, from %s" % (port, web_dir))
    httpd.serve_forever()
