corpus_input = open('speeches.txt', encoding='utf8').read()
#corpus_input = 'The quick brown fox jumped up the fucking tree the filthy little bastard. Who does the quick fox think he is!'
import random



def build_master_corpus (raw_corpus):
    corpus = {}
    corpus_split = raw_corpus.split()
    try:
        for i, word in enumerate(corpus_split, start=0):
            corpus[word] = corpus_split[i + 1]
    except IndexError:

        return corpus

##TODO change corpus generation to account for frequency, currently it just pulls the last value written to the key. Rewrite so that the key is tied to a tuple of the value and the frequency
##TODO add some fuzzy randomness to the selection process
##TODO respect punctuation for sentence end and add logic to keep sentences hanging

corpus=build_master_corpus(corpus_input)


def pick_rand_start(corpus):
    return random.choice(list(corpus.keys()))



def pick_next_word(last_word):
    return corpus[last_word]

def chain_main():

    output_list = []
    start_word = pick_rand_start(corpus)
    output_list.append(start_word)
    last_word = start_word
    for i in range(30):
        this_word = pick_next_word(last_word)
        output_list.append(this_word)
        last_word = this_word

    return ' '.join(output_list)


print(chain_main())