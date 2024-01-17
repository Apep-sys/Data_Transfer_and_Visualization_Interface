import cv2
class MyVideoCapture:
    def __init__(self, video_source=0):
        # Se deschide sursa video
        self.vid = cv2.VideoCapture(r'D:\Downloads\cyber1.mp4')
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Se preia latimea si inaltimea sursei video
        self.width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def release(self):
        # Se elibereaza resursele folosite de sursa video si obiectul este distrus
        self.vid.release()

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Se returneaza un flag de tip boolean pozitiv, iar frame-ul curent este convertit in BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)


# Se elibereaza resursele sursei video si obiectul este distrus
def __del__(self):
    if self.vid.isOpened():
        self.vid.release()