import time
import os
# get the start time
st = time.time()

# main program
# find sum to first 1 million numbers

exe_file_path = "" # file path of exe file

original = "\"home/ex\"" # parameters

ngpin = "\"home/ex\""#paramteres



command = f" python {exe_file_path} --ok_comp {original} --ok_pins_csv {original}/pins.csv  --ng_comps_path {ngpin} --outdir \"C:/Users/Downloads/results-6thmay/output/result_ng\"  --type  \"\" --shape"
# print(command)
os.system(command)  

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

"""
image = PIL.Image.open('.jpg')
image = cv2.imread(PIL.Image.open('.jpg'))
"""