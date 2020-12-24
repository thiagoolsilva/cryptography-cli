import click


@click.command()
@click.option('--name',  help='number of greetings')
def hello(name):
    click.echo('Hello World!')
    click.echo(name)


if __name__ == '__main__':
    hello()
