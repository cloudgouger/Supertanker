import numpy as np
import sounddevice as sd
import soundfile as sf
import dearpygui.dearpygui as dpg
import os

with open("audioFilesConfig.txt", 'r') as audioFilesConfig:
    tempString = audioFilesConfig.read()
    print(tempString)
    audioFiles = tempString.splitlines()
with open("audioNameConfig.txt", 'r') as audioNameConfig:
    tempString = audioNameConfig.read()
    audioNames = tempString.splitlines()
with open("audioIconConfig.txt", 'r') as audioIconConfig:
    tempString = audioIconConfig.read()
    audioIcons = tempString.splitlines()
print(audioFiles)
print(audioIcons)
audioFileExtensionless = []
iconFileExtensionless = []


def playSound(sender, app_data, user_data):
    print(user_data)
    sfx, sR = sf.read(f"data/sounds/{user_data}")
    print(f"read {user_data}")
    sd.play(sfx)
    print("played sound")
def addSound(sender, app_data, user_data):
    print(user_data)

def reloadAudioFiles():
    audioFiles = os.listdir("data/sounds")
    iconFiles = os.listdir("data/icons")
    
    
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
    with open("audioFilesConfig.txt", 'w') as audioFilesConfig:
        for i in audioFiles:
            audioFilesConfig.write(f"{i}\n")
    with open("audioIconConfig.txt", 'w') as audioIconConfig:
        for i in iconFiles:
            audioIconConfig.write(f"{i}\n")

'''
def loadButtons(buttons, audioIcons, audioFiles):
    print("Load buttons has been run")
    for i in buttons:
        try:
            dpg.delete_item(i)
            print(f"deleted item {i}")
        except:
            print("could not delete button, do not be alarmed.")
    buttons = []
    for i, iconName in enumerate(audioIcons):
        imageWidth, imageHeight, imageChannels, imageData = dpg.load_image(iconName)
        with dpg.texture_registry():
            dpg.add_static_texture(
                width=imageHeight,
                height=imageWidth,
                default_value=imageData,
                tag=iconName
            )
            print(f"added texture {iconName}")
    for i, filename in enumerate(audioFiles):
        dpg.add_image_button(audioIcons[i], label=audioFiles[i], callback=playSound, user_data=audioFiles[i], width=100, height=100, tag = f"audio_button_{i}")
        buttons.append(f"audio_button_{i}")
    dpg.delete_item("Supertanker")
    main_window = dpg.window(tag="Supertanker")
    dpg.add_button(label="Add sounds", callback=reloadAudioFiles, tag="add_button", parent=main_window)
    dpg.set_primary_window("Supertanker", True)
'''

        


dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window(tag="Supertanker"):
    for i, iconName in enumerate(audioIcons):
        print(f"loading {iconName}")
        print(dpg.load_image(iconName))
        imageWidth, imageHeight, imageChannels, imageData = dpg.load_image(f"data/icons/{iconName}")
        with dpg.texture_registry():
            dpg.add_static_texture(
                width=imageHeight,
                height=imageWidth,
                default_value=imageData,
                tag=iconName
            )
            print(f"added texture {iconName}")
    for i, filename in enumerate(audioFiles):
        print(audioIcons[i])
        dpg.add_image_button(audioIcons[i], label="button", callback=playSound, user_data=audioFiles[i], width=100, height=100)
        print("added icon")
    dpg.add_button(label="Add sounds", callback=reloadAudioFiles, tag="add_button", parent="main_window")
    dpg.set_primary_window("Supertanker", True)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context

