# title2doi
A client access Crossref Metadata Search to translate article title/auth to doi.

# Requirement
python module: bs4, termcolor(optional)

# Usage
```
python title2doi.py tropical cyclone in warming climate
```

# Setting
In title2doi.py
```
puredoi = True
```
Print doi only rather than "http://dx.doi.org/doi"

```
reverse_print_order = True
```
Print matched article from last to first, so that the best one would be bottom.
