import sys

import click
from goose3 import Goose


@click.command()
@click.argument("url")
@click.option("--n-words", default=-1)
def main(url, n_words):
    article = Goose().extract(url=url)

    paragraphs = [
        para.strip()
        for para in article.cleaned_text.split("\n")
        if para.strip()
    ]
    text_to_output = ""
    for para in paragraphs:
        new_text_to_output = "\n".join([text_to_output, "    " + para])
        if n_words != -1 and len(new_text_to_output.split()) > n_words:
            text_to_output += "\n    [...]"
            break
        text_to_output = new_text_to_output

    publish_date = (
            article.publish_datetime_utc.replace(tzinfo=None)
            if article.publish_datetime_utc is not None
            else None
        )
    click.echo(f"Article datetime in UTC and ISO format:\n    {publish_date}")
    click.echo()
    click.echo("Article contents:")
    click.echo("    {}".format(text_to_output.strip()))


if __name__ == '__main__':
    main()
