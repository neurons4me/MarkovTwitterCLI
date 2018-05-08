corpus_input = open('speeches.txt', encoding='utf8').read()
#corpus_input = 'The quick brown fox jumped up the fucking tree the filthy little bastard. Who does the fucking quick fox think he is!'
import random



def build_master_corpus (raw_corpus):
    corpus = {}
    corpus_split = raw_corpus.split()
    try:
        for i, word in enumerate(corpus_split, start=0):
            next_word = corpus_split[i+1]
            word_next_tuple = (word, next_word)
            if word_next_tuple not in corpus.keys():
                corpus[word_next_tuple] = 1
            elif word_next_tuple in corpus.keys():
                corpus[word_next_tuple] += 1

    except IndexError:

        return corpus

##TODO add some fuzzy randomness to the selection process
##TODO respect punctuation for sentence end and add logic to keep sentences hanging

# corpus=build_master_corpus(corpus_input)

def pick_rand_start(corpus):
    keys_list = list(corpus.keys())
    valid_starting_words = []
    for item in keys_list:
        if item[0].istitle():
            valid_starting_words.append(item[0])

    return random.choice(valid_starting_words)

# rand_start = pick_rand_start(corpus)
# print(rand_start)

def pick_next_word(last_word, corpus):
    keys_list = list(corpus.keys())
    valid_next_words_keys = []
    for item in keys_list:
        if last_word == item[0]:
            valid_next_words_keys.append(item)
    highest_value = 0
    next_word = ''
    random.shuffle(valid_next_words_keys)
    for key in valid_next_words_keys:
        if corpus[key] > highest_value:
            next_word = key[1]


    return next_word

def chain_main():
    corpus = build_master_corpus(corpus_input)
    output_list = []
    start_word = pick_rand_start(corpus)
    output_list.append(start_word)
    last_word = start_word
    for i in range(30):
        this_word = pick_next_word(last_word, corpus)
        output_list.append(this_word)
        last_word = this_word

    return ' '.join(output_list)



for i in range(3):
    print(chain_main())
    print('\n\n')