from collections import Counter
NOspaming = [
    "Nu negalima tu lenktas",
    "Kiek kartu sakyti NESKAITYSIU TO TAVO spamo",
    "NU negrazu spaminti",
    "Nu jei leidi kalbeti tai gero vakaro čatas",
    "dabar negausi močiutes cepelinu už toky",
    "NU rimtai sugauk",
    "Katinas net geresne žinute butu parašes negul tu"
    ]

def has_repeated_letters(word):
    for i in range(0, len(word)-2):
        if word[i] == word[i+1] == word[i+2]:
            return True
    return False

def detect_repeating_words(sentence):
    word_counts = Counter(word for word in sentence.split() if len(word) >= 4)
    return any(count >= 2 for count in word_counts.values())

def detect_repeating_letters(sentence):
    for word in sentence.split():
        if has_repeated_letters(word):
            return True
    return False
def is_spam(text):
    a = detect_repeating_words(text)
    b = detect_repeating_letters(text)
    if a == True:
        return "True"
    elif b == True:
        return "True"
    else:
        return "False"

