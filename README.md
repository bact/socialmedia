# get-stream.py
A script to collect tweets from Twitter stream

- This is done by using Twitter's Stream API to get tweets with a language specified, filtered with 400 commons words in that language

## Commons words
- Burmese	http://1000mostcommonwords.com/tag/burmese-words/
- English	http://world-english.org/english500.htm
- Vietnamese	http://www.101languages.net/vietnamese/vietnamese-word-list/
- Thai common words list, partially drawn from Chulalongkorn University's 400 most used Thai words. http://womenlearnthai.com/index.php/thai-frequency-lists-with-english-definitions/

## Plan
- Check if it's a retweet or not
  - If it is a retweet, does it has an additional text (check id_str)
- Have to get the full tweet, no truncation
  - Check truncated=True
- Keep these attributes: id, retweet_count, favorite_count, retweeted_status(id, favorite_count, retweet_count)

# make-train-data.py

Convert tweets in JSON format to ```__label__X text text tex text``` format as required by fastText.
