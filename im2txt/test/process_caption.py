import tensorflow as tf
import json
from collections import OrderedDict

train_caption_file = "/hdd/data/mscoco/annotations/captions_train2014.json"
val_caption_file = "/hdd/data/mscoco/annotations/captions_val2014.json"

def _load_and_process_metadata(captions_file):
  """Loads image metadata from a JSON file and processes the captions.

  Args:
    captions_file: JSON file containing caption annotations.
    image_dir: Directory containing the image files.

  Returns:
    A list of ImageMetadata.
  """
  with tf.gfile.FastGFile(captions_file, "r") as f:
    caption_data = json.load(f)

  sorted_annotations = sorted(caption_data['annotations'], key=lambda k: k['image_id'])

  with open("image_id_list.txt", "w") as wfimg:
    with open("caption_list.txt", "w") as wfcap:
      for annotation in sorted_annotations:
        caption = annotation['caption'].replace("\n", " ")
        wfimg.write(("%d\n" % annotation["image_id"]))
        wfcap.write(caption.strip()+"\n")

  # Extract the filenames.
  id_to_filename = [(x["id"], x["file_name"]) for x in caption_data["images"]]

  # Extract the captions. Each image_id is associated with multiple captions.
  id_to_captions = {}
  for annotation in caption_data["annotations"]:
    image_id = annotation["image_id"]
    caption = annotation["caption"]
    id_to_captions.setdefault(image_id, [])
    id_to_captions[image_id].append(caption)
    if image_id == 581921:
      print(caption)


  assert len(id_to_filename) == len(id_to_captions)
  assert set([x[0] for x in id_to_filename]) == set(id_to_captions.keys())
  print("Loaded caption metadata for %d images from %s" %
        (len(id_to_filename), captions_file))

if __name__ == "__main__":
  _load_and_process_metadata(train_caption_file)
  pass