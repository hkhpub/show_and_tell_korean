# Show And Tell 한국어 버전

This is the final project for Multimedia course CSE6501

## 1. 이미지 캡션 생성
   * Google's [im2txt](https://github.com/tensorflow/models/tree/master/im2txt) 모델 사용 
   * im2txt 설치 및 훈련 방법은 해당 Github repo에 정리되어 있음.
   * 유의해야 할 점은 CNN image 분석 모델은 pre-trained 모델 파일을 사용하고 LSTM이 추가된 언어생성 모델은 직접 훈련해야 됨.

### 시스템 구조

![](/docs/system_architecture.png)

## 2. 이미지 캡션 생성 데모 페이지
   * webdemo 폴더에 있음.
   * python django framework를 사용함.
   
![](/docs/demo1.png)

#### 2.1 django 설치
    pip install django
#### 2.2 네이버 번역 API 연동
[https://developers.naver.com/products/translator](https://developers.naver.com/products/translator)
    
> Naver developer Client ID, Client Secret 필요함.

#### 2.3 구글 번역 연동
Python Library 사용 - [Googletrans](http://py-googletrans.readthedocs.io/en/documentation/)

#### 2.4 실행방법
> webdemo 폴더에서 다음 명령어 실행

    python manage.py runserver 0.0.0.0:8000
   
#### 2.5 show and tell 캡션 생성 모델 호출
im2txt\_analyzer.py 파일의 analyze_image 함수에 정의되어 있고 주의 할 부분은 다음 3가지 파일의 경로를 올바르게 지정해야 함.
> 1. tensorflow checkpoint 파일
>
> 2. vocabulary 파일
> 
> 3. 업로드한 분석 대상 이미지 파일

예시
    
    FLAGS = {
        "checkpoint_path": "/home/hkh/sources/im2txt/im2txt/model/train",
        "vocab_file": "/hdd/data/mscoco/tfdata/word_counts.txt",
        "input_files": "/home/hkh/sources/im2txt/webdemo"+filename,
    }

## 3. 한국어 이미지 캡션 수집 툴
* 데모 페이지와 동일하게 webdemo 웹 어플리케이션으로 구성됨.
* 현재 200이미지를 대상으로 구성되었고 추후 MSCOCO 전체 8만장 이미지를 대상으로 확장할 예정임.
* 자세한 부분은 views.py 파일의 image\_gallery, modal\_view 참조.

![](/docs/demo2.png)

![](/docs/demo3.png)

## 4. 시스템 데모 동영상
[![동영상보기](/docs/video_thumbnail.png)](https://www.youtube.com/watch?v=jWRQNcan0tg)
