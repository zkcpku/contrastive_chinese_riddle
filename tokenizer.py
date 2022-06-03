from collections import Counter


class MyTokenizer:
    def __init__(self, vocab_size):
        self.vocab_size = vocab_size
        self.id2token = ['[CLS]', '[PAD]','[SEP]', '[UNK]', "[BOS]", "[EOS]"]
        self.token2id = {token: i for i, token in enumerate(self.id2token)}
        self.cls_token, self.sep_token, self.pad_token, self.unk_token, self.bos_token, self.eos_token = \
            "[CLS]", "[SEP]", "[PAD]", "[UNK]", "[BOS]", "[EOS]"
        self.special_tokens = [self.cls_token, self.sep_token, self.pad_token, self.unk_token, self.bos_token, self.eos_token]
        self.cls_token_id = self.token2id['[CLS]']
        self.pad_token_id = self.token2id['[PAD]']
        self.sep_token_id = self.token2id['[SEP]']
        self.unk_token_id = self.token2id['[UNK]']
        self.bos_token_id = self.token2id['[BOS]']
        self.eos_token_id = self.token2id['[EOS]']
        self.counter = Counter()

    def tokenize(self, text):
        if type(text) == list:
            return text
        return text.split()
    
    def convert_tokens_to_ids(self, tokens):
        return [self.token2id.get(token, self.unk_token_id) for token in tokens]
    
    def decode(self, ids):
        return [self.id2token[id] for id in ids]
    
    def add_document(self, document):
        self.counter.update(document)

    def add_token_to_vocab(self, token):
        self.token2id[token] = len(self.id2token)
        self.id2token.append(token)

    @staticmethod
    def from_corpus(corpus, vocab_size):
        # corpus should be a list of list of tokens
        tokenizer = MyTokenizer(vocab_size)
        for text in corpus:
            tokenizer.add_document(text)
        pairs = tokenizer.counter.most_common(vocab_size - len(tokenizer.id2token))
        for token, _ in pairs:
            tokenizer.add_token_to_vocab(token)
        print(tokenizer.id2token[:200])
        return tokenizer

