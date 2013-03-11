import flask
import content


pages = flask.Blueprint('pages', __name__)


@pages.route('/')
def home():
    return flask.render_template('home.html', talks=content.talks)


@pages.route('/<talk_id>.html')
def talk(talk_id):
    return flask.render_template('talk.html', talk=content.talks[talk_id])
