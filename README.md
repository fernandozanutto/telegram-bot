# Run local:

pip install -r requirements.txt
python main.py --local

# Deploy to Google Cloud Functions

gcloud functions deploy webhook --set-env-vars "BOT_TOKEN=YOUR_TOKEN_HERE" --runtime python312 --trigger-http

curl "https://api.telegram.org/bot<YOUR_TOKEN_HERE>/setWebhook?url=URL_RETURNED_FROM_PREVIOUS_COMMAND
