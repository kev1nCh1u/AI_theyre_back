# 他們回來了

## 檔案位置

### 1. source code
    
    face_recognition_demo > face_recognition_demo.py

    src

### 1. data

    face_data

    face_gallery

### 1. 操作手冊

    操作手冊.pdf

### 1. ppt 投影片

    PPT.pptx

## face
```
cd /home/user/AI_theyre_back/src

python ./face_recognition_demo.py -m_fd ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-detection-retail-0004/FP16/face-detection-retail-0004.xml -m_lm ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/landmarks-regression-retail-0009/FP16/landmarks-regression-retail-0009.xml -m_reid ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-reidentification-retail-0095/FP16/face-reidentification-retail-0095.xml -l /home/user/Desktop/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so --verbose -fg "/home/user/AI_theyre_back/image/face_cut" --run_detector --allow_grow

python ./face_recognition_demo.py -m_fd ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-detection-retail-0004/FP16/face-detection-retail-0004.xml -m_lm ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/landmarks-regression-retail-0009/FP16/landmarks-regression-retail-0009.xml -m_reid ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-reidentification-retail-0095/FP16/face-reidentification-retail-0095.xml -l /home/user/Desktop/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so --verbose -fg  "/home/user/AI_theyre_back/image/face_gallery"
```