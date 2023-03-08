from os import getenv 

api_id = getenv("API_ID")
api_hash = getenv("API_HASH")
mongodb = getenv ("MONGODB")
bot_token = getenv("TOKEN")
HELP = """**--Help--\n Kuki is your AI chat Bot friend Just Start conversation \n\n the premium Version of Kuki chatbot is Available for purchase ,it can include more features like Kuki learns from your everyday activity 
,she will never miss you(bot can have memory) , and you can train her well \nCommands\n/start Restarts the Bot \n/bots to get list of our bots made by cartx team\n
/cast to Broadcast message for bot users , you should have to be an admin to use this feature you can require this in our group or using feedback command and promote your products via our bot \n
/users to get how many users we have\n
/msg send message for one specified user \n
/admins to get list of admins of this bot \n**"""
headers = {
    'Content-type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-M135FU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://chat.kuki.ai/chat',}
