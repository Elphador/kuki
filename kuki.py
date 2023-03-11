from pyrogram import Client, filters, enums 
from pyrogram.errors import UserNotParticipant , FloodWait,InputUserDeactivated , UserIsBlocked , PeerIdInvalid
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle 
from  pymongo import MongoClient
import asyncio , requests,  json
from time import sleep 
from kconfig import HELP,headers ,api_id, api_hash, mongodb,  bot_token 
import datetime 
print("123........")



"buttons"
channel = InlineKeyboardButton("Channel🌴",url='https://t.me/neuralp')
group = InlineKeyboardButton("Group🪺",url='https://t.me/neuralg')
donate = InlineKeyboardButton("Donate VPS🦭",url="https://t.me/neuralg")
feedback = InlineKeyboardButton("Subscribe Premium🍿",url='https://t.me/neuralf')
help = InlineKeyboardButton("Help📃",callback_data='help')
mark = InlineKeyboardMarkup([[InlineKeyboardButton("🥬team Neural🌽",url = "https://t.me/neuralp")]])   

app = Client ("grabber",api_id=api_id,api_hash=api_hash, bot_token=bot_token)
cli = MongoClient(mongodb); db = cli.database; cuser = db.cuser ; cadmin = db.cadmin

frce = {"status":"off"}
bot = app ; admins = [] ; admi = cadmin.find({}) 
for guy in admi :
    admins.append(guy['admins'])
    
    

    
    

@bot.on_message(filters.private & filters.command("cast") & filters.user(admins))
async def cast(bot,msg):
    txt = msg.text
    block = " ."
    idinvalid  = " ."
    dec = " ."
    mesg = txt.replace('/cast',"")
    for user in cuser.find():
        print(user)
        try :
            await bot.send_message(user['userid'],mesg , reply_markup=mark)
        except UserIsBlocked:
            block+=f"{user['userid']} : {user['name']} :  @{user['username']}\n"
        except InputUserDeactivated:
            dec+=f"{user['userid']} : {user['name']} : @{user['username']}"
        except PeerIdInvalid:
            idinvalid+=f" {user['userid']} : {user['name']} : @{user['username']}"
        except FloodWait:
            await asyncio.sleep(e.x)     
   
        except Exception as error:
          await msg.reply(error)
    await msg.reply(f"cast logs\n\nBlocked User \n{block} \n Invalid Ids \n {idinvalid} Deactivated\n {dec}")  
    
@bot.on_message( filters.command("msg") & filters.user(admins))    
async def  messe(bot,msg):
    try :
        text = msg.copy(msg.text)
        ruid = text.split(" ")[1]
        mesgt = text.replace('/msg',"").replace(ruid,'')
        await bot.send_message(int(ruid), f"{mesgt}\n\n\n **Neural Programmers CEO**",reply_markup=mark) 
        await msg.reply("your message sent successfully")
        
    except Exception as error:
        await msg.reply(f"not sent\n{error} ")   
        
@app.on_message( filters.command("admins") & filters.user(admins))
async def admit(bot, msg):
    aid = " ."
    for x in cadmin.find({}):
        id = x['admins']
        prr = x['promoted']
        print(admins,id , prr)
        aid+= f"id {id} : promoted by {prr} \n"
    await msg.reply(aid)
    
@bot.on_message(filters.command("force") & filters.user(admins))       
def force(bot , msg):
    st = frce['status']
    cr = msg.reply(f"**Current Force Join Status {st}🦊**")
    tos = msg.text.split(" ")[1]
    frce["status"] = tos
    sleep(10)
    cr.edit(f"**Current Force Join Set to {st}🦊**")
    
    
@bot.on_message(filters.private & filters.command("set") )
def set(bot, msg):
    id = msg.text.replace("/set","")
    prp = msg.from_user.first_name 
    vals = {"admins":int(id),"promoted":prp}
    cadmin.insert_one(vals)
    cut = cadmin.find_one({"admins":int(id)})
    bot.send_message(int(id),f"you have promoted to admin by {prp}")
    msg.reply("Promoting New Admin Done🦊")
    
    

    
@bot.on_message(filters.private & filters.command("bots"))
def bots(bot, msg):
    msg.reply("list of our bots\n @ChatGtp_proBot")
        
    
    
@bot.on_message(filters.private & filters.command("start"))
async def start(bot, msg):
  
    name = msg.from_user.first_name 
    userid = msg.from_user.id
    username = msg.from_user.username  
    exs = cuser.find_one({'userid':userid})

    print(exs)
    user = {"name":name,"userid":userid,"username":username, "date":datetime.datetime.now()}
    if not exs :
      cuser.insert_one(user)
    else:
      pass
    markup = InlineKeyboardMarkup([[channel, group], [donate,feedback],[help]])
    await msg.reply(f"**Hello {username} My name Is Kuki I'm an Ai Chat Bot , I'm here to waste my time talking with you**",
    reply_markup= markup )

@bot.on_message(filters.private & filters.command("feedback"))
async def feeback (bot , msg):
    msgt = msg.text.replace('/feedback','')
    usr = msg.from_user.id 
    for ad in admins:
        await bot.send_message(int(ad),f"feedback from {usr}\n{msgt}")   
    
@bot.on_message( filters.private & filters.command("users")) 
def users(bot, msg):
    usr = cuser.find()
    c = len(list(usr))
    msg.reply(f"**we have {c}37 users at this moment🦝**")
@app.on_message(filters.private & filters.text)
async def kuk(bos, msg):
    if frce['status'] == 'on' :
        try :
            await bot.get_chat_member(-1001776406696 ,msg.from_user.id)
        except UserNotParticipant:
            await msg.reply("**Sorry i can't help you a lot on this ,Join the channel before our meeting**",
            reply_markup = InlineKeyboardMarkup([[channel]]))
            return
    else :
        pass
    data = {
    'input': msg.text,
    'botkey': 'icH-VVd4uNBhjUid30-xM9QhnvAaVS3wVKA3L8w2mmspQ-hoUB3ZK153sEG3MX-Z8bKchASVLAo~',
    'channel': '7',
    'sessionid': '483453398',
    'client_name': 'uuiprod-un18e6d73c-user-439215',
    'id': 'true',}
    resp = requests.post('https://icap.iconiq.ai/talk', headers=headers, data=data)
    print(resp.content)
    aqe = json.loads(resp.text); lst = aqe['responses'][0] 
    
    await msg.reply(lst) 
        
    
@bot.on_callback_query() 
async def calls(bot,update):
    name = update.message.from_user.first_name
    chat_id = update.message.chat.id; call = update.data
    if call == "help":
        await update.message.reply(HELP)
    else :
        await update.message.reply("oh forgotten button report bug ")            
            
            
            
bot.run()            
