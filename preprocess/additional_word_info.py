import os
import sys
sys.path.append('/home/zhangkechi/workspace/riddle/')

import pandas as pd
from hanzi_chaizi.hanzi_chaizi import HanziChaizi
import json
from tqdm import tqdm
###init chaizi
hc = HanziChaizi()
###pinyin2nopinyin
nopinyin2pinyin = {'a':'ā á ǎ à','o':'ō ó ǒ ò','e':'ē é ě è','i':'ī í ǐ ì','u':'ū ú ǔ ù','ü':'ǖ ǘ ǚ ǜ'}
nopinyin2pinyin = {k:nopinyin2pinyin[k].split(' ') for k in nopinyin2pinyin}
pinyin2nopinyin = {}
for k in nopinyin2pinyin:
    for each_k in nopinyin2pinyin[k]:
        pinyin2nopinyin[each_k] = k
###pinyin
cidian_path = '/home/zhangkechi/workspace/riddle/dataset/pinyin.txt'
with open(cidian_path,'r') as f:
    pinyin = f.readlines()
word2pinyin = {}
for e in pinyin[2:]:
    element_in_e = e.strip().split(' ')
    this_pinyin = element_in_e[1]
    this_pinyin = ''.join([pinyin2nopinyin[k] if k in pinyin2nopinyin else k for k in this_pinyin])
    this_word = element_in_e[-1]
    word2pinyin[this_word] = list(set(this_pinyin.split(',')))


def get_additional_word_info(word):
    try:
        pinyin = word2pinyin[word]
    except Exception as e:
        pinyin  = []
    try:    
        chaizi = hc.query(word)
    except Exception as e:
        chaizi = [word]
    return pinyin,chaizi

def isChinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

def add_info_into_csv(cst_path):
    print(cst_path)
    df = pd.read_csv(cst_path)
    df_len = len(df)
    print(df_len)
    save_rst = []
    error_word = []
    for i in tqdm(range(df_len)):
        Q = df.loc[i]['Q']
        A = df.loc[i]['A']
        this_rst = {}
        this_rst['Q'] = ''.join([e for e in Q if isChinese(e)])
        this_rst['A'] = A
        this_rst['Q_pinyin'] = []
        this_rst['Q_chaizi'] = []
        this_rst['A_pinyin'] = []
        this_rst['A_chaizi'] = []
        None_FLAG = False
        for each_word in Q:
            each_additional_info = get_additional_word_info(each_word)
            # if each_additional_info is None:
            #     error_word.append(each_word)
            #     # None_FLAG = True
            #     # break
            this_rst['Q_pinyin'].append(each_additional_info[0])
            this_rst['Q_chaizi'].append(each_additional_info[1])
        # if None_FLAG:
        #     continue
        
        for each_word in A:
            each_additional_info = get_additional_word_info(each_word)
            # if each_additional_info is None:
            #     error_word.append(each_word)
            #     # None_FLAG = True
            #     # break
            this_rst['A_pinyin'].append(each_additional_info[0])
            this_rst['A_chaizi'].append(each_additional_info[1])
        # if None_FLAG:
        #     continue

        save_rst.append(this_rst)
    print(len(save_rst))
    # print(len(set(error_word)))
    # print(len(error_word))
    # print(set(error_word))
    # print(len([e for e in set(error_word) if not isChinese(e)]))
    # print([e for e in set(error_word) if not isChinese(e)])
    with open(cst_path + '.json','w') as f:
        json.dump(save_rst,f,ensure_ascii=False)
    return save_rst


def main_for_seq(csv_path):
    save_rst = add_info_into_csv(csv_path)
    save_for_seq = []
    for each_rst in save_rst:
        this_save_for_seq = {}
        this_save_for_seq['input'] = []
        this_save_for_seq['output'] = []
        for i in range(len(each_rst['Q'])):
            this_save_for_seq['input'].append(each_rst['Q'][i])
            this_save_for_seq['input'].extend(each_rst['Q_pinyin'][i])
            this_save_for_seq['input'].extend(each_rst['Q_chaizi'][i])
        
        for i in range(len(each_rst['A'])):
            this_save_for_seq['output'].append(each_rst['A'][i])
            this_save_for_seq['output'].extend(each_rst['A_pinyin'][i])
            this_save_for_seq['output'].extend(each_rst['A_chaizi'][i])
        save_for_seq.append(this_save_for_seq)
    # return save_for_seq
    with open(csv_path + '.for_seq.json','w') as f:
        json.dump(save_for_seq,f,ensure_ascii=False)

def main_for_seq_only_chaizi(csv_path):
    save_rst = add_info_into_csv(csv_path)
    save_for_seq = []
    for each_rst in save_rst:
        this_save_for_seq = {}
        this_save_for_seq['input'] = []
        this_save_for_seq['output'] = []
        for i in range(len(each_rst['Q'])):
            this_save_for_seq['input'].append(each_rst['Q'][i])
            # this_save_for_seq['input'].extend(each_rst['Q_pinyin'][i])
            this_save_for_seq['input'].extend(each_rst['Q_chaizi'][i])
        
        for i in range(len(each_rst['A'])):
            this_save_for_seq['output'].append(each_rst['A'][i])
            # this_save_for_seq['output'].extend(each_rst['A_pinyin'][i])
            this_save_for_seq['output'].extend(each_rst['A_chaizi'][i])
        save_for_seq.append(this_save_for_seq)
    # return save_for_seq
    with open(csv_path + '.for_seq_only_chaizi.json','w') as f:
        json.dump(save_for_seq,f,ensure_ascii=False)

def main_for_seq_only_word(csv_path):
    save_rst = add_info_into_csv(csv_path)
    save_for_seq = []
    for each_rst in save_rst:
        this_save_for_seq = {}
        this_save_for_seq['input'] = []
        this_save_for_seq['output'] = []
        for i in range(len(each_rst['Q'])):
            this_save_for_seq['input'].append(each_rst['Q'][i])
            # this_save_for_seq['input'].extend(each_rst['Q_pinyin'][i])
            # this_save_for_seq['input'].extend(each_rst['Q_chaizi'][i])
        
        for i in range(len(each_rst['A'])):
            this_save_for_seq['output'].append(each_rst['A'][i])
            # this_save_for_seq['output'].extend(each_rst['A_pinyin'][i])
            # this_save_for_seq['output'].extend(each_rst['A_chaizi'][i])
        save_for_seq.append(this_save_for_seq)
    # return save_for_seq
    with open(csv_path + '.for_seq_only_word.json','w') as f:
        json.dump(save_for_seq,f,ensure_ascii=False)


def generate_fake_csv(Qs, As, output_csv):
    csv_lines = []
    csv_lines.append('Q,A\n')
    for i in range(len(Qs)):
        if i >= len(As):
            this_As = As[-1]
        else:
            this_As = As[i]
        csv_lines.append(Qs[i] + ',' + this_As + '\n')
    
    with open(output_csv,'w') as f:
        f.writelines(csv_lines)

def fake_csv_for_valid(valid_csv_path):
    df = pd.read_csv(valid_csv_path)
    Qs = df['Q'].tolist()
    As = df['A'].tolist()
    As = list(set(As))
    print(len(As))
    generate_fake_csv(Qs, As, valid_csv_path + '.fake.csv')

def fake_csv_for_test(Q_path, A_path):
    with open(Q_path) as f:
        Qs = f.readlines()
    Qs = [q.strip() for q in Qs]
    with open(A_path) as f:
        As = f.readlines()
    As = [a.strip() for a in As]
    print(len(Qs))
    print(len(set(Qs)))
    print(len(As))
    print(len(set(As)))
    generate_fake_csv(Qs, As, Q_path + '.fake.csv')

if __name__ == '__main__':
    # main_for_seq_only_word('/home/zhangkechi/workspace/riddle/dataset/train.csv')
    # main_for_seq_only_word('/home/zhangkechi/workspace/riddle/dataset/valid.csv')

    # fake_csv_for_valid('/home/zhangkechi/workspace/riddle/dataset/valid.csv')
    # main_for_seq_only_chaizi('/home/zhangkechi/workspace/riddle/dataset/valid.csv.fake.csv')

    fake_csv_for_test('/home/zhangkechi/workspace/riddle/dataset/test.txt','/home/zhangkechi/workspace/riddle/dataset/dict.txt')
    main_for_seq_only_chaizi('/home/zhangkechi/workspace/riddle/dataset/test.txt.fake.csv')




