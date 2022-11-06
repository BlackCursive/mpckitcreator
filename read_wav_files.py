import os
from soundfile import SoundFile

directory_path = os.getcwd()
folder_name = os.path.basename(directory_path)

sample_list = []
no_of_frames = []

### Function to get Filename and Number of Samples from WAV files
def wavFolder(folder):
  count=0
  for file in os.listdir(directory_path):
    if file.endswith(".WAV") or file.endswith(".wav"):
      with SoundFile(file, 'r') as myfile:
        count +=1
        filename = myfile.name
        sample_list.append(filename)
        frames = myfile.frames-1
        no_of_frames.append(frames)
        print(f"{count} - Sample Name: {filename} / No. of Frames: {frames}")
wavFolder(directory_path)
