from parglare import NodeNonTerm, NodeTerm
import sys

TAG_CLASSES = {
    'TAG_CONTF': "container-fluid",
    'TAG_CONT': "container",
    'TAG_ROW': "row",
    'TAG_COL': "col",
}

INDENT_NAMES = [
    "ROW_LIST",
    "COL_LIST",
    "ROW_EXPR"
]


def pretty_print(ast, indentation=-1):
    for node in ast:
        if type(node) is NodeNonTerm:
            if node.symbol.name in TAG_CLASSES.keys():
                tag_content = "".join([x.value for x in node.children])
                indentation_str = "\t" * indentation
                print(f"{indentation_str}{tag_content}")
            else:
                if node.symbol.name in INDENT_NAMES:
                    pretty_print(node.children, indentation + 1)
                else:
                    pretty_print(node.children, indentation)


def generate_html(ast, fout=sys.stdout, context_stack=[]):
    for node in ast:
        if type(node) is NodeNonTerm:
            context_name = node.symbol.name
            if context_name in TAG_CLASSES.keys():
                indentation_str = '\t' * (len(context_stack) + 2)
                if context_name != "TAG_COL":
                    context_stack.append(context_name)
                    fout.write(f"{indentation_str}<div class='{TAG_CLASSES[context_name]}'>\n")
                else:
                    if context_stack[-1] != 'COL_ROW':
                        fout.write(f"{indentation_str}<div class='{TAG_CLASSES[context_name]}'></div>\n")
                    else:
                        indentation_str = '\t' * (len(context_stack) + 1)
                        fout.write(f"{indentation_str}<div class='{TAG_CLASSES[context_name]}'>\n")
            else:
                if context_name == 'COL_ROW':
                    context_stack.append(context_name)
            generate_html(node.children, fout, context_stack)
        elif type(node) is NodeTerm:
            if node.symbol.name == "expr_close":
                if len(context_stack) > 0:
                    context_stack.pop()
                    indentation_str = "\t" * (len(context_stack) + 2)
                    fout.write(f"{indentation_str}</div>\n")
