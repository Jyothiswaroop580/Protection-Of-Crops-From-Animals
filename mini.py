import tensorflow as tf 
import numpy as np
from IPython.display import Image
from tensorflow.keras.preprocessing import image
from keras.applications import imagenet_utils
mobile = tf.keras.applications.mobilenet_v2.MobileNetV2()
filename='E:/Mini_project/data/test/forest_pig/6 (2).jpg'
img = image.load_img(filename,target_size=(224,224))
resized_img = image.img_to_array(img)
final_image = np.expand_dims(resized_img,axis=0)
final_image = tf.keras.applications.mobilenet.preprocess_input(final_image)
final_image.shape
predictions = mobile.predict(final_image)
results = imagenet_utils.decode_predictions(predictions)
List = ['Sheep','Cow','Forest pig','Elephant','Wolf','Armadillo','Rabbit']
if results[0][0][1]=='ram' or results[0][0][1]=='hog':
    print(List[0])
elif results[0][0][1]=='ox':
    print(List[1])
elif results[0][0][1]=='wild_boar':
    print(List[2])
elif results[0][0][1]=='African_elephant' or results[0][0][1]=='Indian_elephant':
    print(List[3])
elif results[0][0][1]=='coyote' or results[0][0][1]=='red_wolf' or results[0][0][1]=='grey_fox':
    print(List[4])
elif results[0][0][1]=='armadillo':
    print(List[5])
elif results[0][0][1]=='wood_rabbit' or results[0][0][1]=='hare':
    print(List[6])
else:
    print(results[0][0][1])
