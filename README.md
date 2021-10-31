# title2doi
A client access Crossref Metadata Search to translate article title/auth to doi.

# Requirement
python module: bs4, termcolor(optional)

# Usage
```
python title2doi.py tropical cyclone in warming climate
```
Then the title, authors, publish info and doi will print out.
There will be several papers match the keywords, best match will be below.

```
sh doi2bib 10.1175/jas-d-13-0155.1
```
Will translate doi into bibtex format, or other formats.
# Setting (title2doi.py)
In title2doi.py
```
puredoi = True
```
Print doi only rather than "http://dx.doi.org/doi"

```
reverse_print_order = True
```
Print matched article from last to first, so that the best one would be bottom.

# Setting (doi2bib)
In doi2bib, modify the fmt to the format you want. Here are available options: bibtex apa harvard ris ieee mla vancouver chicago
bibtex is the default.

# Troubleshooting
If that does not work, you could give:
```
python retry.py
```
a shot. (The title is hardcoded in this file, so you can do a whole list at once).
