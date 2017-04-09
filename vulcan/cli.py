import logging

import vulcan
import vulcan.config

import click


log = logging.getLogger(__name__)


class Context(object):
    '''Dummy Context class for Click group context.
    '''
    pass


@click.group()
@click.option('--debug', is_flag=True, help='Enables debug mode.')
@click.option('--config', type=click.Path(exists=True), default='./vulcan.yaml', help='Configuration file path. Defaults to ./vulcan.yaml.') # pylint: disable=line-too-long
@click.version_option(vulcan.__version__)
@click.pass_context
def cli(ctx, debug, config):
    '''Formula build tool for SaltStack.

    See https://github.com/iamseth/saltstack-vulcan for documentation.
    '''
    lvl = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=lvl, format='%(asctime)s %(levelname)s %(message)s')
    ctx.obj = Context()
    ctx.obj.cfg_file = config
    ctx.obj.cfg = vulcan.config.Config(config)
    ctx.obj.debug = debug


@cli.command()
@click.pass_context
def install(ctx):
    '''Install all non-installed formulas.
    '''
    formulas = ctx.obj.cfg.formulas
    for formula in formulas:
        formula.install()

@cli.command()
@click.pass_context
def update(ctx):
    '''Update or install formulas.
    '''
    formulas = ctx.obj.cfg.formulas
    for formula in formulas:
        formula.update()


if __name__ == '__main__':
    cli() #pylint: disable=no-value-for-parameter
