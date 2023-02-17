#importa a biblioteca do telegram bot
import telebot

#cadastra a chave do bot
chave_api = "6135444449:AAHGvbOBJ5VS1wnZafXbRvwA4m1yk1tIB8Q"

bot = telebot.TeleBot(chave_api)


@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
  bot.send_message(mensagem.chat.id,
                   "pedido feito, sua pizza sera entregue em 30 minutos")


@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
  bot.send_message(mensagem.chat.id,
                   "pedido feito, seu hamburguer sera entregue em 30 minutos")


@bot.message_handler(commands=["salada"])
def salada(mensagem):
  bot.send_message(mensagem.chat.id,
                   "pedido feito, sua salada sera entregue em 30 minutos")


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
  texto = """Escolha uma das opções: 
  /pizza pizza
  /hamburguer hamburguer
  /salada salada"""
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
  texto = """Sinto muito que tenha dado algo de errado com o seu pedido.
Para mandar uma reclamação utilize este email:

Reclame-aqui@comida-delivey.com"""
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
  bot.send_message(
    mensagem.chat.id,
    "obrigado {}!, André agradeceu o abraço".format(mensagem.chat.username))


# verifica de a mensagem enviada
def verificar(mensagem):
  return True


#em caso afirmativo o bot manda uma msg:
@bot.message_handler(func=verificar)
def responder(mensagem):

  texto = """Escolha uma das opções para continuar:
  /opcao1 Fazer um pedido
  /opcao2 Reclamação de um pedido
  /opcao3 mandar um abraço para André
  Responder qualquer outra coisa não ira funcionar, clique em uma das opções"""
  #envia uma mensagem com o texto
  bot.reply_to(mensagem, texto)


bot.polling()