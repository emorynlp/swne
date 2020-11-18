import os
import glob
import json

def main(dat_dir):
    sen_count, tok_count, ent_count = 0, 0, 0
    sen_exc_count, tok_exc_count, ent_exc_count = 0, 0, 0
    
    for filename in glob.glob(os.path.join(dat_dir, '*.json')):
        print(filename)
        d = json.load(open(filename))
        sentences = d['sentences']
        entities = d['named_entities']
        sentences_exc = d['sentences_exc']
        entities_exc = d['named_entities_exc']
        
        sen_count += len(sentences)
        tok_count += sum([len(sen) for sen in sentences])
        ent_count += len(entities)

        sen_exc_count += len(sentences_exc)
        tok_exc_count += sum([len(sen) for sen in sentences_exc])
        ent_exc_count += len(entities_exc)

    print(sen_count, tok_count, ent_count)
    print(sen_exc_count, tok_exc_count, ent_exc_count)


if __name__ == "__main__":
    DAT_DIR = '../dat/swne'
    main(DAT_DIR)
