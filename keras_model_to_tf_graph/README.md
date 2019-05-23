# Convert a Keras Model into a Tensorflow Graph

- 1 Execute Freeze from Keras to sav eyour Keras Model ckpt files. In this case we will save the Trained Wide ResNet
- 2 Execute the freeze_graph.py in the following way:

    python3 freeze_graph.py --input_meta_graph=/model/model_name.ckpt.meta \  
     --input_checkpoint=/model/model_name.ckpt \ 
     --output_graph=/tmp/frozen_graph.pb \
     --output_node_names="pred_gender/Softmax:0, pred_age/Softmax:0" \  
     --input_binary=True
