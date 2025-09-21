import re
from typing import Dict

def search_in_file(filename: str, query: str,
                   case_sensitive: bool = False,   # 👈 دلوقتي بيسيب البحث غير حساس لحالة الأحرف
                   whole_word: bool = False,
                   show_byte_index: bool = True) -> Dict:

    flags = 0 if case_sensitive else re.IGNORECASE
    if whole_word:
        pattern = re.compile(r'\b' + re.escape(query) + r'\b', flags)
    else:
        pattern = re.compile(re.escape(query), flags)

    matches = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except UnicodeDecodeError:
        with open(filename, 'r', encoding='latin-1') as f:
            text = f.read()

    for m in pattern.finditer(text):
        start = m.start()
        end = m.end()

        pre_text = text[:start]
        line_num = pre_text.count('\n') + 1
        last_newline = pre_text.rfind('\n')
        if last_newline == -1:
            col_num = start + 1
        else:
            col_num = start - last_newline

        start_byte_index = None
        if show_byte_index:
            start_byte_index = len(text[:start].encode('utf-8'))

        matches.append({
            'line': line_num,
            'col': col_num,
            'line_text': text.splitlines()[line_num-1] if line_num-1 < len(text.splitlines()) else '',
            'start_char_index': start,
            'end_char_index': end,
            'start_byte_index': start_byte_index
        })

    result = {
        'found': len(matches) > 0,
        'matches': matches
    }
    return result

# مثال استخدام
if __name__ == "__main__":
    fname = "travel-around-the-world.txt"     # غير لاسم ملفك
    q = "Thailand"               # الكلمة أو الرقم اللي عايز تدور عليه
    res = search_in_file(fname, q)

    if res['found']:
        print("True — The Text Was Found. Number Of Results: ", len(res['matches']))
        for i, m in enumerate(res['matches'], 1):
            print(f"#{i}: Line {m['line']}, Column {m['col']}, Literal Location (start) = {m['start_char_index']}, Byte = {m['start_byte_index']}")
            print(" The Text Is In The Line :", m['line_text'].strip())
    else:
        print("False — The Text Does't Exist.")