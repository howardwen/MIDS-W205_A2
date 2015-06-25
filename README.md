# MIDS-W205_A2

Bucket: howardwenw205assignment2

NBAFinals2015
https://s3-us-west-2.amazonaws.com/howardwenw205assignment2/%23NBAFinals2015.txt

Warriors
https://s3-us-west-2.amazonaws.com/howardwenw205assignment2/%23Warriors.txt

NBAFinals2015 and Warriors
https://s3-us-west-2.amazonaws.com/howardwenw205assignment2/%23NBAFinals2015_%23Warriors.txt


Step 1.
I downloaded the Twitter data (Using Twitter_Download.py) as Json files daily with chunking at 5000 tweets for the week between June 8, 2015 to June 14, 2015.

Step 2.
I extracted the tweets from the Json file (Using Encoding_To_Text.py) and added them to a .txt file

Step 3.
I processed each word in the Tweets (Using Text_Processing.py) using a stopword list with the addition of the following stop words ['.',',','\'','?',':','#','@','rt','http','!',"'s",'-',';']
Then I created a historgram of the 30 most common words.
