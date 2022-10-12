# BulkDownloadDiscordMessages
download up to all the messages from a discord server

the program requires three arguments run with

`python download.py most_recent_msg_id channel_id auth_code how_many`

you can obtain `auth_code` by doing inspect element on discord in the browser (or client), going to network, finding the `messages` packet, and getting `authorization` value in the header

![how to get your discord authorization code](https://raw.githubusercontent.com/spencerhhubert/BulkDownloadDiscordMessages/main/assets/how_get_auth_code.jpg)

you can get the `most_recent_msg_id` by right clicking a message and doing "Copy ID"

you can get `channel_id` from the last section of the url if you open your desired discord server in the browser

![how to get the channel id of a discord server](https://raw.githubusercontent.com/spencerhhubert/BulkDownloadDiscordMessages/main/assets/get_channel_id.jpg)

`how_many` is just an int for how many messages you want to download from before `most_recent_msg_id`