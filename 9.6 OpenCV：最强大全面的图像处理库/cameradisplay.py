import cv2
img_path = 'camera.jpg'     #//等待识别的图像
#//采样图片
def CatchUsbVideo(window_name):
    cv2.namedWindow(window_name)
    cap = cv2.VideoCapture(0) # //视频来源，从摄像头获得 （也可以来自一段已存好的视频）
    while cap.isOpened():
        ok, frame = cap.read()  # //读取一帧数据
        if not ok:
            break

        # //每300ms刷新一次显示,输入‘q’退出程序
        cv2.imwrite(img_path, frame)
        cv2.putText(frame, " is what", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0) , 4)  #//添加文字显示
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break

    # //释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    CatchUsbVideo("get pic v1.0")
