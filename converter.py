import re

translations = {
    "=": "==",
    "←": "=",
    "≠": "!=",
    "≤": "<=",
    "≥": ">=",
    "–": "-",
    "AND": "and",
    "OR": "or",
    "NOT": "not",
    "constant ": "",
    "DIV": "//",
    "MOD": "%",
    "USERINPUT": "input()",
    "THEN": "",
    "ELSE IF": "elif",
}

def fix_output(x):
    return f"{x.group(1).replace('OUTPUT', '')}print({x.group(2)})"

def fix_repeat_until(x):
    result = f"{x.group(1).replace('REPEAT', 'while True:')}{x.group(2)}{x.group(3)}{x.group(4)}{x.group(3)}if ({x.group(7)}): break"
    #print(result)
    return result

def fix_for_loop(x):
    result = f"for {x.group(1)} in range({x.group(2)},{x.group(3)}+1):"
    #print(result)
    return result

regex_translations = {
    r"(OUTPUT)(.+)": fix_output,
    r"END(SUBROUTINE|WHILE|IF|FOR)": "",
    r"(.*(?:SUBROUTINE|WHILE|ELSE IF|IF|ELSE).*)": lambda x: x.group(1) + ":",
    r"\b(SUBROUTINE)": "def",
    r"(REPEAT)([\s\S]+?)(\s*)(.*)\n(.*)(UNTIL)(.*)": fix_repeat_until,
    r"(RETURN|WHILE|IF|ELSE)": lambda x: x.group().lower(),
    r"FOR\s*(\w)\s*=\s*(\d*)\s*TO\s*(\d)": fix_for_loop
}


def convert(string: str):
    result = string
    for k, v in translations.items():
        result = result.replace(k, v)

    for regex_expression, process_function in regex_translations.items():
        if isinstance(process_function, str):
            result = re.sub(regex_expression, lambda x: process_function, result, flags=re.IGNORECASE)
        else:
            result = re.sub(regex_expression, process_function, result, flags=re.IGNORECASE)

    return result