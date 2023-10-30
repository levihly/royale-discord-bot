# importing libraries
import os, random, asyncio, importlib, discord
from discord import app_commands
from dotenv import load_dotenv
from draw import draw1, draw2, draw3, draw4, draw_winner

# import environment variables
load_dotenv()

TOKEN = os.getenv('TOKEN')
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'{client.user.name} {client.user.id} is logging in...')
    print(f'Version: {discord.__version__}\n')
    await tree.sync()

    await client.change_presence(activity=discord.Game('Fortnite'))

    print('Successfully connected!')



@tree.command(description='Starts a Royale match for people to join')
@app_commands.describe(setting='The setting of the battle royale.')
@app_commands.choices(setting = [
    app_commands.Choice(name='Default', value='mode_default'),
    app_commands.Choice(name='Fortnite', value='mode_fortnite'),
    app_commands.Choice(name='Zombie Apocalypse', value='mode_zombie'),
    ])
@app_commands.describe(characters='The set of characters you want to join. Default Any')
@app_commands.choices(characters = [
    app_commands.Choice(name='All', value='characters_all'),
    app_commands.Choice(name='Fortnite', value='characters_fortnite'),
    app_commands.Choice(name='Zombie Apocalypse', value='characters_zombie'),
    ])
@app_commands.describe(num_chars='The number of characters you want to join. Default 10')
async def rstart(interaction, setting: str=None, characters: str=None, num_chars: int=None):

    # setting default parameters
    if setting == None:
        setting = 'mode_default'
    if characters == None:
        characters = 'characters_all'
    if num_chars == None:
        num_chars = 10

    lobby = discord.Embed(title='ROYALE STARTING SOON!',
        description='Join the battle!',
        color=0xFFFFFF)
    lobby.add_field(name='Theme:     ', value =f'{setting}', inline=False)
    lobby.add_field(name='Character set:     ', value =f'{characters}', inline=False)
    lobby.add_field(name='# of characters:     ', value =f'{num_chars}', inline=False)
    lobby.set_thumbnail(url='https://i.imgur.com/TGRjVkM.jpg')

    join = Join(setting, characters, num_chars)

    await interaction.response.send_message(embed=lobby, view=join)

    join.message = await interaction.original_response()
    join.channel = interaction.channel


class Join(discord.ui.View):

    def __init__(self, setting = None, characters = None, num_chars = None,
                 players = list, pictures = list, chars = list, char_pics = list):
        super().__init__(timeout=7)
        
        self.setting = setting
        self.characters = characters
        self.num_chars = num_chars
        self.players = []
        self.pictures = []

    @discord.ui.button(label='Click to join!',
                       style=discord.ButtonStyle.green, emoji='⚔️')
    
    async def join_button(self, interaction: discord.Interaction,
                          button: discord.ui.Button):
        
        self.players.append(str(interaction.user.display_name))
        self.pictures.append(interaction.user.display_avatar)
        
        button.disabled = True
        button.label = "You're in!"
        button.emoji = '💪'
        
        await interaction.response.edit_message(view=self)

    async def on_timeout(self):
        
        for button in self.children:
            button.disabled = True

        mode = importlib.import_module(self.setting)
        character_set = importlib.import_module(self.characters)

        chars = character_set.characters()[0]
        char_pics = character_set.characters()[1]

        # add chosen number of characters to player list
        for i in range(self.num_chars):
            char = random.randint(0, len(chars)-1)
            # add random character to players and delete from original list so not duplicated
            self.players.append(chars[char])
            del chars[char]

            self.pictures.append(char_pics[char])
            del char_pics[char]

        if not self.players:
            button.label = 'Maybe next time?'
            button.emoji = '😔'
            timeout = discord.Embed(
            title='ROYALE CANCELED!',
                description="No one joined!",
                color=0xFFFFFF)
            timeout.set_thumbnail(url='https://i.imgur.com/E37ipb1.jpg')
        else:
            button.label = 'Battle started!'
            button.emoji = '⏲️'
            timeout = discord.Embed(
            title='ROYALE IN PROGRESS!',
                description="Who do you think's gonna win?",
                color=0xFFFFFF)
            timeout.set_thumbnail(url='https://i.imgur.com/sEVTxj6.png')

        await self.message.edit(embed=timeout, view=self)

        # until one person left
        while len(self.players) > 1:
            
            num_players = random.randint(1, min(len(self.players), 4))
            lethal = random.randint(1, 100)

            pairs = list(zip(self.players, self.pictures))
            pairs = random.sample(pairs, num_players)
            p, pic = zip(*pairs)
            
            if len(p) == 1:
                
                nonlethal = mode.one(p)[0]
                lethal1 = mode.one(p)[1]

                if lethal <= 70:
                    result = random.choice(nonlethal)

                    file = draw1('templates/1-nonlethal.png', pic)
                    
                else:
                    result = random.choice(lethal1)
                    self.players.remove(p[0])
                    self.pictures.remove(pic[0])

                    file = draw1('templates/1-lethal1.png', pic)
                    
            if len(p) == 2:
                
                nonlethal = mode.two(p)[0]
                lethal1 = mode.two(p)[1]
                lethal2 = mode.two(p)[2]

                if lethal <= 50:
                    result = random.choice(nonlethal)
                    
                    file = draw2('templates/2-nonlethal.png', pic)
                elif lethal <= 85:
                    result = random.choice(lethal1)
                    self.players.remove(p[1])
                    self.pictures.remove(pic[1])

                    file = draw2('templates/2-lethal1.png', pic)
                else:
                    result = random.choice(lethal2)
                    self.players.remove(p[0])
                    self.players.remove(p[1])
                    self.pictures.remove(pic[0])
                    self.pictures.remove(pic[1])

                    file = draw2('templates/2-lethal2.png', pic)

            if len(p) == 3:
                
                nonlethal = mode.three(p)[0]
                lethal1 = mode.three(p)[1]
                lethal2 = mode.three(p)[2]
                lethal3 = mode.three(p)[3]
                
                if lethal <= 50:
                    result = random.choice(nonlethal)

                    file = draw3('templates/3-nonlethal.png', pic)
                elif lethal <= 75:
                    result = random.choice(lethal1)
                    self.players.remove(p[2])
                    self.pictures.remove(pic[2])

                    file = draw3('templates/3-lethal1.png', pic)
                elif lethal <= 90:
                    result = random.choice(lethal2)
                    self.players.remove(p[1])
                    self.players.remove(p[2])
                    self.pictures.remove(pic[1])
                    self.pictures.remove(pic[2])

                    file = draw3('templates/3-lethal2.png', pic)
                else:
                    result = random.choice(lethal3)
                    self.players.remove(p[0])
                    self.players.remove(p[1])
                    self.players.remove(p[2])
                    self.pictures.remove(pic[0])
                    self.pictures.remove(pic[1])
                    self.pictures.remove(pic[2])
                    

                    file = draw3('templates/3-lethal3.png', pic)

            if len(p) == 4:

                nonlethal = mode.four(p)[0]
                lethal1 = mode.four(p)[1]
                lethal2 = mode.four(p)[2]
                lethal3 = mode.four(p)[3]
                lethal4 = mode.four(p)[4]

                if lethal <= 50:
                    result = random.choice(nonlethal)

                    file = draw4('templates/4-nonlethal.png', pic)
                elif lethal <= 70:
                    result = random.choice(lethal1)
                    self.players.remove(p[3])
                    self.pictures.remove(pic[3])

                    file = draw4('templates/4-lethal1.png', pic)
                elif lethal <= 80:
                    result = random.choice(lethal2)
                    self.players.remove(p[2])
                    self.players.remove(p[3])
                    self.pictures.remove(pic[2])
                    self.pictures.remove(pic[3])

                    file = draw4('templates/4-lethal2.png', pic)
                elif lethal <= 90:
                    result = random.choice(lethal3)
                    self.players.remove(p[1])
                    self.players.remove(p[2])
                    self.players.remove(p[3])
                    self.pictures.remove(pic[1])
                    self.pictures.remove(pic[2])
                    self.pictures.remove(pic[3])

                    file = draw4('templates/4-lethal3.png', pic)
                else:
                    result = random.choice(lethal4)
                    self.players.remove(p[0])
                    self.players.remove(p[1])
                    self.players.remove(p[2])
                    self.players.remove(p[3])
                    self.pictures.remove(pic[0])
                    self.pictures.remove(pic[1])
                    self.pictures.remove(pic[2])
                    self.pictures.remove(pic[3])

                    file = draw4('templates/4-lethal4.png', pic)

            event = discord.Embed(
                description=f'{result}',
                color=0xFFFFFF)
            event.set_image(url="attachment://pic.jpg")
            
            await self.channel.send(file=file, embed=event)

            await asyncio.sleep(3)
            
        if self.players:
            winner = self.players[0]
            winner_pic = self.pictures[0]

            comment = random.choice(mode.winner_comment(p))

            file = draw_winner(winner_pic)
            
        else:
            winner = 'No one'

            comment = random.choice(mode.no_winner_comment())

            file = None

        win_card = discord.Embed(
                description=f'{winner} wins! {comment}',
                color=0xFFFFFF)
        win_card.set_image(url="attachment://pic.jpg")
            
        await self.channel.send(file=file, embed=win_card)
                
            


# run
client.run(TOKEN)
