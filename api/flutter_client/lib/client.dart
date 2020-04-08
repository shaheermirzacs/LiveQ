import 'package:grpc/grpc.dart';
import 'interface.pb.dart';
import 'interface.pbgrpc.dart';
import 'song.dart';
import 'package:shared_preferences/shared_preferences.dart';

class Client {
  ClientChannel channel;
  LiveQClient stub;
  String key;
  
  Client() {
    channel = ClientChannel('34.71.85.54', port: 80, options: const ChannelOptions(credentials: ChannelCredentials.insecure()));  
    stub = LiveQClient(channel, options: CallOptions(timeout: Duration(seconds: 30)));
  }

  Future<String> CreateRoom(String room_name) async {
    final msg = CreateRequest()
      ..roomName = room_name;
    final createReply = await stub.createRoom(msg);
    if(createReply.status.status == 0){
      key = createReply.roomKey;
      return createReply.roomKey;
    }
    else {
      return 'Error: CreateRoom Failed.';
    }
  }

  Future<String> JoinRoom(String room_key) async{
    key = room_key;
    final msg = KeyRequest()
      ..roomKey = key;
    final joinReply = await stub.joinRoom(msg);
    if(joinReply.status.status == 0) {
      return joinReply.roomName;
    }
    else {
      return 'Error: JoinRoom Failed.';
    }
  }

  void AddService(String service_name) async{
    final service = ServiceMsg()
      ..name = service_name;
    final msg = ServiceRequest()
      ..service = service
      ..roomKey = key;
    final reply = await stub.addService(msg);
    if(reply.status != 0) {
      print('Error: AddService Failed.');
    }
  }
  
  Future<List<String>> GetServices() async{
    final request = KeyRequest()
      ..roomKey = key;
    List<String> services;
    try {
      await for (var service in stub.getServices(request)) {
        services.add(service.name);
      }
    }
    catch (e) {
      print('Error: $e');
    }
    return services;
  }

  Future<List<String>> 
  Future<void> AddSong(Song song) async{
    final songObj = SongMsg()
      ..songId = song.id
      ..uri = song.uri
      ..name = song.trackName
      ..artist = song.artists
      ..imageUri = song.imageUri
      ..duration = Int64(song.duration)
      ..service = song.service.name;
    
    final msg = SongRequest()
      ..song = songObj
      ..roomKey = key;
    final reply  = await stub.addSong(msg);
    if(reply.status != 0) {
      print('Error: AddSong Failed.');
    }
  }

  Future<void> testDeleteSong(String key) async{

  }

  void testUpdateQueue(String key) async{ 

  }
}