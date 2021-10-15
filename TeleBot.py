import telegram


bot = telegram.Bot(token = "1822189493:AAEI77_kfaWMbDE0S3pqLGdavBaoz_q2Wck")
chat_id = 1928384776

bot.sendMessage(chat_id = chat_id, text = 'aa')
# for i in bot.getUpdates():
#     print(i.message)