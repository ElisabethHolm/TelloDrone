#python 3.8.10
import socket
import threading
import time
from stats import Stats
#split up cpnnecting to ports (one class for recieving, one for sending)
#try to figure out how the other class is getting the video frame/frame object (use print(objectName.__dict__) )
class Tello(object):
    def __init__(self):
        """
        Constructor.
        """
        self.local_ip = ''
        self.local_port = 8889
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.local_ip, self.local_port))

        # thread for receiving cmd ack
        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        self.tello_ip = '192.168.10.1'
        self.tello_port = 8889
        self.tello_address = (self.tello_ip, self.tello_port)
        self.log = []
        '''
        #added for camera access
        self.cam_ip = '0.0.0.0'
        self.cam_port = 8890
        self.cam_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.cam_sock.bind((self.cam_ip, self.cam_port))
        self.cam_address = (self.cam_ip, self.cam_port)

        # thread for receiving video
        self.receive_video_thread = threading.Thread(target=self._receive_video_thread)
        self.receive_video_thread.daemon = True
        self.receive_video_thread.start()

        #added for sensor data access
        self.state_ip = '0.0.0.0'
        self.state_port = 11111
        self.state_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.state_sock.bind((self.state_ip, self.state_port))
        self.state_address = (self.state_ip, self.state_port)
        '''

        self.MAX_TIME_OUT = 15.0

    #def send_command(self, command, command_type):
    def send_command(self, command):
        """
        Send a command to the ip address. Will be blocked until
        the last command receives an 'OK'.
        If the command fails (either b/c time out or error),
        will try to resend the command
        :param command: (str) the command to send
        :param ip: (str) the ip of Tello
        :return: The latest command response
        """

        self.log.append(Stats(command, len(self.log)))
        '''
        #if it's a camera command
        if command_type == "cam" :
            self.socket.sendto(command.encode('utf-8'), self.cam_address)
            print(f'sending command: {command} to {self.cam_ip}')

        #if it's a state command
        elif command_type == "state":
            self.socket.sendto(command.encode('utf-8'), self.state_address)
            print(f'sending command: {command} to {self.state_ip}')
        '''
        if 1==2:
            print("oh?")

        #if it's a general command
        else:
            self.socket.sendto(command.encode('utf-8'), self.tello_address)
            print(f'sending command: {command} to {self.tello_ip}')

        start = time.time()
        while not self.log[-1].got_response():
            now = time.time()
            diff = now - start
            if diff > self.MAX_TIME_OUT:
                print(f'Max timeout exceeded... command {command}')
                return
        print(f'Done!!! sent command: {command}')


    #def _receive_thread(self, command_type): #need to input command_type somewhere, but this isn't called anywhere it just kind of runs
    def _receive_thread(self):
        """
        Listen to responses from the Tello.
        Runs as a thread, sets self.response to whatever the Tello last returned.
        """
        packet_data = ""
        while True:
            '''
            if command_type == "cam":
                try:
                    res_string, ip = self.socket_video.recvfrom(2048)
                    packet_data += res_string
                    # end of frame
                    if len(res_string) != 1460:
                        for frame in self._h264_decode(packet_data):
                            self.frame = frame
                        packet_data = ""

                except socket.error as exc:
                    print("Caught exception socket.error : %s" % exc)
            '''
            if 1 == 2:
                print("oh??")

            else:
                try:
                    self.response, ip = self.socket.recvfrom(1024)
                    print(f'from {ip}: {self.response}')

                    self.log[-1].add_response(self.response)
                except Exception as exc:
                    print(f'Caught exception socket.error : {exc}')

    ''' #combined into one receive function (above)
    def _receive_video_thread(self):
        """
        Listens for video streaming (raw h264) from the Tello.
        Runs as a thread, sets self.frame to the most recent frame Tello captured.
        """
        packet_data = ""
        while True:
            try:
                res_string, ip = self.socket_video.recvfrom(2048)
                packet_data += res_string
                # end of frame
                if len(res_string) != 1460:
                    for frame in self._h264_decode(packet_data):
                        self.frame = frame
                    packet_data = ""

            except socket.error as exc:
                print("Caught exception socket.error : %s" % exc)
    '''
    '''
    def _h264_decode(self, packet_data):
        """
        decode raw h264 format data from Tello

        :param packet_data: raw h264 data array

        :return: a list of decoded frame
        """
        res_frame_list = []
        frames = self.decoder.decode(packet_data)
        for framedata in frames:
            (frame, w, h, ls) = framedata
            if frame is not None:
                # print 'frame size %i bytes, w %i, h %i, linesize %i' % (len(frame), w, h, ls)

                frame = np.fromstring(frame, dtype=np.ubyte, count=len(frame), sep='')
                frame = (frame.reshape((h, ls / 3, 3)))
                frame = frame[:, :w, :]
                res_frame_list.append(frame)

        return res_frame_list
    '''

    def on_close(self):
        """
        On close.
        :returns: None.
        """
        pass

    def get_log(self):
        """
        Gets the logs.
        :returns: Logs.
        """
        return self.log