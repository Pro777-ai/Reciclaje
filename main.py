import discord
from discord.ext import commands
import random
import os

# Intents son las acciones que el bot puede realizar
intents = discord.Intents.default()
intents.message_content = True

# Iniciando nuestro bot
bot = commands.Bot(command_prefix='$', intents=intents)

# Evento que se despliega al iniciar nuestro bot
@bot.event
async def on_ready():
    print(f"Señor hemos inicado como {bot.user}")

# Estableciendo el comando llamado meme
@bot.command()
async def meme(ctx):
    imagenes_cargadas = random.choice(os.listdir("Memes"))
    with open(f'Memes/{imagenes_cargadas}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

# Información sobre los comandos
@bot.command()
async def info(ctx):
    info = """
    - $basura - te manda información sobre los contenedores de basura
    - $como_ayudo - te dice cómo puedes ayudar al medio ambiente
    - $porque - te dice por qué debes reciclar y cuidar el medio ambiente
    - $meme - te manda un meme sobre un reciclaje o proteccion al medio ambiente
    """
    await ctx.send(info)
 
# Información sobre los contenedores de basura
@bot.command()
async def basura(ctx):
    mensaje = """
    El azul es para el papel
    El verde es para el vidrio o materiales de vidrio
    El amarillo es para el plástico
    El naranja para residuos orgánicos
    El rojo para residuos peligrosos para el medio ambiente y el ser humano
    El gris para otros tipos de desechos en general
    """
    await ctx.send(mensaje)

# Cómo ayudar al medio ambiente
@bot.command()
async def como_ayudo(ctx):
    como_ayudo = """
    1. Apagar las luces
    2. Utilizar bombillas de bajo consumo y luces LED
    3. Reciclar
    4. Comprar productos con certificado ecológico
    5. Evitar coger el coche
    6. Plantar árboles
    7. Evitar los plásticos
    8. Cerrar los grifos
    9. Desconectar los aparatos electrónicos
    10. Evitar el consumismo
    11. Dar otras ideas para mejorar el planeta en la pagina de la que procede el enlace a aqui
    12. Transmitir estas enseñazas o consejos
    """
    await ctx.send(como_ayudo)

# Razones por las que reciclar
@bot.command()
async def porque(ctx):
    porque = """
    Entre las principales razones para cuidar el medio ambiente podemos destacar las siguientes:
    - Asegurar la supervivencia de la especie humana.
    - Favorecer la supervivencia y evolución del resto de seres vivos.
    - Permitir que haya equilibrio ecológico.
    - No hay un planeta B en el que podamos vivir como en la Tierra, por lo que es nuestro único 
      hogar y el de las futuras generaciones.
    """
    await ctx.send(porque)

bot.run("MTEyOTA5MzA4OTQ0NTgxMDI1MA.GomLYd.UPYv2PVJf-3Bihmv6G6iZsZsC0RhkkTNbaIAEs")
