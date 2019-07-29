# package-tracking
[![Build Status](https://travis-ci.org/botisko/package-tracking.svg?branch=master)](https://travis-ci.org/botisko/package-tracking)

An utility for finding delivery status for Ceska posta

## Prerequisites
```
Python >= 3.7
```

## Before the first run
```
pip install -r requirements.txt
```

## Running
The Python cpost_tracking.py script syntax is following:
```
package_tracking.py [-h] -p PACKAGE
```

*Note: following examples are given for Fedora 30 with Python 3.7 installed*

Lets say you want to find out where is your package with tracking number ABCDE12345678:
```
python package_tracking.py -p ABCDE12345678
```

Example output:
```
===================ABCDE12345678====================
====================================================
= 13.7.2019 | Odeslání zásilky do České republiky. =
====================================================
```

## Written In
* [Python 3.7.0](https://docs.python.org/3/)

## Authors
* **botisko** - *Initial work* - [package-tracking](https://github.com/botisko/package-tracking/)
