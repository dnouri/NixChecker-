import click

from nixchecker import article


@click.group()
def cli():
    pass


@cli.command()
@click.argument("url")
@click.option("--n-words", default=-1)
def extract_article(url, n_words):
    extract = article.extract(url, n_words)
    

    click.echo(f"Article datetime in UTC and ISO format:\n    {extract.publish_date}")
    click.echo()
    click.echo("Article contents:")
    click.echo(f"    {extract.text}")


if __name__ == '__main__':
    cli()
