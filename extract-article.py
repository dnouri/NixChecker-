import sys

from goose3 import Goose


g = Goose()
article = g.extract(url=sys.argv[1])
article

print()
print("# NixChecker checking in")
print()
print("Hey there you asked me to grab the article with the title:")
print(article.title)
print()
print("meta_description:")
print()
print(article.meta_description)
print()
print("cleaned_text:")
print()
print(article.cleaned_text)
print()
print()
