import math


class OmegaNetwork:
    def __init__(self, num_nodes):
        """
        Initialize an Omega Network instance.
        :param num_nodes: Total number of nodes (must be a power of 2).
        """
        if not (num_nodes > 0 and (num_nodes & (num_nodes - 1)) == 0):
            raise ValueError("Number of nodes must be a power of 2.")
        self.num_nodes = num_nodes
        self.num_stages = int(math.log2(num_nodes))

    def calculate_next_position(self, current_position, destination, stage):
        """
        Calculate the next position based on the provided formula.
        :param current_position: Current position of the node.
        :param destination: Destination node in binary representation.
        :param stage: Current stage in the network.
        :return: Next position in the network.
        """
        # Determine the next position base calculation
        if current_position < self.num_nodes / 2:
            next_position = 2 * current_position  # Lower half
        else:
            next_position = 2 * current_position + 1 - self.num_nodes  # Upper half

        # Determine the destination bit for the current stage
        dest_bit = (destination >> (self.num_stages - stage - 1)) & 1

        # Adjust the next position based on the destination bit and current position parity
        if (next_position & 1) ^ dest_bit:  # If the parity doesn't match the destination bit
            next_position ^= 1  # Toggle the least significant bit

        return next_position

    def omega_network_path(self, source, destination, debug=False):
        """
        Find the path from source to destination in an Omega Network.
        :param source: The starting node (integer, 0-indexed).
        :param destination: The ending node (integer, 0-indexed).
        :param debug: Whether to print debug information.
        :return: List of tuples representing the path through stages.
        """
        if source < 0 or source >= self.num_nodes or destination < 0 or destination >= self.num_nodes:
            raise ValueError("Source and destination must be within range of nodes.")

        path = []
        current_position = source

        for stage in range(self.num_stages):
            # Calculate the next position
            next_position = self.calculate_next_position(current_position, destination, stage)

            # Debug output
            if debug:
                print(f"Stage {stage}: {current_position} -> {next_position}")

            # Record the path
            path.append((stage, current_position, next_position))

            # Update the current position
            current_position = next_position

        return path

    def simulate_network(self, source):
        """
        Simulate paths from a given source to all destinations.
        :param source: Source node.
        :return: Dictionary of paths to all destinations.
        """
        if source < 0 or source >= self.num_nodes:
            raise ValueError("Source must be within range of nodes.")

        all_paths = {}
        for destination in range(self.num_nodes):
            path = self.omega_network_path(source, destination)
            all_paths[destination] = path

        return all_paths

    def visualize_path(self, path):
        """
        Visualize the path through the Omega Network.
        :param path: The path as a list of tuples (stage, src, dest).
        """
        print("Visualization of Path:")
        for stage, src, dest in path:
            print(f"Stage {stage}: [Node {src}] -> [Node {dest}]")

    def routing_statistics(self):
        """
        Calculate and display routing statistics for the network.
        """
        print("Routing Statistics:")
        for source in range(self.num_nodes):
            for destination in range(self.num_nodes):
                path = self.omega_network_path(source, destination)
                print(f"Source {source} -> Destination {destination}: {path}")


# Example usage
if __name__ == "__main__":
    num_nodes = 8  # Number of nodes (must be a power of 2)
    source = 5     # Example source node
    destination = 2  # Example destination node

    omega = OmegaNetwork(num_nodes)

    # Compute and display a specific path
    path = omega.omega_network_path(source, destination, debug=True)
    print("\nPath through Omega Network:")
    for stage, src, dest in path:
        print(f"Stage {stage}: {src} -> {dest}")

    # Visualize the path
    omega.visualize_path(path)

    # Simulate all paths from the source
    all_paths = omega.simulate_network(source)
    print("\nAll Paths from Source:")
    for dest, p in all_paths.items():
        print(f"Destination {dest}: {p}")

    # Display routing statistics
    print("\nRouting Statistics:")
    omega.routing_statistics()
