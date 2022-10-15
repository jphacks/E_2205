import { TwitterApi } from 'twitter-api-v2';

// Instantiate with desired auth type (here's Bearer v2 auth)
const twitterClient = new TwitterApi({
  bearerToken: process.env.BEARER_TOKEN,
  appKey: process.env.CONSUMER_KEY,
  appSecret: process.env.CONSUMER_SECRET,
  accessToken: process.env.ACCESS_TOKEN,
  accessSecret: process.env.ACCESS_TOKEN_SECRET,
});

const homeTimeline = await twitterClient.v2.homeTimeline({ exclude: 'replies' })

  for await (const tweet of homeTimeline) {
    console.log(tweet.text);
  }