# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: temporal/api/query/v1/message.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .temporal.api.common import v1
from .temporal.api.enums import v1


@dataclass
class WorkflowQuery(betterproto.Message):
    query_type: str = betterproto.string_field(1)
    query_args: v1.Payloads = betterproto.message_field(2)


@dataclass
class WorkflowQueryResult(betterproto.Message):
    result_type: v1.QueryResultType = betterproto.enum_field(1)
    answer: v1.Payloads = betterproto.message_field(2)
    error_message: str = betterproto.string_field(3)


@dataclass
class QueryRejected(betterproto.Message):
    status: v1.WorkflowExecutionStatus = betterproto.enum_field(1)
