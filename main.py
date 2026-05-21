import numpy as np
import sounddevice as sd
import soundfile as sf
import dearpygui.dearpygui as dpg
import os
import shutil

audioFiles = os.listdir("data/sounds")
iconFiles = os.listdir("data/icons")

audioFileExtensionless = []
iconFileExtensionless = []
audioToAdd = []
iconToAdd = []

for filename in audioFiles:
    if filename[0] == '.':
        audioFiles.remove(filename)
for filename in iconFiles:
    if filename[0] == '.':
        iconFiles.remove(filename)

for i, filename in enumerate(audioFiles):
    name, fileExtension = os.path.splitext(filename)
    audioFileExtensionless.append(name)
for i, filename in enumerate(iconFiles):
    name, fileExtension = os.path.splitext(filename)
    iconFileExtensionless.append(name)

audioFiles.sort()
iconFiles.sort()

print(audioFiles)
print(iconFiles)
audioFileExtensionless = []
iconFileExtensionless = []


def playSound(sender, app_data, user_data):
    print(user_data)
    sfx, sR = sf.read(f"data/sounds/{user_data}")
    print(f"read {user_data}")
    sd.play(sfx)
    print("played sound")

def addAudio(sender, app_data, user_data):
    audioToAdd.append(app_data['file_path_name'])
    audioToAdd.append(app_data['file_name'])
    shutil.copy2(app_data['file_path_name'], f'data/sounds/{app_data['file_name']}')

def addIcon(sender, app_data, user_data):
    iconToAdd.append(app_data['file_path_name'])
    iconToAdd.append(app_data['file_name'])
    

def addEntry(sender, app_data, user_data):
    if (len(audioToAdd) == 2 and len(iconToAdd) == 2):
        shutil.copy2(audioToAdd[0], f'data/sounds/{audioToAdd[1]}')
        shutil.copy2(iconToAdd[0], f'data/sounds/{iconToAdd[1]}')

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()


with dpg.file_dialog(show=False, tag="mp3_dialog", width=700, height=400,callback=addAudio, user_data="mp3"):
    dpg.add_file_extension(".mp3")
with dpg.file_dialog(show=False, tag="png_dialog", width=700, height=400,callback=addAudio, user_data="png"):
    dpg.add_file_extension(".png")

with dpg.font_registry():
    newFont = dpg.add_font("data/opensans.ttf", 20)

def showDialogs():
    dpg.show_item("mp3_dialog") 
    dpg.show_item("png_dialog")


with dpg.window(tag="Supertanker"):
    dpg.bind_font(newFont)

    dpg.add_button(label="add sound", callback=showDialogs)
    for i, iconName in enumerate(iconFiles):
        print(f"loading {iconName}")
        print(dpg.load_image(iconName))
        try:
            imageWidth, imageHeight, imageChannels, imageData = dpg.load_image(f"data/icons/{iconName}")
            with dpg.texture_registry():
                dpg.add_static_texture(
                    width=imageHeight,
                    height=imageWidth,
                    default_value=imageData,
                    tag=iconName
                )
                print(f"added texture {iconName}")
        except:
            print("texture could not be added")
    for i, filename in enumerate(audioFiles):
        try:
            dpg.add_image_button(iconFiles[i], label="button", callback=playSound, user_data=audioFiles[i], width=100, height=100)
            print(f"added icon {iconFiles[i]}")
        except:
            print(f"failed {filename}")
    dpg.set_primary_window("Supertanker", True)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context

