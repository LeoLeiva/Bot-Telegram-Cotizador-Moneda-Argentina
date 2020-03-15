#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import requests

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Hola! Por favor selecciona la moneda")
    update.message.reply_text("Dolar oficial /dolar")
    update.message.reply_text("Dolar blue /dolarblue")
    update.message.reply_text("Euro oficial /euro")
    update.message.reply_text("Euro blue /euroblue")
    update.message.reply_text("Para volver a ver este menu simplemente toca en /start")


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def dolar(update, content):
    r = requests.get('http://api.bluelytics.com.ar/v2/latest').json()

    oficompra = float(r["oficial"]['value_buy'])
    coficompra = '%.2f' %oficompra
    ofiventa = float(r["oficial"]['value_sell'])
    cofiventa = '%.2f' %ofiventa
    soli = float(ofiventa + (ofiventa*0.3))
    csoli = '%.2f' %soli
    timeupdate = str(r["last_update"])

    update.message.reply_text("U$S Oficial Compra      | " + str(coficompra))
    update.message.reply_text("U$S Oficial Venta       | " + str(cofiventa))
    update.message.reply_text("U$S Oficial C/Imp. Pais | " + str(csoli))
    update.message.reply_text("Ultima Actualizacion: " + timeupdate[:10] + " | Hora: " + timeupdate[11:19])


def dolarblue(update, content):
    r = requests.get('http://api.bluelytics.com.ar/v2/latest').json()

    bluecompra = float(r["blue"]['value_buy'])
    cbluecompra = '%.2f' %bluecompra
    blueventa = float(r["blue"]['value_sell'])
    cblueventa= '%.2f' %blueventa
    timeupdate = str(r["last_update"])

    update.message.reply_text("U$S Blue Compra      | " + str(cbluecompra))
    update.message.reply_text("U$S Blue Venta       | " + str(cblueventa))
    update.message.reply_text("Ultima Actualizacion: " + timeupdate[:10] + " | Hora: " + timeupdate[11:19])


def euro(update, content):
    r = requests.get('http://api.bluelytics.com.ar/v2/latest').json()

    eoficompra = float(r["oficial_euro"]['value_buy'])
    ceoficompra = '%.2f' %eoficompra
    eofiventa = float(r["oficial_euro"]['value_sell'])
    ceofiventa = '%.2f' %eofiventa
    esoli = float(eofiventa + (eofiventa*0.3))
    cesoli = '%.2f' %esoli
    timeupdate = str(r["last_update"])

    update.message.reply_text("Euro Oficial Compra      | " + str(ceoficompra))
    update.message.reply_text("Euro Oficial Venta       | " + str(ceofiventa))
    update.message.reply_text("Euro Oficial C/Imp. Pais | " + str(cesoli))
    update.message.reply_text("Ultima Actualizacion: " + timeupdate[:10] + " | Hora: " + timeupdate[11:19])


def euroblue(update, content):
    r = requests.get('http://api.bluelytics.com.ar/v2/latest').json()

    ebluecompra = float(r["blue_euro"]['value_buy'])
    cebluecompra = '%.2f' %ebluecompra
    eblueventa = float(r["blue_euro"]['value_sell'])
    ceblueventa = '%.2f' %eblueventa
    timeupdate = str(r["last_update"])

    update.message.reply_text("Euro Blue Compra      | " + str(cebluecompra))
    update.message.reply_text("Euro Blue Venta       | " + str(ceblueventa))
    update.message.reply_text("Ultima Actualizacion: " + timeupdate[:10] + " | Hora: " + timeupdate[11:19])


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1110773023:AAHuxnjeO_XzAc-n_6JZtSRDn4W7FtmoAZ8", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("dolar", dolar))
    dp.add_handler(CommandHandler("dolarblue", dolarblue))
    dp.add_handler(CommandHandler("euro", euro))
    dp.add_handler(CommandHandler("euroblue", euroblue))

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