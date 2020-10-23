import numpy as np
import time
import cv2
import cv2.aruco as aruco

pi = 3.1415926
mtx = np.array([
    [3151.45, 0, 1456.97],
    [0, 3157.04, 1995.06],
    [0, 0, 1],
])
#
# ip摄像头拍视频的时候设置的是 1920 x 1080，长宽比是一样的，
# ip摄像头设置分辨率的时候注意一下


dist = np.array([0.45381735, -2.37093369, -0.00734813, -0.00426619, 4.02310968])

video = "rtsp://admin:admin@192.168.43.1:8554/live"  # 手机ip摄像头
# 根据ip摄像头在你手机上生成的ip地址更改，右上角可修改图像分辨率

cap = cv2.VideoCapture(video)

font = cv2.FONT_HERSHEY_SIMPLEX  # font for displaying text (below)

# num = 0
while True:
    ret, frame = cap.read()
    # operations on the frame come here

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
    # DICT_6X6_250 6 is the length of aruco code, 250 is the total num of 6X6 code.
    parameters = aruco.DetectorParameters_create()

    '''
    detectMarkers(...)
        detectMarkers(image, dictionary[, corners[, ids[, parameters[, rejectedI
        mgPoints]]]]) -> corners, ids, rejectedImgPoints
    '''

    # lists of ids and the corners beloning to each id
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray,
                                                          aruco_dict,
                                                          parameters=parameters)

    #    if ids != None:
    if ids is not None:

        rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, 0.05, mtx, dist)
        # Estimate pose of each marker and return the values rvet and tvec---different
        # from camera coeficcients
        (rvec - tvec).any()  # get rid of that nasty numpy value array error
        print("rotation is :", rvec * 180 / pi)  # color of axis : (X:red, Y:green, Z:blue):
        #       aruco.drawAxis(frame, mtx, dist, rvec, tvec, 0.1) #Draw Axis
        #       aruco.drawDetectedMarkers(frame, corners) #Draw A square around the markers
        # rotate_matrix = np.array([[0, 0, 0],
        #                           [0, 0, 0],
        #                           [0, 0, 0]])
        rotate_matrix=np.zeros((3,3),dtype=np.float)
        cv2.Rodrigues(rvec[0], rotate_matrix)
        print(rotate_matrix)
        for i in range(rvec.shape[0]):
            aruco.drawAxis(frame, mtx, dist, rvec[i, :, :], tvec[i, :, :], 0.03)
            aruco.drawDetectedMarkers(frame, corners)
        ###### DRAW ID #####
    #        cv2.putText(frame, "Id: " + str(ids), (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)

    else:
        ##### DRAW "NO IDS" #####
        cv2.putText(frame, "No Ids", (0, 64), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)

    if key == 27:  # 按esc键退出
        print('esc break...')
        cap.release()
        cv2.destroyAllWindows()
        break

    if key == ord(' '):  # 按空格键保存
        filename = str(time.time())[:10] + ".jpg"
        cv2.imwrite(filename, frame)
