import os
from random import sample
from soundfile import SoundFile
import xml.etree.ElementTree as ET

directory_path = os.getcwd()
folder_name = os.path.basename(directory_path)

sample_list = []
no_of_frames = []

### Function to get Filename and Number of Samples from WAV files
def wavFolder(folder):
  for file in os.listdir(directory_path):
    if file.endswith(".WAV") or file.endswith(".wav"):
      with SoundFile(file, 'r') as myfile:
        filename = myfile.name
        sample_list.append(filename)
        frames = myfile.frames-1
        no_of_frames.append(frames)
        # print(f"file = {sample_list}\n")
        # print(f"Number of Frames = {no_of_frames}\n")
wavFolder(directory_path)

###
with open("template.xml", "r") as templateFile:
    template = templateFile.read()

template = template.replace('__PROGRAMNAME__', folder_name)

with open("instrument.xml", "r") as instrumentFile:
    instrument = instrumentFile.read()

# for x, y in zip(sample_list, no_of_frames):
#   # instrument = instrument.replace('__INSTNUMBER__', samplename)
#   with open('test.xml', "a") as file:
#     instrument = instrument.replace('__SAMPLENAME__', x).replace('__SLICEEND__', str(y))
#     file.write(instrument)

for count, x, y in zip(range(len(sample_list)),sample_list, no_of_frames):
  with open('test.xml', "a") as file:
    file.write(instrument.replace('__SAMPLENAME__', x).replace('__SLICEEND__', str(y)).replace('__INSTNUMBER__', str(count+1)))
    file.write("\n")

# instrumentandlayers = instrument.replace('__INSTRUMENTSANDLAYERS__')

newFilename = folder_name + ".xpm"

# with open(newFilename, "w") as file:
#     file.write(template)
    # file.write(instrument)

###

### Function to get Filename and Number of Samples from newly created Program kit
def read_smpl_list(xpm):
  pads = 127
  tree = ET.parse(xpm)
  root = tree.getroot()
  for i in range(0,pads):
    smplTxt = root[1][22][i][66][0][18].text
    slcEnd = root[1][22][i][66][0][24].text
    if smplTxt != None:
      print(f"{i+1} Sample Name : {smplTxt} / Slice End : {slcEnd}")
    else:
      pass
# read_smpl_list(newFilename)
