# Text Classification Experiments

This repository contains experiments in Vietnamese text classification problems. It is a part of [underthesea](https://github.com/magizbox/underthesea) project.

# Reports

![](https://img.shields.io/badge/F1-86.7%25-red.svg)

# Usage

Setup Environment

```
# clone project
$ git clone git@github.com:magizbox/underthesea.ner.git

# create environment
$ cd underthesea.ner
$ conda create -n uts.classification python=3.4
$ pip install -r requirements.txt
$ pip install git+https://github.com/magizbox/underthesea.flow
```

# Related Works

* Vietnamese Text Classification publications, [link](https://github.com/magizbox/underthesea/wiki/Vietnamese-NLP-Publications#text-classification)

# Results

SVM (ngrams) : 0.55 (F1 Weighted)