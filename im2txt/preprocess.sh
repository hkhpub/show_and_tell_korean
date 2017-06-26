SCRATCH_DIR="/hdd/data/mscoco"
TRAIN_IMAGE_DIR="${SCRATCH_DIR}/train2014"
VAL_IMAGE_DIR="${SCRATCH_DIR}/val2014"
TRAIN_CAPTIONS_FILE="${SCRATCH_DIR}/annotations/captions_train2014.json"
VAL_CAPTIONS_FILE="${SCRATCH_DIR}/annotations/captions_val2014.json"
OUTPUT_DIR="${SCRATCH_DIR}/output"

python data/build_mscoco_data.py \
  --train_image_dir="${TRAIN_IMAGE_DIR}" \
  --val_image_dir="${VAL_IMAGE_DIR}" \
  --train_captions_file="${TRAIN_CAPTIONS_FILE}" \
  --val_captions_file="${VAL_CAPTIONS_FILE}" \
  --output_dir="${OUTPUT_DIR}" \
  --word_counts_output_file="${OUTPUT_DIR}/word_counts.txt"