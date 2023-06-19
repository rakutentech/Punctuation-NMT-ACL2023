import sys
import re
import random

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

for s, r in zip(source_text, reference_text):
    if re.search('\w', s[-1]):
        try:
            option = x
        except:
            print(
                "What do you want to do? 1. Add Fullstop 2. Add Exclamation 3. Add Question 4. Add Random Char 5. Delete Final Char"
            )
            x = input()
        add_char = ''
        if x == '1':
            if src_lang in ['de', 'en', 'uk']:
                add_char = '.'
            elif src_lang == 'ja':
                add_char = '。'
        elif x == '2':
            if src_lang in ['de', 'en', 'uk']:
                add_char = '!'
            elif src_lang == 'ja':
                add_char = '！'
        elif x == '3':
            if src_lang in ['de', 'en', 'uk']:
                add_char = '?'
            elif src_lang == 'ja':
                add_char = '？'
        elif x == '4':
            sentchars = ''.join(s.split())
            add_char = random.choice(sentchars)
        elif x == '5':
            src_w.write(s[:-1] + '\n')
            ref_w.write(r + '\n')

        else:
            print("invalid choice")
            break

        if x != '5':
            src_w.write(s + add_char + '\n')
            ref_w.write(r + '\n')
    elif s[-1] in ['。', '.', '！', '!', '？', '?']:
        src_w.write(s[:-1] + '\n')
        ref_w.write(r + '\n')
