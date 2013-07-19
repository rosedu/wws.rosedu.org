ROSEdu Web Workshops
====================

Repository for the ``wws.rosedu.org`` (not existing yet) source.
Site is made by Frozen-Flask_ starting with a Flask application.
As a result we get static files to upload on server. Like Jekyll
but more flexible.

.. _Frozen-Flask: http://pythonhosted.org/Frozen-Flask/


Development
-----------

1. Local clone::

    $ git clone https://github.com/rosedu/wws.rosedu.org.git
    $ cd wws.rosedu.org

2. Virtualenv, dependencies::

    $ virtualenv sandbox
    $ echo '*' > sandbox/.gitignore
    $ source sandbox/bin/activate
    $ pip install -r requirements-dev.txt

3. Run local server::

    $ echo 'DEBUG=on' > .env
    $ honcho start

4. Upload to server::

    $ ./manage.py freeze
    $ rsync -rtv --del build/ user@remote.server:/var/www
