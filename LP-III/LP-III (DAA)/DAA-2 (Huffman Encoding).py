class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(char_freqs):
    """Builds a Huffman tree from a dictionary of character frequencies.

    Args:
        char_freqs: A dictionary mapping characters to their frequencies.

    Returns:
        The root node of the Huffman tree.
    """

    min_heap = []
    for char, freq in char_freqs.items():
        node = HuffmanNode(char, freq)
        min_heap.append(node)

    while len(min_heap) > 1:
        node1 = min_heap.pop(0)
        node2 = min_heap.pop(0)

        new_node = HuffmanNode(None, node1.freq + node2.freq)
        new_node.left = node1
        new_node.right = node2

        min_heap.append(new_node)

    return min_heap[0]


def generate_huffman_codes(root):
    """Generates Huffman codes for all characters in the Huffman tree.

    Args:
        root: The root node of the Huffman tree.

    Returns:
        A dictionary mapping characters to their Huffman codes.
    """

    huffman_codes = {}

    def traverse(node, code):
        if node.char is not None:
            huffman_codes[node.char] = code
            return

        traverse(node.left, code + "0")
        traverse(node.right, code + "1")

    traverse(root, "")

    return huffman_codes


def compress_data(data, huffman_codes):
    """Compresses data using Huffman coding.

    Args:
        data: The data to compress.
        huffman_codes: A dictionary mapping characters to their Huffman codes.

    Returns:
        The compressed data.
    """

    compressed_data = ""
    for char in data:
        compressed_data += huffman_codes[char]

    return compressed_data


def decompress_data(compressed_data, huffman_tree):
    """Decompresses data using Huffman coding.

    Args:
        compressed_data: The compressed data.
        huffman_tree: The root node of the Huffman tree.

    Returns:
        The decompressed data.
    """

    decompressed_data = ""
    node = huffman_tree

    for bit in compressed_data:
        if bit == "0":
            node = node.left
        else:
            node = node.right

        if node.char is not None:
            decompressed_data += node.char
            node = huffman_tree

    return decompressed_data


if __name__ == "__main__":
    # Create a dictionary of character frequencies.
    char_freqs = {}
    for char in input("Enter the data to compress: "):
        char_freqs[char] = char_freqs.get(char, 0) + 1

    # Build a Huffman tree.
    root = build_huffman_tree(char_freqs)

    # Generate Huffman codes.
    huffman_codes = generate_huffman_codes(root)

    # Compress the data.
    compressed_data = compress_data(input("Enter the data to compress: "), huffman_codes)

    # Decompress the data.
    decompressed_data = decompress_data(compressed_data, root)

    # Print the compressed and decompressed data.
    print("Compressed data:", compressed_data)
    print("Decompressed data:", decompressed_data)
