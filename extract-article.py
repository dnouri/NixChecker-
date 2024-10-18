import sys

import click

from nixchecker import cli


@click.command()
@click.argument("url")
@click.option("--n-words", default=-1)
def extract_article(url, n_words):
    return cli.extract_article.callback(url, n_words)


extract_article()
