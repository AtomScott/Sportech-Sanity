rm -r docs
jupyter nbconvert --to notebook --execute make.ipynb
hugo
