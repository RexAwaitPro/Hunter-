import requests
from bs4 import BeautifulSoup
from aiogram import *
import time

rex = Dispatcher(Bot('6873040140:AAH9lhEr2yGv8Fmt3GsDhClRevR38EGl5d4'))

def cmdshead(dev):
    return rex.message_handler(commands=dev)

def cloud(url):
    response = requests.get(url)
    if 'cf-ray' in response.headers:
        return True
    else:
        return False
    
def googleQuery(busqueda):
    sec = requests.Session()
    req = sec.get(f"https://www.google.com/search?q={busqueda}&start={10}").text
    soupUrl = BeautifulSoup(req, 'html.parser').find_all('a', href=True)
    return soupUrl


@cmdshead('start')
async def start(message):
    await message.reply(f'''<b>[•] {message['from']['first_name']}

[•] Interractua con el bot preciona <code>/cmds</code> y mira la lista de comandos.
    
━━━━━━━━━
[•] ⇾ create : @RexAwait                        
[•] ⇾ The 𝗪𝗼𝗿𝗹𝗱𝘀 of 𝗔𝗽𝗶𝘀
[•] ⇾ @TheWorldsOfApis
━━━━━━━━━</b>''')

@cmdshead('cmds')
async def start(msg):
    await msg.reply(f'''<b>[•] Comandos Bot acceso

[•] ⇾ Free comandos: <code>/id</code> | <code>/start</code> | <code>/cmds</code> 
[•] ⇾ Premium comandos: <code>/GoogleQuery</code> 

━━━━━━━━━
[•] ⇾ The 𝗪𝗼𝗿𝗹𝗱𝘀 of 𝗔𝗽𝗶𝘀
[•] ⇾ @TheWorldsOfApis
━━━━━━━━━
    </b>''')


@cmdshead('googleQuery')
async def start(msg):
    with open('grupos.txt', mode='r+', encoding='utf-8') as archivo:
        xq = archivo.readlines()
        if str(msg['chat']['id']) + '\n' in xq:
            palaclave = msg.text[len('/googleQuery '):]
            if not palaclave : return await msg.reply('<code>/googleQuery dorks</code> - falto la dorks')
        
            msg1 = await msg.reply('<code>❗️ Iniciando busquedas.. ❗️</code>')
            urls = []
            for link in googleQuery(palaclave):
                url = link['href']
                if url.startswith('/url?q='):
                    url = url[7:].split('&')[0]
                    if 'google' not in url and url not in urls:
                        urls.append(url)

            messag = ""
            messag += f"<b>[•] Hunts Dorks  ✅\n\n[•] Id user : <code>{msg['from']['id']}</code>\n[•] UserName: <code>{msg['from']['username']}</code>\n[•]Dorks: <code>{palaclave}</code>\n[•]   ━━ Resultado  ━━ [•]</b>"
            
            for url in urls:
                    if cloud(url):
                        messag += f"<b>\n\n[•] Url : <code>{url} </code>- Cloudflare ✅</b>"
                        time.sleep(1.5)
                        await msg1.edit_text(messag)
                    else:
                        messag += f"<b>\n\n[•] Url : <code>{url} </code></b>"
                        time.sleep(1)
                        await msg1.edit_text(messag)
            monton = len(urls)
            if monton == 0 :
                messag += f'''<b>\n\n[•] Response : Failure ❌
[•] No se han encontrado  urls 
[•] Prueba diferentes palabras clave.
[•] Dorks dead ‼️
           
[•] {msg['from']['first_name']}
━━━━━━━━━
[•] ⇾ The 𝗪𝗼𝗿𝗹𝗱𝘀 of 𝗔𝗽𝗶𝘀
[•] ⇾ @TheWorldsOfApis
━━━━━━━━━</b>'''
                await msg1.edit_text(messag)
            else:
                messag += f'''<b>\n\n[•] Monton : <code>{monton}</code>\n[•] {msg['from']['first_name']}
━━━━━━━━━
[•] ⇾ The 𝗪𝗼𝗿𝗹𝗱𝘀 of 𝗔𝗽𝗶𝘀
[•] ⇾ @TheWorldsOfApis
━━━━━━━━━</b>'''
                await msg1.edit_text(messag)
        else: return await msg.reply('<b> Chat no authorizado consulta con mi creador <code>RexAwait (max)</code> para liberarlo.</b>')


@cmdshead('id')
async def start(msg):
    await msg.reply(f"<b>[•] ⇾ id User: <code>{msg['from']['id']}</code>\n[•] ⇾ id chat: <code>{msg['chat']['id']}</code></b>")

@cmdshead('lista')
async def start(msg):
    if msg['from']['id'] == 6411167257:
        with open('grupos.txt', mode='r+', encoding='utf-8') as archivo:
            x = archivo.readlines()
        ass = await msg.reply('<b>Hi señor Max. </b>')
        time.sleep(1.5)
        ss = ""
        ss += ' <b>Users id access bot :\n\n</b>'
        for s in x:
            ss += f'<b>[•] <code>{s} </code></b>'
            await ass.edit_text(ss)
        mm = len(x)
        ss += f'''<b>\n[•] Monton ⇾ <code>{mm}</code>
━━━━━━━━━
[•] ⇾ The 𝗪𝗼𝗿𝗹𝗱𝘀 of 𝗔𝗽𝗶𝘀
[•] ⇾ @TheWorldsOfApis
━━━━━━━━━</b>'''
        await ass.edit_text(ss)

    else: return await msg.reply('<b> Losiento solo le respondo a mi creador <code>RexAwait (max)</code></b>')


@cmdshead('aproved')
async def start(message):
    if 6411167257  == message['from']['id']:
        idw = message.text[len('/aproved '):]
        with open('grupos.txt', 'a') as ile:
            ile.write(idw +'\n')
        await message.reply(f'<b>El usuario con el id {idw} ha sido aprovado ✅</b>')
    else: message.reply('<b>Este comando es solo para @Rexawait</b>')
       
@cmdshead('reproved')
async def start(message):
    if 6411167257  == message['from']['id']:
        idw = message.text[len('/reaproved '):]
        with open('grupos.txt', mode='r+', encoding='utf-8') as archivo:
            x = archivo.readlines()
            if f'{idw}\n' in x:  
                x.remove(f'{idw}\n')  
                await message.reply(f'<b>El usuario con el id {idw} ha sido expulsado de la lista de accesso ✅</b>')
                archivo.seek(0)  
                archivo.writelines(x)  
                archivo.truncate() 
            else: 
                await message.reply(f'<b>El usuario con el id {idw} No esta en la lista.</b>')    




@cmdshead('aprovedchat')
async def start(message):
    if 6411167257  == message['from']['id']:
        idw = message.text[len('/aprovedchat '):]
        with open('grupos.txt', 'a') as ile:
            ile.write(idw +'\n')
        await message.reply(f'<b>El grupo con el id {idw} ha sido aprovado ✅</b>')
    else: message.reply('<b>Este comando es solo para @Rexawait</b>')
      

@cmdshead('reprovedchat')
async def start(message):
    if 6411167257  == message['from']['id']:
        idw = message.text[len('/reprovedchat '):]
        with open('grupos.txt', mode='r+', encoding='utf-8') as archivo:
            x = archivo.readlines()
            if f'{idw}\n' in x:  
                x.remove(f'{idw}\n')  
                await message.reply(f'<b>El grupo con el id {idw} ha sido expulsado de la lista de accesso ✅</b>')
                archivo.seek(0)  
                archivo.writelines(x)  
                archivo.truncate() 
            else: 
                await message.reply(f'<b>El grupo con el id {idw} No esta en la lista.</b>')    




@cmdshead('cmdsmax')
async def start(msg):
    if msg['from']['id'] == 6411167257:
        await msg.reply("""<b>[•] ⇾ Bloque de comandos  
        
[•] ⇾ start
[•] ⇾ cmds 
[•] ⇾ id
[•] ⇾ lista
[•] ⇾ aproved
[•] ⇾ reproved
[•] ⇾ aprovedchat 
[•] ⇾ reprovedchat
[•] ⇾ googleQuery</b>""")

print('main : onli')
executor.start_polling(rex)
