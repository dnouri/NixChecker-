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
    

    click.echo(f"Title: {extract.title}")
    click.echo(f"Date: {extract.publish_date}")
    click.echo(f"URL: {extract.url}")
    click.echo("Text:")
    click.echo(f"    {extract.text}")


if __name__ == '__main__':
    cli()
