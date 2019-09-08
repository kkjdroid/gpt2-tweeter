import gpt_2_simple as gpt2
sess = gpt2.start_tf_sess()
def fuck(model_name = "124M", data_path='C:\\\\Users\\pogop\\OneDrive\\Desktop\\NKJ.txt', steps = 600, run_name = 'run1'):
	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/
	gpt2.finetune(sess,data_path,model_name=model_name,steps=steps,run_name=run_name)   # steps is max number of training steps
	return
