# bitcoindesigned-infographics-i18n
Translation files for bitcoindesigned's infographics for easy contribution.

The goal of this repository is to create an organized and crowdsourced manner to translate the infographics from [bitcoindesigned](https://www.bitcoindesigned.com/ "bitcoindesigned") into many different languages and, therefore, be able to impact many more people.

This document will explain how to contribute and what to expect from this initiative.

## General process
The infographics are all graphic files in .ai format that need to be updated by hand for every new translation, since even a small difference in the length of the text might affect the size and positioning of other elements around it. Because of that, the translation will be done to the separate text files with the infographic content (using the .pot files in English as sources).

Every 2 weeks (or less if we have the availability), the new translations will be added to the infographics by the bitcoindesigned team and those translations will be published in a list of available languages for the respectives infographics. [See the example here](https://www.bitcoindesigned.com/infographics/what-does-it-really-mean-to-have-bitcoins/), where the links to different languages are displayed at the end of the page.

## Project organization
The project is organized with one folder for each infographic. The folders are named to match the slug you find in the page where the infographic is published at bitcoindesigned.com. For example:

URL: https://www.bitcoindesigned.com/infographics/what-is-bitcoin-the-currency/
Folder name: what-is-bitcoin-the-currency

Inside each infographic folder you'll find:
* The source-text.txt file, which is the original content file.
* The source-text.txt.pot file, which is the template you will use to create your translation.
* The translations that have been made to that infographic as .po files with the name corresponding to the language code (pt.po for Portuguese, fr.po for French, etc).
* The compiled translation files (.mo).

## Translation guidelines
When creating a translation for an infographic, there are some important things to keep in mind:
* Please keep the text formatting you see in the source (such as all caps, quotes, parenthesis, etc) - as long as they exist in the language, of course. That's because you might be translating to a language that I can't understand a single thing, so I must have these clues to adapt the text correctly.
* The text usually has a very limited space to be displayed, so try to make it as short as possible without jeopardizing the message. As a rule of thumb, keep it in a similar length to the original version.
* The tone of the infographics is very conversational to keep it simple for people to understand it. But do avoid very local expressions and slangs.
* Focus on the message and not necessarily on translating every word. You might want to keep the actual infographic next to you to give you more context.

## Contributing with Git

1. Clone this repository.
2. Fork a branch from master naming it with the infographic's slug with a language code (e.g. what-is-bitcoin-the-currency-en_UK)
3. Open the .pot template file using a proper application (such as [Poedit](https://poedit.net/download)) and create a new translation file (.po) for the language you'll be translating to (for example, the file pt.po will be created for a Portuguese translation) in the same directory as the source file or just open an existing .po file in case your contribution is improving an existing translation.
4. Pull request.

## Contributing without Git
If you don't use Git and still want to contribute, you're also very welcome. Here's how you can work on the translations:

1. In the right side of this page, near the top, find the green 'Clone or download' button, click it and choose 'Download Zip' (make sure the branch drop-down menu is on "master").
2. Open the .zip file and go into the folder of the infographic you wish to translate.
3. Open the .pot template file using a proper application (such as [Poedit](https://poedit.net/download)) and create a new translation file (.po) for the language you'll be translating to (for example, the file pt.po will be created for a Portuguese translation) or just open an existing .po file in case your contribution is improving an existing translation.
4. When finished with the file, send it to the e-mail btctranslations@patestevao.com. You can send it directly or via a link to a cloud drive service.

## Adding yourself as a translator
At the end of each infographic source file, there is an entry for a translator name, as follows:
```
Translator: [Your name/handle or "Crowdsourced translation"]
```

This is where, if you desire, you should entry your name or the preferred handle to appear in the infographic and identify you as a contributor.
If you prefer to keep your contribution private, just add the equivalent of "Crowdsourced translation" in your language.

So there are the two possible outputs for this entry.

Translator chose to put his name/handle:
```
Translator: Alice Bob
```

Translator prefers not to put his name/handle:
```
Translator: Crowdsourced translation
```

## License
You can find the license of this repository and all its files in the file "LICENSE.md" or [here](https://creativecommons.org/licenses/by-sa/4.0/). You agree that any contributions and translations made to this projects will be licensed under the same terms.