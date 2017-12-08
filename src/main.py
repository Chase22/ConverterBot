#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Encoding Regex: (\d\.?\d?)+( ?[^0-9|\s]*)

"""Simple Bot to reply to Telegram messages.

This program is dedicated to the public domain under the CC0 license.

This Bot uses the Updater class to handle the bot.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from appconfig import AppConfig
from converter import Converter
import logging, pint, re

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

#Compile Regex
regexString = "^(\d+\.?\d*)(\S*)"
regex = re.compile(regexString)

#get Unitregistry
ureg = pint.UnitRegistry();

#get Converter
converter = Converter()


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def convert(bot, update):
    counter = 0
    
    message = update.message.reply_to_message
    text = message.text
    parts = list(text.split(' '))
    endmsg = list()

    i = 0
    while i < len(parts):
        string = parts[i]
        i += 1
        if string[0].isdigit():
            result = regex.match(string)
            token = list(result.group(1,2))
            
            #endmsg.append('{{{}}}'.format(counter))
            counter += 1
            if not token[1]:
                token [1] = parts[i]
                i += 1
            print(token)
            try:
                measurement = ureg((token[0]+'*'+token[1]).lower())
                measurement = converter.convert(measurement)
                endmsg.append('{:.02fP}'.format(measurement))
            except pint.UndefinedUnitError:
                print ('Unit not defined')
        else:
            endmsg.append(string)
    
    msgString = ' '.join(endmsg)
    
    update.message.reply_text(msgString)
    print(msgString)
    return


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    #load the config
    config = AppConfig()
    
    print('start')
    
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    print(config.config['Telegram']['key'])
    updater = Updater(config.config['Telegram']['key'])

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("convert", convert))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, convert))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

