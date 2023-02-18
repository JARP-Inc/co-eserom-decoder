def main():
    eserom_dict = {
        "10": "A",
        "0111": "B",
        "0101": "C",
        "011": "D",
        "1": "E",
        "1101": "F",
        "001": "G",
        "1111": "H",
        "11": "I",
        "1000": "J",
        "010": "K",
        "1011": "L",
        "00": "M",
        "01": "N",
        "000": "O",
        "1001": "P",
        "0010": "Q",
        "101": "R",
        "111": "S",
        "0": "T",
        "110": "U",
        "1110": "V",
        "100": "W",
        "0110": "X",
        "0100": "Y",
        "0011": "Z",
        "10000": "1",
        "11000": "2",
        "11100": "3",
        "11110": "4",
        "11111": "5",
        "01111": "6",
        "00111": "7",
        "00011": "8",
        "00001": "9",
        "00000": "0",
    }

    # THIS IS THE SOLUTION !!1!
    def eserom_decoder(sentence):
        words = sentence.split("  ")
        decoded_sentence = []
        for word in words:
            decoded_word = "".join([eserom_dict[letter] for letter in word.split(" ")])
            decoded_sentence.append(decoded_word)
        return " ".join(decoded_sentence)

    def test():
        data_in = "1111 1 1011 1011 000  100 000 101 1011 011"

        expected_output = "HELLO WORLD"
        actual_output = eserom_decoder(data_in)
        assert actual_output == expected_output
        print("passed")

    # test()


if __name__ == "__main__":
    main()
