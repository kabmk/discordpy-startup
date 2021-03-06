from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import traceback

bot = commands.Bot(command_prefix='^')
token = os.environ['DISCORD_BOT_TOKEN']
#await ctx.send('1')
#scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
#await ctx.send('2')
#credentials = ServiceAccountCredentials.from_json_keyfile_name('vital-platform-303420-29489015e433.json', scope)
#await ctx.send('3')
#gc = gspread.authorize(credentials)

#SPREADSHEET_KEY = '1CG2ek5j5XjbEGtWQQn2JCBaCxawD5J7DGyX33Mc4nKo'
#workbook = gc.open_by_key(SPREADSHEET_KEY)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def reg(ctx):
    await ctx.send('1')
bot.run(token)
