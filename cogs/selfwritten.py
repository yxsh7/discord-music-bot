# Migrating work from old bot
# 19 NOV 2021


from enum import Flag
from inspect import Arguments
import discord
from discord import colour
from discord import client
from discord import user
from discord.channel import DMChannel 
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.core import command
from discord.flags import Intents
from discord.guild import Guild
import random
Intents.members=True

# INITIALIZE COG
class selfwritten(commands.Cog):

    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def checkcog(self,ctx):
        await ctx.send('loaded 1.0')

    # MATH COMMANDS 

    @commands.command(pass_context=True)
    async def add(self, ctx, a: int, b: int):
     result=a+b
     await ctx.send("**{}**  :white_check_mark:".format(result))

    @commands.command(pass_context=True)
    async def subtract(self,ctx, a: int, b: int):
     result=a-b
     await ctx.send("**{}**  :white_check_mark:".format(result))

    @commands.command(pass_context=True)
    async def multiply(self,ctx, a: int, b: int):
     result=a*b
     await ctx.send("**{}**  :white_check_mark:".format(result))

    @commands.command(pass_context=True)
    async def divide(self,ctx, a: int, b: int):
     result=a/b
     await ctx.send("**{}  :white_check_mark:**".format(result))

    @commands.command(pass_context=True)
    async def square(self,ctx, a: int):
     result=a*a
     await ctx.send("**{}  :white_check_mark:**".format(result))

    @commands.command(pass_context=True)
    async def cube(self,ctx, a: int):
     result=a*a*a
     await ctx.send("**{}  :white_check_mark: **".format(result)) 

    # INFO
    @commands.command(pass_context=True)
    async def info(self,ctx):
     embed = discord.Embed(
        title = "BOT INFO",
        description = "Currently under Development",
        colour= discord.Colour.blue()
        )
     embed.set_thumbnail(url='https://codestories.gr/wp-content/uploads/2020/03/Understanding-Bot-and-Spider-Filtering-from-Google-Analytics.jpg')
     embed.add_field(name=':keyboard: Developer', value='**Yash.K :flag_in:**', inline=False)
     embed.add_field(name=':scroll: First Release',value='**17 NOV 2021**', inline=False)
     embed.add_field(name=':e_mail: Contact ', value='**yashkamthe03@gmail.com**', inline=False)

     await ctx.send(embed=embed)


    # FUN COMMANDS 
    @commands.command(pass_context=True)
    async def roll(self,ctx):
     await ctx.send(random.choice([  "**:hourglass_flowing_sand: Rolling Dice. . . . . :game_die: You rolled the Dice & got 1!**",
                                     "**:hourglass_flowing_sand: Rolling Dice. . . . . :game_die: You rolled the Dice & got 2!**",
                                     "**:hourglass_flowing_sand: Rolling Dice. . . . . :game_die: You rolled the Dice & got 3!**",
                                     "**:hourglass_flowing_sand: Rolling Dice. . . . . :game_die: You rolled the Dice & got 4!**",
                                     "**:hourglass_flowing_sand: Rolling Dice. . . . . :game_die: You rolled the Dice & got 5!**",
                                     "**:hourglass_flowing_sand: Rolling Dice. . . . . :game_die: You rolled the Dice & got 6!**",]))

    @commands.command(pass_context=True)
    async def cat(self,ctx):
     
     embed = discord.Embed(title="Random Cat :cat:",
                          color=660000)
     embed.set_footer(text='Cat Library by Isha')
     embed.set_image(url=random.choice(["https://media2.giphy.com/media/ND6xkVPaj8tHO/giphy.gif?itemid=11039959",
                                       "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/11/enhanced/webdr10/anigif_enhanced-17445-1446481940-10.gif?itemid=5384805",
                                       "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/12/enhanced/webdr12/anigif_enhanced-1659-1446484096-3.gif?itemid=11535890",
                                       "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/12/enhanced/webdr04/anigif_enhanced-28149-1446484224-2.gif",
                                       "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/12/enhanced/webdr05/anigif_enhanced-2462-1446484330-3.gif",
                                       "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/12/enhanced/webdr06/anigif_enhanced-1080-1446484438-3.gif",
                                       "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/11/enhanced/webdr09/anigif_enhanced-26523-1446483536-5.gif",
                                       "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/12/enhanced/webdr11/anigif_enhanced-28840-1446485158-10.gif",
                                       "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/11/enhanced/webdr13/anigif_enhanced-17467-1446482522-2.gif",
                                       "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/11/enhanced/webdr13/anigif_enhanced-12805-1446481904-2.gif",
                                       "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/12/enhanced/webdr11/anigif_enhanced-24820-1446484272-3.gif",
                                       "https://media1.tenor.com/images/50d8c74c49e9013ab936f7029b46c7d6/tenor.gif?itemid=10419296",
                                       "https://media.giphy.com/media/UotLuplZSzKRa/giphy.gif",
                                       "https://media.giphy.com/media/klktLjcZgdNUQ/giphy.gif",
                                       "https://media.giphy.com/media/QFf4klFdmCbHq/giphy.gif",
                                       "https://media.giphy.com/media/BVhyvArvWrggU/giphy.gif",
                                       "https://media.giphy.com/media/5ldfj1DCIHa8/giphy.gif",
                                       "https://media.giphy.com/media/fWpx3rbEPlGY8/giphy.gif",
                                       "https://media.giphy.com/media/Ydq9AtGX2Kc24/giphy.gif",
                                       "https://media.giphy.com/media/q1MeAPDDMb43K/giphy.gif",
                                       "https://media.giphy.com/media/118lTJFyUJYyze/giphy.gif",
                                       "https://media.giphy.com/media/xJjs8eGVbjNYY/giphy.gif",
                                       "https://media.giphy.com/media/ggcdQxc40QNEI/giphy.gif",
                                       "https://media.giphy.com/media/Ov5NiLVXT8JEc/giphy.gif",
                                       "https://media.giphy.com/media/OzfuTIX1ngz7O/giphy.gif",
                                       "https://media2.giphy.com/media/VqrAsdR88b9VC/giphy.gif",
                                       "https://media.giphy.com/media/26BoElcdr7OiEHmfu/giphy.gif",]))
                                       
                                       
     await ctx.send(embed=embed)

# DOG
# ADD DOG GIF LINKS
    @commands.command(pass_context=True)
    async def dog(self,ctx):
     embed = discord.Embed(title="Random Dog :dog: ", Color=660000)
     embed.set_footer(text= "Library By Isha")
     embed.set_image(url=random.choice(["",
                                       "",]))

     await ctx.send(embed=embed)

    # HELP COMMANDS
    @commands.command(pass_context=True)
    async def helpme(self,ctx):
      embed = discord.Embed(
         title = 'BOT HELPDESK',
         description = 'Commands Information',
         colour = discord.Colour.blue()
         )

      embed.set_thumbnail(url='https://codestories.gr/wp-content/uploads/2020/03/Understanding-Bot-and-Spider-Filtering-from-Google-Analytics.jpg'),
      embed.add_field(name="Prefix", value="?", inline=False)
      embed.add_field(name="info", value="Gives the information about the bot.", inline=False)
      embed.add_field(name="helpmusic", value="Gives you commands related to music", inline=False)
      embed.add_field(name="helpfun", value="Gives you commands realted to fun", inline=False)
      embed.add_field(name="helputility", value="Gives you commands related to utility", inline=False)

    
      await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def helpmusic(self,ctx):
        
        
        
        embed = discord.Embed(
         title = 'MUSIC HELPDESK',
         description = 'Commands Information',
         colour = discord.Colour.blue()
         )

        embed.set_thumbnail(url='https://codestories.gr/wp-content/uploads/2020/03/Understanding-Bot-and-Spider-Filtering-from-Google-Analytics.jpg')
        embed.add_field(name="Prefix", value="?", inline=False)
        embed.add_field(name=":inbox_tray: connect", value="**Joins the bot to the music channel you are currently in.**", inline=False)
        embed.add_field(name=":outbox_tray:  disconnect", value="Make the bot leave the current voice channel", inline=False)
        embed.add_field(name=":minidisc: play", value="Use play commands before the song keywords, \n Example. ?play faded", inline=False)
        embed.add_field(name=":track_next: skip", value="Skips the currently playing song", inline=False)
        embed.add_field(name=":pause_button: pause", value="Pauses the currently playing song", inline=False)
        embed.add_field(name=":arrow_forward: resume", value="Resumes the paused song", inline=False)
        
        await ctx.send(embed=embed)

    
    @commands.command(pass_context=True)
    async def helputility(self,ctx):

        embed=discord.Embed(
            title='UTILITY HELPDESK',
            description='Commands Information',
            colour=discord.Colour.blue()
         
        )

        embed.set_thumbnail(url='https://codestories.gr/wp-content/uploads/2020/03/Understanding-Bot-and-Spider-Filtering-from-Google-Analytics.jpg')
        
        
        embed.add_field(name="add [number] [number]", value="Adds two numbers", inline=False)
        embed.add_field(name="subtract [number] [number]", value="subtracts second number from the first", inline=False)
        embed.add_field(name="multiply [number] [number]",value="Multiplies 2 numbers",inline=False)
        embed.add_field(name="divide [number] [number]",value="Divides the Number",inline=False)
        embed.add_field(name="square [number]",value="Squares the number",inline=False)
        embed.add_field(name="cube [number]",value="Cubes the number",inline=False)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def helpfun(self, ctx):

     embed=discord.Embed(
            title='FUN HELPDESK',
            description='Commands Information',
            colour=discord.Colour.blue()

        )

     embed.add_field(name="dog", value="Try it!", inline=False)
     embed.add_field(name="cat", value="Try it!", inline=False)

     await ctx.send(embed=embed)






    

def setup(bot):
    bot.add_cog(selfwritten(bot))

   