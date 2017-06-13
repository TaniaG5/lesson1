from telegram.ext import Updater, CommandHandler

def start_bot(bot, updater):
	mytext = """Привет, пользователь!

	Я простой бот и понимаю только команду /start"""
	update.message.reply_text(mytext)

def main():
	updtr = Updater('398360932:AAGmxNaX95gS9sqaU-saK47Iqr19Pj9XZ48')

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))

	updtr.start_polling()
	updtr.idle()

if __name__== "__main__":
	main()

