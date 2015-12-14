import sys
import json

def report_term_frequency(tweet_json_file):
    tweet_fh = open(tweet_json_file)
    term_counts = {}    # dictionary to record counts of terms
    term_total = 0
    
    for line in tweet_fh:
        tweet_json = json.loads(line)
        if 'text' in tweet_json:        # tweets have 'text' field
            # since it is a tweet, log terms
            terms = tweet_json["text"].split(' ')
            for term in terms:
                stripped_term = term.strip()
                e_term = stripped_term.encode('utf-8')
                if len(e_term) == 0:
                    continue
                if e_term not in term_counts:
                    term_counts[e_term] = 0
                term_counts[e_term] += 1
                term_total += 1
    tweet_fh.close()

    ''' now print out terms and term frequencies '''

    for term in term_counts.keys():
        freq = float(term_counts[term]) / float(term_total)
        outline = term + " " + format(freq, '.3f')
        print outline

def main():
    tweet_filename = sys.argv[1]
#    tweet_filename = 'output.txt'
    report_term_frequency(tweet_filename)

if __name__ == '__main__':
    main()
