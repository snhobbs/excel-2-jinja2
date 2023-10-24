# render-df

I've been searching for the shortest repo I can put up that does a genuinely useful task.
This one, like all the others, is cheating.

My obsession with the worlds most popular interpreter (excel if this isn't clear) continues. This takes a spreadsheet and a jinja2 template and pumps each page into the template. The template just refers to each of the data frames.

As the python isn't actually doing anything in most circumstances why not just get rid of it and use a command line tool? This opens up the ability to compile these tools into a makefile.

I'm cheating here because the entire code base is just stitched together with 4 other libraries.



In general I like to use pandas DataFrames to render Jinja2 templatess.
All info is typically held in the template.
This tool takes a multipage spreadsheet and shoves it into a template.

Inputs:
    + Spreadsheet. Each page is a named variable. This is pumped into the template as a variable using kwargs. It is used by name by the template.
    + Template: Template worries about how to turn the data into something
    + Output name


Process:
    + openpyexcel loads all pages
    + Pandas dataframe from page
    + make dictionary of pages
    + render template


Uses:
    Primarily make files. Use as a stand alone command line tool.
    The raison d'être is to script the generation of kicad schematics in a way I can think about.

