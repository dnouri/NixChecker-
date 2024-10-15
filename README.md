# 💻👾 [python/emacs/llm] NixChecker an online twitter fact checker bot

## Abstract

We'll create a fact checking bot.  It will be able to respond
automatically on Twitter to requests for fact checking a newspaper
article that you send it.

The fact check will include a brief text of a summary and the facts
presented in the article.  It will then continue to assess the main
points in the article to the best of its ability, using a score.

## Installation

Download the [source of this project NixChecker
here](https://github.com/dnouri/NixChecker-/archive/refs/heads/main.zip).

Unzip it and use a Terminal to navigate to the folder that you just
unzipped.

Create a virtual environment to get started.  This may work
differently on Windows!

```bash
python3 -m venv venv
source venv/bin/activate
```

Remember to activate the environment whenever you start a new
terminal, or you get back to the project.

You can also install project dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python extract-article.py \
    "https://www.france24.com/en/americas/20240918-federal-reserve-lowers-us-interest-rates-weeks-before-us-election"
```

You can use the llm CLI tool to summarise the article offline like so:

```bash
pip install llm llm-gpt4all click
python extract-article.py https://magit.vc/ | \
    llm -m mistral-7b-instruct-v0 -s "Summarise this article and include why it's a great tool"
```

Or you can use the same tool to use an [llm
template](https://llm.datasette.io/en/stable/templates.html) to
perhaps extract structured information from the news article instead.
The template file containing the prompt may then be located at
`~/.config/io.datasette.llm/templates/extract-structured.yaml`:

```bash
python extract-article.py https://www.middleeasteye.net/news/mass-burial-unidentifiable-bodies-accounts-israeli-attacks-lebanon --n-words=1000 | \
    llm -m mistral-7b-openorca -t extract-structured
```

## References and starting points

- [Drawing board](https://excalidraw.com/#room=82b362639e1ad71b39d4,I9XVsgPU74nyorqfhR9cCA)
- [goose3](https://github.com/goose3/goose3)
- [Twitter Discover](https://danielnouri.org/notes/2020/06/14/search-your-favorited-tweets-and-articles-with-twitter-discover/)
- [Messages API](https://huggingface.co/docs/text-generation-inference/en/messages_api)

### Goose3

```pycon
Python 3.11.2 (main, Aug 26 2024, 07:20:54) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from goose3 import Goose
>>> g = Goose()
>>> article = g.extract(url=url)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'url' is not defined
>>> url = 'https://www.france24.com/en/middle-east/20240918-what-we-know-about-lebanon-s-exploding-pagers'
>>> article = g.extract(url=url)
>>> article
<goose3.article.Article object at 0x7fd0bc7d84d0>
>>> article.title
'What we know about Lebanon’s exploding devices'
```

### Developer stuff

- [Magit](https://magit.vc/)

## Pomodoros

We are streaming the creation of this tool on Twitch.  And here's a
TODO list for that:

Times are in CEST

- [x] 2024-09-19 10:45 Project outline
  - [x] Github repo
- [x] 2024-09-19 11:30 Command line Goose 3
- [x] 2024-09-19 11:55 Pipe newspaper article into `llm` tool
