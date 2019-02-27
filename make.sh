rm -r docs
python make_index.py
jupyter nbconvert --to notebook --execute make.ipynb
hugo
git add .
git commit -m "Updated with make.sh"
git push origin master
