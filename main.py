import os



files = [file  for file in os.listdir("Scripts")]
for sp in files:
    print(f"Running{sp}")
    os.system(f"nohup python {sp} &")
