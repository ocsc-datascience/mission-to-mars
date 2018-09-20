# Mission to Mars

A web-scraping project, part of the USC Data Analytics Certificate Program.

The premis of this project is to exercise web scraping techniques
studied in class. We employ Beautiful Soup 4, the Splinter packages,
and Chrome Driver to process and scrape various web pages with
information related to planet Mars.

We first put together a Jupyter Notebook with all the scraping
code. Then we turn the scraping code into a regular Python
script. This script is then triggered by a HTTP GET on a Python/Flask
endpoint. The results are stored in MongoDB. Finally, for the root
("/") endpoint, we generate a HTML/Jinja2 template and let Flask
retrieve the data from MongoDB and render it using the template.
