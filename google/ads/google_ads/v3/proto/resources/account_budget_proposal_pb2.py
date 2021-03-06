# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/resources/account_budget_proposal.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v3.proto.enums import account_budget_proposal_status_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_account__budget__proposal__status__pb2
from google.ads.google_ads.v3.proto.enums import account_budget_proposal_type_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_account__budget__proposal__type__pb2
from google.ads.google_ads.v3.proto.enums import spending_limit_type_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_spending__limit__type__pb2
from google.ads.google_ads.v3.proto.enums import time_type_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_time__type__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/resources/account_budget_proposal.proto',
  package='google.ads.googleads.v3.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v3.resourcesB\032AccountBudgetProposalProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V3.Resources\312\002!Google\\Ads\\GoogleAds\\V3\\Resources\352\002%Google::Ads::GoogleAds::V3::Resources'),
  serialized_pb=_b('\nEgoogle/ads/googleads_v3/proto/resources/account_budget_proposal.proto\x12!google.ads.googleads.v3.resources\x1aHgoogle/ads/googleads_v3/proto/enums/account_budget_proposal_status.proto\x1a\x46google/ads/googleads_v3/proto/enums/account_budget_proposal_type.proto\x1a=google/ads/googleads_v3/proto/enums/spending_limit_type.proto\x1a\x33google/ads/googleads_v3/proto/enums/time_type.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xaf\x0e\n\x15\x41\x63\x63ountBudgetProposal\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\'\n\x02id\x18\x0e \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x33\n\rbilling_setup\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0e\x61\x63\x63ount_budget\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12m\n\rproposal_type\x18\x04 \x01(\x0e\x32V.google.ads.googleads.v3.enums.AccountBudgetProposalTypeEnum.AccountBudgetProposalType\x12j\n\x06status\x18\x0f \x01(\x0e\x32Z.google.ads.googleads.v3.enums.AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus\x12\x33\n\rproposed_name\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12>\n\x18\x61pproved_start_date_time\x18\x14 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x44\n\x1eproposed_purchase_order_number\x18\x0c \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0eproposed_notes\x18\r \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x12\x63reation_date_time\x18\x10 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x12\x61pproval_date_time\x18\x11 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12@\n\x18proposed_start_date_time\x18\x12 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x12X\n\x18proposed_start_time_type\x18\x07 \x01(\x0e\x32\x34.google.ads.googleads.v3.enums.TimeTypeEnum.TimeTypeH\x00\x12>\n\x16proposed_end_date_time\x18\x13 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x01\x12V\n\x16proposed_end_time_type\x18\t \x01(\x0e\x32\x34.google.ads.googleads.v3.enums.TimeTypeEnum.TimeTypeH\x01\x12>\n\x16\x61pproved_end_date_time\x18\x15 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x02\x12V\n\x16\x61pproved_end_time_type\x18\x16 \x01(\x0e\x32\x34.google.ads.googleads.v3.enums.TimeTypeEnum.TimeTypeH\x02\x12\x45\n\x1eproposed_spending_limit_micros\x18\n \x01(\x0b\x32\x1b.google.protobuf.Int64ValueH\x03\x12n\n\x1cproposed_spending_limit_type\x18\x0b \x01(\x0e\x32\x46.google.ads.googleads.v3.enums.SpendingLimitTypeEnum.SpendingLimitTypeH\x03\x12\x45\n\x1e\x61pproved_spending_limit_micros\x18\x17 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueH\x04\x12n\n\x1c\x61pproved_spending_limit_type\x18\x18 \x01(\x0e\x32\x46.google.ads.googleads.v3.enums.SpendingLimitTypeEnum.SpendingLimitTypeH\x04:z\xea\x41w\n.googleads.googleapis.com/AccountBudgetProposal\x12\x45\x63ustomers/{customer}/accountBudgetProposals/{account_budget_proposal}B\x15\n\x13proposed_start_timeB\x13\n\x11proposed_end_timeB\x13\n\x11\x61pproved_end_timeB\x19\n\x17proposed_spending_limitB\x19\n\x17\x61pproved_spending_limitB\x87\x02\n%com.google.ads.googleads.v3.resourcesB\x1a\x41\x63\x63ountBudgetProposalProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V3.Resources\xca\x02!Google\\Ads\\GoogleAds\\V3\\Resources\xea\x02%Google::Ads::GoogleAds::V3::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_account__budget__proposal__status__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_account__budget__proposal__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_spending__limit__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_time__type__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_ACCOUNTBUDGETPROPOSAL = _descriptor.Descriptor(
  name='AccountBudgetProposal',
  full_name='google.ads.googleads.v3.resources.AccountBudgetProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.id', index=1,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='billing_setup', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.billing_setup', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_budget', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.account_budget', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposal_type', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.proposal_type', index=4,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.status', index=5,
      number=15, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposed_name', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.proposed_name', index=6,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='approved_start_date_time', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.approved_start_date_time', index=7,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposed_purchase_order_number', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.proposed_purchase_order_number', index=8,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposed_notes', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.proposed_notes', index=9,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creation_date_time', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.creation_date_time', index=10,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='approval_date_time', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.approval_date_time', index=11,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposed_start_date_time', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.proposed_start_date_time', index=12,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposed_start_time_type', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.proposed_start_time_type', index=13,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposed_end_date_time', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.proposed_end_date_time', index=14,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposed_end_time_type', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.proposed_end_time_type', index=15,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='approved_end_date_time', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.approved_end_date_time', index=16,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='approved_end_time_type', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.approved_end_time_type', index=17,
      number=22, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposed_spending_limit_micros', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.proposed_spending_limit_micros', index=18,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposed_spending_limit_type', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.proposed_spending_limit_type', index=19,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='approved_spending_limit_micros', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.approved_spending_limit_micros', index=20,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='approved_spending_limit_type', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.approved_spending_limit_type', index=21,
      number=24, type=14, cpp_type=8, label=1,
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
  serialized_options=_b('\352Aw\n.googleads.googleapis.com/AccountBudgetProposal\022Ecustomers/{customer}/accountBudgetProposals/{account_budget_proposal}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='proposed_start_time', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.proposed_start_time',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='proposed_end_time', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.proposed_end_time',
      index=1, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='approved_end_time', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.approved_end_time',
      index=2, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='proposed_spending_limit', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.proposed_spending_limit',
      index=3, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='approved_spending_limit', full_name='google.ads.googleads.v3.resources.AccountBudgetProposal.approved_spending_limit',
      index=4, containing_type=None, fields=[]),
  ],
  serialized_start=460,
  serialized_end=2299,
)

_ACCOUNTBUDGETPROPOSAL.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['billing_setup'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['account_budget'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['proposal_type'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_account__budget__proposal__type__pb2._ACCOUNTBUDGETPROPOSALTYPEENUM_ACCOUNTBUDGETPROPOSALTYPE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_account__budget__proposal__status__pb2._ACCOUNTBUDGETPROPOSALSTATUSENUM_ACCOUNTBUDGETPROPOSALSTATUS
_ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['approved_start_date_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_purchase_order_number'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_notes'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['creation_date_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['approval_date_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_start_date_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_start_time_type'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_time__type__pb2._TIMETYPEENUM_TIMETYPE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_end_date_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_end_time_type'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_time__type__pb2._TIMETYPEENUM_TIMETYPE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['approved_end_date_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['approved_end_time_type'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_time__type__pb2._TIMETYPEENUM_TIMETYPE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_spending_limit_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_spending_limit_type'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_spending__limit__type__pb2._SPENDINGLIMITTYPEENUM_SPENDINGLIMITTYPE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['approved_spending_limit_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_ACCOUNTBUDGETPROPOSAL.fields_by_name['approved_spending_limit_type'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_spending__limit__type__pb2._SPENDINGLIMITTYPEENUM_SPENDINGLIMITTYPE
_ACCOUNTBUDGETPROPOSAL.oneofs_by_name['proposed_start_time'].fields.append(
  _ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_start_date_time'])
_ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_start_date_time'].containing_oneof = _ACCOUNTBUDGETPROPOSAL.oneofs_by_name['proposed_start_time']
_ACCOUNTBUDGETPROPOSAL.oneofs_by_name['proposed_start_time'].fields.append(
  _ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_start_time_type'])
_ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_start_time_type'].containing_oneof = _ACCOUNTBUDGETPROPOSAL.oneofs_by_name['proposed_start_time']
_ACCOUNTBUDGETPROPOSAL.oneofs_by_name['proposed_end_time'].fields.append(
  _ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_end_date_time'])
_ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_end_date_time'].containing_oneof = _ACCOUNTBUDGETPROPOSAL.oneofs_by_name['proposed_end_time']
_ACCOUNTBUDGETPROPOSAL.oneofs_by_name['proposed_end_time'].fields.append(
  _ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_end_time_type'])
_ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_end_time_type'].containing_oneof = _ACCOUNTBUDGETPROPOSAL.oneofs_by_name['proposed_end_time']
_ACCOUNTBUDGETPROPOSAL.oneofs_by_name['approved_end_time'].fields.append(
  _ACCOUNTBUDGETPROPOSAL.fields_by_name['approved_end_date_time'])
_ACCOUNTBUDGETPROPOSAL.fields_by_name['approved_end_date_time'].containing_oneof = _ACCOUNTBUDGETPROPOSAL.oneofs_by_name['approved_end_time']
_ACCOUNTBUDGETPROPOSAL.oneofs_by_name['approved_end_time'].fields.append(
  _ACCOUNTBUDGETPROPOSAL.fields_by_name['approved_end_time_type'])
_ACCOUNTBUDGETPROPOSAL.fields_by_name['approved_end_time_type'].containing_oneof = _ACCOUNTBUDGETPROPOSAL.oneofs_by_name['approved_end_time']
_ACCOUNTBUDGETPROPOSAL.oneofs_by_name['proposed_spending_limit'].fields.append(
  _ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_spending_limit_micros'])
_ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_spending_limit_micros'].containing_oneof = _ACCOUNTBUDGETPROPOSAL.oneofs_by_name['proposed_spending_limit']
_ACCOUNTBUDGETPROPOSAL.oneofs_by_name['proposed_spending_limit'].fields.append(
  _ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_spending_limit_type'])
_ACCOUNTBUDGETPROPOSAL.fields_by_name['proposed_spending_limit_type'].containing_oneof = _ACCOUNTBUDGETPROPOSAL.oneofs_by_name['proposed_spending_limit']
_ACCOUNTBUDGETPROPOSAL.oneofs_by_name['approved_spending_limit'].fields.append(
  _ACCOUNTBUDGETPROPOSAL.fields_by_name['approved_spending_limit_micros'])
_ACCOUNTBUDGETPROPOSAL.fields_by_name['approved_spending_limit_micros'].containing_oneof = _ACCOUNTBUDGETPROPOSAL.oneofs_by_name['approved_spending_limit']
_ACCOUNTBUDGETPROPOSAL.oneofs_by_name['approved_spending_limit'].fields.append(
  _ACCOUNTBUDGETPROPOSAL.fields_by_name['approved_spending_limit_type'])
_ACCOUNTBUDGETPROPOSAL.fields_by_name['approved_spending_limit_type'].containing_oneof = _ACCOUNTBUDGETPROPOSAL.oneofs_by_name['approved_spending_limit']
DESCRIPTOR.message_types_by_name['AccountBudgetProposal'] = _ACCOUNTBUDGETPROPOSAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccountBudgetProposal = _reflection.GeneratedProtocolMessageType('AccountBudgetProposal', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTBUDGETPROPOSAL,
  __module__ = 'google.ads.googleads_v3.proto.resources.account_budget_proposal_pb2'
  ,
  __doc__ = """An account-level budget proposal.
  
  All fields prefixed with 'proposed' may not necessarily be applied
  directly. For example, proposed spending limits may be adjusted before
  their application. This is true if the 'proposed' field has an
  'approved' counterpart, e.g. spending limits.
  
  Please note that the proposal type (proposal\_type) changes which fields
  are required and which must remain empty.
  
  
  Attributes:
      resource_name:
          The resource name of the proposal. AccountBudgetProposal
          resource names have the form:  ``customers/{customer_id}/accou
          ntBudgetProposals/{account_budget_proposal_id}``
      id:
          The ID of the proposal.
      billing_setup:
          The resource name of the billing setup associated with this
          proposal.
      account_budget:
          The resource name of the account-level budget associated with
          this proposal.
      proposal_type:
          The type of this proposal, e.g. END to end the budget
          associated with this proposal.
      status:
          The status of this proposal. When a new proposal is created,
          the status defaults to PENDING.
      proposed_name:
          The name to assign to the account-level budget.
      approved_start_date_time:
          The approved start date time in yyyy-mm-dd hh:mm:ss format.
      proposed_purchase_order_number:
          A purchase order number is a value that enables the user to
          help them reference this budget in their monthly invoices.
      proposed_notes:
          Notes associated with this budget.
      creation_date_time:
          The date time when this account-level budget proposal was
          created, which is not the same as its approval date time, if
          applicable.
      approval_date_time:
          The date time when this account-level budget was approved, if
          applicable.
      proposed_start_time:
          The proposed start date time of the account-level budget,
          which cannot be in the past.
      proposed_start_date_time:
          The proposed start date time in yyyy-mm-dd hh:mm:ss format.
      proposed_start_time_type:
          The proposed start date time as a well-defined type, e.g. NOW.
      proposed_end_time:
          The proposed end date time of the account-level budget, which
          cannot be in the past.
      proposed_end_date_time:
          The proposed end date time in yyyy-mm-dd hh:mm:ss format.
      proposed_end_time_type:
          The proposed end date time as a well-defined type, e.g.
          FOREVER.
      approved_end_time:
          The approved end date time of the account-level budget.
      approved_end_date_time:
          The approved end date time in yyyy-mm-dd hh:mm:ss format.
      approved_end_time_type:
          The approved end date time as a well-defined type, e.g.
          FOREVER.
      proposed_spending_limit:
          The proposed spending limit.
      proposed_spending_limit_micros:
          The proposed spending limit in micros. One million is
          equivalent to one unit.
      proposed_spending_limit_type:
          The proposed spending limit as a well-defined type, e.g.
          INFINITE.
      approved_spending_limit:
          The approved spending limit.
      approved_spending_limit_micros:
          The approved spending limit in micros. One million is
          equivalent to one unit.
      approved_spending_limit_type:
          The approved spending limit as a well-defined type, e.g.
          INFINITE.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.resources.AccountBudgetProposal)
  ))
_sym_db.RegisterMessage(AccountBudgetProposal)


DESCRIPTOR._options = None
_ACCOUNTBUDGETPROPOSAL._options = None
# @@protoc_insertion_point(module_scope)
