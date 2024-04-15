import nist

from constants import PATH


def main() -> None:
    sequences = nist.read_data(PATH)
    for key in sequences.keys():
        print(key, " results:")
        print("frequency_bit test -->", nist.frequency_bit(sequences[key]))
        print(
            "identical_consecutive_bits test -->",
            nist.identical_consecutive_bits(sequences[key]),
        )
        print(
            "longest_sequence_of_ones_in_block test -->",
            nist.longest_sequence_of_ones_in_block(sequences[key]),
        )


if __name__ == "__main__":
    main()
