# Introduction

THe objective of this bot is (at least for now) to just convert an image to the size and format required by @Sticker bot


# Use @BotFather to get a Token

https://core.telegram.org/bots/tutorial#obtain-your-bot-token

# Run local:

1. `pip install -r requirements.txt`

2. Either add your Token to your environment variables or replace line 15 of main.py with your Token

3. `python main.py --local`

# Deploy to Google Cloud Functions

1. Install Google Cloud CLI - https://cloud.google.com/sdk/docs/install

2. `gcloud functions deploy webhook --set-env-vars "BOT_TOKEN=<YOUR_TOKEN_HERE>" --runtime python312 --trigger-http`

3. `curl "https://api.telegram.org/bot<YOUR_TOKEN_HERE>/setWebhook?url=URL_RETURNED_FROM_PREVIOUS_COMMAND`

# Bot in Action

![image](https://github.com/fernandozanutto/telegram-bot/assets/15229294/771ff7be-0754-4b31-96eb-63d7f0873ef1)

