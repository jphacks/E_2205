import { TwitterApi } from 'twitter-api-v2';

// Instantiate with desired auth type (here's Bearer v2 auth)
const twitterClient = new TwitterApi({
  bearerToken: '*',
  appKey: '*',
  appSecret: '*',
  accessToken: '*',
  accessSecret: '*',
});

const homeTimeline = await twitterClient.v2.homeTimeline({ exclude: 'replies' })

  for await (const tweet of homeTimeline) {
    console.log(tweet.text);
  }