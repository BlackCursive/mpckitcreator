import os
from read_wav_files import *
from templates import *

directory_path = os.getcwd()
folder_name = os.path.basename(directory_path)

### Write Program Name
programName = template.replace('__PROGRAMNAME__', folder_name)

### Write all Wav Files and Number of Samples to instruments
stringList = []
for count, x, y in zip(range(len(sample_list)),sample_list, no_of_frames):
  stringList.append(instruments.replace('__SAMPLENAME__', x).replace('__SLICEEND__', str(y)).replace('__INSTNUMBER__', str(count+1)))

### Write instruments to Program
instrumentAndLayers = programName.replace('__INSTRUMENTSANDLAYERS__', '\n'.join(stringList))

### Create New File With Folder Name
newFilename = folder_name + ".xpm"

### Create New MPC Program
with open(newFilename, "w") as newProgramKitFile:
  newProgramKitFile.write(instrumentAndLayers)
