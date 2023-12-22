# python (location)/Neg_and_pos_reviews.py

# for ex.:
# This is very good
# Not bad


import glob

POS_FILES_PATTERN = '.../pos/*.txt' #your path
NEG_FILES_PATTERN = '.../neg/*.txt' #your path


# Load and parse positive reviews
pos_files = glob.glob(POS_FILES_PATTERN)
pos_reviews = []
for file in pos_files:
    with open(file,encoding='utf-8-sig') as stream:
        content = stream.read()
        words = content.lower().replace('<br />', ' ').split()
        pos_reviews.append(words)

#Load and parse negative reviews
neg_files = glob.glob(NEG_FILES_PATTERN)
neg_reviews = []
for file in neg_files:
    with open(file,encoding='utf-8-sig') as stream:
        content = stream.read()
        words = content.lower().replace('<br />', ' ').split()
        neg_reviews.append(words)

# Get sentence
sentence = input("Leave a comment: ")
words = sentence.lower().replace('<br />', ' ').split()

# Compute sentence sentiment
sentence_sentiment = 0
for word in words:
    positive = 0
    negative = 0
    for review in pos_reviews:
        if word in review:
            positive += 1
    for review in neg_reviews:
        if word in review:
            negative += 1
    all_ = positive + negative
    if all_ != 0:
        word_sentiment = (positive - negative) / all_
    else:
        word_sentiment = 0.0

    print(word, word_sentiment)

    sentence_sentiment += word_sentiment
sentence_sentiment /= len(words)

# Raport
if sentence_sentiment > 0:
    label = 'positive'
else:
    label = 'negative'
print('--')
print("This sentence is", label, ', sentriment =', sentence_sentiment)
