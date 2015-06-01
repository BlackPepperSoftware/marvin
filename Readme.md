Marvin
======
Marvin is a dockerised version of Slack's [python-rtmbot](https://github.com/slackhq/python-rtmbot) with a few silly plugins to provide a bit of fun to our Slack chats.

Prerequisites
-------------

1. A Slack account with a [bot user setup](https://api.slack.com/bot-users)
2. Docker
3. A love of Marvin Gaye

Installation
------------

1. Download the code

        git clone git@github.com:BlackPepperSoftware/marvin
        cd marvin

2. Specify the id of the slack channel you want Marvin to hang out in (Don't forget to invite Marvin to this channel, if it isn't your general channel)

        vi Dockerfile
          ENV MARVIN_SLACK_CHANNEL_ID=Cxxxxxxxx

3. Specify your Google API developer Key that Marvin can use to search Youtube

        vi Dockerfile
          ENV MARVIN_GOOGLE_API_KEY=Axxxxxxxxxxxxxxxxxxxxxxxxxx

3. Add your bot user's token to the rtmbot.conf

        vi rtmbot.conf
          SLACK_TOKEN: "xoxb-11111111111-222222222222222"

4. Build the docker container

        docker build -t blackpepper/marvin .

5. Bring Marvin to life!

        docker run blackpepper/marvin

Plugins
-------

Marvin has a couple of plugins configured, one for choosing an animal of the week, and one for playing music videos from youtube. It's worth noting that Marvin loves his own songs and will suggest a random Marvin Gaye track at every opportunity. He will play other songs if you request them directly though.

Both of the plugins are configured to only respond to direct messages or messages in our #random channel - you'll probably want to change the channel id if you use Marvin outside of BlackPepper

Note: If you add any more plugins, don't forget to add their python dependencies to plugins/requirements.txt

What's the point?
-----------------

Not much - he's just for fun really.
