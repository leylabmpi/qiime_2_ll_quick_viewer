# -*- coding: utf-8 -*-

"""Console script for qiime_2_ll_quick_viewer."""

import click
from qiime_2_ll_quick_viewer import qiime_2_ll_quick_viewer


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-f', '--filename', required=True,
              help="Full path to a Qiime2 visualization file (*.qzv).")
@click.option('-p', '--port', required=True, default=8080,
              help="Port to launch the web server.")
def main(filename, port):
    """Quick viewer for Qiime 2 artifacts.

    It launches a simple web server to visualize the contents of the data
    folder in a browser.
    You can access to the server using a SSH tunnel session.
    """
    qiime_2_ll_quick_viewer.launch_server(filename, port)


if __name__ == "__main__":
    main()
