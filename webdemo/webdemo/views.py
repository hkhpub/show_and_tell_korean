import os
import json
from settings import PROJECT_ROOT
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from im2txt_analyzer import analyze_image

with open(os.path.join(PROJECT_ROOT, '200data.json'), "r") as f:
  image_data = json.load(f)

image_dic = dict()
for image_entry in image_data:
  image_dic[image_entry["image_id"]] = image_entry
  image_path = "/media/mscoco/COCO_train2014_%012d.jpg" % image_entry["image_id"]
  image_name = "COCO_train2014_%012d.jpg" % image_entry["image_id"]
  image_entry["name"] = image_name
  image_entry["path"] = image_path

def upload_file(request):

  if request.method == 'POST' and 'myfile' in request.FILES:
    myfile = request.FILES['myfile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    filename = '/media/'+filename
    uploaded_file_url = fs.url(filename)

    return render(request, 'upload.html', {
      'uploaded_file_url': uploaded_file_url,
      'filename': filename,
    })

  elif request.method == 'POST' and 'filename' in request.POST:
    filename = request.POST['filename']
    captions, google_captions, naver_captions = analyze_image(filename)
    context = {
      'filename': filename,
      'captions': captions,
      'google_captions': google_captions,
      'naver_captions': naver_captions,
    }
    print(context)
    return render(request, 'upload.html', context)

  return render(request, 'upload.html')

def image_gallery(request):

  context = {
      "image_data": image_data
  }
  return render(request, 'img_gallery.html', context)


def modal_view(request, imgid):
  image_id = int(imgid)
  print "image id: ", image_id
  image_entry = image_dic[image_id]
  context = {
    'en_captions': image_entry["en_captions"],
    'ko_captions': image_entry["ko_captions"],
    'image_path': image_entry["path"],
    'image_name': image_entry["name"]
  }
  return render(request, 'modal_tag_view.html', context)