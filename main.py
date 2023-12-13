import os



files = [file  for file in os.listdir("Scripts")]
count = 0
for sp in files:
    print(f"Running{sp}")
    if sp.endswith(".mp4"):
        os.system(f"nohup python {sp} &")
    if count == len(files):
        os.system(f"python {sp}")
    count+=1
