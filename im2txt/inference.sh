PRJ_HOME="/home/hkh/sources/im2txt"
CHECKPOINT_PATH="${PRJ_HOME}/im2txt/model/train"

VOCAB_FILE="/hdd/data/mscoco/tfdata/word_counts.txt"

IMAGE_FILE="/hdd/data/mscoco/val2014/COCO_val2014_000000225405.jpg"

# Build the model.
cd ~/sources/im2txt
bazel build -c opt //im2txt:run_inference

export CUDA_VISIBLE_DEVICES=""

# Run inference to generate captions.
bazel-bin/im2txt/run_inference \
  --checkpoint_path=${CHECKPOINT_PATH} \
  --vocab_file=${VOCAB_FILE} \
  --input_files=${IMAGE_FILE}

