import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesion con {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un {bot.user} y fui creado para dar consejos de la contaminacion!')


consejos = [
    'Usa bolsas reutilizables para tus compras',
    'Evita los productos de un solo uso como sorbetes y cubiertos de plastico',
    'evite usar autos, camiones y otros transportes lo menos posible, en su lugar puedes la bicicleta',
    'no tire nada a la naturaleza que no sea plástico, vidrio ni nada que no sea de la naturaleza',
    'no queme basura, no fume, ni use nada que produzca humo',
    'reutilice el plastico para cacer manualidades, aqui encontrará algunas manualidades: https://www.handfie.com/manualidades-sencillas-con-botellas-de-plastico/03271/'
]
@bot.command()
async def consejo(ctx):
    recomendacion = random.choice(consejos)
    await ctx.send(recomendacion)

# Funcion que explica que es la contaminacion
@bot.command()
async def contaminacion(ctx):
    definicion = "Hablamos de contaminación cuando en un entorno ingresan elementos o sustancias que normalmente no deberían estar en él y que afectan el equilibrio del ecosistema."
    await ctx.send(definicion)
#tiempo de deterioro del plástico
@bot.command()
async def deterioro_del_plastico(ctx):
    tiempo_plastico = "Una simple bolsa de plástico, por ejemplo, puede tardar en descomponerse de media en torno a los 150 años y  Una botella de plástico puede tardar 1.000 años en desaparecer."
    await ctx.send(tiempo_plastico)
@bot.command()
async def contenedores(ctx):
    with open('contenedores/Contenedores-para-el-reciclaje.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

bot.run("token aqui")
