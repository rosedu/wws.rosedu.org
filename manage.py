#!/usr/bin/env python

import os
import flask
from flask.ext.script import Manager
import pages


def create_app():
    app = flask.Flask(__name__)
    app.debug = (os.environ.get('DEBUG') == 'on')
    app.config['FREEZER_RELATIVE_URLS'] = True
    app.config['GOOGLE_ANALYTICS_CODE'] = 'UA-7579199-19'  # events.rosedu.org
    app.register_blueprint(pages.pages)
    return app


manager = Manager(create_app)


@manager.command
def freeze():
    from flask.ext.frozen import Freezer
    freezer = Freezer(flask.current_app)
    freezer.freeze()


if __name__ == '__main__':
    manager.run()
