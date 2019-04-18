rm -r docs
# jupyter nbconvert --to notebook --execute make.ipynb
python3 make_index.py
hugo
git add * 
git commit -m "Updated with make.sh"
git push origin master

