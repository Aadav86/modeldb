# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ...public.uac import Telemetry_pb2 as protos_dot_public_dot_uac_dot_Telemetry__pb2


class TelemetryServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.collectTelemetry = channel.unary_unary(
        '/ai.verta.uac.TelemetryService/collectTelemetry',
        request_serializer=protos_dot_public_dot_uac_dot_Telemetry__pb2.CollectTelemetry.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_Telemetry__pb2.CollectTelemetry.Response.FromString,
        )


class TelemetryServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def collectTelemetry(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TelemetryServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'collectTelemetry': grpc.unary_unary_rpc_method_handler(
          servicer.collectTelemetry,
          request_deserializer=protos_dot_public_dot_uac_dot_Telemetry__pb2.CollectTelemetry.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_Telemetry__pb2.CollectTelemetry.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ai.verta.uac.TelemetryService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
