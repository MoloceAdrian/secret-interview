DevNest Interview.
==================

What does this project do?
==========================

    Given a file, creates a new file with the locations of the bytes in the previous file reversed.
    Arguably there's an even more efficient solution if the use case allowed for the input file to be overwritten,
    as we could of went with 2 indices from start and end until the middle of the file and interchange the bytes.


Requirements
============

* Python3.7 or higher
* pytest framework.


How to Install
==============

The recommandation is the use a virtual environment.

`pip install -r requirements` 

How to use
==========

`python binary_reverse.py file_name1 file_name2 ...`

Where file_name is the name of a file containing binary data.

How to test
===========

`python -m pytest tests/`
