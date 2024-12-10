![wiring](image.jpg)  
  
INSTALL THE DATA :  
https://cainvas-static.s3.amazonaws.com/media/user_data/cainvas-admin/MedNIST.zip  

This dataset was developed in 2017 by Arturo Polanco Lozano and is called MedNIST for radiology and medical imaging. It contains 58,954 images across 6 categories: AbdomenCT (10,000), BreastMRI (8,954), ChestCT (10,000), CXR (10,000), Hand (10,000), and HeadCT (10,000), with a total size of 75.9 MB.  
  
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


  
Finally the CNN model which has trained with 5 epochs gives us these results:  
acc: 0.9990 - loss: 0.0045 - val_acc: 0.9983 - val_loss: 0.0080 - learning_rate: 0.0010.
