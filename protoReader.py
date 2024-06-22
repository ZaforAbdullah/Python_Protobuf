from protoCompile import proto_pb2
from path_helpers import get_protobuf_output_dir

def main():
    # Create an instance of Proto message
    proto_message = proto_pb2.Proto()
    
    # Use the helper function to get the output directory
    protobuf_output_dir = get_protobuf_output_dir("protoOutput", "protobuf_output")
    
    # Read serialized data from file and parse into Proto message
    print("Reading from file:", protobuf_output_dir)
    with open(protobuf_output_dir, "rb") as f:
        proto_message.ParseFromString(f.read())

    # Display the deserialized Proto message
    print("Read Proto message from disk:\n", proto_message)
    print("Username:", proto_message.username)
    print("Total Capacity:", proto_message.total_capcity)
    print("Mobile Number:", proto_message.mobile)
    print("Base Ticket Price:", proto_message.base_ticket_price)
    print("Drive-in:", proto_message.drive_in)
    print("Payment System:", proto_message.payment)
    print("Snacks:", proto_message.snacks)
    print("Movie Ticket Prices:")
    for movie, price in proto_message.movieTicketPrice.items():
        print(f"- {movie}: ${price}")

    # Access ProtoChild message fields
    if proto_message.HasField("protochild"):
        print("ProtoChild:")
        print("- Name:", proto_message.protochild.name)
        print("- Age:", proto_message.protochild.age)
    else:
        print("No ProtoChild information found.")

if __name__ == "__main__":
    main()
