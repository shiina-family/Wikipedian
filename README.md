# Wikipedian

![eyecatch](./images/usage.jpg)

> Wikipedian is a Discord Bot that allows you to search Wikipedia in a better way

### **[✉️ Invite to your server](https://discord.com/api/oauth2/authorize?client_id=751430120962785360&permissions=84992&scope=bot)**

## Usage

### `/wiki <language code> <keywords>` or `/w`

Search an article that contains `keywords` from Wikipedia and send a message with an embed.

For example: `/w en lorem ipsum`, `/wiki ja ダミーテキスト`

### `/search <language code> <keywords>` or `/s`

Search for articles on Wikipedia by `keywords` and send them as a list with an embed.

For example: `/s en lorem ipsum`, `/search ja ダミーテキスト`

### `/random (<language code>)` or `/r`

Randomly send an article from Wikipedia with an embed. The default language code is "en". You can specify the language code as the other commands.

For example: `/random`, `/r ja`

### `/help`

Shows this help

## Required Permissions

- Read Messages
- Send Messages
- Embed Links
- Read Message History

## How it works

Wikipedian uses [Wikipedia API](https://pypi.org/project/wikipedia/) to send embeds with an article from Wikipedia. Send a search request to Wikipedia and format the returned data into an embed.

### NOTE

1. Due to some updates Embed is different looks from the picture.
2. This bot accepts all language codes available on Wikipedia, but it has been tested in English and Japanese only.
3. We have an issue. It's too slow response time. So we want to receive suggestions for code improvements.
4. We are not native English speakers, so we want you to suggestions for better translations.
