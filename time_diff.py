import time
import os
# get the start time
st = time.time()

# main program
# find sum to first 1 million numbers

exe_file_path = "C:/Users/Dimaag-2022/Desktop/Projects/ngtransfer_V3.2.7_exe/ngtransfer_V3.2.7/ngtransfer_V3.2.7.exe"

exe_file_path = "C:/Users/Dimaag-2022/Desktop/Projects/ngtransfer_V3.2.6_gpu/ngtransfer_V3.2.6_multipleNgPins.py"

original = "\"C:/Users/Dimaag-2022/Desktop/Projects/ngtransfer_V3.2.7_exe/sample_test_ngTransfer/0000000333/Sop/Component/0000000000000000/00000011000000000000005\""

ngpin = "\"C:/Users/Dimaag-2022/Desktop/Projects/ngtransfer_V3.2.7_exe/sample_test_ngTransfer/ng_pins_paths.csv\""

tpe = "sop"

command = f" python {exe_file_path} --ok_comp {original} --ok_pins_csv {original}/pins.csv  --ng_comps_path {ngpin} --outdir \"C:/Users/Dimaag-2022/Downloads/results-6thmay/output/result_ng\"  --type  \"sop\" --shape"
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