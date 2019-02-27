import dominate
from dominate.tags import *
import codecs
import os

path = "themes/berbera/layouts/"
file = "themes/berbera/layouts/index.html"
print('{{ define "main" }} \n <main>\n<div class="homepage">', file=codecs.open(file, 'w', 'utf-8'))
intro = open("{0}index_intro.html".format(path), 'r')
print(intro.read(), file=codecs.open(file, 'a', 'utf-8'))

dir1 = os.listdir("content/")
for dir2 in dir1:
    lg_title = div(cls="row", id=dir2)
    lg_title.add(div(cls="col-sm-12").add(h3(dir2,cls="category_header")))

    sm_block = div(cls="row")
    for dir3 in os.listdir("content/{0}".format(dir2)):
        if dir3 == ".ipynb_checkpoints":
            continue
        sm_block.add(div())

    block = div()
    block.add(lg_title)
    block.add(sm_block)
    print(block, file=codecs.open(file, 'a', 'utf-8'))


print('</div> \n</main> \n {{ end }}', file=codecs.open(file, 'a', 'utf-8'))
