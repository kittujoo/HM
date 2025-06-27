"""
Desc: This file contains the response received from a channel configuration get request
"""
from dataclasses import dataclass
from typing import List
from typing import Optional


@dataclass
class CommonMetaParameter:
    paramType: str
    paramData: str


@dataclass
class CommonMetaMessageArgs:
    params: List[CommonMetaParameter]


@dataclass
class CommonMetaMessage:
    resourceId: str
    fmt8bit: str
    source: str
    formatted: str
    argList: CommonMetaMessageArgs = None


@dataclass
class SystemMetaChannelAxis:
    dataInterval: float
    dataInterval: float
    description: CommonMetaMessage


@dataclass
class SystemMetaChannelDataFormat:
    dataType: int
    xAxis: SystemMetaChannelAxis
    yAxis: SystemMetaChannelAxis
    nominalSizeInBytes: int
    nominalDataRateHz: int


@dataclass
class SystemMetaChannelDescriptor:
    enable: bool
    active: bool
    source: int
    deviceType: str
    deviceId: str
    channelName: str
    registeredId: str
    injectionId: str
    channelUuid: str
    channelDescription: CommonMetaMessage
    dataFormat: SystemMetaChannelDataFormat
    channelIdentifier: str


@dataclass
class SystemRepeatChannelDescriptor:
    channelDescriptor: SystemMetaChannelDescriptor


@dataclass
class ChannelConfigurationResponse:
    channels: List[SystemRepeatChannelDescriptor]
    dataModelType: str
    dataModelVersion: int
