from contractlib.annotation import process
import os
def convert_to_training_data(
				input_dir:str ,output_dir:str,
				whitelist: dict={} ,blacklist: dict ={}
				
			)
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)
	
	process.raw_to_multilabel(
					input_dir, output_dir,
					label_whitelist=whitelist, label_blacklist=blacklist,
	)
	
if __name__=='__main__':
	input_dir="/home/libaokui2021/ee/data/"
	output_dir="/home/libaokui2021/ee/data_pro/"
	convert_to_training_data(input_dir,output_dir)