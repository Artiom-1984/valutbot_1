import urllib.request
import telebot

def kurs(i):
    s = urllib.request.urlopen("http://yandex.by").read()
    s = s.decode('utf-8')

    res = s[s.find("USD"):s.find("(за 100)")]

    lis = []
    while 'value_inner' in res:
        res = res[res.find("value_inner"):]
        res = res[res.find(">")+1:]
        lis.append(res[:res.find("<")])
    
    j = 0
    while j < len(lis):
        lis[j] = lis[j].replace(',', '.')
        j = j+1
           
    return lis[i]
    
    
    
def Summa(s):
    result = s.strip()
    if ' ' in result:
        try:
            result = int(result[0: result.find(' ')])
        except ValueError:
            result = 1
    else:
        result = 1
        
    return result
    
    
    

token = '1127857674:AAH3AFp1rV9DCvpgYTwaOXPLM96u1MnGeqk'
bot = telebot.TeleBot(token)
@bot.message_handler(content_types = ['text'])

def azaza(message):
    kort = ('2', '3', '4')
	
    message.text = message.text.lower()
    sum = Summa(message.text)
	
    if 'доллар' in message.text :
        temp = str(sum)
        if temp[-1] == '1':
            valut = ' доллар'
        elif temp[-1] in kort:
            valut = ' доллара'
        else:
            valut = ' долларов'
		
        bot.send_message(message.from_user.id, str(round(sum*float(kurs(0)), 2)) + ' BYN за '+ str(sum) + valut)
		
		
    elif 'евро' in message.text:
        bot.send_message(message.from_user.id, str(round(sum*float(kurs(1)), 2)) + ' BYN за '+ str(sum) + ' евро')
		
		
    elif 'рубл' in message.text:
        if sum == 1 :
            sum = 100
			
        temp = str(sum)
        if temp[-1] == '1':
            valut = ' рубль'
        elif temp[-1] in kort:
            valut = ' рубля'
        else:
            valut = ' рублей'
		
        bot.send_message(message.from_user.id, str(round(sum*float(kurs(2))/100, 2)) + ' BYN за '+ str(sum) + valut)
	
    elif 'byn' in message.text:
        bot.send_message(message.from_user.id, str(round(sum*1/float(kurs(0)), 2)) + ' USD\n' + str(round(sum*1/float(kurs(1)), 2)) + ' EUR\n' + str(round(sum*100/float(kurs(2)), 2)) + ' RUB')
		
    elif message.text == 'курс валют':
        bot.send_message(message.from_user.id, 'USD: '+ kurs(0)+'\n'+ 'EUR: '+ kurs(1) + '\n' + 'RUB: ' + kurs(2)+' (за 100)')
		
    else: 
        bot.send_message(message.from_user.id, 'Не понял!')
	
	

bot.polling(none_stop = True, interval = 0 )






