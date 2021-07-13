import discord
import time
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['maths','calcul'])
    async def math(self, ctx, nombre_1, operateur, nombre_2):
        print('[',(time.strftime("%H:%M:%S")),']','--> Commandes Fun : ', ctx.author.name, '#', ctx.author.discriminator, 'a utilisé la commande math.')
        if operateur == '+':
            msg = await ctx.send('Calcul en cours...')
            nombre_1_math = int(nombre_1)
            nombre_2_math = int(nombre_2)
            resultat = nombre_1_math + nombre_2_math
            if resultat > 99999999:
                resultat = "{:.2e}".format(resultat)
            await msg.edit(content='__Calcul demandé :__')
            await ctx.send("```" + str(nombre_1) + ' + ' + str(nombre_2) + "\n=" + str(resultat) + "```")
        elif operateur == '-':
            msg = await ctx.send('Calcul en cours...')
            nombre_1_math = int(nombre_1)
            nombre_2_math = int(nombre_2)
            resultat = nombre_1_math - nombre_2_math
            if resultat > 99999999:
                resultat = "{:.2e}".format(resultat)
            await msg.edit(content='__Calcul demandé :__')
            await ctx.send("```" + str(nombre_1) + ' - ' + str(nombre_2) + "\n=" + str(resultat) + "```")
        elif operateur == 'x':
            msg = await ctx.send('Calcul en cours...')
            nombre_1_math = int(nombre_1)
            nombre_2_math = int(nombre_2)
            resultat = nombre_1_math * nombre_2_math
            if resultat > 99999999:
                resultat = "{:.2e}".format(resultat)
            await msg.edit(content='__Calcul demandé :__')
            await ctx.send("```" + str(nombre_1) + ' * ' + str(nombre_2) + "\n=" + str(resultat) + "```")
        elif operateur == '/':
            msg = await ctx.send('Calcul en cours...')
            nombre_1_math = int(nombre_1)
            nombre_2_math = int(nombre_2)
            resultat = nombre_1_math / nombre_2_math
            if resultat > 99999999:
                resultat = "{:.2e}".format(resultat)
            await msg.edit(content='__Calcul demandé :__')
            await ctx.send("```" + str(nombre_1) + ' / ' + str(nombre_2) + "\n=" + str(resultat) + "```")
        elif operateur == '^':
            msg = await ctx.send('Calcul en cours...')
            nombre_1_math = int(nombre_1)
            nombre_2_math = int(nombre_2)
            resultat = nombre_1_math ** nombre_2_math
            if resultat > 99999999:
                resultat = "{:.2e}".format(resultat)
            await msg.edit(content='__Calcul demandé :__')
            await ctx.send("```" + str(nombre_1) + ' ^ ' + str(nombre_2) + "\n=" + str(resultat) + "```")
        else:
            await ctx.send('**:warning: Je ne connais pas encore cet opérateur.**')

def setup(client):
    client.add_cog(Fun(client))
    print('Extension "Fun" chargé !\n-----')

def teardown(client):
    client.remove_cog('Fun')
    print('Extension "Fun" déchargé !\n-----')
