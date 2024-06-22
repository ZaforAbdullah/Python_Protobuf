import sys

from protoCompile import proto_pb2
from path_helpers import get_protobuf_output_dir

def main():
    if len(sys.argv) < 10:
        print("Usage: python greetWriter.py <username> <total_capacity> <mobile> <base_ticket_price> <drive_in> <payment> <snacks> <protochild_name> <protochild_age> <movieTicketPrice>")
        return
    
    # Use the helper function to get the output directory
    protobuf_output_dir = get_protobuf_output_dir("protoOutput", "protobuf_output")
    
    # Extract command-line arguments
    username = sys.argv[1]
    total_capacity = int(sys.argv[2])
    mobile = int(sys.argv[3])
    base_ticket_price = float(sys.argv[4])
    drive_in = bool(int(sys.argv[5]))  # Convert to boolean
    payment = getattr(proto_pb2.Proto, sys.argv[6])  # Convert to enum value
    snacks = sys.argv[7].split(',')  # Split snacks into a list
    protochild_name = sys.argv[8]
    protochild_age = sys.argv[9]

    # Process movieTicketPrice map argument
    movie_ticket_price = {}
    if len(sys.argv) > 10:
        movie_ticket_price_args = sys.argv[10:]
        for i in range(0, len(movie_ticket_price_args), 2):
            movie_ticket_price[movie_ticket_price_args[i]] = int(movie_ticket_price_args[i + 1])

    # Create an instance of Proto message
    proto_message = proto_pb2.Proto()

    # Set fields based on command-line arguments
    proto_message.username = username
    proto_message.total_capcity = total_capacity
    proto_message.mobile = mobile
    proto_message.base_ticket_price = base_ticket_price
    proto_message.drive_in = drive_in
    proto_message.payment = payment
    proto_message.snacks.extend(snacks)

    # Set ProtoChild message
    proto_child = proto_message.protochild
    proto_child.name = protochild_name
    proto_child.age = protochild_age

    # Set movieTicketPrice map field
    proto_message.movieTicketPrice.update(movie_ticket_price)

    # Serialize Proto message to a file
    print("Saving to file:", protobuf_output_dir)
    with open(protobuf_output_dir, "wb") as f:
        f.write(proto_message.SerializeToString())

    print("Saved Proto message to disk:\n", proto_message)

if __name__ == "__main__":
    main()
