import warnings
warnings.filterwarnings("ignore")
import tensorflow as tf 
import numpy as np
from tensorflow.keras.preprocessing import image
from keras.applications import imagenet_utils
from playsound import playsound
import cv2
from twilio.rest import Client

def camara(count):
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite("NewPicture.jpg",frame)
        result = False
    videoCaptureObject.release()

    im = cv2.imread('NewPicture.jpg')
    threshold=0
    if len(im.shape) == 3:
        flatImage = np.max(im, 2)
    else:
        flatImage = im
    assert len(flatImage.shape) == 2

    rows = np.where(np.max(flatImage, 0) > threshold)[0]
    if rows.size:
        cols = np.where(np.max(flatImage, 1) > threshold)[0]
        im = im[cols[0]: cols[-1] + 1, rows[0]: rows[-1] + 1]
    else:
        im = im[:1, :1]
    cv2.imwrite('image.png',im)
    filename='image.png'
    img = image.load_img(filename,target_size=(224,224))
    resized_img = image.img_to_array(img)
    final_image = np.expand_dims(resized_img,axis=0)
    final_image = tf.keras.applications.mobilenet.preprocess_input(final_image)
    final_image.shape
    predictions = mobile.predict(final_image)
    results = imagenet_utils.decode_predictions(predictions)
    count=predect(count,results)
    return(count)
    
def SMS(animal):
    account_sid = "ACc2a2dd203984b22f55716"
    auth_token = "9b8c36cdaa099c7c6944"
    client = Client(account_sid, auth_token)
    client.messages.create(from_="+1256680XXXX",body=animal+" entered",to="+91 70759XXXXX")

def predect(count,results):
    file = open('Animal_name.txt','w')
    List = ['Sheep','Cow','Forest pig','Elephant','Wolf','Armadillo','Rabbit','Be care full Tiger','brown bear']
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
        file.write(List[1])
        count=count+1
        playsound('labrador-barking-daniel_simon.mp3')
        if count==2:
            SMS(List[1])
    elif results[0][0][1]=='wild_boar' or results[0][0][1]=='warthog':
        print(List[2])
        file.write(List[2])
        count=count+1
        playsound('Danger Danger.mp3')
        if count==2:
            SMS(List[2])
    elif results[0][0][1]=='African_elephant' or results[0][0][1]=='Indian_elephant':
        print(List[3])
        file.write(List[3])
        count=count+1
        playsound('Danger Danger.mp3')
        if count==2:
            SMS(List[3])
    elif results[0][0][1]=='coyote' or results[0][0][1]=='red_wolf' or results[0][0][1]=='grey_fox':
        print(List[4])
        file.write(List[4])
        count=count+1
        playsound('Danger Danger.mp3')
        if count==2:
            SMS(List[4])
    elif results[0][0][1]=='armadillo':
        print(List[5])
        file.write(List[5])
        count=count+1
        playsound('Danger Danger.mp3')
        if count==2:
            SMS(List[5])
    elif results[0][0][1]=='wood_rabbit' or results[0][0][1]=='hare':
        print(List[6])
        file.write(List[6])
        count=count+1
        playsound('Danger Danger.mp3')
        if count==2:
            SMS(List[6])
    elif results[0][0][1]=='tiger' or results[0][0][1]=='tiger_cat':
        print("Tiger")
        file.write(List[7])
        SMS(List[7])
    elif results[0][0][1]=='brown_bear':
        print("brown bear")
        file.write(List[8])
        SMS(List[8])
    else:
        print(results[0][0][1])
    return(count)

mobile = tf.keras.applications.mobilenet_v2.MobileNetV2()
count=0
#camara()
while(True):
    count=camara(count)
