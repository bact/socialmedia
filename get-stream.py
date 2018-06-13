import configparser
import argparse
from collections import OrderedDict

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

CONFIG_FILENAME = 'accounts.ini'

def read_config(config_filename):
    config = configparser.ConfigParser()

    if not config.read(config_filename):
        print('Cannot read configuration file: {}'.format(config_filename))
        return None

    if 'twitter' not in config:
        print('Cannot find [Twitter] section in: {}'.format(config_filename))
        return None
    twitter_config = config['twitter']

    if 'CONSUMER_KEY' not in twitter_config:
        print('CONSUMER_KEY not found.')
        return None

    if 'CONSUMER_SECRET' not in twitter_config:
        print('CONSUMER_SECRET not found.')
        return None

    if 'ACCESS_TOKEN' not in twitter_config:
        print('ACCESS_TOKEN not found.')
        return None

    if 'ACCESS_SECRET' not in twitter_config:
        print('ACCESS_SECRET not found.')
        return None

    return config

class MyListener(StreamListener):
    def __init__(self, filename):
        self.output_filename = filename

    def on_data(self, data):
        try:
            with open(self.output_filename, 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

def main():
    parser = argparse.ArgumentParser(
        description='Get Twitter stream in a language specified. Filter by common word list.')
    parser.add_argument('lang_code', help='ISO language code (will use to pick word list)')
    parser.add_argument('output_json_file', help='Output file, will be written in JSON format')
    args = vars(parser.parse_args())

    lang = args['lang_code']
    output_filename = args['output_json_file']

    words = []
    common_words_filename = 'data/stopwords-' + lang + '.txt'
    with open(common_words_filename) as f:
        words = f.readlines()
    _words = [w.split() for w in words] # break compound words into single words
    _words = [w for x in _words for w in x] # flattening the list
    words = list(OrderedDict((w, True) for w in _words).keys()) # remove duplicates, preserving order
    del words[400:] # cut it to 400 words (the limit by Twitter API)

    print("Languages: {}".format(lang))
    print("Use word list from: {}".format(common_words_filename))
    print("Number of single words: {}".format(len(words)))

    config = read_config(CONFIG_FILENAME)
    if not config:
        print("Please check values in configuration file: {}".format(CONFIG_FILENAME))
        return
    twitter_config = config['twitter']

    print("Connecting to Twitter stream...")
    auth = OAuthHandler(twitter_config['CONSUMER_KEY'], twitter_config['CONSUMER_SECRET'])
    auth.set_access_token(twitter_config['ACCESS_TOKEN'], twitter_config['ACCESS_SECRET'])

    twitter_stream = Stream(auth, MyListener(output_filename))
    twitter_stream.filter(track=words, languages=[lang])

if __name__ == "__main__": main()
