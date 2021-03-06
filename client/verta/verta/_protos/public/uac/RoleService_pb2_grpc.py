# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ...public.uac import RoleService_pb2 as protos_dot_public_dot_uac_dot_RoleService__pb2


class RoleServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getRoleById = channel.unary_unary(
        '/ai.verta.uac.RoleService/getRoleById',
        request_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.GetRoleById.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.GetRoleById.Response.FromString,
        )
    self.getRoleByName = channel.unary_unary(
        '/ai.verta.uac.RoleService/getRoleByName',
        request_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.GetRoleByName.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.GetRoleByName.Response.FromString,
        )
    self.listRoles = channel.unary_unary(
        '/ai.verta.uac.RoleService/listRoles',
        request_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.ListRoles.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.ListRoles.Response.FromString,
        )
    self.setRole = channel.unary_unary(
        '/ai.verta.uac.RoleService/setRole',
        request_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.SetRole.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.SetRole.Response.FromString,
        )
    self.deleteRole = channel.unary_unary(
        '/ai.verta.uac.RoleService/deleteRole',
        request_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.DeleteRole.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.DeleteRole.Response.FromString,
        )
    self.getBindingRoleById = channel.unary_unary(
        '/ai.verta.uac.RoleService/getBindingRoleById',
        request_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.GetRoleBindingById.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.GetRoleBindingById.Response.FromString,
        )
    self.getRoleBindingByName = channel.unary_unary(
        '/ai.verta.uac.RoleService/getRoleBindingByName',
        request_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.GetRoleBindingByName.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.GetRoleBindingByName.Response.FromString,
        )
    self.listRoleBindings = channel.unary_unary(
        '/ai.verta.uac.RoleService/listRoleBindings',
        request_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.ListRoleBindings.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.ListRoleBindings.Response.FromString,
        )
    self.setRoleBinding = channel.unary_unary(
        '/ai.verta.uac.RoleService/setRoleBinding',
        request_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.SetRoleBinding.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.SetRoleBinding.Response.FromString,
        )
    self.deleteRoleBinding = channel.unary_unary(
        '/ai.verta.uac.RoleService/deleteRoleBinding',
        request_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.DeleteRoleBinding.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.DeleteRoleBinding.Response.FromString,
        )
    self.deleteRoleBindings = channel.unary_unary(
        '/ai.verta.uac.RoleService/deleteRoleBindings',
        request_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.DeleteRoleBindings.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.DeleteRoleBindings.Response.FromString,
        )


class RoleServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def getRoleById(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getRoleByName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def listRoles(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def setRole(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteRole(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getBindingRoleById(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getRoleBindingByName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def listRoleBindings(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def setRoleBinding(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteRoleBinding(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteRoleBindings(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RoleServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getRoleById': grpc.unary_unary_rpc_method_handler(
          servicer.getRoleById,
          request_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.GetRoleById.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.GetRoleById.Response.SerializeToString,
      ),
      'getRoleByName': grpc.unary_unary_rpc_method_handler(
          servicer.getRoleByName,
          request_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.GetRoleByName.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.GetRoleByName.Response.SerializeToString,
      ),
      'listRoles': grpc.unary_unary_rpc_method_handler(
          servicer.listRoles,
          request_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.ListRoles.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.ListRoles.Response.SerializeToString,
      ),
      'setRole': grpc.unary_unary_rpc_method_handler(
          servicer.setRole,
          request_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.SetRole.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.SetRole.Response.SerializeToString,
      ),
      'deleteRole': grpc.unary_unary_rpc_method_handler(
          servicer.deleteRole,
          request_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.DeleteRole.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.DeleteRole.Response.SerializeToString,
      ),
      'getBindingRoleById': grpc.unary_unary_rpc_method_handler(
          servicer.getBindingRoleById,
          request_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.GetRoleBindingById.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.GetRoleBindingById.Response.SerializeToString,
      ),
      'getRoleBindingByName': grpc.unary_unary_rpc_method_handler(
          servicer.getRoleBindingByName,
          request_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.GetRoleBindingByName.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.GetRoleBindingByName.Response.SerializeToString,
      ),
      'listRoleBindings': grpc.unary_unary_rpc_method_handler(
          servicer.listRoleBindings,
          request_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.ListRoleBindings.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.ListRoleBindings.Response.SerializeToString,
      ),
      'setRoleBinding': grpc.unary_unary_rpc_method_handler(
          servicer.setRoleBinding,
          request_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.SetRoleBinding.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.SetRoleBinding.Response.SerializeToString,
      ),
      'deleteRoleBinding': grpc.unary_unary_rpc_method_handler(
          servicer.deleteRoleBinding,
          request_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.DeleteRoleBinding.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.DeleteRoleBinding.Response.SerializeToString,
      ),
      'deleteRoleBindings': grpc.unary_unary_rpc_method_handler(
          servicer.deleteRoleBindings,
          request_deserializer=protos_dot_public_dot_uac_dot_RoleService__pb2.DeleteRoleBindings.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_RoleService__pb2.DeleteRoleBindings.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ai.verta.uac.RoleService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
