import os
from soundfile import SoundFile
import xml.etree.ElementTree as ET

tree = ET.parse('mpc.xpm')
root = tree.getroot()

directory = os.getcwd()

sample_list = []
no_of_frames = []

def wavFolder(folder):
  for file in os.listdir(directory):
    if file.endswith(".WAV") or file.endswith(".wav"):
      with SoundFile(file, 'r') as myfile:
        filename = myfile.name
        sample_list.append(filename)
        frames = myfile.frames-1
        no_of_frames.append(frames)
        # print(f"file = {sample_list}\n")
        # print(f"Number of Frames = {no_of_frames}\n")
wavFolder(directory)


def write_smpl_list():
  for layerNo, sample in zip(range(0, 128), range(len(sample_list))):
    if sample != None:
      SampleName = root[1][22][layerNo][66][0][18].text
      SampleName = sample_list[sample]
      # print(f"{sample} Sample Name : {smplTxt}")
      SliceEnd = root[1][22][layerNo][66][0][24].text
      SliceEnd = no_of_frames[sample]
    else:
      pass
# write_smpl_list()

# tree.write('new.xpm', encoding='utf-8')

# for i in range(0,128):
#   print(f"Insrument Number - {root[1][22][i].attrib}\n")

def read_smpl_list(xpm):
  pads = 127
  tree = ET.parse(xpm)
  root = tree.getroot()
  for i in range(0,pads):
    smplTxt = root[1][2][i][66][0][18].text
    slcEnd = root[1][22][i][66][0][24].text
    if smplTxt != None:
      print(f"{i} Sample Name : {smplTxt}")
      print(f"{i} Slice End : {slcEnd}")
    else:
      pass
read_smpl_list('new.xpm')
