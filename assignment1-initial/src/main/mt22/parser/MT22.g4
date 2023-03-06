grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language = Python3;
}

/* Fragment */
fragment Unterminated: [\n] | EOF;
fragment DoubleQuote: '\\"';
fragment Character: ~[\b\n\f\r\t'"\\] | DoubleQuote | [\b\f\r\t'] | ('\\' [bnfrt'\\]);

/* Keyword */
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
VOID: 'void';
WHILE: 'while';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';

/* Operators */
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
AND: '&&';
OR: '||';
EQ: '==';
NOT_EQ: '!=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';
CONCAT: '::';
NEGATION: '!';

/* Seperators */
SQ_OPEN: '[';
SQ_CLOSE: ']';
CUR_OPEN: '{';
CUR_CLOSE: '}';
R_OPEN: '(';
R_CLOSE: ')';
COMMA: ',';
SEMI_COLON: ';';
COLON: ':';
ASSIGN: '=';

/* Identifier */
ID: [A-Za-z_][A-Za-z0-9_]*;

/* Literal */
INT_LIT: (DEC | '0') { self.text = self.text.replace('_', '') };
FLOAT_LIT: ((INT_LIT? F_Dec F_Exp) | (INT_LIT F_Dec) | (INT_LIT F_Exp)) { self.text = self.text.replace('_', '') };
STR_LIT: '"' Character* '"' {
    temp = self.text
    self.text = temp[1:-1]
};
fragment DEC: [1-9][0-9]*('_' [0-9]+)*;
fragment F_Dec: '.'[0-9]*;
fragment F_Exp: [eE][-+]?[0-9]+;
array_literal: (CUR_OPEN expression_list? CUR_CLOSE);
literal: INT_LIT | FLOAT_LIT | TRUE | FALSE | STR_LIT;

program: (declare)+ EOF;
declare: var_decl | func_decl;

/* Variable declaration */
var_decl returns[n] @init {$n = 0}: varlist COLON var_type (ASSIGN (expression ({ $varlist.text.count(',') > $n }? COMMA expression {$n += 1})*) { $varlist.text.count(',') == $n }?)? SEMI_COLON;
var_type: prim_type | AUTO | array_type;
prim_type: STRING| BOOLEAN | INTEGER | FLOAT;
varlist: ID COMMA varlist | ID;
intList: INT_LIT (COMMA INT_LIT)*;
array_type: ARRAY (SQ_OPEN intList SQ_CLOSE) OF prim_type;
array_Ele: ID(SQ_OPEN expression_list SQ_CLOSE);

/* Function declaration */
func_decl: (main_func | ID COLON FUNCTION func_type (R_OPEN para_list? R_CLOSE) (INHERIT ID)?) block_func;
func_type: var_type | VOID;
para_list: para_dec (COMMA para_dec)*;
para_dec: INHERIT? OUT? para_var COLON var_type;
para_var: ID (SQ_OPEN SQ_CLOSE)?;
main_func: 'main' COLON FUNCTION VOID R_OPEN R_CLOSE;

/* Block phase */
block_func: CUR_OPEN (statement | var_decl)* CUR_CLOSE;

/* Statement */
statement: for_stmt | if_stmt | while_stmt | do_while_stmt | break_stmt | cont_stmt | return_stmt | call_func | assign_stmt | block_func;
for_stmt: FOR R_OPEN ID ASSIGN expression COMMA expression COMMA expression R_CLOSE block_func;
if_stmt: IF R_OPEN expression R_CLOSE statement (ELSE statement)?;
while_stmt: WHILE R_OPEN expression R_CLOSE statement;
do_while_stmt: DO statement WHILE R_OPEN expression R_CLOSE SEMI_COLON;
break_stmt: BREAK SEMI_COLON;
cont_stmt: CONTINUE SEMI_COLON;
return_stmt: RETURN (expression)? SEMI_COLON;
call_func: (ID (R_OPEN expression_list? R_CLOSE) | non_returned_func) SEMI_COLON;
func_call: ID (R_OPEN expression_list? R_CLOSE) | returned_func;
non_returned_func: printInteger | printFloat | printBoolean | printString | superFunc | preventDefault;
returned_func: readInteger | readFloat | readString | readBoolean;
readInteger: 'readInteger' R_OPEN R_CLOSE;
printInteger: 'printInteger' R_OPEN expression R_CLOSE;
readFloat: 'readFloat' R_OPEN R_CLOSE;
printFloat: 'printFloat' R_OPEN expression R_CLOSE;
readBoolean: 'readBoolean' R_OPEN R_CLOSE;
printBoolean: 'printBoolean' R_OPEN expression R_CLOSE;
readString: 'readString' R_OPEN R_CLOSE;
printString: 'printString' R_OPEN expression R_CLOSE;
superFunc: 'super' R_OPEN expression_list R_CLOSE;
preventDefault: 'preventDefault' R_OPEN R_CLOSE;
assign_stmt: (ID | array_Ele) ASSIGN expression SEMI_COLON;

/* Expression */
expression_list: expression (COMMA expression)*;
expression: expression1 CONCAT expression1 | expression1;
expression1: expression1 (EQ | NOT_EQ | LT | LTE | GT | GTE) expression1 | expression2;
expression2: expression2 (AND | OR) expression3 | expression3;
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: NEGATION expression5 | expression6;
expression6: SUB expression6 | expression7;
expression7: array_Ele | operands;

/* Operands */
operands: literal | (R_OPEN expression R_CLOSE) | func_call | ID | array_literal;

/* Comment Line */
CMTLINE: '//' ~[\n\r\f]* -> skip;
CMTBLOCK: '/''*' .*? '*''/' -> skip;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

/* Error Token */
ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' Character* Unterminated {
    esc = ['\n']
    temp = str(self.text)
    if (temp[-1] in esc):
        raise UncloseString(temp[1:-1])
    else:
        raise UncloseString(temp[1:])
};
ILLEGAL_ESCAPE: '"' Character* ('\\' ~[bnfrt'\\] | ~'\\') {
    temp = self.text
    raise IllegalEscape(temp[1:])
};





