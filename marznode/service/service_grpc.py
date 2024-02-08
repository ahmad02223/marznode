# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: marznode/service/service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.client
import grpclib.const

if typing.TYPE_CHECKING:
    import grpclib.server

import marznode.service.service_pb2


class MarzServiceBase(abc.ABC):

    @abc.abstractmethod
    async def AddUser(self, stream: 'grpclib.server.Stream[marznode.service.service_pb2.UserUpdate, marznode.service.service_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveUser(self, stream: 'grpclib.server.Stream[marznode.service.service_pb2.UserUpdate, marznode.service.service_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateUserInbounds(self, stream: 'grpclib.server.Stream[marznode.service.service_pb2.UserUpdate, marznode.service.service_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def RepopulateUsers(self, stream: 'grpclib.server.Stream[marznode.service.service_pb2.UsersUpdate, marznode.service.service_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def FetchInbounds(self, stream: 'grpclib.server.Stream[marznode.service.service_pb2.Empty, marznode.service.service_pb2.InboundsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FetchUsersStats(self, stream: 'grpclib.server.Stream[marznode.service.service_pb2.Empty, marznode.service.service_pb2.UsersStats]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/marznode.MarzService/AddUser': grpclib.const.Handler(
                self.AddUser,
                grpclib.const.Cardinality.UNARY_UNARY,
                marznode.service.service_pb2.UserUpdate,
                marznode.service.service_pb2.Empty,
            ),
            '/marznode.MarzService/RemoveUser': grpclib.const.Handler(
                self.RemoveUser,
                grpclib.const.Cardinality.UNARY_UNARY,
                marznode.service.service_pb2.UserUpdate,
                marznode.service.service_pb2.Empty,
            ),
            '/marznode.MarzService/UpdateUserInbounds': grpclib.const.Handler(
                self.UpdateUserInbounds,
                grpclib.const.Cardinality.UNARY_UNARY,
                marznode.service.service_pb2.UserUpdate,
                marznode.service.service_pb2.Empty,
            ),
            '/marznode.MarzService/RepopulateUsers': grpclib.const.Handler(
                self.RepopulateUsers,
                grpclib.const.Cardinality.UNARY_UNARY,
                marznode.service.service_pb2.UsersUpdate,
                marznode.service.service_pb2.Empty,
            ),
            '/marznode.MarzService/FetchInbounds': grpclib.const.Handler(
                self.FetchInbounds,
                grpclib.const.Cardinality.UNARY_UNARY,
                marznode.service.service_pb2.Empty,
                marznode.service.service_pb2.InboundsResponse,
            ),
            '/marznode.MarzService/FetchUsersStats': grpclib.const.Handler(
                self.FetchUsersStats,
                grpclib.const.Cardinality.UNARY_UNARY,
                marznode.service.service_pb2.Empty,
                marznode.service.service_pb2.UsersStats,
            ),
        }


class MarzServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.AddUser = grpclib.client.UnaryUnaryMethod(
            channel,
            '/marznode.MarzService/AddUser',
            marznode.service.service_pb2.UserUpdate,
            marznode.service.service_pb2.Empty,
        )
        self.RemoveUser = grpclib.client.UnaryUnaryMethod(
            channel,
            '/marznode.MarzService/RemoveUser',
            marznode.service.service_pb2.UserUpdate,
            marznode.service.service_pb2.Empty,
        )
        self.UpdateUserInbounds = grpclib.client.UnaryUnaryMethod(
            channel,
            '/marznode.MarzService/UpdateUserInbounds',
            marznode.service.service_pb2.UserUpdate,
            marznode.service.service_pb2.Empty,
        )
        self.RepopulateUsers = grpclib.client.UnaryUnaryMethod(
            channel,
            '/marznode.MarzService/RepopulateUsers',
            marznode.service.service_pb2.UsersUpdate,
            marznode.service.service_pb2.Empty,
        )
        self.FetchInbounds = grpclib.client.UnaryUnaryMethod(
            channel,
            '/marznode.MarzService/FetchInbounds',
            marznode.service.service_pb2.Empty,
            marznode.service.service_pb2.InboundsResponse,
        )
        self.FetchUsersStats = grpclib.client.UnaryUnaryMethod(
            channel,
            '/marznode.MarzService/FetchUsersStats',
            marznode.service.service_pb2.Empty,
            marznode.service.service_pb2.UsersStats,
        )