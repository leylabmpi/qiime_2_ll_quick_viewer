# -*- coding: utf-8 -*-

"""Console script for qiime_2_ll_quick_viewer."""

import click
from qiime_2_ll_quick_viewer import launch_server

@click.command()
@click.option('-f', '--filename', required=True, help="Full path to a Qiime2 visualization file (*.qzv).")
@click.option('-p', '--port', required=True, default=8080, help="Port to launch the web server.")
def main(filename, port):
    """Quick viewer for Qiime 2 visualization artifacts.\n
    It launches a simple webserver to visualize the contents of the data folder in a browser.
    The webserver is launched in your server and you can access through a SSH session with X11 port forwarding enabled.
    """
    launch_server(filename, port)


if __name__ == "__main__":
    main()
