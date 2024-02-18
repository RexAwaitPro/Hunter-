from aiogram import*
bota = Bot('6781425105:AAGMvbpSiVbESmtbol3V575XKCO4yusgBaQ')
rex=Dispatcher(bota)

aprovedgrup = [-1001779694436]

@rex.message_handler(commands='start')
async def start(msg):
    if msg['chat']['id'] in aprovedgrup:await msg.reply('chat aprovado si puede usar')
    else: await msg.reply('reprovado no se puede usar')
    await msg.reply(msg['chat']['id'])



executor.start_polling(rex)
