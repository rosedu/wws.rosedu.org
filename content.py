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
}
