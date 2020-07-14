# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: temporal/api/replication/v1/message.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class ClusterReplicationConfig(betterproto.Message):
    cluster_name: str = betterproto.string_field(1)


@dataclass
class NamespaceReplicationConfig(betterproto.Message):
    active_cluster_name: str = betterproto.string_field(1)
    clusters: List["ClusterReplicationConfig"] = betterproto.message_field(2)
