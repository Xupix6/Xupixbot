import discord
import time
from discord.ext import commands

remove = False

class Log(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def log(self, ctx, type):
        global remove

        print('[',(time.strftime("%H:%M:%S")),']','--> Commandes Log : ', ctx.author.name, '#', ctx.author.discriminator, 'a utilisé la commande log.')
        if type == 'create':
            channel = discord.utils.get(ctx.guild.text_channels, name='xupixlog')
            if channel:
                await ctx.send('Le salon a déjà été configuré, tout est bon ! :)')
            else:
                create_channel_check = False

                overwrites = {
                                ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                                ctx.guild.me: discord.PermissionOverwrite(read_messages=True)
                                }

                channel = await ctx.guild.create_text_channel('xupixlog', overwrites=overwrites)

                await channel.purge(limit=1)
                msg_to_pin = await channel.send("**:warning: Veuillez ne pas supprimer, ni changer le nom de ce salon, sinon, le bot ne pourra plus fonctionner correctement.**\n*Conseil: Si vous voulez correctement supprimer ce salon, veillez utiliser la commande `$log remove`.\n*Autre conseil: Je vous conseille fortement de muter complétement ce salon, même les mentions car dès que quelqu'un enverra un message, le bot va le logger dans ce salon.*")
                await msg_to_pin.pin()
                await channel.purge(limit=1)

                await ctx.send(':white_check_mark: **Le salon a bien été crée et configuré.**\n*(Note: Vous êtes la seule personne à voir le salon [et les administrateurs aussi] mais vous pourrez toujours changer ses permissions.)*')
        if type == 'remove':
            channel = discord.utils.get(ctx.guild.text_channels, name='xupixlog')
            if channel:
                print('petit zizi')
                await channel.delete(reason='La commande pour supprimer #xupixlog a été executé.')
                await ctx.send(':white_check_mark: **Le salon a bien été supprimé.**')
                return
            else:
                await ctx.send("Le salon n'existe pas. Je ne peux pas le supprimer. Vous devez d'abord le créer en utilisant la commande `xb!log create`.")



    "--------------------------------MEMBRES-------------------------------------"


    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.bot == True:
            bot_check = 'Oui'
        else:
            bot_check = 'Non'
        channel = discord.utils.get(member.guild.text_channels, name='xupixlog')
        if channel:
            embed = discord.Embed(colour=discord.Colour.from_rgb(0, 255, 0))
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_author(name='Une personne a rejoint le serveur.')
            embed.set_footer(text=f'{time.strftime("%H:%M:%S")} (UTC+1)', icon_url=member.guild.icon_url)
            embed.add_field(name='Nom de la personne:', value=f'{member.name}#{member.discriminator}')
            embed.add_field(name='ID de la personne:', value=f'{member.id}')
            embed.add_field(name='Bot:', value=f'{bot_check}')


            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.bot == True:
            bot_check = 'Oui'
        else:
            bot_check = 'Non'
        channel = discord.utils.get(member.guild.text_channels, name='xupixlog')
        if channel:
            embed = discord.Embed(colour=discord.Colour.from_rgb(255, 0, 0))
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_author(name='Une personne a quitté le serveur.')
            embed.set_footer(text=f'{time.strftime("%H:%M:%S")} (UTC+1)', icon_url=member.guild.icon_url)
            embed.add_field(name='Nom de la personne:', value=f'{member.name}#{member.discriminator}')
            embed.add_field(name='ID de la personne:', value=f'{member.id}')
            embed.add_field(name='Bot:', value=f'{bot_check}')


            await channel.send(embed=embed)

    "----------------------------------SALONS-------------------------------------"

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel_1):
        channel = discord.utils.get(channel_1.guild.text_channels, name='xupixlog')

        if channel:
            embed = discord.Embed(colour=discord.Colour.from_rgb(0, 255, 0))
            embed.set_thumbnail(url=self.client.user.avatar_url)
            embed.set_author(name='Un salon a été crée.')
            embed.set_footer(text=f'{time.strftime("%H:%M:%S")} (UTC+1)', icon_url=channel_1.guild.icon_url)
            embed.add_field(name='Nom du salon:', value=f'{channel_1.name}')
            embed.add_field(name='ID du salon:', value=f'{channel_1.id}')


            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel_1):
        channel = discord.utils.get(channel_1.guild.text_channels, name='xupixlog')
        if channel:
            embed = discord.Embed(colour=discord.Colour.from_rgb(255, 0, 0))
            embed.set_thumbnail(url=self.client.user.avatar_url)
            embed.set_author(name='Un salon a été supprimé.')
            embed.set_footer(text=f'{time.strftime("%H:%M:%S")} (UTC+1)', icon_url=channel_1.guild.icon_url)
            embed.add_field(name='Nom du salon:', value=f'{channel_1.name}')
            embed.add_field(name='ID du salon:', value=f'{channel_1.id}')


            await channel.send(embed=embed)


    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        nothing = True
        channel = discord.utils.get(after.guild.text_channels, name='xupixlog')
        if before.position != after.position:
            return

        if channel:
            embed = discord.Embed(description=f'Catégorie du salon modifié: {after.category}\nSalon modifié : #{after.name}', colour=discord.Colour.from_rgb(255, 162, 0))
            embed.set_thumbnail(url=self.client.user.avatar_url)
            embed.set_footer(text=f'ID : {after.id} | {time.strftime("%H:%M:%S")} (UTC+1)', icon_url=after.guild.icon_url)
            if before.name != after.name:
                nothing = False
                embed.add_field(name='Nom du salon:', value=f'{before.name} --> {after.name}', inline=False)
            if before.category != after.category:
                nothing = False
                embed.add_field(name='Catégorie du salon:', value=f'{before.category} --> {after.category}', inline=False)
            if isinstance(before, discord.TextChannel):
                embed.set_author(name='Un salon textuel a été modifié.')
                if before.topic != after.topic:
                    nothing = False
                    embed.add_field(name='Description:', value=f'{before.topic} --> {after.topic}', inline=False)
                if before.slowmode_delay != after.slowmode_delay:
                    nothing = False
                    embed.add_field(name="Mode lent:", value=f'{before.slowmode_delay}s --> {after.slowmode_delay}s', inline=False)
                if before.is_nsfw() != after.is_nsfw():
                    nothing = False
                    if after.is_nsfw() == False:
                        embed.add_field(name="NSFW:", value='Désactivé.', inline=False)
                    else:
                        embed.add_field(name="NSFW:", value='Activé.', inline=False)
            if isinstance(before, discord.VoiceChannel):
                embed.set_author(name='Un salon vocal a été modifié.')
                if before.bitrate != after.bitrate:
                    nothing = False
                    embed.add_field(name="Débit binaire:", value=f'{str(before.bitrate)} bits par secondes --> {str(after.bitrate)} bits par secondes', inline=False)
                if before.user_limit != after.user_limit:
                    nothing = False
                    users_before = f'{before.user_limit} utilisateurs maximum'
                    users_after = f'{after.user_limit} utilisateurs maximum'
                    if before.user_limit == 0:
                        users_before = 'Illimité'
                    if after.user_limit == 0:
                        users_after = 'Illimité'
                    embed.add_field(name="Limite d'utilisateurs:", value=f'{users_before} --> {users_after}', inline=False)


            await channel.send(embed=embed)

    """@commands.Cog.listener()
    async def on_message(self, msg):
        if msg.guild is None:
            return

        if msg.content == "<@!705808166637797406>":
            await msg.channel.send("**Mon préfix est `xb!`**")

        channel = discord.utils.get(msg.guild.text_channels, name='xupixlog')

        if channel:
            if msg.author.id == self.client.user.id:
                return

            if msg.author.bot == True:
                return

            if msg.content == None:
                await channel.send(f"**{msg.author}** a écrit:\n*Le contenu du message est vide.*\ndans <#{msg.channel.id}>. (ID : {msg.id})")

            await channel.send(f'**{msg.author}** a écrit:\n"*{msg.content}*"\ndans <#{msg.channel.id}>. (ID : {msg.id})')"""

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.id == self.client.user.id:
            return

        if before.author.bot == True:
            return

        channel = discord.utils.get(after.guild.text_channels, name='xupixlog')
        if channel:
            if before.channel != channel:
                await channel.send(f'**Un message a été modifié dans <#{after.channel.id}>:**\n__Message original:__\n{before.content}\n__Message modifié:__\n{after.content}\nLien du message: {after.jump_url}')

    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        channel = discord.utils.get(msg.guild.text_channels, name='xupixlog')
        if channel:
            if msg.author.id == self.client.user.id:
                return

            if msg.author.bot == True:
                return

            await channel.send(f"Un message de **{msg.author} (ID:{msg.author.id})** a été supprimé dans <#{msg.channel.id}>:\n__Message supprimé:__\n{msg.content}")

def setup(client):
    client.add_cog(Log(client))
    print('Extension "Log" chargé !\n-----')

def teardown(client):
    client.remove_cog('Log')
    print('Extension "Log" déchargé !\n-----')
