# cloudcache
A simple way to save your large files to discord to be downloaded later

## Features

- **File Upload**: Users can upload large files in chunks to the Discord server.
- **File Download**: Users can download files previously uploaded using file IDs.
- **Chunked Uploads**: Large files are uploaded in smaller chunks to avoid Discord file size limits.

## Prerequisites

- Python 3.6+
- Discord.py
- requests

## Installation

1. Clone this repository:

```
git clone https://github.com/nroggendorff/cloudcache.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Set up a Discord bot and obtain the bot token.

4. Set the `TOKEN` variable in the script to your bot token.

5. Set the guild and channel id respectively.

## Usage

1. Invite the bot to your Discord server.

2. Use the `!upload` command followed by the file path to upload a file:

```
!upload /path/to/your/file.txt
```

3. The bot will upload the file in chunks and provide a unique file ID upon completion.

4. To download a file, use the `!download` command followed by the file ID provided by the bot:

```
!download your_file_id
```

5. The bot will download and assemble the file parts and save it with its original name.

## Notes

- This bot is designed for educational purposes and may need additional error handling for production use.
- Ensure that the bot has appropriate permissions to read/write files and send messages in the Discord channel.

## Contributors

- [nroggendorff](https://huggingface.co/nroggendorff)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
