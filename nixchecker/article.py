from dataclasses import dataclass
from datetime import datetime
import sys

import click
import goose3


@dataclass
class Extract:
    publish_date: datetime
    text: str
    article: goose3.Article


def extract(url, n_words) -> Extract:
    article = goose3.Goose().extract(url=url)

    paragraphs = [
        para.strip()
        for para in article.cleaned_text.split("\n")
        if para.strip()
    ]
    text = ""
    for para in paragraphs:
        new_text = "\n".join([text, "    " + para])
        if n_words != -1 and len(new_text.split()) > n_words:
            text += "\n    [...]"
            break
        text = new_text

    publish_date = (
            article.publish_datetime_utc.replace(tzinfo=None)
            if article.publish_datetime_utc is not None
            else None
        )

    return Extract(
        publish_date=publish_date,
        text=text.strip(),
        article=article,
    )
