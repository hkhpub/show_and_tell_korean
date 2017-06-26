captions_en = []
with open("caption_short_en.txt", "r") as f:
    for line in f.readlines():
        captions_en += [line.strip()]

captions_ko = []
with open("translated_short_ko.txt", "r") as f:
    for line in f.readlines():
        captions_ko += [line.strip()]

image_ids = []
with open("image_id_short.txt", "r") as f:
    for line in f.readlines():
        image_ids += [int(line.strip())]

data = []
image_entry = None
old_image_id = -1
for en_cap, ko_cap, image_id in zip(captions_en, captions_ko, image_ids):
    if old_image_id != image_id:
        if image_entry is not None:
            data += [image_entry]
        image_entry = {"en_captions": [], "ko_captions": [], "image_id": image_id}
        old_image_id = image_id

    image_entry["en_captions"] += [en_cap]
    image_entry["ko_captions"] += [ko_cap.decode("utf8")]

data += [image_entry]
print(data[-1])

import io, json
with io.open('200data.json', 'w', encoding='utf-8') as f:
  f.write(json.dumps(data, ensure_ascii=False))

# with open("200data.json", 'w') as f:
#     json.dumps(data, f)