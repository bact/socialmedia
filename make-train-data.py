import json
import argparse

parser = argparse.ArgumentParser(
    description='Make training data in fastText format')
parser.add_argument('label')
parser.add_argument('twitter_json_file')
parser.add_argument('fasttext_training_file')
args = vars(parser.parse_args())

json_file = open(args['twitter_json_file'], 'r')
training_file = open(args['fasttext_training_file'], 'w', newline='')

json_decoder = json.JSONDecoder()

for line in json_file:
    tweet = json_decoder.decode(line)
    if 'truncated' in tweet and tweet['truncated']:
        continue
    if 'retweeted_status' in tweet and tweet['retweeted_status']:
        tweet = tweet['retweeted_status']

    if 'id_str' in tweet:
        training_file.write('__label__')
        training_file.write(args['label'])
        training_file.write(' ')
        training_file.write(tweet['text'].replace('\n', ' '))
        training_file.write('\n')

json_file.close()
training_file.close()
