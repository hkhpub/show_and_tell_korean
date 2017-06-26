# Directory containing preprocessed MSCOCO data.
PRJ_HOME="/home/hkh/sources/im2txt/im2txt"
MSCOCO_DIR="/hdd/data/mscoco"

# Inception v3 checkpoint file.  
INCEPTION_CHECKPOINT="${PRJ_HOME}/data/inception_v3.ckpt"    

# Directory to save the model.  
MODEL_DIR="${PRJ_HOME}/model"    

# Build the model.
cd ~/sources/im2txt
bazel build -c opt //im2txt/...

# Run the training script.  
# python train.py --input_file_pattern="${MSCOCO_DIR}/tfdata/train-?????-of-00256" --inception_checkpoint_file="${INCEPTION_CHECKPOINT}" --train_dir="${MODEL_DIR}/train" --train_inception=false --number_of_steps=100000
bazel-bin/im2txt/train \
--input_file_pattern="${MSCOCO_DIR}/tfdata/train-?????-of-00256" \
--inception_checkpoint_file="${INCEPTION_CHECKPOINT}" \
--train_dir="${MODEL_DIR}/train" \
--train_inception=false \
--number_of_steps=1000000
