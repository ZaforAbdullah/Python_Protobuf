from protoCompile import proto_pb2
from path_helpers import get_protobuf_output_dir

def main():

    # Create an instance of Proto message
    proto_message = proto_pb2.Proto()

    # Use the helper function to get the output directory
    protobuf_output_dir = get_protobuf_output_dir("protoOutput", "protobuf_output")
    
    # Set fields based on predefined values
    proto_message.username = "Username"
    proto_message.total_capcity = 100
    proto_message.mobile = 1234567890
    proto_message.base_ticket_price = 10.5
    proto_message.drive_in = True
    proto_message.payment = proto_pb2.Proto.CREDIT_CARD
    proto_message.snacks.extend(["Popcorn", "Soda"])
    proto_message.movieTicketPrice["Action"] = 15
    proto_message.movieTicketPrice["Drama"] = 12

    # Create an instance of ProtoChild message and set its fields
    proto_child = proto_pb2.ProtoChild()
    proto_child.name = "protochild"
    proto_child.age = "30"
    proto_message.protochild.CopyFrom(proto_child)

    # Serialize Proto message to a file
    print("Saving to file:", protobuf_output_dir)
    with open(protobuf_output_dir, "wb") as f:
        f.write(proto_message.SerializeToString())

    print("Saved Proto message to disk:\n", proto_message)

if __name__ == "__main__":
    main()
