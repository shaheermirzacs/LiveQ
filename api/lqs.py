import grpc
import interface_pb2
import interface_pb2_grpc
import server_resources
import uuid
import time
import logging
from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class LiveQSevicer(interface_pb2_grpc.LiveQServicer):
    def __init__(self):
        self.db = server_resources.RoomDB()
    
    def CreateRoom(self, request, context):
        reply_info = self.db.AddRoom(request.room_name)
        return interface_pb2.CreateReply(room_key=reply_info[0], host_id=reply_info[1])

    def JoinRoom(self, request, context):
        reply_info = str(self.db.JoinRoom(request.room_key))
        return interface_pb2.JoinReply(guest_id=reply_info)

    def UpdateQueue(self, request, context):
        q = self.db.rooms[request.room_key].q
        for song in q:
            yield song

    def AddSong(self, request, context):
        self.db.AddSong(request.room_key, interface_pb2.QueueReply(song_id=request.song_id, service_id=request.service_id))
        q = self.db.rooms[request.room_key].q
        for song in q:
            yield song

    def DeleteSong(self, request, context):
        self.db.DeleteSong(request.room_key, interface_pb2.QueueReply(song_id=request.song_id, service_id=request.service_id))
        q = self.db.rooms[request.room_key].q
        for song in q:
            yield song
            
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    interface_pb2_grpc.add_LiveQServicer_to_server(LiveQSevicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    logging.basicConfig()
    serve()