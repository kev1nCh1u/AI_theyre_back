# 他們回來了


## source
    source /opt/intel/openvino/bin/setupvars.sh

## 檔案位置

### 1. source code

    src

### 1. data

    image

### 1. 操作手冊

    doc > 操作手冊.pdf

### 1. ppt 投影片
    
    doc > PPT.pptx 

## face
```
cd /home/user/AI_theyre_back/src
```
```
python ./face_recognition_demo.py -m_fd ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-detection-retail-0004/FP16/face-detection-retail-0004.xml -m_lm ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/landmarks-regression-retail-0009/FP16/landmarks-regression-retail-0009.xml -m_reid ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-reidentification-retail-0095/FP16/face-reidentification-retail-0095.xml -l /home/user/Desktop/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so --verbose -fg "/home/user/AI_theyre_back/image/face_cut" --run_detector --allow_grow
```
```
python ./face_recognition_demo.py -m_fd ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-detection-retail-0004/FP16/face-detection-retail-0004.xml -m_lm ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/landmarks-regression-retail-0009/FP16/landmarks-regression-retail-0009.xml -m_reid ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-reidentification-retail-0095/FP16/face-reidentification-retail-0095.xml -l /home/user/Desktop/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so --verbose -fg  "/home/user/AI_theyre_back/image/face_gallery"
```

## face on windows
```
cd C:\Program Files (x86)\IntelSWTools\openvino\bin\
```
```
setupvars.bat
```
```
python G:\我的雲端硬碟\高科大\人工智慧\AI_theyre_back\src\face_recognition_demo.py -m_fd G:\我的雲端硬碟\高科大\人工智慧\AI_theyre_back\model\face-detection-retail-0004.xml -m_lm G:\我的雲端硬碟\高科大\人工智慧\AI_theyre_back\model\landmarks-regression-retail-0009.xml -m_reid G:\我的雲端硬碟\高科大\人工智慧\AI_theyre_back\model\face-reidentification-retail-0095.xml -l C:\Program Files (x86)\IntelSWTools\openvino_2019.3.334\deployment_tools\inference_engine\bin\intel64\Debug\cpu_extension_avx2.dll --verbose -fg  "G:\我的雲端硬碟\高科大\人工智慧\AI_theyre_back\image\face_gallery"
```