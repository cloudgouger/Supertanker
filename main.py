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

def button_callback(sender, app_data, user_data):
    print(user_data)
    sfx, sR = sf.read(user_data)
    print(f"read {user_data}")
    sd.play(sfx)
    sd.wait()

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window(label="Supertanker"):
    dpg.add_text("Test")
    dpg.add_button(label="Press me!", callback=button_callback, user_data=audioFiles[1])
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context




#print("Enter the number of a sound you'd like to play (1-4): ")
#answer = input()
#playAudio(audioFiles[int(answer)-1])