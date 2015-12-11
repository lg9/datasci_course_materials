import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def get_sent_dict(sentiment_file):
    scores = {}
    finn_fh = open(sentiment_file)
    for line in finn_fh.readlines():
        term, score = line.split("\t")
        scores[term] = int(score)
    finn_fh.close()
    return scores

def print_tweet_scores(tweet_json_file, sentiment_dictionary):
    tweet_fh = open(tweet_json_file)
    for line in tweet_fh:
        tweet_json = json.loads(line)
        if 'text' in tweet_json:        # tweets have 'text' field
            # since it is a tweet, calculate and print sentiment score
            score = 0
            words = tweet_json["text"].split(' ')
            for word in words:
                if word in sentiment_dictionary:
                    score += sentiment_dictionary[word]
            print str(score)
    tweet_fh.close()

def main():
    sent_filename = sys.argv[1]
    sent_dict = get_sent_dict(sent_filename)
    tweet_filename = sys.argv[2]
    print_tweet_scores(tweet_filename, sent_dict)
    
##    sent_file = open(sys.argv[1])
##    tweet_file = open(sys.argv[2])
##    hw()
##    lines(sent_file)
##    lines(tweet_file)

if __name__ == '__main__':
    main()
