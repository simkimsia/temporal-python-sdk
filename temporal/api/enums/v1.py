# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: temporal/api/enums/v1/task_queue.proto, temporal/api/enums/v1/workflow.proto, temporal/api/enums/v1/namespace.proto, temporal/api/enums/v1/failed_cause.proto, temporal/api/enums/v1/common.proto, temporal/api/enums/v1/query.proto, temporal/api/enums/v1/event_type.proto, temporal/api/enums/v1/command_type.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class TaskQueueKind(betterproto.Enum):
    TASK_QUEUE_KIND_UNSPECIFIED = 0
    TASK_QUEUE_KIND_NORMAL = 1
    TASK_QUEUE_KIND_STICKY = 2


class TaskQueueType(betterproto.Enum):
    TASK_QUEUE_TYPE_UNSPECIFIED = 0
    # Workflow type of task queue.
    TASK_QUEUE_TYPE_WORKFLOW = 1
    # Activity type of task queue.
    TASK_QUEUE_TYPE_ACTIVITY = 2


class WorkflowIdReusePolicy(betterproto.Enum):
    WORKFLOW_ID_REUSE_POLICY_UNSPECIFIED = 0
    # Allow start a workflow execution using the same workflow Id, when workflow
    # not running.
    WORKFLOW_ID_REUSE_POLICY_ALLOW_DUPLICATE = 1
    # Allow start a workflow execution using the same workflow Id, when workflow
    # not running, and the last execution close state is in [terminated,
    # cancelled, timed out, failed].
    WORKFLOW_ID_REUSE_POLICY_ALLOW_DUPLICATE_FAILED_ONLY = 2
    # Do not allow start a workflow execution using the same workflow Id at all.
    WORKFLOW_ID_REUSE_POLICY_REJECT_DUPLICATE = 3


class ParentClosePolicy(betterproto.Enum):
    PARENT_CLOSE_POLICY_UNSPECIFIED = 0
    # Terminate means terminating the child workflow.
    PARENT_CLOSE_POLICY_TERMINATE = 1
    # Abandon means not doing anything on the child workflow.
    PARENT_CLOSE_POLICY_ABANDON = 2
    # Cancel means requesting cancellation on the child workflow.
    PARENT_CLOSE_POLICY_REQUEST_CANCEL = 3


class ContinueAsNewInitiator(betterproto.Enum):
    CONTINUE_AS_NEW_INITIATOR_UNSPECIFIED = 0
    CONTINUE_AS_NEW_INITIATOR_WORKFLOW = 1
    CONTINUE_AS_NEW_INITIATOR_RETRY = 2
    CONTINUE_AS_NEW_INITIATOR_CRON_SCHEDULE = 3


class WorkflowExecutionStatus(betterproto.Enum):
    """
    (-- api-linter: core::0216::synonyms=disabled     aip.dev/not-precedent:
    There is WorkflowExecutionState already in another package. --)
    """

    WORKFLOW_EXECUTION_STATUS_UNSPECIFIED = 0
    # Value 1 is hardcoded in SQL persistence.
    WORKFLOW_EXECUTION_STATUS_RUNNING = 1
    WORKFLOW_EXECUTION_STATUS_COMPLETED = 2
    WORKFLOW_EXECUTION_STATUS_FAILED = 3
    WORKFLOW_EXECUTION_STATUS_CANCELED = 4
    WORKFLOW_EXECUTION_STATUS_TERMINATED = 5
    WORKFLOW_EXECUTION_STATUS_CONTINUED_AS_NEW = 6
    WORKFLOW_EXECUTION_STATUS_TIMED_OUT = 7


class PendingActivityState(betterproto.Enum):
    PENDING_ACTIVITY_STATE_UNSPECIFIED = 0
    PENDING_ACTIVITY_STATE_SCHEDULED = 1
    PENDING_ACTIVITY_STATE_STARTED = 2
    PENDING_ACTIVITY_STATE_CANCEL_REQUESTED = 3


class HistoryEventFilterType(betterproto.Enum):
    HISTORY_EVENT_FILTER_TYPE_UNSPECIFIED = 0
    HISTORY_EVENT_FILTER_TYPE_ALL_EVENT = 1
    HISTORY_EVENT_FILTER_TYPE_CLOSE_EVENT = 2


class RetryState(betterproto.Enum):
    RETRY_STATE_UNSPECIFIED = 0
    RETRY_STATE_IN_PROGRESS = 1
    RETRY_STATE_NON_RETRYABLE_FAILURE = 2
    RETRY_STATE_TIMEOUT = 3
    RETRY_STATE_MAXIMUM_ATTEMPTS_REACHED = 4
    RETRY_STATE_RETRY_POLICY_NOT_SET = 5
    RETRY_STATE_INTERNAL_SERVER_ERROR = 6
    RETRY_STATE_CANCEL_REQUESTED = 7


class TimeoutType(betterproto.Enum):
    TIMEOUT_TYPE_UNSPECIFIED = 0
    TIMEOUT_TYPE_START_TO_CLOSE = 1
    TIMEOUT_TYPE_SCHEDULE_TO_START = 2
    TIMEOUT_TYPE_SCHEDULE_TO_CLOSE = 3
    TIMEOUT_TYPE_HEARTBEAT = 4


class NamespaceState(betterproto.Enum):
    NAMESPACE_STATE_UNSPECIFIED = 0
    NAMESPACE_STATE_REGISTERED = 1
    NAMESPACE_STATE_DEPRECATED = 2
    NAMESPACE_STATE_DELETED = 3


class ArchivalState(betterproto.Enum):
    ARCHIVAL_STATE_UNSPECIFIED = 0
    ARCHIVAL_STATE_DISABLED = 1
    ARCHIVAL_STATE_ENABLED = 2


class WorkflowTaskFailedCause(betterproto.Enum):
    WORKFLOW_TASK_FAILED_CAUSE_UNSPECIFIED = 0
    WORKFLOW_TASK_FAILED_CAUSE_UNHANDLED_COMMAND = 1
    WORKFLOW_TASK_FAILED_CAUSE_BAD_SCHEDULE_ACTIVITY_ATTRIBUTES = 2
    WORKFLOW_TASK_FAILED_CAUSE_BAD_REQUEST_CANCEL_ACTIVITY_ATTRIBUTES = 3
    WORKFLOW_TASK_FAILED_CAUSE_BAD_START_TIMER_ATTRIBUTES = 4
    WORKFLOW_TASK_FAILED_CAUSE_BAD_CANCEL_TIMER_ATTRIBUTES = 5
    WORKFLOW_TASK_FAILED_CAUSE_BAD_RECORD_MARKER_ATTRIBUTES = 6
    WORKFLOW_TASK_FAILED_CAUSE_BAD_COMPLETE_WORKFLOW_EXECUTION_ATTRIBUTES = 7
    WORKFLOW_TASK_FAILED_CAUSE_BAD_FAIL_WORKFLOW_EXECUTION_ATTRIBUTES = 8
    WORKFLOW_TASK_FAILED_CAUSE_BAD_CANCEL_WORKFLOW_EXECUTION_ATTRIBUTES = 9
    WORKFLOW_TASK_FAILED_CAUSE_BAD_REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_ATTRIBUTES = (
        10
    )
    WORKFLOW_TASK_FAILED_CAUSE_BAD_CONTINUE_AS_NEW_ATTRIBUTES = 11
    WORKFLOW_TASK_FAILED_CAUSE_START_TIMER_DUPLICATE_ID = 12
    WORKFLOW_TASK_FAILED_CAUSE_RESET_STICKY_TASK_QUEUE = 13
    WORKFLOW_TASK_FAILED_CAUSE_WORKFLOW_WORKER_UNHANDLED_FAILURE = 14
    WORKFLOW_TASK_FAILED_CAUSE_BAD_SIGNAL_WORKFLOW_EXECUTION_ATTRIBUTES = 15
    WORKFLOW_TASK_FAILED_CAUSE_BAD_START_CHILD_EXECUTION_ATTRIBUTES = 16
    WORKFLOW_TASK_FAILED_CAUSE_FORCE_CLOSE_COMMAND = 17
    WORKFLOW_TASK_FAILED_CAUSE_FAILOVER_CLOSE_COMMAND = 18
    WORKFLOW_TASK_FAILED_CAUSE_BAD_SIGNAL_INPUT_SIZE = 19
    WORKFLOW_TASK_FAILED_CAUSE_RESET_WORKFLOW = 20
    WORKFLOW_TASK_FAILED_CAUSE_BAD_BINARY = 21
    WORKFLOW_TASK_FAILED_CAUSE_SCHEDULE_ACTIVITY_DUPLICATE_ID = 22
    WORKFLOW_TASK_FAILED_CAUSE_BAD_SEARCH_ATTRIBUTES = 23


class StartChildWorkflowExecutionFailedCause(betterproto.Enum):
    START_CHILD_WORKFLOW_EXECUTION_FAILED_CAUSE_UNSPECIFIED = 0
    START_CHILD_WORKFLOW_EXECUTION_FAILED_CAUSE_WORKFLOW_ALREADY_EXISTS = 1


class CancelExternalWorkflowExecutionFailedCause(betterproto.Enum):
    CANCEL_EXTERNAL_WORKFLOW_EXECUTION_FAILED_CAUSE_UNSPECIFIED = 0
    CANCEL_EXTERNAL_WORKFLOW_EXECUTION_FAILED_CAUSE_EXTERNAL_WORKFLOW_EXECUTION_NOT_FOUND = (
        1
    )


class SignalExternalWorkflowExecutionFailedCause(betterproto.Enum):
    SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_FAILED_CAUSE_UNSPECIFIED = 0
    SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_FAILED_CAUSE_EXTERNAL_WORKFLOW_EXECUTION_NOT_FOUND = (
        1
    )


class EncodingType(betterproto.Enum):
    ENCODING_TYPE_UNSPECIFIED = 0
    ENCODING_TYPE_PROTO3 = 1
    ENCODING_TYPE_JSON = 2


class IndexedValueType(betterproto.Enum):
    INDEXED_VALUE_TYPE_UNSPECIFIED = 0
    INDEXED_VALUE_TYPE_STRING = 1
    INDEXED_VALUE_TYPE_KEYWORD = 2
    INDEXED_VALUE_TYPE_INT = 3
    INDEXED_VALUE_TYPE_DOUBLE = 4
    INDEXED_VALUE_TYPE_BOOL = 5
    INDEXED_VALUE_TYPE_DATETIME = 6


class QueryResultType(betterproto.Enum):
    QUERY_RESULT_TYPE_UNSPECIFIED = 0
    QUERY_RESULT_TYPE_ANSWERED = 1
    QUERY_RESULT_TYPE_FAILED = 2


class QueryRejectCondition(betterproto.Enum):
    QUERY_REJECT_CONDITION_UNSPECIFIED = 0
    # None indicates that query should not be rejected.
    QUERY_REJECT_CONDITION_NONE = 1
    # NotOpen indicates that query should be rejected if workflow is not open.
    QUERY_REJECT_CONDITION_NOT_OPEN = 2
    # NotCompletedCleanly indicates that query should be rejected if workflow did
    # not complete cleanly.
    QUERY_REJECT_CONDITION_NOT_COMPLETED_CLEANLY = 3


class EventType(betterproto.Enum):
    """
    Whenever this list of events is changed do change the function
    shouldBufferEvent in mutableStateBuilder.go to make sure to do the correct
    event ordering.
    """

    EVENT_TYPE_UNSPECIFIED = 0
    EVENT_TYPE_WORKFLOW_EXECUTION_STARTED = 1
    EVENT_TYPE_WORKFLOW_EXECUTION_COMPLETED = 2
    EVENT_TYPE_WORKFLOW_EXECUTION_FAILED = 3
    EVENT_TYPE_WORKFLOW_EXECUTION_TIMED_OUT = 4
    EVENT_TYPE_WORKFLOW_TASK_SCHEDULED = 5
    EVENT_TYPE_WORKFLOW_TASK_STARTED = 6
    EVENT_TYPE_WORKFLOW_TASK_COMPLETED = 7
    EVENT_TYPE_WORKFLOW_TASK_TIMED_OUT = 8
    EVENT_TYPE_WORKFLOW_TASK_FAILED = 9
    EVENT_TYPE_ACTIVITY_TASK_SCHEDULED = 10
    EVENT_TYPE_ACTIVITY_TASK_STARTED = 11
    EVENT_TYPE_ACTIVITY_TASK_COMPLETED = 12
    EVENT_TYPE_ACTIVITY_TASK_FAILED = 13
    EVENT_TYPE_ACTIVITY_TASK_TIMED_OUT = 14
    EVENT_TYPE_ACTIVITY_TASK_CANCEL_REQUESTED = 15
    EVENT_TYPE_REQUEST_CANCEL_ACTIVITY_TASK_FAILED = 16
    EVENT_TYPE_ACTIVITY_TASK_CANCELED = 17
    EVENT_TYPE_TIMER_STARTED = 18
    EVENT_TYPE_TIMER_FIRED = 19
    EVENT_TYPE_CANCEL_TIMER_FAILED = 20
    EVENT_TYPE_TIMER_CANCELED = 21
    EVENT_TYPE_WORKFLOW_EXECUTION_CANCEL_REQUESTED = 22
    EVENT_TYPE_WORKFLOW_EXECUTION_CANCELED = 23
    EVENT_TYPE_REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_INITIATED = 24
    EVENT_TYPE_REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_FAILED = 25
    EVENT_TYPE_EXTERNAL_WORKFLOW_EXECUTION_CANCEL_REQUESTED = 26
    EVENT_TYPE_MARKER_RECORDED = 27
    EVENT_TYPE_WORKFLOW_EXECUTION_SIGNALED = 28
    EVENT_TYPE_WORKFLOW_EXECUTION_TERMINATED = 29
    EVENT_TYPE_WORKFLOW_EXECUTION_CONTINUED_AS_NEW = 30
    EVENT_TYPE_START_CHILD_WORKFLOW_EXECUTION_INITIATED = 31
    EVENT_TYPE_START_CHILD_WORKFLOW_EXECUTION_FAILED = 32
    EVENT_TYPE_CHILD_WORKFLOW_EXECUTION_STARTED = 33
    EVENT_TYPE_CHILD_WORKFLOW_EXECUTION_COMPLETED = 34
    EVENT_TYPE_CHILD_WORKFLOW_EXECUTION_FAILED = 35
    EVENT_TYPE_CHILD_WORKFLOW_EXECUTION_CANCELED = 36
    EVENT_TYPE_CHILD_WORKFLOW_EXECUTION_TIMED_OUT = 37
    EVENT_TYPE_CHILD_WORKFLOW_EXECUTION_TERMINATED = 38
    EVENT_TYPE_SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_INITIATED = 39
    EVENT_TYPE_SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_FAILED = 40
    EVENT_TYPE_EXTERNAL_WORKFLOW_EXECUTION_SIGNALED = 41
    EVENT_TYPE_UPSERT_WORKFLOW_SEARCH_ATTRIBUTES = 42


class CommandType(betterproto.Enum):
    """
    Whenever this list of command types is changed do change the function
    shouldBufferEvent in mutableStateBuilder.go to make sure to do the correct
    event ordering.
    """

    COMMAND_TYPE_UNSPECIFIED = 0
    COMMAND_TYPE_SCHEDULE_ACTIVITY_TASK = 1
    COMMAND_TYPE_REQUEST_CANCEL_ACTIVITY_TASK = 2
    COMMAND_TYPE_START_TIMER = 3
    COMMAND_TYPE_COMPLETE_WORKFLOW_EXECUTION = 4
    COMMAND_TYPE_FAIL_WORKFLOW_EXECUTION = 5
    COMMAND_TYPE_CANCEL_TIMER = 6
    COMMAND_TYPE_CANCEL_WORKFLOW_EXECUTION = 7
    COMMAND_TYPE_REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION = 8
    COMMAND_TYPE_RECORD_MARKER = 9
    COMMAND_TYPE_CONTINUE_AS_NEW_WORKFLOW_EXECUTION = 10
    COMMAND_TYPE_START_CHILD_WORKFLOW_EXECUTION = 11
    COMMAND_TYPE_SIGNAL_EXTERNAL_WORKFLOW_EXECUTION = 12
    COMMAND_TYPE_UPSERT_WORKFLOW_SEARCH_ATTRIBUTES = 13
