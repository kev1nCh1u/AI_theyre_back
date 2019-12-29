# OpenVINO 使用教學

作者：KevinChiu

參考：https://docs.openvinotoolkit.org/latest/_docs_install_guides_installing_openvino_linux.html

## OpenVINO install

到OpenVINO官網安裝OpenVINO，看得懂可以跳過本章節，看不懂看我們懶人包

https://docs.openvinotoolkit.org/latest/_docs_install_guides_installing_openvino_linux.html

選擇你的作業系統來安裝，建議Linux，以下教學也以Linux來說明：


1. 下載OpenVINO https://software.intel.com/en-us/openvino-toolkit/choose-download/free-download-linux

1. 下載完成後，到該檔案的目錄下如：
    ```
    cd ~/Downloads/
    ```

1. 解壓縮該檔案，l_openvino_toolkit_p_\<version\>換成該檔名稱：
    ```
    tar -xvzf l_openvino_toolkit_p_<version>.tgz
    ```

1. 到解壓縮完的目錄下：
    ```
    cd l_openvino_toolkit_p_<version>
    ```

1. 安裝OpenVINO

    用GUI介面安裝
    ```
    sudo ./install_GUI.sh
    ```

    或Command-Line安裝
    ```
    sudo ./install.sh
    ```

1. 在prerequisites回顯示缺乏的軟件，一直下一步就安裝完成了

1. 安裝完成後，到install_dependencies目錄下：
    ```
    cd /opt/intel/openvino/install_dependencies
    ```

1. 執行install_openvino_dependencies.sh
    ```
    sudo -E ./install_openvino_dependencies.sh
    ```

1. 設定環境變數 setupvars.sh：

    每次開啟terminal後都要執行：
    ```
    source /opt/intel/openvino/bin/setupvars.sh
    ```

    如果嫌麻煩也可以加到.bashrc，讓他自動執行：
    ```
    sudo vim ~/.bashrc
    source /opt/intel/openvino/bin/setupvars.sh
    ```
    "i"加在最後一行"ESC"後，":wq"儲存退出

1. 切換到Model Optimizer prerequisites目錄下：
    ```
    cd /opt/intel/openvino/deployment_tools/model_optimizer/install_prerequisites
    ```

1. 配置一些軟件Caffe, TensorFlow, MXNet, Kaldi*, and ONNX：
    ```
    sudo ./install_prerequisites.sh
    ```

## Run a Demo

1. 到Inference Engine demo目錄下：
    ```
    cd /opt/intel/openvino/deployment_tools/demo
    ```

1. 執行demo_squeezenet_download_convert_run.sh：

    下載一些Demo會用到的東西
    ```
    ./demo_squeezenet_download_convert_run.sh
    ```

1. 執行demo：
    ```
    ./demo_security_barrier_camera.sh
    ```
    正常運作就是安裝成功了！


## Build the Sample Applications
```
cd '/opt/intel/openvino/inference_engine/demos'
```
```
./build_demos.sh 
```

## Model downloader 
```
cd /opt/intel/openvino/deployment_tools/tools/model_downloader
```
```
./downloader.py --print_all
```
```
./downloader.py --name 
```


## Security Barrier Camera С++ Demo
```
cd /home/user/omz_demos_build/intel64/Release
```
```
./security_barrier_camera_demo -i /opt/intel/openvino_2019.3.334/deployment_tools/demo/car_1.bmp -m /home/user/openvino_models/ir/FP16/intel/vehicle-license-plate-detection-barrier-0106/FP16/vehicle-license-plate-detection-barrier-0106.xml
```

## yolo
轉tf
```
cd ~/tensorflow-yolo-v3

python convert_weights_pb.py --class_names coco.names  --data_format NHWC --weight_file yolov3.weights 
```
轉IR
```
cd ~/Desktop/openvino/deployment_tools/model_optimizer

sudo python3 mo_tf.py --input_model '/home/user/tensorflow-yolo-v3/frozen_darknet_yolov3_model.pb' --tensorflow_use_custom_operations_config '/home/user/Desktop/openvino/deployment_tools/model_optimizer/extensions/front/tf/yolo_v3.json' --batch 1
```
執行
```
cd ~/omz_demos_build/intel64/Release

./object_detection_demo_yolov3_async -i cam -m '/home/user/Desktop/openvino/deployment_tools/model_optimizer/frozen_darknet_yolov3_model.xml' -d MYRIAD
```
py
```
cd /opt/intel/openvino_2019.3.334/inference_engine/demos/python_demos/object_detection_demo_yolov3_async
```
```
python3 object_detection_demo_yolov3_async.py -i cam -m '/home/user/Desktop/openvino/deployment_tools/model_optimizer/frozen_darknet_yolov3_model.xml' -d MYRIAD
```
```
python3 object_detection_demo_yolov3_async.py -i '/home/user/Videos/FILE0149.MOV'  -m '/home/user/Desktop/openvino/deployment_tools/model_optimizer/frozen_darknet_yolov3_model.xml' -d MYRIAD
```
```
python3 object_detection_demo_yolov3_async.py -i '/home/user/Videos/FILE0149.MOV'  -m '/home/user/Desktop/openvino/deployment_tools/model_optimizer/frozen_darknet_yolov3_model.xml' -d MYRIAD --labels '/home/user/tensorflow-yolo-v3/coco.names' 

```
tiny
```
cd ~/tensorflow-yolo-v3
python convert_weights_pb.py --class_names coco.names  --data_format NHWC --weight_file yolov3-tiny.weights --tiny --output_graph frozen_darknet_yolov3-tiny_model.pb
```
```
cd ~/Desktop/openvino/deployment_tools/model_optimizer
sudo python3 mo_tf.py --input_model '/home/user/tensorflow-yolo-v3/frozen_darknet_yolov3-tiny_model.pb' --tensorflow_use_custom_operations_config '/home/user/Desktop/openvino/deployment_tools/model_optimizer/extensions/front/tf/yolo_v3_tiny.json' --batch 1
```
```
cd /opt/intel/openvino_2019.3.334/inference_engine/demos/python_demos/object_detection_demo_yolov3_async
```
```
python3 object_detection_demo_yolov3_async.py -i '/home/user/Videos/FILE0149.MOV'  -m '/home/user/Desktop/openvino/deployment_tools/model_optimizer/frozen_darknet_yolov3-tiny_model.xml' -d MYRIAD --labels '/home/user/tensorflow-yolo-v3/coco.names' 
```
```
python3 object_detection_demo_yolov3_async.py -i cam  -m '/home/user/Desktop/openvino/deployment_tools/model_optimizer/frozen_darknet_yolov3-tiny_model.xml' -d MYRIAD --labels '/home/user/tensorflow-yolo-v3/coco.names' 
```

## 開啟檔案位置
```
nautilus
xdg-open
```

## intel 開發板 開機啟動
```
> fs0:
> cd EFI\ubuntu
> grubx64.efi
```

## face
```
cd ~/Desktop/openvino/deployment_tools/inference_engine/demos/python_demos/face_recognition_demo
```
```
python ./face_recognition_demo.py -m_fd ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-detection-retail-0004/FP16/face-detection-retail-0004.xml -m_lm ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/landmarks-regression-retail-0009/FP16/landmarks-regression-retail-0009.xml -m_reid ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-reidentification-retail-0095/FP16/face-reidentification-retail-0095.xml -l /home/user/Desktop/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so --verbose -fg "~/AI_class/face_tran" --run_detector --allow_grow
```
```
python ./face_recognition_demo.py -m_fd ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-detection-retail-0004/FP16/face-detection-retail-0004.xml -m_lm ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/landmarks-regression-retail-0009/FP16/landmarks-regression-retail-0009.xml -m_reid ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-reidentification-retail-0095/FP16/face-reidentification-retail-0095.xml -l /home/user/Desktop/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so --verbose -fg  "~/AI_class/face_gallery"
```

## AI_class
```
cd ~/AI_class/face_recognition_demo
```
```
python ./face_recognition_demo.py -m_fd ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-detection-retail-0004/FP16/face-detection-retail-0004.xml -m_lm ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/landmarks-regression-retail-0009/FP16/landmarks-regression-retail-0009.xml -m_reid ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-reidentification-retail-0095/FP16/face-reidentification-retail-0095.xml -l /home/user/Desktop/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so --verbose -fg "/home/user/AI_class/face_tran/" --run_detector --allow_grow
```
```
python ./face_recognition_demo.py -m_fd ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-detection-retail-0004/FP16/face-detection-retail-0004.xml -m_lm ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/landmarks-regression-retail-0009/FP16/landmarks-regression-retail-0009.xml -m_reid ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-reidentification-retail-0095/FP16/face-reidentification-retail-0095.xml -l /home/user/Desktop/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so --verbose -fg  "/home/user/AI_class/face_gallery/"
```