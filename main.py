import numpy as np
import sounddevice as sd
import soundfile as sf
import dearpygui.dearpygui as dpg
import os
import shutil

directories = os.listdir('data/')
searchableDirs = []
audioFiles = []
tempDict = {}
for x in directories:
    if '.' not in x:
        searchableDirs.append(x)
for x in searchableDirs:
    files = os.listdir(f'data/{x}/')
    files.sort()
    for y in files:
        tempDict['name'] = x
        if '.' in y:
            if '.mp3' in y:
                tempDict['audio'] = y
            if '.png' in y:
                tempDict['icon'] = y
    audioFiles.append(tempDict)
    tempDict = {}
print(audioFiles)
        
exit()



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

