Flaskr
======

The basic blog app built in the Flask `tutorial`_, amended to use
flaskr-security-too instead of hand-coding an authentication system.

.. _tutorial: http://flask.pocoo.org/docs/tutorial/
.. _security: https://flask-security-too.readthedocs.io/en/stable/


Install
-------

**Be sure to use the same version of the code as the version of the docs
you're reading.** You probably want the latest tagged version, but the
default Git version is the master branch. ::

    # clone the repository
    $ git clone https://github.com/jnsnow/flaskr-security
    $ cd flaskr-security
    # checkout the correct version
    $ git tag  # shows the tagged versions
    $ git checkout latest-tag-found-above

Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ . venv/bin/activate

Or on Windows cmd::

    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat

Install Flaskr::

    $ pip install -e .


Run
---

::

    $ export FLASK_APP=flaskr
    $ export FLASK_ENV=development
    $ flask init-db
    $ flask run

Or on Windows cmd::

    > set FLASK_APP=flaskr
    > set FLASK_ENV=development
    > flask init-db
    > flask run

Open http://127.0.0.1:5000 in a browser.


Test
----

::

    $ pip install '.[test]'
    $ pytest

Run with coverage report::

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser
