# rubika robot
import os
try:
    import requests
except:
    os.system("pip install requests")
try:
    import rubika
    
except:
    os.system("pip install rubika")
    
try:
    import datetime
except:
    os.system('pip install datetime')
#-----
green = '\033[32m'

red = '\033[31m'

blue = '\033[36m'

pink = '\033[35m'

yellow = '\033[93m'

darkblue = '\033[34m'

white = '\033[00m'
#---
from re import findall
from rubika import Bot
from requests import get
import requests
import time
from datetime import datetime

import uuid
import string
import random

#def random_string_generator(str_size, allowed_chars):
 # return ''.join(random.choice(allowed_chars) for x in range(str_size))
#chars = string.ascii_letters + string.punctuation
#size = 20

#code = (random_string_generator(size, chars))

import random,string,uuid
from random import choice

def random_string_generator(str_size, allowed_chars):
  return ''.join(random.choice(allowed_chars) for x in range(str_size))
chars = string.ascii_letters + string.punctuation
size = 20

cod = (random_string_generator(size, chars))
cod1 = (random_string_generator(size, chars))
cod2 = (uuid.uuid1())
cod3 = (random_string_generator(size, chars))
cod4 = (uuid.uuid1())
cod5 = (uuid.uuid1())
cod6 = cod,cod1,cod2,cod3,cod4,cod5
code = (random.choice(cod6))

#---------
cod = (uuid.uuid1())

#------ clear
try:
    os.system("clear")
except:
    os.system("cls")
# clear -----
time.sleep(1)
print()
banner = F"""{blue}
rubika robot for online user and self 
{darkblue}
(py-bot) library rubika ; robot"""

print(banner)
print()
time.sleep(1)
rbt = input(F"{yellow}please enter yout api hash account {green}(auth) {white}>>> {pink}")
print()
time.sleep(1)
gp = input(F"{yellow}please enter guid group rubika {white}>>> {pink}")
print()
time.sleep(1)
esm = input(F"{yellow}please enter your name account robot {white}>>> {pink}")
print()
time.sleep(1)
biu = input(F"{yellow}please enter your bio account robot {white}>>> {pink}")
print()
time.sleep(1)
joing = input(F"{yellow}please enter your link group {white}>>> {pink}")
print()
time.sleep(1)
print(f"{red}okay starting robot {green}-!")
time.sleep(1)
try:
    os.system("clear")
except:
    os.system('cls')
time.sleep(0.5)

#------------
bot = Bot("AppName",auth=F"{rbt}")
target = f"{gp}"
#-------------
# names robot ----

bot.joinGroup(F"{joing}")

bot.sendMessage(target,"start")

print (bot.editProfile(bio=biu))

print (bot.editProfile(name=esm))

#--------------
# talking robot -----
def hasInsult(msg):
	swData = [False,None]
	for i in open("dontReadMe.txt").read().split("\n"):
		if i in msg:
			swData = [True, i]
			break
		else: continue
	return swData

def hasAds(msg):
	links = list(map(lambda ID: ID.strip()[1:],findall("@[\w|_|\d]+", msg))) + list(map(lambda link:link.split("/")[-1],findall("rubika\.ir/\w+",msg)))
	joincORjoing = "joing" in msg or "joinc" in msg

	if joincORjoing: return joincORjoing
	else:
		for link in links:
			try:
				Type = bot.getInfoByUsername(link)["data"]["chat"]["abs_object"]["type"]
				if Type == "Channel":
					return True
			except KeyError: return False

# static variable
answered, sleeped, retries = [], False, {}

while True:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]

		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue

		open("id.txt","w").write(str(messages[-1].get("message_id")))

		for msg in messages:
			if msg["type"]=="Text" and not msg.get("message_id") in answered:
				if not sleeped:
					if hasInsult(msg.get("text"))[0] and not msg.get("author_object_guid") in admins :
						#ID = loads(c.decrypt(getUserInfo(msg.get("author_object_guid")).json().get("data_enc"))).get("data").get("user").get("username")
						#sendMessage(guid, f"#اخطار @{ID}", msg["message_id"])
						bot.deleteMessages(target, [str(msg.get("message_id"))])

					elif hasAds(msg.get("text")) and not msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [str(msg.get("message_id"))])

					elif "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "!sleep" and msg.get("author_object_guid") in admins :
						sleeped = True
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "!del" and msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("reply_to_message_id")])
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("!ban") and msg.get("author_object_guid") in admins :
						try:
							guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
							if not guid in admins :
								bot.banGroupMember(target, guid)
								bot.sendMessage(target, "✅", message_id=msg.get("message_id"))
							else :
								bot.sendMessage(target, "❎", message_id=msg.get("message_id"))
								
						except IndexError:
							bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
							bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("!send") :
						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "شما یک پیام ناشناس دارید:\n"+" ".join(msg.get("text").split(" ")[2:]))
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "سلام" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "hi love how are you -? ❤️", message_id=msg.get("message_id"))

					elif msg.get("text") == "بیا بخورش" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "kunto", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "اره" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "be kiram", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "نه" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "okayا", message_id=msg.get("message_id"))

					elif msg.get("text") == "خوبی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "yeah", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "سلامتی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "i love you ♥️", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ایول" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "khandidam", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "😡" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "hey", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "چقدر منو دوست داری" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "Much ❤️", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "استقلال" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "hey 💙", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "💙" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "you noob ! 💙", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "پرسپولیس" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "hey ❤", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "❤" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "hey ❤", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "😎" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "you powerful :)", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "😂" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "LOL :|", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "😐" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "Poker Face", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "😂😂" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "LOL TO ALL", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "هی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "hey", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "mmd" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "the godا", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ali" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "the noob", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "چی بلدی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "ls *", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "هویت" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "i am robot :/", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "amirا" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "the noob", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "لینک" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "[ https://rubika.ir/joing/CCGEHABG0UPQXIZXUKFZGZBZMTKCQRHY ] پیدا شد", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "گوه نخور" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "okay", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ربات" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بله", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "خودتو معرفی کن" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "i am the god !", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ممنون" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "okay my friend", message_id=msg.get("message_id"))

					elif msg.get("text") == "لیست" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, f"not found [{user}]", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "تبادل" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "not found user", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بای" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "کجا بچه", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "چه خبر" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "salamati", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "عشق" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "❤️", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "منم خوبم" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "شکر خدا", message_id=msg.get("message_id"))

					elif msg.get("text") == "فدات" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "no❤️", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بی تر ادب" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "okay my brother", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "هعی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "hey dadash", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "مرسی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "ok", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بمولا" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "im the god", message_id=msg.get("message_id"))
					# re ......--------------
te = (datetime.today())

#-------------------
					elif msg.get("text").startswith("!report") :
						
						bot.sendMessage(target,"okay :) starting repoter for filter ", message_id=msg.get("message_id"))
						#
					
					elif msg.get("text") == "کد"  and msg.get("author_object_guid") :
						
						bot.sendMessage(target,f"code report channel:\n\n`({code})`\n\n 2 order! ★\n code storng create by robot uid ", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ساعت" and msg.get("author_object_guid") :
						
						bot.sendMessage(target,f"time the: \n({te})\n\n :) ♥", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "تایم" and msg.get("author_object_guid") :
						
						bot.sendMessage(target,f"time is the: \n({te})\n\n♥ :)", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بش" and msg.get("author_object_guid") :
						
						bot.sendMessage(target,f"({user}) اوکی", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "باشه" and msg.get("author_object_guid") :
						bot.sendMessage(target,f"({user}) ♥ اوکی داداش", message_id=msg.get("message_id"))
						
#end talking the robot---------
					elif msg.get("text").startswith("!add") :
						bot.invite(target, [bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]])
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "!lock" :
						print(bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","AddMember"]).text)
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "!unlock" :
						bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","SendMessages","AddMember"])
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg["text"].startswith("!font"):
						response = get(f"https://api.codebazan.ir/font/?text={msg['text'].split()[1]}").json()
						#print("\n".join(list(response["result"].values())))
						try:
							bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:10])).text
							bot.sendMessage(target, "دایرکت اکانت رو چک کن", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "not submit :(", message_id=msg["message_id"])

					elif msg.get("text").startswith("!jok"):
						
						try:
							response = get("https://api.codebazan.ir/jok/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "not found ❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("!time"):
						
						try:
							response = get("https://api.codebazan.ir/time-date/?td=all").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "not found ❌", message_id=msg["message_id"])

				else:
					if msg.get("text") == "!wakeup" and msg.get("author_object_guid") in admins :
						sleeped = False
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

			elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
				name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
				data = msg['event_data']
				if data["type"]=="RemoveGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"bye bye {user}️", message_id=msg["message_id"])
				
				elif data["type"]=="AddedGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"hi [{user}] your baby i welcome to [{name}] ★ \n\nplz join : @caetorr \n(♥)i love you my bro :)", message_id=msg["message_id"])
				
				elif data["type"]=="LeaveGroup":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"bye bye {user}️", message_id=msg["message_id"])
					
				elif data["type"]=="JoinedGroupByLink":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"hello [{user}] my baby \n welcome to [{name}] \n \njoin @mu3alman :)) i love you (♥)", message_id=msg["message_id"])

			answered.append(msg.get("message_id"))

	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue
