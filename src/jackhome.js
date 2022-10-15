import { TwitterApi } from 'twitter-api-v2';

const jack_id = '12';

// Instantiate with desired auth type (here's Bearer v2 auth)
const twitterClient = new TwitterApi('*********************');

// Tell typescript it's a readonly app
const readOnlyClient = twitterClient.readOnly;

const jackTimeline = await readOnlyClient.v2.userTimeline(jack_id, {
    expansions: ['attachments.media_keys', 'attachments.poll_ids', 'referenced_tweets.id'],
    'media.fields': ['url'],
  });
  
  // jackTimeline.includes contains a TwitterV2IncludesHelper instance
  for await (const tweet of jackTimeline) {
    console.log(tweet.text);
  }

console.log(jackTimeline)