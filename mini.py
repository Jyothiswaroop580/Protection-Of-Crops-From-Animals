import tensorflow as tf 
import numpy as np
from IPython.display import Image
from tensorflow.keras.preprocessing import image
from keras.applications import imagenet_utils
from playsound import playsound
import cv2
from twilio.rest import Client
    
mobile = tf.keras.applications.mobilenet_v2.MobileNetV2()
filename='E:/Mini_project/data/test/cow/OIP-_6CJGv4_77hKyrXuGH4pTAHaE7.jpeg'
img = image.load_img(filename,target_size=(224,224))
resized_img = image.img_to_array(img)
final_image = np.expand_dims(resized_img,axis=0)
final_image = tf.keras.applications.mobilenet.preprocess_input(final_image)
final_image.shape
predictions = mobile.predict(final_image)
results = imagenet_utils.decode_predictions(predictions)
count=0

def camara():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite("C:/Users/swaroop/Downloads/NewPicture.jpg",frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
def SMS(animal):
    account_sid = "ACc2a2dd203984b22f55716430ab52d93e"
    auth_token = "fa92505e3aded17b54d9c9708cd1948e"
    client = Client(account_sid, auth_token)
    client.messages.create(from_="+12566809509",body=animal+" arived",to="+91 XXXXXXXXXX")

def predect(count):
    file = open('Animal_name.txt','w')
    List = ['Sheep','Cow','Forest pig','Elephant','Wolf','Armadillo','Rabbit']
    if count==2:
        count=0
    if results[0][0][1]=='ram' or results[0][0][1]=='hog':
        print(List[0])
        file.write(List[0])
        count=count+1
        if count==2:
            SMS(List[0])
    elif results[0][0][1]=='ox':
        print(List[1])
        file.write(List[3])
        count=count+1
        playsound('labrador-barking-daniel_simon.mp3')
        if count==2:
            SMS(List[1])
    elif results[0][0][1]=='wild_boar':
        print(List[2])
        file.write(List[2])
        count=count+1
        if count==2:
            SMS(List[2])
    elif results[0][0][1]=='African_elephant' or results[0][0][1]=='Indian_elephant':
        print(List[3])
        file.write(List[3])
        count=count+1
        if count==2:
            SMS(List[3])
    elif results[0][0][1]=='coyote' or results[0][0][1]=='red_wolf' or results[0][0][1]=='grey_fox':
        print(List[4])
        file.write(List[4])
        count=count+1
        if count==2:
            SMS(List[4])
    elif results[0][0][1]=='armadillo':
        print(List[5])
        file.write(List[5])
        count=count+1
        if count==2:
            SMS(List[5])
    elif results[0][0][1]=='wood_rabbit' or results[0][0][1]=='hare':
        print(List[6])
        file.write(List[6])
        count=count+1
        if count==2:
            SMS(List[6])
    else:
        print(results[0][0][1])
        file.write(results[0][0][1])
        count=count+1
        if count==2:
            SMS(results[0][0][1])
    file.close()
    return(count)
#camara()
i=0
while(true):
    count=predect(count)
    print(results,count)
    i=i+1
