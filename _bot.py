import random
import string
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk import WordNetLemmatizer


warnings.filterwarnings('ignore')
nltk.download('popular', quiet=True)

with open('data/bot.txt', 'r', encoding='utf8', errors='ignore') as fin:
    raws = fin.read().lower()

tokenSent = nltk.sent_tokenize(raws)
tokenWord = nltk.word_tokenize(raws)

# preprocessing
lmr = WordNetLemmatizer()


def lmTokens(tokens):
    return [lmr.lemmatize(token) for token in tokens]


removePunctDictionary = dict((ord(punct), None)
                             for punct in string.punctuation)


def lmNormalize(text):
    return lmTokens(nltk.word_tokenize(text.lower().translate(removePunctDictionary)))


# keyword match
INPUT = ('hello', 'hi', 'help')
RESPONSE = ['hi', 'hey', 'hello', 'Am a Server, can i help you ?']

# greetings word
def greetings(text):
    if(text == ''):
        return "=== Selamat datang di Server BOT Indonesia ===\n BOT akan membantu anda mengenal lebih jauh tentang Indonesia..."
    else:
        for word in text.split():
            if word.lower() in INPUT:
                return random.choice(RESPONSE)

# response from server after greeting input
def response(text):
    wordResponse = ''
    tokenSent.append(text)
    TfidfVec = TfidfVectorizer(tokenizer=lmNormalize, stop_words='id')
    tfidf = TfidfVec.fit_transform(tokenSent)
    val = cosine_similarity(tfidf[-1], tfidf)
    idx = val.argsort()[0][-2]
    flat = val.flatten()
    flat.sort()
    requestTfidf = flat[-2]
    if(requestTfidf == 0):
        wordResponse = wordResponse+"Sorry, I don't understand..."
    else:
        wordResponse = wordResponse+tokenSent[idx]
    return wordResponse
