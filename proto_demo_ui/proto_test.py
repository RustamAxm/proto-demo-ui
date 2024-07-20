
from generation.py_gen import proto_app_pb2


def fill_dict(type_comlect, out_dict):
    DESCRIPTORS = type_comlect.message_type.fields_by_name
    for (field_name, field_descriptor) in DESCRIPTORS.items():
        if field_descriptor.message_type:
            # Composite field
            out_dict[field_name] = {}
            fill_dict(field_descriptor, out_dict[field_name])
        else:
            # Raw type
            out_dict[field_name] = field_descriptor.type


def get_proto_dict():
    app = proto_app_pb2.Application()
    DESCRIPTORS = app.DESCRIPTOR.fields_by_name

    out_dict = {}
    for (field_name, field_descriptor) in DESCRIPTORS.items():
        if field_descriptor.message_type:
            out_dict[field_name] = {}
            fill_dict(field_descriptor, out_dict[field_name])
        else:
            # Raw type
            out_dict[field_name] = field_descriptor.type

    return out_dict


if __name__ == '__main__':
    get_proto_dict()
