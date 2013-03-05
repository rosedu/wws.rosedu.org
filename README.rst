ROSEdu Web Workshops
====================

Repository cu sursa site-ului ``wws.rosedu.org`` (care încă nu există).
Site-ul este generat cu Frozen-Flask_ plecând de la o aplicație Flask.
Rezultă niște fișiere statice care se uploadează pe server. Seamănă cu
Jekyll doar că e mai flexibil.

.. _Frozen-Flask: http://pythonhosted.org/Frozen-Flask/


Development
-----------

1. Clonă locală::

    $ git clone https://github.com/rosedu/wws.rosedu.org.git
    $ cd wws.rosedu.org

2. Virtualenv, dependențe::

    $ virtualenv sandbox
    $ echo '*' > sandbox/.gitignore
    $ source sandbox/bin/activate
    $ pip install -r requirements-dev.txt

3. Rulat server local::

    $ echo 'DEBUG=on' > .env
    $ honcho start

4. Upload pe server::

    $ ./manage.py freeze
    $ rsync -rtv --del build/ user@remote.server:/var/www
