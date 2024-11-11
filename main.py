from telegram.ext import Application 

def main(): 
    """
    Handles the inirial launch of the promra (entry point).
    """

    token = ""
    Application = Application.builder().token(token).concurrent_updates(True).read_timeout(30).write_timeout(30).build()
    print("Telegram Bot started!", flush=True)
    Application.run_polling()

    if __name__ == "__main__":
        main()