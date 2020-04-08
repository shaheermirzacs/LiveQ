# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: interface.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='interface.proto',
  package='liveq',
  syntax='proto3',
  serialized_options=b'\n\005LiveQB\nLiveQProtoP\001',
  serialized_pb=b'\n\x0finterface.proto\x12\x05liveq\"\"\n\rCreateRequest\x12\x11\n\troom_name\x18\x01 \x01(\t\"O\n\x0b\x43reateReply\x12\x1d\n\x06status\x18\x01 \x01(\x0b\x32\r.liveq.Status\x12\x10\n\x08room_key\x18\x02 \x01(\t\x12\x0f\n\x07host_id\x18\x03 \x01(\t\"\x1e\n\nKeyRequest\x12\x10\n\x08room_key\x18\x01 \x01(\t\"O\n\tJoinReply\x12\x1d\n\x06status\x18\x01 \x01(\x0b\x32\r.liveq.Status\x12\x11\n\troom_name\x18\x02 \x01(\t\x12\x10\n\x08guest_id\x18\x03 \x01(\t\"F\n\x0eServiceRequest\x12\x10\n\x08room_key\x18\x01 \x01(\t\x12\"\n\x07service\x18\x02 \x01(\x0b\x32\x11.liveq.ServiceMsg\"\x18\n\x06Status\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x1a\n\nServiceMsg\x12\x0c\n\x04name\x18\x01 \x01(\t\"{\n\x07SongMsg\x12\x0f\n\x07song_id\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0e\n\x06\x61rtist\x18\x04 \x01(\t\x12\x11\n\timage_uri\x18\x05 \x01(\t\x12\x10\n\x08\x64uration\x18\x06 \x01(\x05\x12\x0f\n\x07service\x18\x07 \x01(\t\"=\n\x0bSongRequest\x12\x1c\n\x04song\x18\x01 \x01(\x0b\x32\x0e.liveq.SongMsg\x12\x10\n\x08room_key\x18\x02 \x01(\t2\xf9\x02\n\x05LiveQ\x12\x38\n\nCreateRoom\x12\x14.liveq.CreateRequest\x1a\x12.liveq.CreateReply\"\x00\x12\x31\n\x08JoinRoom\x12\x11.liveq.KeyRequest\x1a\x10.liveq.JoinReply\"\x00\x12\x34\n\nAddService\x12\x15.liveq.ServiceRequest\x1a\r.liveq.Status\"\x00\x12\x37\n\x0bGetServices\x12\x11.liveq.KeyRequest\x1a\x11.liveq.ServiceMsg\"\x00\x30\x01\x12\x31\n\x08GetQueue\x12\x11.liveq.KeyRequest\x1a\x0e.liveq.SongMsg\"\x00\x30\x01\x12.\n\x07\x41\x64\x64Song\x12\x12.liveq.SongRequest\x1a\r.liveq.Status\"\x00\x12\x31\n\nDeleteSong\x12\x12.liveq.SongRequest\x1a\r.liveq.Status\"\x00\x42\x15\n\x05LiveQB\nLiveQProtoP\x01\x62\x06proto3'
)




_CREATEREQUEST = _descriptor.Descriptor(
  name='CreateRequest',
  full_name='liveq.CreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='room_name', full_name='liveq.CreateRequest.room_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=60,
)


_CREATEREPLY = _descriptor.Descriptor(
  name='CreateReply',
  full_name='liveq.CreateReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='liveq.CreateReply.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='room_key', full_name='liveq.CreateReply.room_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host_id', full_name='liveq.CreateReply.host_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=141,
)


_KEYREQUEST = _descriptor.Descriptor(
  name='KeyRequest',
  full_name='liveq.KeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='room_key', full_name='liveq.KeyRequest.room_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=173,
)


_JOINREPLY = _descriptor.Descriptor(
  name='JoinReply',
  full_name='liveq.JoinReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='liveq.JoinReply.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='room_name', full_name='liveq.JoinReply.room_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guest_id', full_name='liveq.JoinReply.guest_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=175,
  serialized_end=254,
)


_SERVICEREQUEST = _descriptor.Descriptor(
  name='ServiceRequest',
  full_name='liveq.ServiceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='room_key', full_name='liveq.ServiceRequest.room_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service', full_name='liveq.ServiceRequest.service', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=256,
  serialized_end=326,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='liveq.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='liveq.Status.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=328,
  serialized_end=352,
)


_SERVICEMSG = _descriptor.Descriptor(
  name='ServiceMsg',
  full_name='liveq.ServiceMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='liveq.ServiceMsg.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=354,
  serialized_end=380,
)


_SONGMSG = _descriptor.Descriptor(
  name='SongMsg',
  full_name='liveq.SongMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='song_id', full_name='liveq.SongMsg.song_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uri', full_name='liveq.SongMsg.uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='liveq.SongMsg.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='artist', full_name='liveq.SongMsg.artist', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_uri', full_name='liveq.SongMsg.image_uri', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='liveq.SongMsg.duration', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service', full_name='liveq.SongMsg.service', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=382,
  serialized_end=505,
)


_SONGREQUEST = _descriptor.Descriptor(
  name='SongRequest',
  full_name='liveq.SongRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='song', full_name='liveq.SongRequest.song', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='room_key', full_name='liveq.SongRequest.room_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=507,
  serialized_end=568,
)

_CREATEREPLY.fields_by_name['status'].message_type = _STATUS
_JOINREPLY.fields_by_name['status'].message_type = _STATUS
_SERVICEREQUEST.fields_by_name['service'].message_type = _SERVICEMSG
_SONGREQUEST.fields_by_name['song'].message_type = _SONGMSG
DESCRIPTOR.message_types_by_name['CreateRequest'] = _CREATEREQUEST
DESCRIPTOR.message_types_by_name['CreateReply'] = _CREATEREPLY
DESCRIPTOR.message_types_by_name['KeyRequest'] = _KEYREQUEST
DESCRIPTOR.message_types_by_name['JoinReply'] = _JOINREPLY
DESCRIPTOR.message_types_by_name['ServiceRequest'] = _SERVICEREQUEST
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['ServiceMsg'] = _SERVICEMSG
DESCRIPTOR.message_types_by_name['SongMsg'] = _SONGMSG
DESCRIPTOR.message_types_by_name['SongRequest'] = _SONGREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEREQUEST,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:liveq.CreateRequest)
  })
_sym_db.RegisterMessage(CreateRequest)

CreateReply = _reflection.GeneratedProtocolMessageType('CreateReply', (_message.Message,), {
  'DESCRIPTOR' : _CREATEREPLY,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:liveq.CreateReply)
  })
_sym_db.RegisterMessage(CreateReply)

KeyRequest = _reflection.GeneratedProtocolMessageType('KeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _KEYREQUEST,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:liveq.KeyRequest)
  })
_sym_db.RegisterMessage(KeyRequest)

JoinReply = _reflection.GeneratedProtocolMessageType('JoinReply', (_message.Message,), {
  'DESCRIPTOR' : _JOINREPLY,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:liveq.JoinReply)
  })
_sym_db.RegisterMessage(JoinReply)

ServiceRequest = _reflection.GeneratedProtocolMessageType('ServiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEREQUEST,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:liveq.ServiceRequest)
  })
_sym_db.RegisterMessage(ServiceRequest)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:liveq.Status)
  })
_sym_db.RegisterMessage(Status)

ServiceMsg = _reflection.GeneratedProtocolMessageType('ServiceMsg', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEMSG,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:liveq.ServiceMsg)
  })
_sym_db.RegisterMessage(ServiceMsg)

SongMsg = _reflection.GeneratedProtocolMessageType('SongMsg', (_message.Message,), {
  'DESCRIPTOR' : _SONGMSG,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:liveq.SongMsg)
  })
_sym_db.RegisterMessage(SongMsg)

SongRequest = _reflection.GeneratedProtocolMessageType('SongRequest', (_message.Message,), {
  'DESCRIPTOR' : _SONGREQUEST,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:liveq.SongRequest)
  })
_sym_db.RegisterMessage(SongRequest)


DESCRIPTOR._options = None

_LIVEQ = _descriptor.ServiceDescriptor(
  name='LiveQ',
  full_name='liveq.LiveQ',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=571,
  serialized_end=948,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateRoom',
    full_name='liveq.LiveQ.CreateRoom',
    index=0,
    containing_service=None,
    input_type=_CREATEREQUEST,
    output_type=_CREATEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='JoinRoom',
    full_name='liveq.LiveQ.JoinRoom',
    index=1,
    containing_service=None,
    input_type=_KEYREQUEST,
    output_type=_JOINREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddService',
    full_name='liveq.LiveQ.AddService',
    index=2,
    containing_service=None,
    input_type=_SERVICEREQUEST,
    output_type=_STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetServices',
    full_name='liveq.LiveQ.GetServices',
    index=3,
    containing_service=None,
    input_type=_KEYREQUEST,
    output_type=_SERVICEMSG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetQueue',
    full_name='liveq.LiveQ.GetQueue',
    index=4,
    containing_service=None,
    input_type=_KEYREQUEST,
    output_type=_SONGMSG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddSong',
    full_name='liveq.LiveQ.AddSong',
    index=5,
    containing_service=None,
    input_type=_SONGREQUEST,
    output_type=_STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteSong',
    full_name='liveq.LiveQ.DeleteSong',
    index=6,
    containing_service=None,
    input_type=_SONGREQUEST,
    output_type=_STATUS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LIVEQ)

DESCRIPTOR.services_by_name['LiveQ'] = _LIVEQ

# @@protoc_insertion_point(module_scope)
