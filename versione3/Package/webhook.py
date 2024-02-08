from discord_webhook import DiscordWebhook, DiscordEmbed
from Package import screenBot




def webhook_print( url , title , description , img_name = None , color = 'ff0000' , author = None , trofei_screen = False):
    pc_user = "Luke-Laptop_real"
    
    webhook = DiscordWebhook(url=url)
    embed = DiscordEmbed(title=title,
                         description=description, color=color)
    embed.set_timestamp()
    embed.set_footer(text = pc_user)
    webhook.add_embed(embed)

    if(trofei_screen):
        if(img_name != None):
            #screenBot.take_screenshot(870, 290, 490, 200, label='_dd_termination')  # Trofei screen
            screenBot.take_screenshot(830, 60, 570, 960, label='_dd_termination')   # Full App screen
            with open("./Screenshot/screenshot_dd_termination.png", "rb") as f:
                webhook.add_file(file=f.read(), filename=img_name)
    else:
        if(img_name != None):
            screenBot.take_screenshot(830, 60, 570, 960, label='_dd_termination')   # Full App screen
            with open("./Screenshot/screenshot_dd_termination.png", "rb") as f: 
                webhook.add_file(file=f.read(), filename=img_name)
    response = webhook.execute()   # Invio webhook

