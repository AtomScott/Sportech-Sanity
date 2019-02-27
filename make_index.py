import codecs
import os

path = "themes/berbera/layouts/"
file = "themes/berbera/layouts/index.html"
print('{{ define "main" }} \n <main>\n<div class="homepage">', file=codecs.open(file, 'w', 'utf-8'))
intro = open("{0}index_intro.html".format(path), 'r')
print(intro.read(), file=codecs.open(file, 'a', 'utf-8'))

dir1 = os.listdir("content/")
for dir2 in dir1:
    lg_title = '\
    <div class="row" id="'+dir2+'">\
    <div class="col-sm-12">\
    <h3 class="category_header">'+dir2+'</h3>\
    </div>\
    </div>\
    '

    for dir3 in os.listdir("content/{0}".format(dir2)):
        if dir3 == ".ipynb_checkpoints":
            continue

        block = '\
        <div class="row">\
        <div class="col-sm-12">\
        <div class="card">\
        <h4 class="card-header">'+dir3+'</h4>\
        <div class="card-body">\
        <ul>\
        {{ range (where .Pages "File.Dir" "in" "'+dir2+'/'+dir3+'").Reverse }}/\
        <li>\
        <a href="{{.Permalink}}">{{.Title}}</a>\
        </li>\
        {{ end }}\
        </ul> \
        </div>\
        </div>\
        </div>\
        </div>\
        '

    print(lg_title, file=codecs.open(file, 'a', 'utf-8'))
    print(block, file=codecs.open(file, 'a', 'utf-8'))

print('</div> \n</main> \n {{ end }}', file=codecs.open(file, 'a', 'utf-8'))
