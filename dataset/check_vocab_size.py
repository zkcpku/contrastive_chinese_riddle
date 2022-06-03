from collections import Counter
import json

def get_corpus(json_paths):
    corpus_data = []
    for each_json_path in json_paths:
        with open(each_json_path,'r') as f:
            js = json.load(f)
            for each_js in js:
                corpus_data.append(each_js['input'])
                corpus_data.append(each_js['output'])
    return corpus_data


def get_corpus_counter(corpus_data):
    corpus_counter = Counter()
    for each_data in corpus_data:
        corpus_counter.update(each_data)
    return corpus_counter

if __name__ == '__main__':
    json_paths = ['/home/zhangkechi/workspace/riddle/dataset/train.csv.for_seq_only_word.json',
    '/home/zhangkechi/workspace/riddle/dataset/valid.csv.for_seq_only_word.json']
    corpus_data = get_corpus(json_paths)
    corpus_counter = get_corpus_counter(corpus_data)
    print(len(corpus_counter))
    print(max([len(e) for e in corpus_data]))
    import pdb;pdb.set_trace()