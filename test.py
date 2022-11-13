import cv2
import csv
import os
class OrganizeData(object):
    def __init__(self) -> None:
        self.directory_path = r"C:\Users\dell\Desktop\pyqt\1"
        #self.metadata = 
        self.data_field = {"color1", "depth1", "cmd", "odom"} 
        self.frame_count=0
        self.current_frame_data = {}

    def read_files(self):
        print(os.path.join(self.directory_path))
        if "color1" in self.data_field:
            self.color_video_1 = cv2.VideoCapture(os.path.join(self.directory_path, "color1.avi"))

        if "depth1" in self.data_field:
            self.colorized_depth_video_1 = cv2.VideoCapture(os.path.join(self.directory_path, "colorized_depth1.avi"))
        if "color2" in self.data_field:
            self.color_video_1 = cv2.VideoCapture("color2.avi")
        if "depth2" in self.data_field:
            self.colorized_depth_video = cv2.VideoCapture("colorized_depth_2.avi")

        filename = open('1/data.csv', 'r')
 
        # creating dictreader object
        file = csv.DictReader(filename)
        if "cmd" in self.data_field:
            self.cmd_angular_x = []
            self.cmd_angular_y = []
        if "odom" in self.data_field:   
            self.odom_angle_x=[]
            self.odom_angle_z=[]
            self.odom_position_x=[]
        for col in file:
            self.cmd_angular_x.append(col['cmd_angular_x'])
            self.cmd_angular_y.append(col['cmd_angular_y'])
            self.odom_angle_x.append(col['odom_angle_x'])
            self.odom_angle_z.append(col['odom_angle_z'])
            self.odom_position_x.append(col['odom_position_x'])

    def start(self):
        self.read_files()
        while(self.color_video_1.isOpened()):
        #while True:
            print(1)
            ret1, color1 = self.color_video_1.read()
            ret2, colorized_depth1 = self.colorized_depth_video_1.read()
            self.current_frame_data['color1'] = color1
            self.current_frame_data['colorized_depth1'] = colorized_depth1
            self.current_frame_data['cmd']={}
            self.current_frame_data['cmd']['angular_x'] = self.cmd_angular_x[self.frame_count]
            self.current_frame_data['cmd']['angular_y'] = self.cmd_angular_x[self.frame_count]
            self.current_frame_data['odom']={}
            self.current_frame_data['odom']['angle_x'] = self.odom_angle_x[self.frame_count]
            self.current_frame_data['odom']['angle_z'] = self.odom_angle_z[self.frame_count]
            self.current_frame_data['odom']['position_x'] = self.odom_position_x[self.frame_count]
            self.frame_count +=1
            print(self.current_frame_data)
            
if __name__=="__main__":
    a = OrganizeData()
    a.start()

            




        
       