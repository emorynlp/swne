import os
import glob
import json

def main(gold_dir):
    sen_count = 0
    tok_count = 0
    ent_count = 0
    
    for filename in glob.glob(os.path.join(gold_dir, '*.json')):
        print(filename)
        d = json.load(open(filename))
        sentences = d['sentences']
        entities = d['name_entities']
        sen_count += len(sentences)
        tok_count += sum([len(sen) for sen in sentences])
        ent_count += len(entities)

    print(sen_count, tok_count, ent_count)
   


if __name__ == "__main__":
    GOLD_DIR = '../ner/gold'
    main(GOLD_DIR)


