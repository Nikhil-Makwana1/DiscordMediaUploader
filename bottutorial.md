
# Discord Bot Creation and Adding it to Your Server


## Step 1: Creating a Discord Application
1. Visit the **[Discord Developer Portal](https://discord.com/developers/applications)** and log in with your Discord account.
2. Click on the `New Application` button to create a new application for your bot.
3. Enter a catchy name for your application and click `Create`.

## Step 2: Creating a Bot for Your Application
1. In the left sidebar, navigate to the **Bot** section under **Settings**.
2. Click on the `Add Bot` button to bring your application to life!
3. Under the **Token** section, click on the `Copy` button to save your bot token securely.

## Step 3: Empowering Your Bot with Required Intents
1. Still in the **Bot** section, scroll down to the **Privileged Gateway Intents** area.
2. Enable the following powerful intents:
   - ☑️ Server Members Intent
   - ☑️ Message Content Intent
   > Note: These intents may require verification for bots in 100 or more servers.

## Step 4: Configuring Bot Permissions
1. Explore the **OAuth2** section in the left sidebar, under **Settings**.
2. Scroll down to the **Scopes** area and select the `bot` checkbox.
3. Delve into the **Bot Permissions** section and choose the permissions your bot needs. Make sure to include the **Attach Files** permission for uploading attachments.
4. Voilà! A unique URL will be generated. Copy this URL for the next step.

## Step 5: Inviting Your Bot to Your Server
1. Open a new browser tab and paste the copied URL. This will whisk you away to a page where you can integrate your bot into your server.
2. Select the desired server where you want to unleash your bot's potential, then click **"Authorize"**. Complete any additional verification steps if prompted.

> Remember: Treat your bot token like a secret artifact! Safeguard it from prying eyes and avoid sharing it publicly or committing it to public repositories.
