# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dummy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0b\x64ummy.proto"\x1d\n\x0c\x44ummyRequest\x12\r\n\x05input\x18\x01 \x01(\t"\x1f\n\rDummyResponse\x12\x0e\n\x06output\x18\x01 \x01(\t2\xe8\x01\n\x0c\x44ummyService\x12(\n\x07\x45xecute\x12\r.DummyRequest\x1a\x0e.DummyResponse\x12\x36\n\x13\x45xecuteClientStream\x12\r.DummyRequest\x1a\x0e.DummyResponse(\x01\x12\x36\n\x13\x45xecuteServerStream\x12\r.DummyRequest\x1a\x0e.DummyResponse0\x01\x12>\n\x19\x45xecuteClientServerStream\x12\r.DummyRequest\x1a\x0e.DummyResponse(\x01\x30\x01\x62\x06proto3'
)


_DUMMYREQUEST = DESCRIPTOR.message_types_by_name["DummyRequest"]
_DUMMYRESPONSE = DESCRIPTOR.message_types_by_name["DummyResponse"]
DummyRequest = _reflection.GeneratedProtocolMessageType(
    "DummyRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DUMMYREQUEST,
        "__module__": "dummy_pb2"
        # @@protoc_insertion_point(class_scope:DummyRequest)
    },
)
_sym_db.RegisterMessage(DummyRequest)

DummyResponse = _reflection.GeneratedProtocolMessageType(
    "DummyResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DUMMYRESPONSE,
        "__module__": "dummy_pb2"
        # @@protoc_insertion_point(class_scope:DummyResponse)
    },
)
_sym_db.RegisterMessage(DummyResponse)

_DUMMYSERVICE = DESCRIPTOR.services_by_name["DummyService"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _DUMMYREQUEST._serialized_start = 15
    _DUMMYREQUEST._serialized_end = 44
    _DUMMYRESPONSE._serialized_start = 46
    _DUMMYRESPONSE._serialized_end = 77
    _DUMMYSERVICE._serialized_start = 80
    _DUMMYSERVICE._serialized_end = 312
# @@protoc_insertion_point(module_scope)
