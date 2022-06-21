# pythonProject5
## Requirements
Python >= 3.5  
PyTorch >= 1.0.0  
Opencv2 ==3.4.1  
scipy==1.2.0  
Numpy == 1.14.3  
scikit_image==0.14.2  
opencv_python==4.1.2.30  
torchvision==0.2.1  
matplotlib==3.0.3  
numpy==1.15.4  
face_alignment==1.0.1  
Pillow==6.2.1  
PyYAML==5.1.2  

This is the environment for our experiments. Later versions of these packages might need a few modifications of the code.
Although our method is not limited to any specific CUDA and cuDNN version, 
it's strongly encouraged that you use the latest version of these toolkits. It seems that the RFR-Net could run slowly in older CUDA version due to its recurrent design.

## Move to our project file
cd ./gan_final

## Datasets
We use CelebA (Wild + Align) dataset for inpainting.  
FAN algorithm makes landmark ground truth.  
`./scripts/preprocess_landmark.py` generates landmarks of the images with FAN algorithm.  
`python3 ./scripts/preprocess_landmark.py --path path_to_train_data_images --output path_to_train_data_landmarks`

## Training
In `train.py`, there are some directory path at `__init__`. Change if you meet errors.  
In `train.py`, there are two options, `lm_train` and `inpaint_train`.  

### lm_trian
`lm_train` trains the landmarks prediction model.  
Un-annotate `trainer.lm_train()` at line 222 & Annotate `trainer.inpaint_trian()` at line 223.  
Run `python3 ./train.py` in `gan_final`.  

### inpaint_train
`inpaint_train` trains the inpainting model.  
Un-annotate `trainer.inpaint_trian()` at line 223 & Annotate `trainer.lm_train()` at line 222.  
Run `python3 ./train.py` in `gan_final`.  

## Testing
In `test.py`, there are some directory path at `__init__`. Change if you meet errors.  
Run `python3 ./test.py` in `gan_final`.  
