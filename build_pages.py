""""
take a git repository and display:
    - branches list (<repo>/index.html)
    - commits list (<repo>/<branch>/index.html)
    - each commit (<repo>/<branch>/<commit>.html)
"""
import sys
import os
import pathlib

import git
from lys import L, raw


REPO_DIR = sys.argv[1]
OUTPUT_DIR = sys.argv[2]

template = open('template.html').read()

repo = git.Repo(REPO_DIR)

# <repo>/index.html listing branches
pathlib.Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
with open(f'{OUTPUT_DIR}/index.html', 'w') as f:
    html = L.ul / (
        (
            L.li / L.a(href=branch.name) / branch.name
        ) for branch in repo.branches
    )
    f.write(template.replace('{{CONTENT}}', str(html)).replace('template_files/', '../template_files/'))

for branch in repo.branches:

    # <repo>/<branch>/index.html
    pathlib.Path(f'{OUTPUT_DIR}/{branch.name}').mkdir(parents=True, exist_ok=True)
    with open(f'{OUTPUT_DIR}/{branch.name}/index.html', 'w') as f:
        html = L.ul / (
            (
                L.li / L.a(href=commit.hexsha + '.html') / commit.message.strip().split('\n')[0]
            ) for commit in repo.iter_commits(branch)
        )
        f.write(template.replace('{{CONTENT}}', str(html)).replace('template_files/', '../../template_files/'))

    for commit in repo.iter_commits(branch):

        # <repo>/<branch>/<commit>.html
        with open(f'{OUTPUT_DIR}/{branch.name}/{commit.hexsha}.html', 'w') as f:
            files_modified = []

            for file in commit.tree:
                content = (commit.tree / file.name).data_stream.read().decode('utf-8')
                if commit.parents:
                    if file.name in commit.parents[0].tree:
                        content_before = (commit.parents[0].tree / file.name).data_stream.read().decode('utf-8')

                        if content != content_before:
                            open('a.txt', 'w').write(content_before)
                            open('b.txt', 'w').write(content)
                            os.system('php -dextension=/home/damien/repos/mediawiki-php-wikidiff2/modules/wikidiff2.so dodiff.php a.txt b.txt > c.txt')
                            html_diff = open('c.txt').read()

                            files_modified.append(
                                (
                                    L.p / (
                                        L.h4 / file.name,
                                        raw(html_diff),
                                    )
                                )
                            )

            html = L.p / (
                L.h1 / commit.message,
                files_modified,
            )

            f.write(template.replace('{{CONTENT}}', str(html)).replace('template_files/', '../../template_files/'))
