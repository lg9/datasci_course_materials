import sys
import json

def get_sent_dict(sentiment_file):
    scores = {}
    finn_fh = open(sentiment_file)
    for line in finn_fh.readlines():
        term, score = line.split("\t")
        scores[term] = int(score)
    finn_fh.close()
    return scores

def score_nonsent_terms(tweet_json_file, sentiment_dictionary):
    tweet_fh = open(tweet_json_file)
    term_counts = {}    # dictionary to record counts of non-sentiment terms
    term_scores = {}    # dictionary to record score sums of non-sentiment terms
    for line in tweet_fh:
        tweet_json = json.loads(line)
        if 'text' in tweet_json:        # tweets have 'text' field
            # since it is a tweet, calculate and print sentiment score
            score = 0
            terms = tweet_json["text"].split(' ')
            for term in terms:
                if term in sentiment_dictionary:
                    score += sentiment_dictionary[term]
            for term in terms:
                if term not in sentiment_dictionary:
                    e_term = term.encode('utf-8')
                    if e_term not in term_counts:
                        term_counts[e_term] = 0
                        term_scores[e_term] = 0
                    term_counts[e_term] += 1
                    term_scores[e_term] += score
    tweet_fh.close()

    ''' now print out average scores for non-sentiment terms
        that appear at least 3 times but fewer than 50% of the max times.
        This is a very simplistic method, but I hope it will make the grade. '''
    max_count = 0
    for term in term_counts.keys():
        if term_counts[term] > max_count:
            max_count = term_counts[term]

    for term in sorted(term_counts.keys()):
        if term_counts[term] > 3 and term_counts[term] < max_count/2:
            score = float(term_scores[term]) / float(term_counts[term])
#            outline = term + "      " + str(term_counts[term]) + "  " + str(term_scores[term]) + "       " + str(score)
            outline = term + " " + format(score, '.3f')
            print outline

def main():
    sent_filename = sys.argv[1]
#    sent_filename = 'AFINN-111.txt'
    sent_dict = get_sent_dict(sent_filename)
    tweet_filename = sys.argv[2]
#    tweet_filename = 'output.txt'
    score_nonsent_terms(tweet_filename, sent_dict)

if __name__ == '__main__':
    main()
