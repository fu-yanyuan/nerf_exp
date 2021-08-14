import cv2 as cv


def rescale(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def extract_frames(VideoFile, SavePath, output_fps=1, scale=1):
    print(VideoFile)
    print(SavePath)
    cap = cv.VideoCapture(VideoFile)

    frameRate = cap.get(5) # refer to cap.get(int)
    print("#frames =", cap.get(7)) # total number of frames in this video 
    print("fps =", cap.get(5)) # framerate
    print("h, w = ", cap.get(4), cap.get(3))

    while cap.isOpened():
        frameID = cap.get(1) # current frame number
        isTrue, frame = cap.read()
        if not isTrue:
            print("can't receive any frame (stream end?)")
            break
        # cv.imshow('frame', frame)

        # resize 
        if(scale != 1):
            frame = rescale(frame, scale)

        # save frames
        if (output_fps*frameID) % round(frameRate) == 0:
            # fileName = SavePath + "/image_" + str(int((output_fps*frameID)/round(frameRate))) + ".png"
            fileName = SavePath + "/image_" + str(int(frameID)) + ".png"
            cv.imwrite(fileName, frame)

        # quit and save for query
        k = cv.waitKey(20)
        if k == ord('q'):
            break
    print("h, w = ", cap.get(4)*scale, cap.get(3)*scale)
    cap.release()




