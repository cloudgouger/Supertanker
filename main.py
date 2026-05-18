import numpy as np
import sounddevice as sd
import soundfile as sf
import dearpygui.dearpygui as dpg

audioFiles = [
    "squeaky-toy_1.mp3",
    "mlg-airhorn.mp3",
    "cow-moo.mp3",
    "vine-boom.mp3"
]

audioNames = [
    "Squeaky Toy",
    "MLG Airhorn",
    "Cow Moo",
    "Vine boom"
]

audioIcons = [
    "rubber-duck.png",
    "air-horn.png",
    "cow.png",
    "explosion.png"
]

def button_callback(sender, app_data, user_data):
    print(user_data)
    sfx, sR = sf.read(user_data)
    print(f"read {user_data}")
    sd.play(sfx)
    print("played sound")



dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

for i, iconName in enumerate(audioIcons):
    imageWidth, imageHeight, imageChannels, imageData = dpg.load_image(iconName)
    with dpg.texture_registry():
        dpg.add_static_texture(
            width=imageHeight,
            height=imageWidth,
            default_value=imageData,
            tag=iconName
        )

with dpg.window(tag="Supertanker"):
    dpg.add_text("Test")
    for i, filename in enumerate(audioFiles):
        dpg.add_image_button(audioIcons[i], label=audioNames[i], callback=button_callback, user_data=audioFiles[i], width=100, height=100)
dpg.set_primary_window("Supertanker", True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context

