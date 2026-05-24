import numpy as np
import sounddevice as sd
import soundfile as sf
import dearpygui.dearpygui as dpg
import os
import shutil

directories = os.listdir('data/')
searchableDirs = []
audioFiles = []
textButtons = []
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

def setDevice(sender, app_data, user_data):
    sd.default.device = app_data

def playSound(sender, app_data, user_data):
    print(f"button pressed: {sender}")
    print(user_data)
    sfx, sR = sf.read(user_data)
    print(f"read {user_data}")
    sd.play(sfx)
    print("played sound")



dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()


#with dpg.file_dialog(show=False, tag="mp3_dialog", width=700, height=400,callback=addAudio, user_data="mp3"):
    #dpg.add_file_extension(".mp3")
#with dpg.file_dialog(show=False, tag="png_dialog", width=700, height=400,callback=addAudio, user_data="png"):
    #dpg.add_file_extension(".png")

with dpg.font_registry():
    newFont = dpg.add_font("data/opensans.ttf", 20)

def showDialogs():
    dpg.show_item("mp3_dialog") 
    dpg.show_item("png_dialog")


with dpg.window(tag="Supertanker"):
    dpg.bind_font(newFont)
    for i, texname in enumerate(audioFiles):
        try:
            print(f"trying to add data/{texname['name']}/{texname['icon']}")
            imageWidth, imageHeight, imageChannels, imageData = dpg.load_image(f"data/{texname['name']}/{texname['icon']}")
            with dpg.texture_registry():
                dpg.add_static_texture(
                    width=imageWidth,
                    height=imageHeight,
                    default_value=imageData,
                    tag=texname['name']
                    
                )
            print("added successfully")
        except:
            print("failed to add texture to registry. adding sound without icon")
            textButtons.append(texname['name'])
    for i, filename in enumerate(audioFiles):
        for x in textButtons:
            if x == filename['name']:
                try:
                    print(f"trying to add button {x}")
                    dpg.add_button(label=filename['name'], callback=playSound, user_data=f"data/{filename['name']}/{filename['audio']}", width=100, height=100)
                except:
                    print("could not add text button")
        try:
            print(f"trying to add button {filename['name']}")
            dpg.add_image_button(filename['name'], callback=playSound, user_data=f"data/{filename['name']}/{filename['audio']}", width=100, height=100)
        except:
            print("could not add image button")
    audioDevices = sd.query_devices()
    deviceNames = []
    for x in audioDevices:
        deviceNames.append(f"{x['name']}")
    dpg.add_combo(items=deviceNames, callback=setDevice)

    dpg.set_primary_window("Supertanker", True)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context

