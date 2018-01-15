from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import argparse

parser = argparse.ArgumentParser(
    description='Get Twitter stream in a language specified. Filter by common word list.')
parser.add_argument('lang_code')
parser.add_argument('output_json_file')
args = vars(parser.parse_args())

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open(args['output_json_file'], 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

words = []
common_words_filename = 'words-' + args['lang_code'] + '.txt'
print("Language: {}".format(args['lang_code']))
print("Use word list from: {}".format(common_words_filename))

with open(common_words_filename) as f:
    words = f.readlines()
del words[400:]
words = [word.strip() for word in words] 

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=words, languages=[args['lang_code']])
