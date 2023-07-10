import enum
import os
import sys
import json
import util
import shutil
from jinja2 import Environment, FileSystemLoader

vol_count = 36
environment = Environment(loader=FileSystemLoader("Support"))
template = environment.get_template("resource_template.html")

if not os.path.exists("Resources"):
    os.makedirs("Resources")
shutil.copyfile("Support/kontinua.css", "Resources/kontinua.css")

if not os.path.exists("user.cfg"):
    shutil.copyfile("Support/default.cfg", "user.cfg")

with open("user.cfg", "r") as config_fd:
    config = json.load(config_fd)

# Gather all metadatas    
book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]
books_metadata = []
all_topics = {}
for book in book_nums:
    print(f"Indexing book {book}...")
    (book_metadatas, topics) = util.gather_data("../Chapters", book, config)
    books_metadata.append(book_metadatas)
    all_topics.update(topics)

# Actually generate the HTML pages
book_indices = list(range(vol_count))
for i in book_indices:
    book_str = str(i + 1).zfill(2)
    metadatas = books_metadata[i]
    context = {"topics": all_topics, "chapters":metadatas}
    content = template.render( topics=all_topics, chapters=metadatas, book_str=book_str)
    filename = f"Resources/Workbook-{book_str}.html"
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"Wrote {filename}")