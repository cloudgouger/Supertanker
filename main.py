import numpy as np
import sounddevice as sd
import soundfile as sf
import dearpygui.dearpygui as dpg
import os

with open("audioFilesConfig.txt", 'w+') as audioFilesConfig:
    audioFiles = audioFilesConfig.readlines()
with open("audioNameConfig.txt", 'w+') as audioNameConfig:
    audioNames = audioNameConfig.readlines()
with open("audioIconConfig.txt", 'w+') as audioIconConfig:
    audioIcons = audioIconConfig.readlines()
buttons = []



def playSound(sender, app_data, user_data):
    print(user_data)
    sfx, sR = sf.read(user_data)
    print(f"read {user_data}")
    sd.play(sfx)
    print("played sound")
def addSound(sender, app_data, user_data):
    print(user_data)

def reloadAudioFiles():
    audioFileList = os.listdir("data/sounds")
    iconFileList = os.listdir("data/icons")
    audioFileExtensionless = []
    iconFileExtensionless = []
    for i, filename in enumerate(audioFileList):
        name, fileExtension = os.path.splitext(filename)
        audioFileExtensionless.append(name)
    for i, filename in enumerate(iconFileList):
        name, fileExtension = os.path.splitext(filename)
        iconFileExtensionless.append(name)
    for i, filename in enumerate(audioFileList):
        if audioFileExtensionless[i] == iconFileExtensionless[i]:
            audioFiles.append(audioFileList[i])
            audioIcons.append(iconFileList[i])
    print(audioFileList)
    print(iconFileList)
    with open("audioFilesConfig.txt", 'w') as audioFilesConfig:
        for i in audioFileList:
            audioFilesConfig.write(f"{i}\n")
    with open("audioIconConfig.txt", 'w') as audioIconConfig:
        for i in iconFileList:
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
    for i, filename in enumerate(audioFiles):
        dpg.add_image_button(audioIcons[i], label=audioNames[i], callback=playSound, user_data=audioFiles[i], width=100, height=100)
        print("added icon")
    dpg.add_button(label="Add sounds", callback=reloadAudioFiles, tag="add_button", parent="main_window")
    dpg.set_primary_window("Supertanker", True)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context

