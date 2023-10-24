#!/usr/bin/env python3

'''
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
'''

import jinja2
import click
import pandas
import openpyxl
import click


def main(source_f, template):
    sheet_names = pandas.ExcelFile(source_f).sheet_names
    dfs = dict([[sheet.replace(" ", "_"), pandas.read_excel(source_f, sheet_name=sheet)] for sheet in sheet_names])

    return template.render(**dfs)


@click.command()
@click.option("--source", required=True, help="Source spreadsheet")
@click.option("--template", required=True, help="Jinja2 template file")
@click.option("-o", required=True, help="Output file name")
def cli_main(source, template, o):
    template_f = template
    source_f = source
    output = o
    with open(template_f, 'r') as f:
        template = jinja2.Template(f.read())

    out = main(source_f=source_f, template=template)
    with open(output, 'w') as f:
        f.write(out)

if __name__ == "__main__":
    cli_main()
