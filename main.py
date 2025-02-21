import Constants as keys
from telegram.ext import *
import Responses as R
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

print("Bot avviato...")

def start_command(update: Update, context: CallbackContext) -> None:
    first_name = update.message.chat.first_name
    username = update.message.chat.username
    last_name = update.message.chat.last_name
    update.message.reply_text(f'''
    Ciao {first_name}!👋🏻\nSono lo SneakerSizeBot ,\naiuto il mio creatore (@antonio_colapietra su Instagram) a gestire le richieste dei clienti!✨
    \n \nPer avere l'elenco delle taglie\npremi qui --->\t /taglie
    ''')
    print("\n\n*************************************")
    print("chi sta usando il bot?")
    print(f"il nome è:\t{first_name}")
    print(f"il cognome è:\t{last_name}")
    print(f"lo username è:\t{username}")
    print("*************************************")


def closefriend_command(update, context):
    first_name = update.message.chat.first_name
    update.message.reply_text(f'''
       Ciao {first_name}, se sai di questo comando è perchè sei nei miei amici stretti su Instagram! Divertiti e spero che ti sia utile questo bot!\n \nSe trovi qualche errore avvisami ❤
       ''')
    update.message.reply_text("💫")


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    query.answer(f"Hai selezionato la taglia {query.data}")

    query.edit_message_text(text=f"Per verificare la disponibilità di questa taglia premi qui ---> /{query.data}")

def taglie_command(update: Update, context: CallbackContext) -> None:
    keyboard = [

        [   InlineKeyboardButton("36", callback_data='36'),
            InlineKeyboardButton("36.5", callback_data='365')
         ],
        [    InlineKeyboardButton("37.5", callback_data='375'),
            InlineKeyboardButton("38", callback_data='38')
        ],
        [
            InlineKeyboardButton("38.5", callback_data='385'),
            InlineKeyboardButton("39", callback_data='39')
        ],
        [   InlineKeyboardButton("40", callback_data='40'),
            InlineKeyboardButton("40.5", callback_data='405')
        ],
        [   InlineKeyboardButton("41", callback_data='41'),
            InlineKeyboardButton("42", callback_data='42')
        ],
        [   InlineKeyboardButton("42.5", callback_data='425'),
            InlineKeyboardButton("43", callback_data='43')
         ],
        [   InlineKeyboardButton("44", callback_data='44'),
             InlineKeyboardButton("44.5", callback_data='445')
         ],
        [   InlineKeyboardButton("45", callback_data='45'),
            InlineKeyboardButton("45.5", callback_data='455')
         ],
        [   InlineKeyboardButton("46", callback_data='46'),
            InlineKeyboardButton("47", callback_data='47')
         ],

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Scegli una taglia!💫', reply_markup=reply_markup)

def taglia_command(update, context):
    update.message.reply_text(
        f'Forse stavi cercando "/taglie"? \nNel caso premi qui ---> /taglie')


def aiuto_command(update, context):
    first_name = update.message.chat.first_name
    update.message.reply_text(f'''
    Ciao {first_name}!👋🏻\n \nPer verificare la disponibilità di una determinata taglia non devi fare altro che scrivere '/taglie' oppure la taglia che stai cercando preceduta dallo slash ( / ) !
    \n \nEsempi:\n \n/40---> per vedere la disponibilità della taglia 40\n \n/405---> per vedere la disponibiltà della taglia 40.5
    ''')








def trentasei_command(update, context):
    update.message.reply_text(f'Perfetto!\n\nHai selezionato la taglia 36, questi sono i vari modelli disponibili: \n')
    id = update.effective_chat.id

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD1391-002/nike-dunk-low-retro-medium-grey-varsity-red-2021-1-1000.png",
                          caption="Nike Dunk Low 'Varsity Grey'")
    update.message.reply_text(
        f'Questo è tutto! Se vuoi verificare la disponibilità di altre taglie\npremi qui ---> /taglie')


def trentaseiemezzo_command(update, context):
    update.message.reply_text(f'Perfetto!\n\nHai selezionato la taglia 36.5, questi sono i vari modelli disponibili: \n')
    id = update.effective_chat.id

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD1391-100/nike-dunk-low-retro-white-black-2021-1-1000.png",
                          caption="Nike Dunk Low 'Black-White'")
    update.message.reply_text(
        f'Questo è tutto! Se vuoi verificare la disponibilità di altre taglie\npremi qui ---> /taglie')


def trentasetteemezzo_command(update, context):
    update.message.reply_text(f'Perfetto!\n\nHai selezionato la taglia 37.5, questi sono i vari modelli disponibili: \n')
    id = update.effective_chat.id

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/554725-074/air-jordan-1-mid-banned-2020-gs-2-1000.png",
                          caption="Air Jordan 1 Mid 'Banned'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/554275-173%20-%20554725-173/air-jordan-1-mid-chicago-2020-gs-2-1000.png",
                          caption="Air Jordan 1 Mid 'Chicago 2021'")


    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD1391-002/nike-dunk-low-retro-medium-grey-varsity-red-2021-1-1000.png",
                          caption="Nike Dunk Low 'Varsity Grey'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD1503-102/nike-dunk-low-orange-pearl-2-1000.png",
                          caption="Nike Dunk Low 'Orange Pearl'")
    update.message.reply_text(f'Questo è tutto! Se vuoi verificare la disponibilità di altre taglie\npremi qui ---> /taglie')


def trentotto_command(update, context):
    update.message.reply_text(f'Perfetto!\n\nHai selezionato la taglia 38, questi sono i vari modelli disponibili: \n')
    id = update.effective_chat.id

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/554725-074/air-jordan-1-mid-banned-2020-gs-2-1000.png",
                          caption="Air Jordan 1 Mid 'Banned'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/554725-132/air-jordan-1-mid-igloo-island-green-gs-2-1000.png",
                          caption="Air Jordan 1 Mid 'Tropical Twist'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/554725-170/air-jordan-1-mid-white-university-gold-gs-2-1000.png",
                          caption="Air Jordan 1 Mid 'University Gold'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/BQ6472-500/air-jordan-1-mid-barely-rose-2-1000.png",
                          caption="Air Jordan 1 Mid 'Barely Rose'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/BQ6472-800/air-jordan-1-mid-barely-orange-w-2-1000.png",
                          caption="Air Jordan 1 Mid 'Guava Ice'")


    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/554725-069/air-jordan-1-mid-chicago-black-toe-gs-2-1000.png",
                          caption="Air Jordan 1 Mid 'Chicago 2020'")


    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DJ4695-122/air-jordan-1-mid-gym-red-black-white-gs-2-1000.png",
                          caption="Air Jordan 1 Mid 'Gym Red'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD1391-002/nike-dunk-low-retro-medium-grey-varsity-red-2021-1-1000.png",
                          caption="Nike Dunk Low 'Varsity Grey'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD1391-100/nike-dunk-low-retro-white-black-2021-1-1000.png",
                          caption="Nike Dunk Low 'Black-White'")
    update.message.reply_text(
        f'Questo è tutto! Se vuoi verificare la disponibilità di altre taglie\npremi qui ---> /taglie')


def trentottoemezzo_command(update, context):
    update.message.reply_text(f'Perfetto!\n\nHai selezionato la taglia 38.5, questi sono i vari modelli disponibili: \n')
    id = update.effective_chat.id

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/554725-074/air-jordan-1-mid-banned-2020-gs-2-1000.png",
                          caption="Air Jordan 1 Mid 'Banned'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/555112-105/air-jordan-1-mid-geometric-gs-1-1000.png",
                          caption="Air Jordan 1 Mid 'Geometric'")


    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/555112-103/air-jordan-1-mid-gs-white-light-arctic-pink-2-1000.png",
                          caption="Air Jordan 1 Mid 'Artic Pink'")


    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD2224-200/air-jordan-1-mid-se-particle-beige-2-1000.png",
                          caption="Air Jordan 1 Mid 'Particle Beige'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/CZ4385-016/air-jordan-1-mid-se-black-dark-beetroot-w-2-1000.png",
                          caption="Air Jordan 1 Mid 'Beetroot'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DJ4695-122/air-jordan-1-mid-gym-red-black-white-gs-2-1000.png",
                          caption="Air Jordan 1 Mid 'Gym Red'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/554724-140/air-jordan-1-mid-white-racer-blue-2-1000.png",
                          caption="Air Jordan 1 Mid 'Gym Blue'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/555088-105/air-jordan-1-retro-high-dark-mocha-2-1000.png",
                          caption="Air Jordan 1 High 'Mocha'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DB3610-105/air-jordan-1-zoom-air-cmft-psg-paris-saint-germain-2-1000.png",
                          caption="Air Jordan 1 High 'Paris Saint-Germain'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD1391-002/nike-dunk-low-retro-medium-grey-varsity-red-2021-1-1000.png",
                          caption="Nike Dunk Low 'Varsity Grey'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD1391-100/nike-dunk-low-retro-white-black-2021-1-1000.png",
                          caption="Nike Dunk Low 'Black-White'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD1399-100/nike-dunk-high-retro-white-vast-grey-2021-1-1000.png",
                          caption="Nike Dunk High 'Neutral Grey'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD1503-103/nike-dunk-low-photon-dust-w-2-1000.png",
                          caption="Nike Dunk Low 'Photon Dust'")
    update.message.reply_text(
        f'Questo è tutto! Se vuoi verificare la disponibilità di altre taglie\npremi qui ---> /taglie')


def trentanove_command(update, context):
    update.message.reply_text(f'Perfetto!\n\nHai selezionato la taglia 39, questi sono i vari modelli disponibili: \n')
    id = update.effective_chat.id

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/554725-074/air-jordan-1-mid-banned-2020-gs-2-1000.png",
                          caption="Air Jordan 1 Mid 'Banned'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/555112-105/air-jordan-1-mid-geometric-gs-1-1000.png",
                          caption="Air Jordan 1 Mid 'Geometric'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/BQ6472-800/air-jordan-1-mid-barely-orange-w-2-1000.png",
                          caption="Air Jordan 1 Mid 'Guava Ice'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/554725-133/air-jordan-1-mid-crimson-tint-gs-2-1000.png",
                          caption="Air Jordan 1 Mid 'Crimson Tint'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/554725-084/air-jordan-1-mid-gs-black-racer-blue-2-1000.png",
                          caption="Air Jordan 1 Mid 'Racer Blue'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DJ4695-122/air-jordan-1-mid-gym-red-black-white-gs-2-1000.png",
                          caption="Air Jordan 1 Mid 'Gym Red'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/CD0461-002/air-jordan-1-high-og-seafoam-w-2-1000.png",
                          caption="Air Jordan 1 High 'Sea Foam White'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD1391-002/nike-dunk-low-retro-medium-grey-varsity-red-2021-1-1000.png",
                          caption="Nike Dunk Low 'Varsity Grey'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD1503-102/nike-dunk-low-orange-pearl-2-1000.png",
                          caption="Nike Dunk Low 'Orange Pearl'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD1391-100/nike-dunk-low-retro-white-black-2021-1-1000.png",
                          caption="Nike Dunk Low 'Black-White'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD1399-101/nike-dunk-high-syracuse-2021-2-1000.png",
                          caption="Nike Dunk High 'Orange'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD1503-100/nike-dunk-low-coast-1-1000.png",
                          caption="Nike Dunk Low 'Coast'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DC7770-160/air-jordan-4-retro-fire-red-2020-2-1000.png",
                          caption="Air Jordan 4 Retro 'Fire Red'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/408452-700/air-jordan-4-lightning-2021-gs-2-1000.png",
                          caption="Air Jordan 4 Retro 'Lightning'")
    update.message.reply_text(
        f'Questo è tutto! Se vuoi verificare la disponibilità di altre taglie\npremi qui ---> /taglie')


def quaranta_command(update,context):
    update.message.reply_text(f'Perfetto!\n\nHai selezionato la taglia 40, questi sono i vari modelli disponibili: \n')
    id = update.effective_chat.id

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DJ4695-122/air-jordan-1-mid-gym-red-black-white-gs-2-1000.png", caption="Air Jordan 1 Mid 'Gym Red'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/554725-074/air-jordan-1-mid-banned-2020-gs-2-1000.png",
                          caption="Air Jordan 1 Mid 'Banned'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/555112-103/air-jordan-1-mid-gs-white-light-arctic-pink-2-1000.png",
                          caption="Air Jordan 1 Mid 'Artic Pink'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/555088-500/air-jordan-1-retro-high-court-purple-white-2-1000.png",
                          caption="Air Jordan 1 High 'Court Purple'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD1391-002/nike-dunk-low-retro-medium-grey-varsity-red-2021-1-1000.png",
                          caption="Nike Dunk Low 'Varsity Grey'")

    context.bot.sendPhoto(chat_id=id, photo=
    "http://cdn.shopify.com/s/files/1/0451/4935/6195/products/nike-dunk-high-sp-varsity-maize-2-1000_1200x1200.png?v=1609886991",
                          caption="Nike Dunk High 'Varsity Maize'")
    update.message.reply_text(
        f'Questo è tutto! Se vuoi verificare la disponibilità di altre taglie\npremi qui ---> /taglie')


def quarantaemezzo_command(update, context):
    update.message.reply_text(f'Perfetto!\n\nHai selezionato la taglia 40.5, questi sono i vari modelli disponibili: \n')
    id = update.effective_chat.id

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/555088-118/air-jordan-1-retro-high-white-black-volt-university-gold-2-1000.png",
                          caption="Air Jordan 1 High 'Volt'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/555088-500/air-jordan-1-retro-high-court-purple-white-2-1000.png",
                          caption="Air Jordan 1 High 'Court Purple'")
    update.message.reply_text(
        f'Questo è tutto! Se vuoi verificare la disponibilità di altre taglie\npremi qui ---> /taglie')


def quarantuno_command(update, context):
    update.message.reply_text(f'Perfetto!\n\nHai selezionato la taglia 41, questi sono i vari modelli disponibili: \n')
    id = update.effective_chat.id

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD2224-200/air-jordan-1-mid-se-particle-beige-2-1000.png",
                          caption="Air Jordan 1 Mid 'Particle Beige'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DB3610-105/air-jordan-1-zoom-air-cmft-psg-paris-saint-germain-2-1000.png",
                          caption="Air Jordan 1 High 'Paris Saint German'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/555088-134/air-jordan-1-retro-high-white-university-blue-black-2-1000.png",
                          caption="Air Jordan 1 High 'University Blue UNC'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/555088-500/air-jordan-1-retro-high-court-purple-white-2-1000.png",
                          caption="Air Jordan 1 High 'Court Purple'")
    update.message.reply_text(
        f'Questo è tutto! Se vuoi verificare la disponibilità di altre taglie\npremi qui ---> /taglie')


def quarantadue_command(update, context):
    update.message.reply_text(f'Perfetto!\n\nHai selezionato la taglia 42, questi sono i vari modelli disponibili: \n')
    id = update.effective_chat.id

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DH4268-001/air-jordan-1-high-zoom-air-cmft-london-2-1000.png",
                          caption="Air Jordan 1 High 'London'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD6834-402/air-jordan-1-mid-se-signal-blue-dd6834-402-2-1000.png",
                          caption="Air Jordan 1 Mid 'Signal BLue'")
    update.message.reply_text(
        f'Questo è tutto! Se vuoi verificare la disponibilità di altre taglie\npremi qui ---> /taglie')


def quarantadueemezzo_command(update, context):
    update.message.reply_text(f'Perfetto!\n\nHai selezionato la taglia 42.5, questi sono i vari modelli disponibili: \n')
    id = update.effective_chat.id

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DB3610-105/air-jordan-1-zoom-air-cmft-psg-paris-saint-germain-2-1000.png",
                          caption="Air Jordan 1 High 'Paris Saint-Germain'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/CT0978-300/air-jordan-1-high-zoom-cmft-stadium-green-2-1000.png",
                          caption="Air Jordan 1 High 'Stadium Green'")
    update.message.reply_text(
        f'Questo è tutto! Se vuoi verificare la disponibilità di altre taglie\npremi qui ---> /taglie')


def quarantatre_command(update, context):
    update.message.reply_text(f'Perfetto!\n\nHai selezionato la taglia 43, questi sono i vari modelli disponibili: \n')
    id = update.effective_chat.id

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/555088-402/air-jordan-1-retro-high-hyper-royal-smoke-grey-2-1000.png",
                          caption="Air Jordan 1 High 'Hyper Royal'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DD1391-100/nike-dunk-low-retro-white-black-2021-1-1000.png",
                          caption="Nike Dunk 'Black-White'")
    update.message.reply_text(
        f'Questo è tutto! Se vuoi verificare la disponibilità di altre taglie\npremi qui ---> /taglie')


def quarantaquattro_command(update, context):
    update.message.reply_text(f'Perfetto!\n\nHai selezionato la taglia 44, questi sono i vari modelli disponibili: \n')
    id = update.effective_chat.id

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/AO9944-441/air-jordan-1-low-unc-w-1-1000.png",
                          caption="Air Jordan 1 Low 'UNC'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/555088-105/air-jordan-1-retro-high-dark-mocha-2-1000.png",
                          caption="Air Jordan 1 High 'Mocha'")

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DB3610-105/air-jordan-1-zoom-air-cmft-psg-paris-saint-germain-2-1000.png",
                          caption="Air Jordan 1 High 'Paris Saint-Germain'")

    update.message.reply_text(
        f'Questo è tutto! Se vuoi verificare la disponibilità di altre taglie\npremi qui ---> /taglie')


def quarantaquattroemezzo_command(update, context):
    update.message.reply_text(f'Perfetto!\n\nHai selezionato la taglia 44.5, questi sono i vari modelli disponibili: \n')
    id = update.effective_chat.id

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/163862C/chuck-70-off-white-hi-163862c-white-cone-black-2-1000.png",
                          caption="Converse x Off-White Chuck Taylor")
    update.message.reply_text(
        f'Questo è tutto! Se vuoi verificare la disponibilità di altre taglie\npremi qui ---> /taglie')


def quarantacinque_command(update, context):
    update.message.reply_text(f'Purtroppo non è disponibile nessun modello di taglia 45.\n \nPer selezionare altre taglie\npremi qui --->\t /taglie')


def quarantacinqueemezzo_command(update, context):
    update.message.reply_text(f'Perfetto!\n\nHai selezionato la taglia 45.5, questi sono i vari modelli disponibili: \n')
    id = update.effective_chat.id

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/DA3595-100/air-jordan-3-retro-fragment-2-1000.png",
                          caption="Air Jordan 3 x Fragment")
    update.message.reply_text(
        f'Questo è tutto! Se vuoi verificare la disponibilità di altre taglie\npremi qui ---> /taglie')


def quarantasei_command(update, context):
    update.message.reply_text(f'Perfetto!\n\nHai selezionato la taglia 46, questi sono i vari modelli disponibili: \n')
    id = update.effective_chat.id

    context.bot.sendPhoto(chat_id=id, photo=
    "https://images.restocks.net/products/CU9225-100/nike-air-force-1-low-supreme-box-logo-white-2-1000.png",
                          caption="Air Force 1 x Supreme")
    update.message.reply_text(
        f'Questo è tutto! Se vuoi verificare la disponibilità di altre taglie\npremi qui ---> /taglie')


def quarantasette_command(update, context):
    update.message.reply_text(f'Purtroppo non è disponibile nessun modello di taglia 47.\n \nPer selezionare altre taglie\npremi qui --->\t /taglie')











def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("aiuto", aiuto_command))
    dp.add_handler(CommandHandler("amore", amore_command))
    dp.add_handler(CommandHandler("amicistretti", closefriend_command))
    dp.add_handler(CommandHandler("36", trentasei_command))
    dp.add_handler(CommandHandler("365", trentaseiemezzo_command))
    dp.add_handler(CommandHandler("375", trentasetteemezzo_command))
    dp.add_handler(CommandHandler("38", trentotto_command))
    dp.add_handler(CommandHandler("385", trentottoemezzo_command))
    dp.add_handler(CommandHandler("39", trentanove_command))
    dp.add_handler(CommandHandler("40", quaranta_command))
    dp.add_handler(CommandHandler("405", quarantaemezzo_command))
    dp.add_handler(CommandHandler("405", quarantaemezzo_command))
    dp.add_handler(CommandHandler("41", quarantuno_command))
    dp.add_handler(CommandHandler("42", quarantadue_command))
    dp.add_handler(CommandHandler("425", quarantadueemezzo_command))
    dp.add_handler(CommandHandler("43", quarantatre_command))
    dp.add_handler(CommandHandler("44", quarantaquattro_command))
    dp.add_handler(CommandHandler("445", quarantaquattroemezzo_command))
    dp.add_handler(CommandHandler("45", quarantacinque_command))
    dp.add_handler(CommandHandler("455", quarantacinqueemezzo_command))
    dp.add_handler(CommandHandler("46", quarantasei_command))
    dp.add_handler(CommandHandler("47", quarantasette_command))
    dp.add_handler(CommandHandler("taglie", taglie_command))
    dp.add_handler(CommandHandler("taglia", taglia_command))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.text, handle_message))


    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
