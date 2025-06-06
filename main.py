import discord
from discord.ext import commands
from keep_alive import keep_alive
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')

@bot.event
async def on_member_update(before, after):
    new_roles = [role for role in after.roles if role not in before.roles]
    for role in new_roles:
        if "vanity" in role.name.lower():
            canal = discord.utils.get(after.guild.text_channels, name="👑・✦vanity")
            if canal:
                await canal.send(f'(◍˘ᵕ˘)　❢₊　{after.mention} recibió el rol **vanity** ✨ ¡Gracias por apoyar!')
                embed = discord.Embed(
                    title="💝 ¡Gracias por usar nuestro vanity!",
                    description=(
                        "💖 ¡Gracias por usar nuestro vanity! Tu apoyo ayuda a que el servidor crezca y se vea aún más bonito ✨\n"
                        "Nos alegra tenerte aquí, ¡esperamos que disfrutes tu estancia! 🫶\n"
                        "︶︶︶︶︶︶︶\n💌 con cariño, el staff ♡"
                    ),
                    color=0xF9A8D4
                )
                embed.set_thumbnail(url="https://i.imgur.com/K1cLuE8.jpeg")
                embed.set_image(url="https://i.imgur.com/676U5HW.gif")
                embed.set_footer(text="Servidor agradecido 💖")
                await canal.send(embed=embed)

keep_alive()
try:
    bot.run(os.environ['DISCORD_TOKEN'])
except Exception as e:
    print(f'❌ Error al iniciar el bot: {e}')

