import discord
import dotenv
import os

dotenv.load_dotenv()

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True


class DiscordBot(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return
        if "happy birthday" in message.content.lower():
            await message.channel.send("Happy Birthday!!! 🎉🎉🎉")

    async def on_member_join(self, member):
        await member.send("Hi {}!".format(member.name))
        await member.send("Welcome to my server. I hope you enjoy your stay")
        await member.send("Please make sure to be nice to people in the server")

        channel = self.get_channel(849443705471369226)
        await channel.send("Everybody, please welcome a new member {}".format(member.name))


if __name__ == '__main__':
    bot = DiscordBot(intents=intents)
    bot.run(TOKEN)