!pip install cmudict
import cmudict
cmu = cmudict.dict() 

ARPABET2IPA = {
    # Vowels
    "AA":"ɑ", "AE":"æ", "AH":"ʌ", "AO":"ɔ", "AW":"aʊ", "AY":"aɪ",
    "EH":"ɛ", "ER":"ɝ", "EY":"eɪ", "IH":"ɪ", "IY":"i", "OW":"oʊ",
    "OY":"ɔɪ", "UH":"ʊ", "UW":"u",
    # Stops & Affricates
    "P":"p", "B":"b", "T":"t", "D":"d", "K":"k", "G":"ɡ",
    "CH":"t͡ʃ", "JH":"d͡ʒ",
    # Fricatives
    "F":"f", "V":"v", "TH":"θ", "DH":"ð", "S":"s", "Z":"z",
    "SH":"ʃ", "ZH":"ʒ", "HH":"h",
    # Nasals & Liquids
    "M":"m", "N":"n", "NG":"ŋ", "L":"l", "R":"ɹ",
    # Glides
    "Y":"j", "W":"w"
}

ANSI_COLORS = [
    "\033[96m",  # cyan
    "\033[95m",  # magenta
    "\033[94m",  # blue
    "\033[93m",  # yellow
    "\033[92m",  # green
    "\033[91m",  # red
]
RESET = "\033[0m"


vowel_ipa = "ɑæʌɔaʊaɪɛɝeɪɪioʊɔɪʊu"

def get_phonemes(word):                   # to get the phoneme out of word

   phones = cmu.get(word, [])
   if not phones:
     raise ValueError(f"word not found in the cmudict: {word}")
   return phones[0]

def get_apa(phoneme):
    return "".join(ARPABET2IPA[p.rstrip("012")] for p in phoneme)


def get_syllable(ipa):                    # to get the syllables 
      chunks= []
      str_sylb = "" 
      for ch in ipa:
        if ch in vowel_ipa:
          if str_sylb:
            chunks.append(str_sylb)
            str_sylb= ch
        else: 
            str_sylb += ch
 
      if str_sylb:
        chunks.append(str_sylb)
      return chunks     

def colour_syl(syllable):                  # to colour the syllables 
     
     colored_syl = []
     for i, syl in enumerate(syllable): 
      colour = ANSI_COLORS[i % len(ANSI_COLORS)]
      colored_syl.append(f"{colour}{syl}{RESET}")
     return "".join(colored_syl)





word = input("type the word to get the IPA").strip().lower()
phonemes = get_phonemes(word)
ipa = get_apa(phonemes)
syllable = get_syllable(ipa)
 

print(f"this is the IPA for {word}: {ipa} ")
print(f"this is the coloured syllable: {colour_syl(syllable)}")
