from parglare import Grammar, Parser
from BS4GenGrammar import GRAMMAR
from BS4HTMLTemplate import HTML_TEMPLATE_PRELUDE, HTML_TEMPLATE_END
from BS4GenUtils import generate_html
import click


@click.command(name="generate")
@click.option('-t', '--template', required=True, help='Template to generate the HTML.')
@click.option('-o', '--output', help='Path to the output file.')
@click.option('-l', '--lang', help='Language code for the generated HTML (i.e. "en")')
@click.option('-i', '--title', help='Title of the generated HTML (inside <title> tag)')
def generate_html_from_template(template, output=None, lang=None, title=None):
    g = Grammar.from_string(GRAMMAR)
    p = Parser(g, build_tree=True)
    if lang is None:
        lang = 'en'
    if title is None:
        title = 'Title'
    with open(template, "r") as f:
        content = "".join(f.readlines())
        ast = p.parse(content)
        if output is not None:
            with open(output, "w") as fout:
                fout.write(HTML_TEMPLATE_PRELUDE
                           .replace('%%LANG%%', lang)
                           .replace('%%TITLE%%', title))
                generate_html(ast, fout=fout)
                fout.write(HTML_TEMPLATE_END)
        else:
            print(HTML_TEMPLATE_PRELUDE
                  .replace('%%LANG%%', lang)
                  .replace('%%TITLE%%', title))
            generate_html(ast)
            print(HTML_TEMPLATE_END)


if __name__ == '__main__':
    generate_html_from_template()
