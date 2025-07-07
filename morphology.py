import re 



import re, sys, json 

IRREG = {
          "children": ("child", "-ren", "plur"),                  #------------> add more words as per you need 
          "went": ("go", "-ent","past")
         }



RULES = [
    (re.compile(r"^(.+?)ies$"),           lambda m: (m[1]+"y", "-ies", "PLUR")),
    (re.compile(r"^(.+?)([sxz]|[sh]ch)es$"), lambda m: (m[1]+m[2], "-es", "PLUR")),
    (re.compile(r"^(.+?)s$"),             lambda m: (m[1], "-s", "PLUR")),
    (re.compile(r"^(.+?)ied$"),           lambda m: (m[1]+"y", "-ied", "PAST")),
    (re.compile(r"^(.+?)ed$"),            lambda m: (m[1], "-ed", "PAST")),
    (re.compile(r"^(.+?)(ing|ઓ|એ)$"),    lambda m: (m[1], "-"+m[2], "OTHER")),
]


def split_word(word: str):
    if word in IRREG:
        IRREG[word]

    for pat, fun in RULES:
       m = pat.match(word)

       if m:
           return fn(m.groups())
      
       return word, "", "UNK"


word= input("enter the word ?").strip().lower()
base, affix, tag = split_word(word)
print(json.dumps({"surface": word, "base": base, "affix": affix, "tag": tag}, ensure_ascii= False, indent = 2))
