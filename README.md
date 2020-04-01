# wikidiff2-git-viewer

🗿 A static git web browser using the [Wikidiff2](https://www.mediawiki.org/wiki/Wikidiff2) diff engine

Example of output: https://dam.io/wikidiff2-git-viewer/lois-en-construction/systeme_universel_de_retraite/8aee8f4856d8493ef43ae52d38633582be697f6d.html

## Usage

```terminal
> python build_pages.py <git_repository> <output_directory>
```

## Why ?

There's a two main problems I have with the GitHub diffs:

- If there's a small change on a long line, it doesn't highlight the small change, making the diff useless
- The font being monospace, it's not well-made for diffing prose
