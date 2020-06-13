GRAMMAR = r"""
E:          EXPR_LIST
            | EMPTY;

TAG_CONTF:  tag_open tag_contf_name tag_close;
TAG_CONT:   tag_open tag_cont_name tag_close; 
TAG_ROW:    tag_open tag_row_name tag_close;
TAG_COL:    tag_open tag_col_name tag_close;

CONT_TAGS:  TAG_CONTF
            | TAG_CONT;

COL_ROW:    TAG_COL expr_open ROW_EXPR expr_close;

COL_OR_ROW: TAG_COL
            | COL_ROW;

COL_LIST:   COL_OR_ROW+;

COL_EXPR:   expr_open COL_LIST expr_close;

ROW_EXPR:   TAG_ROW COL_EXPR;

ROW_LIST:   expr_open ROW_EXPR+ expr_close;

CONT_EXPR:  expr_open CONT_TAGS ROW_LIST expr_close;

EXPR_LIST:  CONT_EXPR+;             

terminals
tag_open:           "[";
tag_close:          "]";
expr_open:          "(";
expr_close:         ")";
tag_contf_name:     "contf";
tag_cont_name:      "cont";
tag_row_name:       "row";
tag_col_name:       "col";
"""