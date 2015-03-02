import sys

import click

from .app import app


@click.group()
def cli():
    pass


@cli.command()
@click.option('--host', default='127.0.0.1')
@click.option('--port', default=5000, type=int)
@click.option('--debug/--no-debug', 'use_debugger', is_flag=True, default=True)
@click.option('--reload/--no-reload', 'use_reloader', is_flag=True,
              default=True)
@click.option('--threaded', is_flag=True)
@click.option('--processes', default=1, type=int)
@click.option('--passthrough-errors', is_flag=True)
def runserver(host, port, use_debugger, use_reloader, threaded, processes,
        passthrough_errors):
    app.run(host=host,
            port=port,
            debug=use_debugger,
            use_debugger=use_debugger,
            use_reloader=use_reloader,
            threaded=threaded,
            processes=processes,
            passthrough_errors=passthrough_errors)
