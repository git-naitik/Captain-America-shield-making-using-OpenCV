import cv2
from cvzone.HandTrackingModule import HandDetector
cap=cv2.VideoCapture(0)
detector=HandDetector()
shield=cv2.imread("shield.png",cv2.IMREAD_UNCHANGED)
shield=cv2.resize(shield,(200,200))

def placeimg(overlay,background,x,y):
    h,w,c=overlay.shape
    try:
        mask=overlay[...,3:]/255.0
        overlayimage=overlay[...,:3]
        background[int(y-h/2):int(y+h/2),int(x-w/2):int(x+w/2)]=(1-mask)*background[int(y-h/2):int(y+h/2),int(x-w/2):int(x+w/2)]+mask*overlayimage
        return background
    except:
        return background


while True:
    ret,img=cap.read()
    hands=detector.findHands(img,False)
    for hand in hands:
        cx,cy=hand["center"]
        img=placeimg(shield,img,cx,cy)
    cv2.imshow("Naitik",img)
    cv2.waitKey(1)


