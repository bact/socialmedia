# Collection

* We collect tweets in Thai language between 9 October 2016 to XX October 2016.
* This is done by using Twitter's Stream API to select tweets with a language 'th' and has one of common Thai words.
* Thai common words list comprise of 53 words.
* Fifty drawn from Chulalongkorn University's 400 most used Thai words.
* Another three words ("less", "down", "receive") were added to balanced the "direction" of the words ("more", "up", "give" are already in the top 50)

# Plan

* Check if it's a retweet or not
  * If it is a retweet, does it has an additional text (check id_str)
* Have to get the full tweet, no truncation
  * Check truncated=True
* Keep these attributes: id, retweet_count, favorite_count, retweeted_status(id, favorite_count, retweet_count)


Missing counts
In very rare cases the Streaming API may elect to deliver an incomplete Tweet field instead of waiting for data which is taking a long time to fetch. In the case of a numeric count, this will manifest as a -1 value. If you happen to see any counts with values of -1, use the REST API to backfill accurate values as needed.
