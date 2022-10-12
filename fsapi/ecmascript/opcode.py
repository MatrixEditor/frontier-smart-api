# MIT License

# Copyright (c) 2022 MatrixEditor

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
__doc__ = '''
'''

__all__ = [
  'ECMASCRIPT_MAGIC_BYTES', 'ECMASCRIPT_HDR_LEN', 'ESOP'
]

# ECMAScripts' magic bytes defined in little-endian encoding.
# 
# When looking at the bytes in source files these bytes might be in the 
# following format: 07 00 AD DE.
ECMASCRIPT_MAGIC_BYTES = 0xDEAD0007

# Defines the actual header length for compiled ECMAScripts.
# 
# Note that this number represents the full header including the four magic
# bytes defined in ECMASCRIPT_MAGIC_BYTES.
# 
# @see ECMASCRIPT_MAGIC_BYTES
ECMASCRIPT_HDR_LEN = 0x24

# Defines all bytecodes that can be translated into expressions.
ESOP = {
  # Longstanding JavaScript/ECMAScript bytecodes.
  0:   "nop",
  1:   "push",
  2:   "popv",
  3:   "enterwith",
  4:   "leavewith",
  5:   "return",
  6:   "goto",
  7:   "ifeq",
  8:   "ifne",

  # Get the arguments object for the current, lightweight function activation
  9:   "args", 

  # ECMA-compliant for-in loop with argument or local variable loop control.
  10:  "forarg",
  11:  "forvar",

  12:  "dup",
  13:  "dup2",
  14:  "setconst",
  15:  "bitor",
  16:  "bitxor",
  17:  "bitand",
  18:  "eq",
  19:  "ne",
  20:  "lt",
  21:  "le",
  22:  "gt",
  23:  "ge",
  24:  "lsh",
  25:  "rsh",
  26:  "ursh",
  27:  "add",
  28:  "sub",
  29:  "mul",
  30:  "div",
  31:  "mod",
  32:  "not",
  33:  "bitnot",
  34:  "neg",
  35:  "new", 
  36:  "delname",
  37:  "delprop",
  38:  "delelem",
  39:  "typeof",
  40:  "void", 
  41:  "incname",
  42:  "incprop",
  43:  "incelem",
  44:  "decname",
  45:  "decprop",
  46:  "decelem",
  47:  "nameinc",
  48:  "propinc",
  49:  "eleminc",
  50:  "namedec",
  51:  "propdec",
  52:  "elemdec",
  53:  "getprop",
  54:  "setprop",
  55:  "getelem",
  56:  "setelem",
  57:  "pushobj",
  58:  "call",
  59:  "name",
  60:  "number",
  61:  "string",
  62:  "zero",
  63:  "one",
  64:  "null", 
  65:  "this", 
  66:  "false", 
  67:  "true", 
  68:  "or",
  69:  "and",

  # The switch bytecodes have variable length
  70:  "tableswitch",
  71:  "lookupswitch",

  # New, infallible/transitive identity ops.
  72:  "eq",
  73:  "ne",

  # Lexical closure constructor.
  74:  "closure",

  # Export and import ops.
  75:  "exportall",
  76:  "exportname",
  77:  "importall",
  78:  "importprop",
  79:  "importelem",

  # Push object literal
  80:  "object",

  # Pop value and discard it.
  81:  "pop",

  # Convert value to number, for unary +
  82:  "pos",

  # Trap into debugger for breakpoint, etc.
  83:  "trap",

  # Fast get/set ops for function arguments and local variables.
  84:  "getarg",
  85:  "setarg",
  86:  "getvar",
  87:  "setvar",

  # Push unsigned 16-bit int constant.
  88:  "uint16",

  # Object and array literal support.
  89:  "newinit",
  90:  "endinit",
  91:  "initprop",
  92:  "initelem",
  93:  "defsharp",
  94:  "usesharp",

  # Fast inc/dec ops for args and local vars.
  95:  "incarg",
  96:  "incvar",
  97:  "decarg",
  98:  "decvar",
  99:  "arginc",
  100: "varinc",
  101: "argdec",
  102: "vardec",

  # Initialize for-in iterator.
  103: "forin",

  # ECMA-compliant for/in ops.
  104: "forname",
  105: "forprop",
  106: "forelem",
  107: "pop2",

  # ECMA-compliant assignment ops.
  108: "bindname",
  109: "setname",

  # Exception handling ops.
  110: "throw",

  # 'in' and 'instanceof' ops.
  111: "in", 
  712: "instanceof",

  # debugger op
  113: "debugger",

  # gosub/retsub for finally handling
  114: "gosub",
  115: "retsub",

  # More exception handling ops.
  116: "exception",
  117: "setsp",

  # ECMA-compliant switch statement ops.
  118: "condswitch",
  119: "case",
  120: "default",

  # ECMA-compliant call to eval op
  121: "eval",

  # ECMA-compliant helper for 'for (x[i] in o)' loops.
  122: "enumelem",

  # Getter and setter prefix bytecodes.  These modify the next bytecode, either
  # an assignment or a property initializer code, which then defines a property
  # getter or setter.
  123: "get",
  124: "set",

  # Prolog bytecodes for defining function, var, and const names.
  125: "deffun",
  126: "defconst",
  127: "defvar",

  # Auto-clone (if needed due to re-parenting) and push an anonymous function.
  128: "anonfunobj",

  # ECMA ed. 3 named function expression.
  129: "namedfunobj",
  130: "setlocalpop",

  # ECMA-mandated parenthesization opcode, which nulls the reference base register
  131: "group",

  # Host object extension: given 'o.item(i) = j'
  132: "setcall",

  # Exception handling no-ops
  133: "try",
  134: "finally",

  # Swap the top two stack elements.
  135: "swap",

  # Bytecodes that avoid making an arguments object in most cases:
  # 'argsub gets arguments[i] from fp->argv, if i is in [0, fp->argc-1].
  # 'argcnt' returns fp->argc.
  136: "argsub",
  137: "argcnt",

  # Define a local function object as a local variable.
  # The local variable's slot number is the first immediate two-byte operand
  # The function object's atom index is the second immediate operand.
  138: "deflocalfun",

  # Extended jumps.
  139: "gotox",
  140: "ifeqx",
  141: "ifnex",
  142: "orx",
  143: "andx",
  144: "gosubx",
  145: "casex",
  146: "defaultx",
  147: "tableswitchx",
  148: "lookupswitchx",

  # Placeholders for a real jump opcode set during backpatch chain fixup.
  149: "backpatch",
  150: "backpatch_pop",

  # Set pending exception from the stack, to trigger rethrow.
  151: "throwing",

  # Set and get return value pseudo-register in stack frame.
  152: "setrval",
  153: "retrval",

  # Optimized global variable ops
  154: "getgvar",
  155: "setgvar",
  156: "incgvar",
  157: "decgvar",
  158: "gvarinc",
  159: "gvardec",

  # Regular expression literal
  160: "regexp",

  # XML (ECMA-357, a.k.a. "E4X") support.
  161: "defxmlns",
  162: "anyname",
  163: "qnamepart",
  164: "qnameconst",
  165: "qname",
  166: "toattrname",
  167: "toattrval",
  168: "addattrname",
  169: "addattrval",
  170: "bindxmlname",
  171: "setxmlname",
  172: "xmlname",
  173: "descendants",
  174: "filter",
  175: "endfilter",
  176: "toxml",
  177: "toxmllist",
  178: "xmltagexpr",
  179: "xmleltexpr",
  180: "xmlobject",
  181: "xmlcdata",
  182: "xmlcomment",
  183: "xmlpi",
  184: "getmethod",
  185: "getfunns",
  186: "foreach",
  187: "deldesc",

  # Opcodes for extended literal addressing
  188: "uint24",
  189: "literal",
  190: "findname",
  191: "litopx",

  # Opcodes to help the decompiler deal with XML.
  192: "startxml",
  193: "startxmlexpr",
  194: "setmethod",

  #  Stop interpretation, emitted at end of script to save the threaded bytecode
  195: "stop",

  # Get an extant property or element value, throwing ReferenceError if the
  # identified property does not exist.
  196: "getxprop",
  197: "getxelem",
  198: "typeof", 

  # Block-local scope support.
  199: "enterblock",
  200: "leaveblock",
  201: "getlocal",
  202: "setlocal",
  203: "inclocal",
  204: "declocal",
  205: "localinc",
  206: "localdec",
  207: "forlocal",

  # Iterator, generator, and array comprehension support.
  208: "startiter",
  209: "enditer",
  210: "generator",
  211: "yield",
  212: "arraypush",
  213: "foreachkeyval",

  # Variant of 'enumelem' (122) for destructuring const (const [a, b] = ...).
  214: "enumconstelem",
  215: "leaveblockexpr"
}