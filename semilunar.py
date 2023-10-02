import telebot
from telebot import types
from telegram import Bot
import csv

bot = telebot.TeleBot('6678774310:AAHIAUsvw9-YEX8zlT-nEy3yJ0dDdOhpitA')

global user_name
user_name = ''

commands = {
    'educacao_sexual': 'Educação Sexual e Saúde Reprodutiva',
    'imunizacao': 'Vacinação e Prevenção de Doenças',
    'nutricao': 'Nutrição e Atividade Física',
    'eca': 'Estatuto da Criança e do Adolescente',
    'sobre': 'Conheça um pouco sobre a Semi-Lunar',
}

def create_custom_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for command, description in commands.items():
        markup.add(types.KeyboardButton(description))
    return markup

commandsEstatuto = {
    'direitos': 'Direitos das crianças e dos adolescentes',
    'deveres': 'Deveres das crianças e dos adolescentes',
    'voltar': 'Voltar ao menu de navegação'
}

def create_estatuto_custom_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for command, description in commandsEstatuto.items():
        markup.add(types.KeyboardButton(description))
    return markup

@bot.message_handler(func=lambda message: message.text in commandsEstatuto.values())
def percorrer_commands_estatuto(message):
    for command, description in commandsEstatuto.items():
        if description == message.text and message.text == 'Direitos das crianças e dos adolescentes':
            pergunta_usuario = bot.register_next_step_handler(message, direitos)
            user_state = {}
        elif description == message.text and message.text == 'Deveres das crianças e dos adolescentes':
            pergunta_usuario = bot.register_next_step_handler(message, deveres)
            user_state = {}
        elif description == message.text and message.text == 'Voltar ao menu de navegação':
            pergunta_usuario = bot.register_next_step_handler(message, voltar)
            user_state = {}

def direitos(message):
    bot.reply_to(message, '''O ECA (Estatuto da Criança e do Adolescente) garante uma série de direitos super importantes para as crianças e adolescentes no Brasil. 🌟

Direito à Vida 👶🌿: Isso significa que toda criança tem o direito de nascer, crescer e viver em um ambiente seguro e saudável.

Direito à Saúde 🏥💉: As crianças têm o direito de receber cuidados médicos, vacinações e tratamento sempre que necessário para se manterem saudáveis.

Direito à Educação 📚🎒: Todas as crianças têm o direito de ir à escola e receber uma boa educação para se desenvolverem.

Direito ao Lazer 🎉🤸‍♂️: Crianças também têm o direito de brincar, se divertir e relaxar, afinal, isso é importante para o desenvolvimento delas.

Direito à Convivência Familiar e Comunitária 👨‍👩‍👧‍👦🏡: Isso significa que as crianças têm o direito de viver em um ambiente familiar amoroso e seguro. E, quando isso não é possível, têm o direito de serem acolhidas em um lar adotivo.

Direito à Proteção contra a Violência ✋❌: O ECA protege as crianças contra qualquer forma de violência, seja ela física, psicológica ou sexual.

Direito à Liberdade de Expressão 🗣️📢: Crianças e adolescentes têm o direito de expressar suas opiniões e serem ouvidos em questões que os afetam.

Direito à Não Discriminação 🙅‍♂️🙅‍♀️: O ECA proíbe qualquer tipo de discriminação com base em raça, cor, religião, gênero ou qualquer outra característica.

Esses são apenas alguns dos direitos garantidos pelo ECA. Ele existe para garantir que todas as crianças e adolescentes tenham a oportunidade de crescer de forma saudável, segura e feliz, com todas as chances de se tornarem adultos bem-sucedidos e realizados. 😊🌈👫🌼
''')
    
def deveres(message):
    bot.reply_to(message, '''Assim como as crianças e adolescentes têm direitos, eles também têm alguns deveres importantes de acordo com o ECA (Estatuto da Criança e do Adolescente). Vamos dar uma olhada nos principais deveres deles:

Dever de Respeito 🤝🙏: Crianças e adolescentes devem respeitar os adultos, professores, colegas e outras pessoas, tratando-os com educação e consideração.

Dever de Estudar 📚🎓: É importante que eles frequentem a escola e se esforcem para aprender, pois a educação é fundamental para o seu desenvolvimento.

Dever de Colaborar em Casa 👨‍👩‍👧‍👦🏡: Eles devem ajudar em tarefas domésticas e cuidar de seus pertences, mostrando responsabilidade em casa.

Dever de Cuidar da Própria Saúde 🏥💪: Isso significa cuidar da higiene pessoal, seguir as orientações médicas e evitar comportamentos prejudiciais à saúde.

Dever de Respeitar as Regras da Comunidade 🚸🏡: Eles devem seguir as regras da escola, do bairro e da comunidade onde vivem, contribuindo para um ambiente harmonioso.

Dever de Respeitar o Meio Ambiente 🌍🌳: Crianças e adolescentes também têm a responsabilidade de cuidar do meio ambiente, evitando o desperdício e ajudando a preservar a natureza.

Dever de Não Praticar Atos Infracionais 🚫👮‍♂️: É importante que eles não se envolvam em atividades criminosas e respeitem as leis do país.

Dever de Participar de Atividades Sociais 👫🤝: Eles podem se envolver em atividades sociais, como grupos de jovens, para ajudar a melhorar a comunidade e se desenvolverem como cidadãos responsáveis.

Esses deveres são importantes para que as crianças e adolescentes cresçam de forma responsável, respeitosa e contribuam para uma sociedade mais justa e harmoniosa. 😊🤗🌟👦👧

''')
    
def voltar(message):
    bot.send_message(message.chat.id, f"""Selecione o comando""", reply_markup=create_custom_keyboard()) 


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, """Olá! Eu sou a Semi-Lunar 🌙
                     
Estou aqui para tirar suas dúvidas sobre esse período tão intenso e confuso que é a adolescência, não seja tímido(a), suas conversas estão seguras 😉.
                     
Mas antes, como você quer ser chamado(a)?""")
    bot.register_next_step_handler(message, receive_name)

def receive_name(message):
    user_name = message.text
    bot.send_message(message.chat.id, f"""Ótimo, {user_name}! É um prazer te conhecer 🤗. 
Agora, selecione o comando sobre o que deseja conversar.""", reply_markup=create_custom_keyboard()) 

@bot.message_handler(func=lambda message: message.text in commands.values())
def handle_command(message):
    for command, description in commands.items():
        if description == message.text and message.text == 'Educação Sexual e Saúde Reprodutiva':
            if user_name:
                bot.send_message(message.chat.id, f"Qual a sua dúvida? {user_name}? ")
            else:
                bot.send_message(message.chat.id, f"Qual a sua dúvida? ")
            pergunta_usuario = bot.register_next_step_handler(message, educacaosexual)
            user_state = {}

        elif description == message.text and message.text == 'Vacinação e Prevenção de Doenças':
            if user_name:
                bot.send_message(message.chat.id, f"Qual a sua dúvida? {user_name}? ")
            else:
                bot.send_message(message.chat.id, f"Qual a sua dúvida? ")
            pergunta_usuario = bot.register_next_step_handler(message, vacinacao)
            user_state = {}

        elif description == message.text and message.text == 'Nutrição e Atividade Física':
            
            if user_name:
                bot.send_message(message.chat.id, f'''{user_name}, para te oferecer uma melhor experiência precisamos de algumas informações para calcular seu IMC (Índice de Massa Corporal), ok? 😉🤩
Vamos lá, digite seu peso ⚖️ como no exemplo:  75.5''')
            else:
                bot.send_message(message.chat.id, f'''Para te oferecer uma melhor experiência precisamos de algumas informações para calcular seu IMC (Índice de Massa Corporal), ok? 😉🤩
Vamos lá, digite seu peso ⚖️ como no exemplo:  75.5''')
            pergunta_usuario = bot.register_next_step_handler(message, alt)
            # user_state = {}
            
        elif description == message.text and message.text == 'Estatuto da Criança e do Adolescente':
            if user_name:
                bot.send_message(message.chat.id, f'''O ECA, ou Estatuto da Criança e do Adolescente, é uma lei muito importante aqui no Brasil que foi criada para proteger os direitos das crianças e adolescentes. É como um conjunto de regras e direitos que garante que os mais jovens tenham uma vida melhor e mais segura. 🌟

Pensa assim: o ECA diz que toda criança e adolescente tem direito à vida, à saúde, à educação, ao lazer, à convivência familiar e comunitária, entre outros. Ele também proíbe coisas ruins, como o trabalho infantil em condições perigosas, a exploração sexual de crianças e adolescentes e o uso deles em atividades criminosas. ❌🚫

O ECA também estabelece que, quando um jovem comete um erro, em vez de ir para a prisão, ele deve receber medidas socioeducativas que visam à sua ressocialização, ou seja, ajudá-lo a se tornar uma pessoa melhor. 🤝✅

Então, basicamente, o ECA é uma lei que protege os direitos das crianças e adolescentes, garantindo que eles tenham uma infância e adolescência saudável e segura, e que sejam tratados com dignidade e respeito. É como uma grande proteção para os mais jovens, para que cresçam felizes e bem cuidados. 🤗👶👧🧒👦
''', reply_markup=create_estatuto_custom_keyboard())
            else:
                bot.send_message(message.chat.id, f'''O ECA, ou Estatuto da Criança e do Adolescente, é uma lei muito importante aqui no Brasil que foi criada para proteger os direitos das crianças e adolescentes. É como um conjunto de regras e direitos que garante que os mais jovens tenham uma vida melhor e mais segura. 🌟

Pensa assim: o ECA diz que toda criança e adolescente tem direito à vida, à saúde, à educação, ao lazer, à convivência familiar e comunitária, entre outros. Ele também proíbe coisas ruins, como o trabalho infantil em condições perigosas, a exploração sexual de crianças e adolescentes e o uso deles em atividades criminosas. ❌🚫

O ECA também estabelece que, quando um jovem comete um erro, em vez de ir para a prisão, ele deve receber medidas socioeducativas que visam à sua ressocialização, ou seja, ajudá-lo a se tornar uma pessoa melhor. 🤝✅

Então, basicamente, o ECA é uma lei que protege os direitos das crianças e adolescentes, garantindo que eles tenham uma infância e adolescência saudável e segura, e que sejam tratados com dignidade e respeito. É como uma grande proteção para os mais jovens, para que cresçam felizes e bem cuidados. 🤗👶👧🧒👦
''', reply_markup=create_estatuto_custom_keyboard())

            
        elif description == message.text and message.text == 'Conheça um pouco sobre a Semi-Lunar':
            bot.send_message(message.chat.id,'''Olá, sou a Semi-Lunar🌙, sou um chatbot feito especialmente para te orientar! 🤩 
Curiosidade: O nome ‘semi-lunar’ é um osso em forma de lua localizado na palma da mão.
                             
	    Visite nossas redes sociais:
	    💌 E-mail: semi.lunar11@gmail.com
	    📸 Instagram: @semilunarsocial
                             
Sobre as desenvolvedoras: 
“Nossa paixão pela programação e saúde levou a criar um chat dedicado a orientar sobre a saúde do adolescente. Juntas, trabalhamos duro para tornar essa ideia uma realidade. Nosso chat oferece informações e orientações valiosas sobre o cuidado com a saúde das crianças e adolescentes, abordando temas que vão desde o crescimento e desenvolvimento até a prevenção de doenças e promoção de um estilo de vida saudável.

Maria Layana de Queiroz Oliveira - Cursa informática na EEEP Maria Célia Pinheiro Falcão e está concluindo o curso técnico em enfermagem.
Rayane Emanuela de Souza Silva - Cursa informática na EEEP Maria Célia Pinheiro Falcão e está cursando o técnico em enfermagem.

Orientador do projeto: Professor Massaro Victor.
Co-orientadora: Professora Conceição Feitosa.
''')
            user_state = {}
            
def processar_pergunta_educacaosexual(pergunta, message):
    with open(f"C:\\Users\\olive\\Documents\\Python Scripts\\Consultas\\educacaoSexual.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        respostas = None
        imagemUrl = None

        pergunta = pergunta.lower()

        for row in reader:
            for palavra_chave in row[0].split(';'):
                if palavra_chave.lower() in pergunta:
                    respostas = row[1]
                    imagemUrl = row[2] if len(row) > 2 else None
                    break

        if respostas is not None:
            if imagemUrl is not None:
                bot.send_photo(message.chat.id, imagemUrl, reply_markup=create_custom_keyboard())
            
            return f'''{respostas}

Para fazer outra pergunta selecione o tópico novamente no teclado.''' 

        else:
            return "Desculpe, não encontrei uma resposta 😔🥺. Reformule sua dúvida e garanta que selecionou o tópico correto."

def educacaosexual(message):
    pergunta_usuario = message.text

    resposta = processar_pergunta_educacaosexual(pergunta_usuario, message)

    bot.reply_to(message, resposta)

def processar_pergunta_vacinacao(pergunta, message):
    with open(f"C:\\Users\\olive\\Documents\\Python Scripts\\Consultas\\vacinacaoPrevencao.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        respostas = None
        imagemUrl = None

        pergunta = pergunta.lower()

        for row in reader:
            for palavra_chave in row[0].split(';'):
                if palavra_chave.lower() in pergunta:
                    respostas = row[1]
                    imagemUrl = row[2] if len(row) > 2 else None
                    break

        if respostas is not None:
            if imagemUrl is not None:
                bot.send_photo(message.chat.id, imagemUrl, reply_markup=create_custom_keyboard())
            return f'''{respostas}

Para fazer outra pergunta selecione o tópico novamente no teclado.'''
        else:
            return "Desculpe, não encontrei uma resposta 😔🥺. Reformule sua dúvida e garanta que selecionou o tópico correto."
        
def vacinacao(message):
    pergunta_usuario = message.text

    resposta = processar_pergunta_vacinacao(pergunta_usuario, message)

    bot.reply_to(message, resposta)

def processar_pergunta_nutricao(pergunta, message):
    with open(f"C:\\Users\\olive\\Documents\\Python Scripts\\Consultas\\nutricao.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        respostas = None
        imagemUrl = None

        pergunta = pergunta.lower()

        for row in reader:
            for palavra_chave in row[0].split(';'):
                if palavra_chave.lower() in pergunta:
                    respostas = row[1]
                    imagemUrl = row[2] if len(row) > 2 else None
                    break

        if respostas is not None:
            if imagemUrl is not None:
                bot.send_photo(message.chat.id, imagemUrl, reply_markup=create_custom_keyboard())
            return respostas
        else:
            return "Desculpe, não encontrei uma resposta 😔🥺. Reformule sua dúvida e garanta que selecionou o tópico correto."

def nutricao(message):
    pergunta_usuario = message.text

    resposta = processar_pergunta_nutricao(pergunta_usuario, message)

    bot.reply_to(message, resposta)

def alt(message):
    while True:
        try:
            global pes
            pes = float(message.text)
            bot.reply_to(message, 'Muito bem! seu peso foi registrado. Agora, informe sua altura 📏 como no exemplo: 1.70')
            bot.register_next_step_handler(message, peso)
            break
        except ValueError:
            bot.reply_to(message, 'Desculpe, parece que você não inseriu uma altura válida 😓😢. Por favor, informe sua altura usando um número, por exemplo, 1.70')
            bot.register_next_step_handler(message, alt)
            break
def peso(message):
    while True:
        try:
            global alt
            alt = float(message.text)
            imc = pes / (alt * alt)
            
            if imc < 18.5:
                situaçao = 'Magreza'
                text = '''Parece que você está um pouco abaixo do peso. Não se preocupe, isso pode ser resolvido. 💪💡
Dieta: Priorize alimentos ricos em proteína e calorias saudáveis, como peixes, ovos, nozes e abacate. 🍳🥑
Exercícios: Opte por treinos de resistência e musculação para ganhar massa muscular. 🏋️‍♂️💪'''
            elif 18.5 <= imc < 25:
                situaçao = 'Peso normal'
                text = '''Parabéns, você está com o peso ideal! Mantenha esse caminho saudável. 👏🥗
Dieta: Continue com uma alimentação equilibrada, com muitas frutas, legumes e grãos integrais. 🍎🥦🍞
Exercícios: Faça exercícios aeróbicos regulares, como corrida, ciclismo ou dança, para manter-se em forma. 🏃‍♂️🚴‍♀️💃'''
            elif 25 <= imc < 30:
                situaçao = 'Sobrepeso'
                text = '''Você está um pouquinho acima do peso, mas sem estresse, podemos melhorar isso. 💪🥦
Dieta: Reduza alimentos processados e açúcares, e controle as porções. 🚫🍰🍔
Exercícios: Combine treinamento cardiovascular com treinos de força para queimar calorias e construir músculos. 🏋️‍♀️🏃‍♀️'''
            elif 30 <= imc < 35:
                situaçao = 'Obesidade grau 1'
                text = '''Seu IMC indica obesidade, mas lembre-se, estamos aqui para ajudar. 🤗❤️
Dieta: Consulte um nutricionista para criar um plano de refeições adequado. 🍏🥗
Exercícios: Comece com atividades de baixo impacto, como natação ou caminhada, e gradualmente aumente a intensidade. 🏊‍♂️🚶‍♀️🏋️‍♂️'''
            elif 35 <= imc < 40:
                situaçao = 'Obesidade Severa'
                text = '''Seu IMC indica obesidade severa, mas lembre-se, estamos aqui para ajudar. 🤗❤️
Dieta: Consulte um nutricionista para criar um plano de refeições adequado. 🍏🥗
Exercícios: Comece com atividades de baixo impacto, como natação ou caminhada, e gradualmente aumente a intensidade. 🏊‍♂️🚶‍♀️🏋️‍♂️'''
            else:
                situaçao = 'Obesidade Mórbida'
                text = '''Seu IMC indica obesidade mórbida, mas lembre-se, estamos aqui para ajudar. 🤗❤️
Dieta: Consulte um nutricionista para criar um plano de refeições adequado. 🍏🥗
Exercícios: Comece com atividades de baixo impacto, como natação ou caminhada, e gradualmente aumente a intensidade. 🏊‍♂️🚶‍♀️🏋️‍♂️'''

            bot.reply_to(message, f'''Excelente 😃! O resultado do seu imc é {imc:.2f}, o que significa: {situaçao}. 
{text}''', reply_markup=create_custom_keyboard())
            break

        except ValueError:
            bot.reply_to(message, 'Desculpe, parece que você não inseriu um peso válido 😓😢. Por favor, informe sua altura usando um número, por exemplo, 1.60')
            bot.register_next_step_handler(message, alt)
            break
        
bot.polling()
