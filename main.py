import os



files = [file  for file in os.listdir("Scripts")]
for sp in files:
    print(f"Running{sp}")
    if list.index(sp) == len(files)-1:
          os.system(f"python {sp} ")
    else:
      os.system(f"nohup python {sp} &")
