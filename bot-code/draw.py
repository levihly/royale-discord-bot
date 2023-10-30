from easy_pil import Editor, load_image
from discord import File

def draw1(template, pic):
    background = Editor(template)
    profile_image1 = load_image(str(pic[0]))
    profile1 = Editor(profile_image1).resize((150, 150)).circle_image()
    background.paste(profile1, (425,75))
    
    file = File(fp=background.image_bytes, filename="pic.jpg")
    return file

def draw2(template, pic):
    background = Editor(template)
    profile_image1 = load_image(str(pic[0]))
    profile_image2 = load_image(str(pic[1]))
    profile1 = Editor(profile_image1).resize((150, 150)).circle_image()
    profile2 = Editor(profile_image2).resize((150, 150)).circle_image()
    background.paste(profile1, (300,75))
    background.paste(profile2, (550,75))
    
    file = File(fp=background.image_bytes, filename="pic.jpg")
    return file

def draw3(template, pic):
    background = Editor(template)
    profile_image1 = load_image(str(pic[0]))
    profile_image2 = load_image(str(pic[1]))
    profile_image3 = load_image(str(pic[2]))
    profile1 = Editor(profile_image1).resize((150, 150)).circle_image()
    profile2 = Editor(profile_image2).resize((150, 150)).circle_image()
    profile3 = Editor(profile_image3).resize((150, 150)).circle_image()
    background.paste(profile1, (175,75))
    background.paste(profile2, (425,75))
    background.paste(profile3, (675,75))

    file = File(fp=background.image_bytes, filename="pic.jpg")
    return file


def draw4(template, pic):
    background = Editor(template)
    profile_image1 = load_image(str(pic[0]))
    profile_image2 = load_image(str(pic[1]))
    profile_image3 = load_image(str(pic[2]))
    profile_image4 = load_image(str(pic[3]))
    profile1 = Editor(profile_image1).resize((150, 150)).circle_image()
    profile2 = Editor(profile_image2).resize((150, 150)).circle_image()
    profile3 = Editor(profile_image3).resize((150, 150)).circle_image()
    profile4 = Editor(profile_image4).resize((150, 150)).circle_image()
    background.paste(profile1, (50,75))
    background.paste(profile2, (300,75))
    background.paste(profile3, (550,75))
    background.paste(profile4, (800,75))

    file = File(fp=background.image_bytes, filename="pic.jpg")
    return file

def draw_winner(winner_pic):
    background = Editor('templates/winner.png')
    profile_image = load_image(str(winner_pic))
    profile = Editor(profile_image).resize((250,250)).circle_image()
    background.paste(profile, (225, 100))

    file = File(fp=background.image_bytes, filename="pic.jpg")
    return file
