# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fashion.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rfashion.proto\x12\x07\x66\x61shion\"B\n\x08\x43ustomer\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\r\n\x05phone\x18\x04 \x01(\t\"\x18\n\nCustomerId\x12\n\n\x02id\x18\x01 \x01(\x05\"\x07\n\x05\x45mpty2\xb3\x02\n\x0f\x43ustomerService\x12\x38\n\x0e\x43reateCustomer\x12\x11.fashion.Customer\x1a\x11.fashion.Customer\"\x00\x12\x38\n\x0cReadCustomer\x12\x13.fashion.CustomerId\x1a\x11.fashion.Customer\"\x00\x12\x38\n\x0eUpdateCustomer\x12\x11.fashion.Customer\x1a\x11.fashion.Customer\"\x00\x12:\n\x0e\x44\x65leteCustomer\x12\x13.fashion.CustomerId\x1a\x11.fashion.Customer\"\x00\x12\x36\n\rListCustomers\x12\x0e.fashion.Empty\x1a\x11.fashion.Customer\"\x00\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fashion_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CUSTOMER._serialized_start=26
  _CUSTOMER._serialized_end=92
  _CUSTOMERID._serialized_start=94
  _CUSTOMERID._serialized_end=118
  _EMPTY._serialized_start=120
  _EMPTY._serialized_end=127
  _CUSTOMERSERVICE._serialized_start=130
  _CUSTOMERSERVICE._serialized_end=437
# @@protoc_insertion_point(module_scope)
