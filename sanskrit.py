import sys
import importlib.abc
import importlib.util
from pathlib import Path

import ast
import tokenize
from tokenize import TokenInfo
import io


# sanskrit-to-Python mappings
sanskrit_keywords = {
    "सत्":"True",
    "असत्":"False",
    "नास्ति":"None",
#--------------------------
    "च":"and",
    "वा":"or",
    "न":"not",
#--------------------------
    "अथ": "else",
    "अथयदि": "elif",
    "यदि": "if",
#--------------------------
    "परिहरन": "for", #repeat - परिहरन
    "यावत्‌": "while", #until - यावत्‌
    "अग्रिम": "break",
    "विराम": "continue",
    "गच्छतु":"pass", #"let it go" / "move on" (lit. "let it go away")
#--------------------------
    "नियोग": "def", #function - नियोग
    "निर्वतनम्": "return",
    "अनाम": "lambda",#nameless
#--------------------------
    "प्रयततु": "try",
    "विहाय": "except",
    "अन्ततः":"finally",
    "विगर्हते":"raise", #"rebukes" / "points out a fault" (used for raising objections)
    "निश्चितयति":"assert",  #"to confirm" / "to verify"
#--------------------------
    "आयात": "import",#see this
    "यतः":"from",  #"from where" / "from" (origin)
    "नाम्ना":"as",  #"by name" / "as named"
#--------------------------
    "सर्वत्रगम्":"global",  #	"that which goes everywhere" / "global"
    "असामीपिक":"nonlocal",  #"not nearby" (literally "nonlocal")
    "अपनयति":"del",  #"removes" / "takes away"
#--------------------------
    "विधि": "class",
    "सह":"with",
    "यत्नतः":"async",  #	Means "with effort" or "non-blocking" (figurative match for asynchronous behavior)
    "प्रतीक्षेत्":"await",  #Means "let it wait" / "should wait" — imperative form, fits well
#--------------------------
    "इति": "in",
    "अस्ति":"is",
    "दत्ते":"yield",  #Means "gives" or "offers" — a very natural match for yield in generators
#--------------------------functions
    "पङ्क्तिः": "range",  #पङ्क्तिः
    "मुद्रण": "print",
    "प्रवेशयति":"input",
#---------------------------temporary_use
    "यूनिकोडअङ्क":"ord",
#---------------------------
    "sanskrit":"python"
}

def parse_syntax(translated_code):
    try:
        ast.parse(translated_code)
        return translated_code  # Valid Python code
    except SyntaxError as e:
        print(f"Syntax error in translated code: {e}")
        return None  # Return None to indicate invalid code

def translate_sanskrit(code: str) -> str:
    result = []
    # tokenize.tokenize() requires bytes input
    bytes_io = io.BytesIO(code.encode('utf-8'))
    tokens = tokenize.tokenize(bytes_io.readline)

    #making sure previous token should not be '.' so the it is not part of any class
    prev_tok_string = 0

    for tok in tokens:
        if tok.type == tokenize.NAME and tok.string in sanskrit_keywords and prev_tok_string != '.':
            tok = TokenInfo(tok.type, sanskrit_keywords[tok.string], tok.start, tok.end, tok.line)
        prev_tok_string = tok.string
        result.append(tok)

    translated_code = tokenize.untokenize(result).decode('utf-8')
    return parse_syntax(translated_code)


# Custom import loader and finder
class esspyLoader(importlib.abc.SourceLoader):
    def __init__(self, path):
        self.path = path

    def get_filename(self, fullname):
        return self.path

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            sanskrit_code = f.read()
        return translate_sanskrit(sanskrit_code).encode('utf-8')

class esspyFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        module_path = Path(fullname.replace(".", "/") + ".esspy")
        if module_path.exists():
            return importlib.util.spec_from_loader(fullname, esspyLoader(str(module_path)))
        return None

# Activate the import hook globally
sys.meta_path.insert(0, esspyFinder())

# Script runner
def run_sanskrit_file(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            sanskrit_code = f.read()
        translated_code = translate_sanskrit(sanskrit_code)
        exec(compile(translated_code, file_path, "exec"), {"__name__": "__main__"})
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error while running sanskrit code:\n{e}")

# CLI entrypoint
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sanskrit.py <file.esspy>")
    else:
        run_sanskrit_file(sys.argv[1])
