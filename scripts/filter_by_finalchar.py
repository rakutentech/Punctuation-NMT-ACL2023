import sys
import re

src = open(sys.argv[1], 'r')
ref = open(sys.argv[2], 'r')

source_text = [x.rstrip() for x in src.readlines()]
reference_text = [x.rstrip() for x in ref.readlines()]

punct_dict = {}
char_count = 0

src_lang = sys.argv[1][-2:]
tgt_lang = sys.argv[2][-2:]

prefix = sys.argv[3]

src_w = open("{}.{}-{}.{}".format(prefix, src_lang, tgt_lang, src_lang), 'w')
ref_w = open("{}.{}-{}.{}".format(prefix, src_lang, tgt_lang, tgt_lang), 'w')

print(
    "Which do you want to filter out? 1. Fullstop 2. Exclamation 3. Question 4. Random Character"
)
x = input()

src_uniq = []
ref_uniq = []

for s, r in zip(source_text, reference_text):
    if s in src_uniq or r in ref_uniq:
        pass
    else:
        src_uniq.append(s)
        ref_uniq.append(r)

        if x == '4' and re.search('\w', s[-1]):
            src_w.write(s + '\n')
            ref_w.write(r + '\n')
        elif x == '1' and s[-1] in ['。', '.']:
            src_w.write(s + '\n')
            ref_w.write(r + '\n')
        elif x == '2' and s[-1] in ['！', '!']:
            src_w.write(s + '\n')
            ref_w.write(r + '\n')
        elif x == '3' and s[-1] in ['？', '?']:
            src_w.write(s + '\n')
            ref_w.write(r + '\n')
        else:
            continue
