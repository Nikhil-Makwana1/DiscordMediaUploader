
<h1 align="center">Discord Media Uploader: Automated Mass File Uploading for Discord Server. </h1>
<p align="center">
  <img src="https://i.imgur.com/eei1wpA.png" alt="Logo" width="200">
</p>
<p align="center">
  <strong>Automatic Mass File Uploading to Discord Server.</strong>
</p>
<p align="center">
  <a href="#description">Description </a>
  ·
  <a href="#review">Review </a>
  ·
  <a href="#installation">Installation</a>
  ·
  <a href="#usage">Usage</a>
  ·
   <a href="#features">Features</a>
  ·
  <a href="#contributing">Contributing</a>
  ·
  <a href="#license">License</a>
</p>

## Description

Discord Media Uploader is a Python bot that automates the process of uploading files to your Discord server. It allows you to easily share media files, documents, and more with your server members without the need for manual interaction. 
Simply run the bot, and it will monitor a designated folder for new files and upload them to the server automatically. It saves you time and effort by streamlining the file-sharing process.

## Review

<p align="center">
  <img src="resource/gif1.gif">
  <img src="resource/gif2.gif">
</p>

## Installation

To use Discord Media Uploader, follow these steps:

1. Clone the repository or download the source code.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Obtain a Discord bot token. You can create a new bot and obtain the token from the Discord Developer Portal. [Tutorial](./bottutorial.md)
4. Configure the bot settings in the `config.py` file. Set the `TOKEN` variable to your Discord bot token.
5. Paste all your media files in the `media` folder.
5. Run the bot by executing the `DiscordMediaUploader.py` file using Python.
6. Type `!kaboom` in the Channel where you want to upload all your files

## Usage

1. Make sure the bot is running and connected to your Discord server.
2. Drop the files into the `media` folder.
3. The bot will automatically detect new files in the folder and upload them to the specified channel in your Discord server.
4. You can monitor the bot's activity through the console output or check the logs for a record of uploaded files.

## Features

1. **Automatic Mass File Uploading:** The bot automatically detects and uploads multiple files placed in the designated folder, allowing you to upload a large number of files to your Discord server effortlessly.
2. **Supports Various File Types:** Upload media files, documents, and more to your Discord server. The bot supports a wide range of file types, making it versatile for sharing different types of content.
3. **No Duplicate Upload:** The bot checks for duplicate files and ensures that files are not uploaded multiple times. This prevents clutter and helps maintain organization within your Discord server.
4. **Logging and Tracking:** Keep track of uploaded files through a log file for easy reference. The bot records information about each uploaded file, including the file name, upload timestamp, and the size of the file.
## Contributing

Contributions to Discord Media Uploader are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them thoroughly.
4. Commit your changes and push them to your forked repository.
5. Submit a pull request, explaining your changes and their benefits.

## License

This project is licensed under the [MIT License](LICENSE).

⭐️ Star the Repository: If you find this project useful, please consider giving it a star on GitHub to show your support. Thank you!