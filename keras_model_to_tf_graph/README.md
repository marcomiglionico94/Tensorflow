# Convert a Keras Model into a Tensorflow Graph

- 1) Execute **freeze_from_keras.py** to save your Keras Model ckpt files. In this case we will save the Trained Wide ResNet
- 2) Execute the **freeze_graph.py** in the following way:

		$python3 freeze_graph.py --input_meta_graph=./model/model_name.ckpt.meta 
		--input_checkpoint=./model/model_name.ckpt 
		--output_graph=./model/frozen_graph.pb 
		--output_node_names="pred_gender/Softmax, pred_age/Softmax"   
		--input_binary=True "

The output node names arguments are printed when you run point 1.

If you are using a NCS2 and you want to convert the graph generated into an IR (xml and bin files) optimized model use the following command(mo_tf.py is a file that is installed with OPENVINO toolkit):

	$python3 mo_tf.py \
	--input_model xxx.pb \
	--output_dir path/to/your/output \
	--data_type FP16 \
	--input_shape [1,?,?,?]
