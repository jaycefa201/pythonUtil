from difflib import context_diff
import sys
# sys.stdout = open('output_3.txt', 'w')
fw = open('output_3.txt', 'w')

with open('document_1.txt', 'r', encoding='UTF-8') as f1:
    with open('document_2.txt', 'r', encoding='UTF-8') as f2:
        diff = context_diff(f1.readlines(), f2.readlines(), fromfile='f1', tofile='f2')
        for line in diff:
            if line != "":
                if line.startswith("-") or line.startswith("!") or line.startswith("+") or line.startswith("=") or line.startswith("*"):
                    print(line)
                    fw.write(line)
fw.close()