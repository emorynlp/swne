import os
import glob
import json
import string


def nontext(sentence, bidx, tout=None):
    curr_token = sentence[bidx]

    if  curr_token in {'#', '--'}:
        return bidx
    elif curr_token == '<':
        eidx = next((i for i, token in enumerate(sentence[bidx+1:], bidx+1) if token == '>'), -1)
        if eidx == -1: return -1
        if eidx + 1 < len(sentence) and sentence[eidx + 1] == '>': eidx += 1
        if tout: tout.write('{}\n'.format(' '.join(sentence[bidx:eidx+1])))
        return eidx
    
    return -1


def main(in_dir, out_dir, tout=None):
    for in_file in glob.glob(os.path.join(in_dir, '*.json')):
        print(in_file)
        doc = json.load(open(in_file))
        old_sentences = doc['sentences']
        new_sentences = []
        old_entities = doc['name_entities']
        new_entities = []
        map_sentences = [-1] * len(old_sentences)
        map_tokens = []

        for sid, old_sentence in enumerate(old_sentences):
            tmap = [-1] * len(old_sentence)
            map_tokens.append(tmap)
            new_sentence = []
            bidx = 0
            while bidx < len(old_sentence):
                eidx = nontext(old_sentence, bidx, tout)
                if eidx < 0:
                    tmap[bidx] = len(new_sentence)
                    new_sentence.append(old_sentence[bidx])
                else:
                    bidx = eidx
                bidx += 1
            
            if new_sentence and (len(new_sentence) > 2 or any(e[0] == sid for e in old_entities)):
                map_sentences[sid] = len(new_sentences)
                new_sentences.append(new_sentence)

        for old_entity in old_entities:
            old_sid = old_entity[0]
            old_bid = old_entity[1]
            old_eid = old_entity[2]
            label = old_entity[3]
            old_sentence = old_sentences[old_sid]

            new_sid = map_sentences[old_sid]
            if new_sid < 0: continue
            new_sentence = new_sentences[new_sid]

            tmap = map_tokens[old_sid]
            new_bid = tmap[old_bid]
            new_eid = tmap[old_eid - 1] + 1
            if new_bid < 0 or new_bid < 0: continue
            new_entity = [new_sid, new_bid, new_eid, label]
            new_entities.append(new_entity)

            # if new_bid < 0 or new_bid < 0 or old_sentence[old_bid:old_eid] != new_sentence[new_bid:new_eid]:
            #     print('==============================')
            #     print(' '.join(old_sentence))
            #     print('{} -> {}'.format(old_sentence[old_bid:old_eid], new_sentence[new_bid:new_eid]))
        
        doc['sentences_exc'] = new_sentences
        doc['named_entities_exc'] = new_entities
    
        out_file = open(os.path.join(out_dir, os.path.basename(in_file)), 'w')
        json.dump(doc, out_file)





if __name__ == "__main__":
    IN_DIR = '../ner/gold'
    OUT_DIR = '../ner/gold-x'
    # tout = open('tmp.txt', 'w')
    main(IN_DIR, OUT_DIR)
