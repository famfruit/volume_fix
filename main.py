from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import sounddevice as sd
import numpy as np
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))



global_vol_ind = []

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    if volume_norm > 1:
        global_vol_ind.append("over")
        #print("MORE THAN WE WANT")
    #print("                                                                                                             ", end="\r")
    #print ("O" * int(volume_norm), end="\r")

if __name__ == "__main__":
    # Unmute
    print(" ")
    volume.SetMute(0, None)
    # Max volume
    volume.SetMasterVolumeLevel(0.0, None)
    print("Sound status:   ON")
    print("Mic status:     Prata igenom micen i 10 sekunder!", end="\r\n")
    with sd.Stream(callback=print_sound):
        sd.sleep(5000)
        if len(global_vol_ind) > 0:
            print("Mic status:     ON      ", end="\r\n")
            print("\nTestet är klart och nedan ser du information från testet.")
            print("Ljudet är på. ")
            print("Micen är på.")
        else:
            print("Mic status:     OFF")
            print("\nTestet är klart och nedan ser du information från testet.")
            print("Ljudet är på. ")
            print("Micen är av.")
            print("För att fixa problemet, se till att micknappen på hörlurarna är på rätt läge. Om det ändå inte fungerar ring ludde så löser han det.")
