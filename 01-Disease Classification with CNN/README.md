Execute the first cell on the notebook  
!unzip -qo "MedNIST.zip"  
!rm "MedNIST.zip"  
  
Then remove all the images on the Medical_test subfolders and continue with the next cells.  
In this project we will use the libraries below :
--> os 
--> numpy
--> pandas
--> random 
--> datetime
--> shutil
--> math
--> matplotlib
--> tensorflow keras
Finally the cnn model which has trained with 5 epoch gives us thses results:  
acc: 0.9990 - loss: 0.0045 - val_acc: 0.9983 - val_loss: 0.0080 - learning_rate: 0.0010
