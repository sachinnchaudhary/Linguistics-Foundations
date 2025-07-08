#input: "He is voracious reader who loves books so much"
#ouput: {
  "PRON": [
    "he",
    "who"
  ],
  "AUX": [
    "is"
  ],
  "ADJ": [
    "voracious"
  ],
  "NOUN": [
    "reader",
    "books"
  ],
  "VERB": [
    "loves"
  ],
  "ADV": [
    "so",
    "much"
  ]
} 



!pip install spacy

import spacy,collections, json 

nlp = spacy.load("en_core_web_sm")


def sem_tree(sent: str):
     
     doc = nlp(sent)
     buckets = collections.defaultdict(list)
     for tok in doc:
       if tok.is_alpha:
          buckets[tok.pos_].append(tok.text)
     return dict(buckets)     
          

while True:
     sent = input("type a sentance or enter a quit(for stop): ").strip().lower()
     if sent == "quit":
        break 
        
     else:
        print(json.dumps(sem_tree(sent), indent = 2)) 
