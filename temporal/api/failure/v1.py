# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: temporal/api/failure/v1/message.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .temporal.api.common import v1
from .temporal.api.enums import v1


@dataclass
class ApplicationFailureInfo(betterproto.Message):
    type: str = betterproto.string_field(1)
    non_retryable: bool = betterproto.bool_field(2)
    details: v1.Payloads = betterproto.message_field(3)


@dataclass
class TimeoutFailureInfo(betterproto.Message):
    timeout_type: v1.TimeoutType = betterproto.enum_field(1)
    last_heartbeat_details: v1.Payloads = betterproto.message_field(2)


@dataclass
class CanceledFailureInfo(betterproto.Message):
    details: v1.Payloads = betterproto.message_field(1)


@dataclass
class TerminatedFailureInfo(betterproto.Message):
    pass


@dataclass
class ServerFailureInfo(betterproto.Message):
    non_retryable: bool = betterproto.bool_field(1)


@dataclass
class ResetWorkflowFailureInfo(betterproto.Message):
    last_heartbeat_details: v1.Payloads = betterproto.message_field(1)


@dataclass
class ActivityFailureInfo(betterproto.Message):
    scheduled_event_id: int = betterproto.int64_field(1)
    started_event_id: int = betterproto.int64_field(2)
    identity: str = betterproto.string_field(3)
    activity_type: v1.ActivityType = betterproto.message_field(4)
    activity_id: str = betterproto.string_field(5)
    retry_state: v1.RetryState = betterproto.enum_field(6)


@dataclass
class ChildWorkflowExecutionFailureInfo(betterproto.Message):
    namespace: str = betterproto.string_field(1)
    workflow_execution: v1.WorkflowExecution = betterproto.message_field(2)
    workflow_type: v1.WorkflowType = betterproto.message_field(3)
    initiated_event_id: int = betterproto.int64_field(4)
    started_event_id: int = betterproto.int64_field(5)
    retry_state: v1.RetryState = betterproto.enum_field(6)


@dataclass
class Failure(betterproto.Message):
    message: str = betterproto.string_field(1)
    source: str = betterproto.string_field(2)
    stack_trace: str = betterproto.string_field(3)
    cause: "Failure" = betterproto.message_field(4)
    application_failure_info: "ApplicationFailureInfo" = betterproto.message_field(
        5, group="failure_info"
    )
    timeout_failure_info: "TimeoutFailureInfo" = betterproto.message_field(
        6, group="failure_info"
    )
    canceled_failure_info: "CanceledFailureInfo" = betterproto.message_field(
        7, group="failure_info"
    )
    terminated_failure_info: "TerminatedFailureInfo" = betterproto.message_field(
        8, group="failure_info"
    )
    server_failure_info: "ServerFailureInfo" = betterproto.message_field(
        9, group="failure_info"
    )
    reset_workflow_failure_info: "ResetWorkflowFailureInfo" = betterproto.message_field(
        10, group="failure_info"
    )
    activity_failure_info: "ActivityFailureInfo" = betterproto.message_field(
        11, group="failure_info"
    )
    child_workflow_execution_failure_info: "ChildWorkflowExecutionFailureInfo" = betterproto.message_field(
        12, group="failure_info"
    )
