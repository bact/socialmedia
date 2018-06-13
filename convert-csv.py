import json
import csv
import argparse

parser = argparse.ArgumentParser(
    description='Convert Twitter stream data from JSON format to CSV format.')
parser.add_argument("json_file")
parser.add_argument("csv_file")
args = vars(parser.parse_args())

json_file = open(args['json_file'], 'r')
csv_file = open(args['csv_file'], 'w', newline='')
writer = csv.writer(csv_file, dialect='excel', quoting=csv.QUOTE_ALL)

json_decoder = json.JSONDecoder()

for line in json_file:
    tweet = json_decoder.decode(line)
    tweet_csv = []
    if 'truncated' in tweet and tweet['truncated']:
        continue
    if 'retweeted_status' in tweet and tweet['retweeted_status']:
        tweet = tweet['retweeted_status']

    if 'id_str' in tweet:
        tweet_csv.append(tweet['id_str'])
        tweet_csv.append(tweet['favorite_count'])
        tweet_csv.append(tweet['retweet_count'])
        tweet_csv.append(tweet['text'].replace('\n', ''))
    #tweet_csv.append(tweet['text'])
        writer.writerow(tweet_csv)
    #print(csv)

json_file.close()
csv_file.close()

# for line in tweets_file:
#     tweet = json_decoder.decode(line)
#     original_tweet = None
#     #print(json.dumps(tweet, sort_keys=True, indent=4))
#     if 'truncated' in tweet and tweet['truncated']:
#         print('[TRUNCATED]')
#     if 'retweeted_status' in tweet and tweet['retweeted_status']:
#         print('***This is RT****')
#         original_tweet = tweet['retweeted_status']
#         print('Tweet ID: %s' % tweet['id_str'])
#         print('Original tweet ID: %s' % original_tweet['id_str'])
#         print('*************')
#     if 'text' in tweet:
#         print(tweet['text'])
#     if original_tweet:
#         print('///////////////')
#         if 'truncated' in original_tweet and original_tweet['truncated']:
#             print('[TRUNCATED] (o)')
#         if 'text' in original_tweet:
#             print(original_tweet['text'])
#     print('-----------------')

#for tweet in json.load(tweets_file):
#    print(tweet)
