import time
import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = 'xb!')
client.remove_command('help')

Statut = cycle(['Version : Beta','Crée par Xupix#0369','Programmation en cours'])
monID = 446283752730263572
l = 0
safe = ["Xupix#0369","XeriosG#5321","XupixBot#6959"]
channel_troll = [707255892785233981]
auteur = 0

#Démarrage du bot

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    change_status.start()
    print('[',(time.strftime("%H:%M:%S")),']',' Connexion Log : ', client.user.name ,' est en ligne. Super !')
    print('-------')
    print('Paramètres :')
    print('-')
    print('Liste safe : ', safe)
    print('-------')



@client.event
async def on_resumed():
    print('[',(time.strftime("%H:%M:%S")),']',' Connexion Log : ','Le bot a été relancé automatiquement', '[',(time.strftime("%H:%M:%S")),']')
    print('-------')


#Commandes

#IMPORTANTIMPORTANTIMPORTANTIMPORTANTIMPORTANTIMPORTANTIMPORTANTIMPORTANTIMPORTANTIMPORTANTIMPORTANTIMPORTANTIMPORTANT

@client.command()
async def reload(ctx, extension):
    if monID == ctx.author.id:
        msg = await ctx.send(f"**Redémarrage de l'extension `{extension}`**")
        try:
            client.reload_extension(f'cogs.{extension}')
        except commands.ExtensionNotFound:
            await msg.edit(content=f":x: **L'extension `{extension}` n'existe pas.**")
            return
        except commands.ExtensionNotLoaded:
            await msg.edit(content=f":x: **L'extension `{extension}` n'a pas encore été chargé.**")
            return
        msg = await msg.edit(content=f":white_check_mark: **L'extension `{extension}` a bien été redémarré !**")
    else:
        await ctx.send(content=':x: **Seul le fondateur de ce bot peut utiliser cette commande**', delete_after=5)

@client.command()
async def load(ctx, extension):
    if monID == ctx.author.id:
        if extension == 'all':
            msg = await ctx.send(f"**Démarrage de toutes les extensions...**")
        else:
            msg = await ctx.send(f"**Démarrage de l'extension `{extension}`...**")
        try:
            if extension == 'all':
                for filename in os.listdir('./cogs'):
                    if filename.endswith('.py'):
                        client.load_extension(f'cogs.{filename[:-3]}')
            else:
                client.load_extension(f'cogs.{extension}')
        except commands.ExtensionNotFound:
            await msg.edit(content=f":x: **L'extension `{extension}` n'existe pas.**")
            return
        except commands.ExtensionAlreadyLoaded:
            await msg.edit(content=f":warning: **L'extension `{extension}` est déjà chargé.**")
            return
        if extension == 'all':
            msg = await msg.edit(content=":white_check_mark: **Toutes les extensions ont bien été démarré !**")
        else:
            msg = await msg.edit(content=f":white_check_mark: **L'extension `{extension}` a bien été démarré !**")
    else:
        await ctx.send(content=':x: **Seul le fondateur de ce bot peut utiliser cette commande**', delete_after=5)

@client.command()
async def unload(ctx, extension):
    if monID == ctx.author.id:
        if extension == 'all':
            msg = await ctx.send(f"**Arrêt de toutes les extensions...**")
        else:
            msg = await ctx.send(f"**Arrêt de l'extension `{extension}`...**")
        try:
            if extension == 'all':
                for filename in os.listdir('./cogs'):
                    if filename.endswith('.py'):
                        client.unload_extension(f'cogs.{filename[:-3]}')
            else:
                client.unload_extension(f'cogs.{extension}')
        except commands.ExtensionNotFound:
            await msg.edit(content=f":x: **L'extension `{extension}` n'existe pas.**")
            return
        except commands.ExtensionNotLoaded:
            await msg.edit(content=f":warning: **L'extension `{extension}` n'est pas chargé.**")
            return
        if extension == 'all':
            msg = await msg.edit(content=":white_check_mark: **Toutes les extensions ont bien été arrêté !**")
        else:
            msg = await msg.edit(content=f":white_check_mark: **L'extension `{extension}` a bien été arrêté !**")
    else:
        await ctx.send(content=':x: **Seul le fondateur de ce bot peut utiliser cette commande**', delete_after=5)

#IMPORTANTIMPORTANTIMPORTANTIMPORTANTIMPORTANTIMPORTANTIMPORTANTIMPORTANTIMPORTANTIMPORTANTIMPORTANTIMPORTANTIMPORTANT

@client.event
async def on_message(message):
    global reponse_troll
    global reponse_troll2
    réponse_random = ['Totalement vrai !', 'Totalement faux !', 'Pas faux...', 'Mais ouais tellement', "Mais tg, je t'ai rien demandé toi !!", 'Peut-être...', 'Exact', 'Bordel, tu vas pas dire "Hein Xupixbot ?" quand même ?', '01001111 01110101 01100001 01101001 01110011']
    if message.author.id == client.user.id:
        return
    if message.content == "<@!705808166637797406>":
        await message.channel.send("**Mon préfix est `xb!`**")
    elif message.channel.id in channel_troll:
        if message.content.startswith('allah') or message.content.startswith('ALLAH'):
            random_choice = random.random()
            if random_choice > 0.5:
                await message.channel.send('est grand')
            else:
                await message.channel.send('AKBAR')
        if message.content.startswith('salut') or message.content.startswith('slt'):
            await message.channel.send('Salut')
            await message.channel.send("et j'espère que tu vas bien te faire enculé ta GROSSE DARONE LA PUTE !")
        if message.content.startswith('ta mère'):
            await message.channel.send('Ton père')
        if message.content.startswith('ta soeur') or message.content.startswith('ton frère'):
            await message.channel.send('Tes enfants en enfer')
        if message.content.startswith('enculé'):
            await message.channel.send('Toi même, enculé !')
        if message.content.startswith('$clear'):
            await message.channel.send('Cleanup ta mère oui')
        if message.content.startswith('Ok') or message.content.startswith('ok'):
            await message.channel.send('Boomer')
        if message.content.startswith('mute.'):
            await message.channel.send('Tu sais que ça sert à rien de me mute.')
        if message.content.startswith('Hein Xupixbot ?'):
            randomm = random.randint(0,8)
            print(randomm)
            await message.channel.send(réponse_random[randomm])
        if message.content.startswith('XXXerioss'):
            await message.channel.send('Arrête de flex Xerios !')
            time.sleep(13)
            await message.channel.send('Putin, il est fou ce mec...')
            time.sleep(20)
            await message.channel.send('Tkt, je rigole')
        if message.content.startswith('Bonne nuit'):
            await message.channel.send('Va dormir, sale flémmard !')
            await message.channel.send('Pardon...')
            await message.channel.send('Bonne nuit :)')
        if message.content.startswith('tg'):
            await message.channel.send('Ok, tu vas voir...')
            async with message.channel.typing():
                time.sleep(5)
            await message.channel.send('```Vous avez été blacklisté !```')
            time.sleep(1)
            await message.channel.send('Qu est ce que tu vas faire mtn ?')
        if message.content.startswith('mdr') or message.content.startswith('xd') or message.content.startswith('ptdr'):
            await message.channel.send('Tu trouves ça drôle ?')
            reponse_troll = message.author.id


        if message.content.startswith('Oui') or message.content.startswith('oui'):
            if message.author.id == reponse_troll:
                await message.channel.send('Ok. Tant mieux pour toi si ça te fait rire.')
                reponse_troll = 0
            else:
                return

    await client.process_commands(message)


#(Commande Troll)

@client.command()
@commands.has_permissions(manage_messages = True)
async def troll(ctx):
    print('[',(time.strftime("%H:%M:%S")),']','--> Commandes Log : ', ctx.author.name, '#', ctx.author.discriminator, 'a utilisé la commande troll.')
    if monID == ctx.author.id:
        if ctx.channel.id in channel_troll:
            channel_troll.remove(ctx.channel.id)
            await ctx.send(':white_check_mark: **Le troll a été désactivé sur ce channel.**')
            print(f'Channel_troll activé : {channel_troll}')
        else:
            channel_troll.append(ctx.channel.id)
            await ctx.send(':white_check_mark: **Le troll a été activé sur ce channel.**')
            print(f'Channel_troll desactivé : {channel_troll}')

    else:
        await ctx.send(':x: Seul le fondateur de ce bot peut utiliser cette commande')


#(Commande HELP)

@client.command(pass_context=True, aliases=['aide'])
@commands.cooldown(1, 15, commands.BucketType.user)
async def help(ctx, commande=None):
    msg_contenu = ':speech_balloon: **Veuillez regarder vos messages privés.**'
    print('[',(time.strftime("%H:%M:%S")),']','--> Commandes Log : ', ctx.author.name, '#', ctx.author.discriminator, 'a utilisé la commande help.')
    author = ctx.message.author
    embed = discord.Embed(colour = discord.Colour.blue())
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.set_footer(text=f'{time.strftime("%H:%M:%S")} (UTC+1)', icon_url=ctx.guild.icon_url)
    if commande == None:
        embed_2 = discord.Embed(description="Le préfixe du bot est `xb!`.\nVous pouvez voir des détails sur une commande en particulier en écrivant `xb!help [commande]`\nNOTE: <obligatoire> - [dispensable] - (action) - *=peut mettre des espaces.", colour = discord.Colour.blue())
        embed_2.set_author(name='Aide:')
        embed_2.set_thumbnail(url=client.user.avatar_url)
        embed_2.set_footer(text=f'{time.strftime("%H:%M:%S")} (UTC+1)', icon_url=ctx.guild.icon_url)
        embed_2.add_field(name='Fun:', value='`math`', inline=False)
        embed_2.add_field(name='Modération:', value='`ban` `clear` `kick` `whois`', inline=False)
        embed_2.add_field(name='Autres', value='`log` `ping` `remove`', inline=False)
        await ctx.author.send(embed=embed_2)
        await ctx.send(':speech_balloon: **Veuillez regarder vos messages privés, je vous ai envoyé la liste de mes commandes.**')
        return
    if commande == 'ban':
        embed.set_author(name='Aide pour la commande `ban`:')
        embed.add_field(name='Fonction', value='Ban un membre mentionné.', inline=False)
        embed.add_field(name='Utilisation de la commande', value='`ban @<membre> [*raison]`', inline=False)
        embed.add_field(name='Permission(s) nécessaire(s)', value='`bannir des membres`', inline=False)
        await ctx.author.send(embed=embed)
        await ctx.send(msg_contenu)
        return
    if commande == 'clear':
        embed.set_author(name='Aide pour la commande `clear`:')
        embed.add_field(name='Fonction', value='Supprime un nombre imposé de messages dans un salon.', inline=False)
        embed.add_field(name='Utilisation de la commande', value='`clear <nombre de messages à supprimer>`', inline=False)
        embed.add_field(name='Permission(s) nécessaire(s)', value='`gérér les messages`', inline=False)
        await ctx.author.send(embed=embed)
        await ctx.send(msg_contenu)
        return
    if commande == 'kick':
        embed.set_author(name='Aide pour la commande `kick`:')
        embed.add_field(name='Fonction', value='Expulse un membre mentionné.', inline=False)
        embed.add_field(name='Utilisation de la commande', value='`kick @<membre> [*raison]`', inline=False)
        embed.add_field(name='Permission(s) nécessaire(s)', value='`expulser des membres`', inline=False)
        await ctx.author.send(embed=embed)
        await ctx.send(msg_contenu)
        return
    if commande == 'log':
        embed.set_author(name='Aide pour la commande `log`:')
        embed.add_field(name='Fonction', value='Log des informations concernant un serveur en créant un salon voué pour cela.', inline=False)
        embed.add_field(name='Utilisation de la commande', value='`log <(commande)>`', inline=False)
        embed.add_field(name='Liste de commandes', value='`create`: Crée le channel #xupixlog pour logger des informations.\n`remove`: Supprime #xupixlog.', inline=False)
        embed.add_field(name='Permission(s) nécessaire(s)', value='`gérér les salons`', inline=False)
        await ctx.author.send(embed=embed)
        await ctx.send(msg_contenu)
        return
    if commande == 'math':
        embed.set_author(name='Aide pour la commande `math`:')
        embed.add_field(name='Fonction', value='Fait un calcul mathématique.', inline=False)
        embed.add_field(name='Utilisation de la commande', value='`math <premier nombre> <opérateur> <deuxième nombre>`', inline=False)
        embed.add_field(name="Liste d'opérateurs", value='``+, -, x, /, ^``', inline=False)
        await ctx.author.send(embed=embed)
        await ctx.send(msg_contenu)
        return
    if commande == 'ping':
        embed.set_author(name='Aide pour la commande `ping`:')
        embed.add_field(name='Fonction', value='Renvoie la latence entre le client et Discord (en millisecondes).', inline=False)
        embed.add_field(name='Utilisation de la commande', value='`ping`', inline=False)
        await ctx.author.send(embed=embed)
        await ctx.send(msg_contenu)
        return
    if commande == 'remove':
        embed.set_author(name='Aide pour la commande `ping`:')
        embed.add_field(name='Fonction', value='Kick le bot du serveur.', inline=False)
        embed.add_field(name='Utilisation de la commande', value='`remove`', inline=False)
        embed.add_field(name='Permission(s) nécessaire(s)', value='`expulser des membres`', inline=False)
        await ctx.author.send(embed=embed)
        await ctx.send(msg_contenu)
        return
    if commande == 'whois':
        embed.set_author(name='Aide pour la commande `whois`:')
        embed.add_field(name='Fonction', value="Montre en détails plein d'informations concernant l'utilisateur mentionné.", inline=False)
        embed.add_field(name='Utilisation de la commande', value='`whois @<membre>`', inline=False)
        embed.add_field(name='Permission(s) nécessaire(s)', value='`gérér les rôles`', inline=False)
        await ctx.author.send(embed=embed)
        await ctx.send(msg_contenu)
        return
    else:
        await ctx.send(":warning: **Cette commande n'existe pas.**")

#(Commande de latence)

@client.command()
async def ping(ctx):
    print('[',(time.strftime("%H:%M:%S")),']','--> Commandes Log : ', ctx.author.name, '#', ctx.author.discriminator, 'a utilisé la commande ping.')
    await ctx.send(f':ping_pong: Pong ! {round(client.latency * 1000)}ms de latence.')

#(Commande de déconnexion)

@client.command()
async def deco(ctx):
    if monID == ctx.author.id:
        print('Déconnexion de', client.user.name,'...')
        msg = await ctx.send('Déconnexion...')
        await client.logout()
        print('Le bot a bien été deconnecté !')
        print('-------')
    else:
        await ctx.send(content=':x: Seul le fondateur de ce bot peut utiliser cette commande', delete_after=5)

#(Commande de kick et ban)

@client.command()
@commands.has_permissions(kick_members = True)
async def remove(ctx):
    msg = await ctx.send(':warning: **Etes-vous sur de vouloir me kick du serveur ?** ✅=Oui ❌=Non')
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")
    @client.event
    async def on_reaction_add(reaction, user):

        if user.id == client.user.id:
            return

        if reaction.emoji == "✅":
            if ctx.author.id == user.id:
                await msg.edit(content=":hand_splayed: **Merci d'avoir utilisé Xupixbot, en espérant vous revoir bientôt !**")
                await ctx.guild.leave()
                return
            else:
                await reaction.remove(user)

        if reaction.emoji == "❌":
            if ctx.author.id == user.id:
                await msg.edit(content=':white_check_mark: **La commande a bien été annulé.**', delete_after=5)
                return
            else:
                await reaction.remove(user)

@client.command()
@commands.has_permissions(manage_roles = True)
async def whois(ctx, member : discord.Member):
    print('[',(time.strftime("%H:%M:%S")),']','--> Commandes Log : ', ctx.author.name, '#', ctx.author.discriminator, 'a utilisé la commande whois.')
    if str(member.status) == "offline":
        description_statut = 'hors-ligne'
    elif str(member.status) == "idle":
        description_statut = 'absent'
    elif str(member.status) == "dnd":
        description_statut = 'en mode "ne pas déranger"'
    else:
        description_statut = 'en ligne'

    embed = discord.Embed(

        description = f"La personne est actuellement {description_statut}.",
        colour = discord.Colour.from_rgb(20, 20, 20)
    )

    embed.set_author(name='Qui est-ce ?')
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f'{time.strftime("%H:%M:%S")} (UTC+1)', icon_url=client.user.avatar_url)
    embed.add_field(name='Nom:', value=f'{member.name}#{member.discriminator} ({member.nick})', inline=False)
    embed.add_field(name='ID:', value=f'{member.id}', inline=False)
    if member.bot == False:
        embed.add_field(name='Est-ce un bot ?', value='Non', inline=False)
    else:
        embed.add_field(name='Est-ce un bot ?', value='Oui', inline=False)
    embed.add_field(name='Est sur le serveur depuis', value=f'Le {member.joined_at}', inline=False)

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, nombre=1):
    print('[',(time.strftime("%H:%M:%S")),']','--> Commandes Log : ', ctx.author.name, '#', ctx.author.discriminator, 'a utilisé la commande clear.')
    await ctx.channel.purge(limit=1)
    await ctx.send(':hourglass_flowing_sand: Nettoyage...')
    time.sleep(0.5)
    await ctx.channel.purge(limit=int(nombre) + 1)
    await ctx.send(':hourglass: Nettoyé !')
    time.sleep(3)
    await ctx.channel.purge(limit=1)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason=None):
    print('[',(time.strftime("%H:%M:%S")),']','--> Commandes Log : ', ctx.author.name, '#', ctx.author.discriminator, 'a utilisé la commande kick.')
    await ctx.channel.purge(limit=1)
    if ctx.message.author.id == member.id:
        await ctx.send(content=':warning: **Vous ne pouvez pas vous kick.**', delete_after=5)
        return

    if str(object=member) in safe:
        await ctx.send(content=':warning: Membre whitelisté par le bot.', delete_after=5)
    else:
        await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason=None):
    print('[',(time.strftime("%H:%M:%S")),']','--> Commandes Log : ', ctx.author.name, '#', ctx.author.discriminator, 'a utilisé la commande ban.')
    await ctx.channel.purge(limit=1)
    if ctx.message.author.id == member.id:
        await ctx.send(content=':warning: **Vous ne pouvez pas vous ban.**', delete_after=5)
        return

    if str(object=member) in safe:
        await ctx.send(content=':warning: Membre whitelisté par le bot.', delete_after=5)
    else:
        await member.ban(reason=reason)

#Statut


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(Statut)))


#Erreurs

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        print('[',(time.strftime("%H:%M:%S")),']','-------> Erreurs Log : ', ctx.author.name, '#', ctx.author.discriminator, 'a exécuter l erreur : CommandOnCooldown')
        await ctx.send(content=f':clock1: **Veillez attendre {round(error.retry_after)} secondes avant de réutiliser cette commande.**', delete_after=3)
        return
    if isinstance(error, commands.CommandNotFound):
        print('[',(time.strftime("%H:%M:%S")),']','-------> Erreurs Log : ', ctx.author.name, '#', ctx.author.discriminator, "a exécuter l'erreur : CommandNotFound")
        await ctx.send(content=':x: **Commande invalide**')
        return
    if isinstance(error, commands.UserInputError):
        print('[',(time.strftime("%H:%M:%S")),']','-------> Erreurs Log : ', ctx.author.name, '#', ctx.author.discriminator, "a exécuter l'erreur : UserInputError")
        await ctx.send(':x: **Veillez utiliser la commande `xb!help [commande]` pour connaître son utilisation correcte.**')
        return
    if isinstance(error, discord.Forbidden):
        print('[',(time.strftime("%H:%M:%S")),']','-------> Erreurs Log : ', ctx.author.name, '#', ctx.author.discriminator, "a exécuter l'erreur : Forbidden")
        await ctx.send(content=':x: **Permissions manquantes ou le bot ne possède pas les permissions pour exécuter cette commande.**')
        return
    if isinstance(error, commands.CommandInvokeError):
        print('---------------------------------------------------------------')
        print('EXCEPTION DETECTE')
        print('[',(time.strftime("%H:%M:%S")),']','-------> Erreurs Log : ', ctx.author.name, '#', ctx.author.discriminator, 'a exécuter l erreur : CommandInvokeError')
        print(str(error))
        print('---------------------------------------------------------------')
        await ctx.send(f':x: **La commande a causé une erreur dans mon programme :c** *Veuillez contacter le fondateur du bot (Xupix#0369) pour plus de détails sur le problème.*\n__**Erreur:**__```{str(error)}```')
        return















#CONNEXION A DISCORD









client.run('NOPE, dont stole my token, you little brat')
