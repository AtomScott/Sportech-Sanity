import codecs
import os

def get_icon(md):
    return

path = "themes/berbera/layouts/"
file = "themes/berbera/layouts/index.html"
print('{{ define "main" }} \n <main>\n<div class="homepage">', file=codecs.open(file, 'w', 'utf-8'))
intro = open("{0}index_intro.html".format(path), 'r')
print(intro.read(), file=codecs.open(file, 'a', 'utf-8'))

# dir1はコンテンツフォルダ！
# dir2は学会名！
# dir3は年！
dir1 = os.listdir("content/")
dir1.remove("authors")
for dir2 in dir1:
    lg_title = '\
    <div class="row" id="'+dir2+'">\
    <div class="col-sm-12">\
    <h3 class="category_header">'+dir2+'</h3>\
    </div>\
    </div>\
    '
    print(lg_title, file=codecs.open(file, 'a', 'utf-8'))

    for dir3 in os.listdir("content/{0}".format(dir2)):
        if dir3 == ".ipynb_checkpoints":
            continue
        file_path = "/{0}/{1}/".format(dir2,dir3)
        block = '\
        <div class="row">\
        <div class="col-sm-12">\
        <div class="card">\
        <h4 class="card-header">'+dir3+'</h4>\
        <div class="card-body">\
        <ul>\
        {{ range (where .Pages "File.Dir" "in" "'+file_path+'").Reverse }}\
        <li>\
        <a href="{{.Permalink}}">{{.Title}} <i class="fas fa-{{.Params.info.sport_icon}}"></i> </a>\
        </li>\
        {{ end }}\
        </ul> \
        </div>\
        </div>\
        </div>\
        </div>\
        '

        print(block, file=codecs.open(file, 'a', 'utf-8'))

print('</div> \n</main> \n {{ end }}', file=codecs.open(file, 'a', 'utf-8'))
