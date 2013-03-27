# encoding: utf-8
from jinja2 import Markup

talks = {
    'git': {
        'title': "Git Is the Answer. I Don't Remember the Question.",
        'speaker': Markup(
            u'<a href="http://pilgrimgray.wordpress.com/">'
            u'Mihai Maruseac</a>, '
            u'<a href="http://ro.linkedin.com/in/razvandeaconescu">'
            u'Răzvan Deaconescu</a>'),
        'speaker-images': [
            '9a378ed2410bdabed82883f2615f6b61',
            '76864a40274a1fd0e8c099f4c9a02c66',
        ],
        'date': "16 martie 10:00 - 13:00",
        'location': "EC-002",
        'abstract': Markup(u"""\
<p>Git este unul dintre cele mai folosite și flexibile soluții de gestiune
a codului (source code management). Poate fi folosit cu succes pentru
versionarea codului, fișierelor de configurare, fișierelor de
organizare, surse LaTeX. Este util, puternic și cool și face partea din
categoria noastră de "must have tools". În cadrul workshop-ului, vă
invităm să urmariți scenariile noastre de folosire a Git:</p>

<ul>
<li>user setup for Git</li>
<li>line endings</li>
<li>local repository creation and setup</li>
<li>commit update (ammed, git rebase -i)</li>
<li>latex beamer, multe actualizari, nevoie de git add -i sau git add -p</li>
<li>resetare de commit-uri (git checkout, git reset)</li>
<li>git update-index --assume-unchanged</li>
<li>conflict resolution</li>
<li>tagging și branching (repository CDL)</li>
<li>branches on virtual machine</li>
<li>branching + patching (nucleul Linux)</li>
<li>git cherry pick</li>
<li>lucrul cu 2 remote-uri: GitHub, fork, actualizare fork + pull request</li>
<li>git bisect</li>
<li>stash</li>
<li>reflog</li>
</ul>
"""),
        'registration-link': 'http://webworkshops.eventbrite.com?ref=elink',
        'registration-iframe': ('http://www.eventbrite.com/tickets-external'
                                '?eid=4442573858&ref=etckt&v=2'),
    },
    'flask-intro': {
        'title': "Flask intro",
        'speaker': Markup(
            u'<a href="http://alex.eftimie.ro/">Alex Eftimie</a>, '
            u'<a href="http://grep.ro/">Alex Morega</a>'),
        'speaker-images': [
            'd43fad239b039cebdb4206cdc692f314',
            '3cedacd1954b723b4f88ea7e3675bc40',
        ],
        'date': "27 martie 18:00 - 20:00",
        'location': "EG306, sala Intel",
        'abstract': Markup(u"""
<p><a href="http://flask.pocoo.org/">Flask</a> este un framework pentru
dezvoltarea de aplicații web. Este ușor de folosit, puternic, lasă multă
libertate în organizarea codului, și are un ecosistem mare de extensii
3rd party.</p>

<p>În acest workshop introductiv vei învăța cum să faci o aplicație de
la zero: instalarea framework-ului, scris view-uri, template-uri, acces
la parametrii de request, lucrul cu o bază de date, lucrul cu sesiune,
autentificare, configurație, deployment.</p>

<p>Workshop-ul va fi hands-on. Laptop-urile sunt opționale, vor fi
calculatoare în sală.</p>
"""),
        'registration-link': 'http://ww-flask.eventbrite.com/',
        'registration-iframe': (''),
    },
}
