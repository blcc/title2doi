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

# Setting (doi2bib) (obsoleted)
In doi2bib, modify the fmt to the format you want. Here are available options: bibtex apa harvard ris ieee mla vancouver chicago
bibtex is the default.

This script is no longer work now. Crossref has API for DOI. Please check the API url:

https://www.crossref.org/documentation/retrieve-metadata/rest-api/

Or try dx.doi.org:
```
curl -LH "Accept: text/bibliography; style=bibtex" http://dx.doi.org/10.5194/gmd-14-7073-2021
```
