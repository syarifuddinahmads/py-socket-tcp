import random # library untuk memilih random text / raw data
import string # library
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk import WordNetLemmatizer

host = '127.0.0.1'
port = 1232

warnings.filterwarnings('ignore')
nltk.download('popular', quiet=True)

# buka data librari atau biasa disebut raw data
with open('data/bot.txt', 'r', encoding='utf8', errors='ignore') as fin:
    raws = fin.read().lower() # cari data raw yang ada pada file raw data

tokenSent = nltk.sent_tokenize(raws)
tokenWord = nltk.word_tokenize(raws)

# preprocessing text atau raw data
lmr = WordNetLemmatizer()


def lmTokens(tokens):
    return [lmr.lemmatize(token) for token in tokens]


removePunctDictionary = dict((ord(punct), None)
                             for punct in string.punctuation)


def lmNormalize(text):
    return lmTokens(nltk.word_tokenize(text.lower().translate(removePunctDictionary)))


# keyword match
INPUT = ('hello', 'hi', 'help') # input matching dari client
RESPONSE = ['hi', 'hey', 'hello', 'Am a Server, can i help you ?'] # response matching dari server untuk client berdasar random choice

# greetings word
def greetings(text):
    if(text == ''): # chek apakah yang diinput client adalah string kosong
        return "=== Selamat datang di Server BOT Indonesia ===\n BOT akan membantu anda mengenal lebih jauh tentang Indonesia..." # sambuta untuk client yang baru terkoneksi
    else:
        for word in text.split(): # looping untuk mencari kata yang relate dengan yang diinput oleh client
            if word.lower() in INPUT: # chek apakah text atau keyword yng diinput client ada di match INPUT
                return random.choice(RESPONSE) # result dari pengecekan ialah random choice dari match RESPONSE yang sudah didefinisikan

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

def handlingResponse(text):
    flag = True
    print("From Client = ",text)
    responseBot = ''
    while (flag == True):
        user_response = text.lower()
        if (user_response != 'bye'):
            if (user_response == 'thanks' or user_response == 'thank you'):
                flag = False
                responseBot ="ROBO: You are welcome.."
                return responseBot
            else:
                if (greetings(user_response) != None):
                    responseBot = greetings(user_response)
                    return responseBot
                else:
                    print("ROBO: ", end="")
                    responseBot = response(user_response)
                    tokenSent.remove(user_response)
                    return responseBot
        else:
            flag = False
            responseBot = "ROBO: Bye! take care.."
            return responseBot
