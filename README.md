# Htonia

Example of serverless python (v3) telegram bot (updates via webhook).

## Requires
 - Pre-configured telegram bot account;
 - Account at now.sh and it's tools

        npm i -g now

## How to
1. Create local ```cfg.py``` in project directory with your bot token (```TOKEN```);
2. ```now``` (gives you public url for next steps);
3. Enable webhooks for bot. (```HTTP POST``` to ```https://api.telegram.org/bot{your_bot_token}/setWebhook?url={url_to_send_updates_to}```);
3. Enable webhook in GitLab -> Project -> Settings -> Integrations ```{url_to_send_updates_to}/gitlab``` (got it from step 2); Do not forget to set secret token (```SECRET_TOKEN```) both in GitLab integrations and cfg.py;
4. Write something to bot, it should reply with chat_id needed for cfg.py;
5. Set ```CHAT_ID``` in cfg.py to numeric value from previous step;
4. Profit. You can test event notification in same Integrations menu.

Don't forget to edit metadata in now.json and package.json


