# Dataset

Our dataset consists of JSON files formatted as follows:

* `doc_id`: the document ID inherited from the [SwDA](https://github.com/cgpotts/swda) corpus
* `annotator`: the annotator ID
* `text`: the entire contents of the dialogue in plain text
* `sentences`: list of sentences where each sentence is represented by a list of tokens.
* `name_entities` : list of entities where each entity is presented by a tuple of:
  * `sentence_id`: the ID of the sentence where the entity is found
  * `begin_token_index`: the index of the first token in the entity (staring from 0; inclusive)
  * `end_token_index`: the index of the last token in the entity (staring from 0; exclusive)
  * `label`: the entity label
* `sentences_exc`: list of sentences where:
  * Non-textual tokens are removed (e.g., \<Radio>)
  * Sentences whose lengths are  `<=2` and do not include any entity are discarded
* `name_entities_exc`: list of entities that are remapped to sentences in `sentences_exc`


## Statistics

 \ | Dialogues | Sentences  | Tokens | Entities |
|:---:|:---:|:---:|:---:|:---:|
Original | 227 | 31,552 | 281,756 | 5,220 |
Trimmed  | 227  | 21,449 | 244,817 | 5,218 |
