import os
from soundfile import SoundFile

directory = '/content/drive/MyDrive/Colab Notebooks/wav_converter/'
os.chdir(directory)

# directory = os.getcwd()

print("Return a dictionary of available formats.\n")
sf.available_formats()

print("Return a dictionary of available subtypes.\n")
sf.available_subtypes('WAV')

print("Return the default subtype for a given format.\n")
sf.default_subtype('WAV')

for filename in os.listdir(directory):
  if filename.endswith(".WAV") or filename.endswith(".wav"):
    with SoundFile(filename, 'r') as myfile:
      print(f"Filename = {myfile.name}")
      print(f"Number of Samples = {myfile.frames-1}")
      print(f"Sample Rate = {myfile.samplerate} Hz")
      if myfile.subtype == 'PCM_16':
        print(f"Resolution = 16 bits")
      if myfile.subtype == 'PCM_24':
        print(f"Resolution = 24 bits")
      if myfile.subtype == 'PCM_32' or  myfile.subtype == 'FLOAT':
        print(f"Resolution = 32 bits")
      if myfile.channels == 2:
        print(f"Channels = Stereo \n")
      else:
        print(f"Channels = Mono \n")
