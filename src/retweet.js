import { TwitterApi } from 'twitter-api-v2';

// Instantiate with desired auth type (here's Bearer v2 auth)
const twitterClient = new TwitterApi({
  bearerToken: process.env.BEARER_TOKEN,
  appKey: process.env.CONSUMER_KEY,
  appSecret: process.env.CONSUMER_SECRET,
  accessToken: process.env.ACCESS_TOKEN,
  accessSecret: process.env.ACCESS_TOKEN_SECRET,
});

const me = '1581116917070561281'
const tweet_id = '1581422727080316928'

await twitterClient.v2.retweet(me, tweet_id);
