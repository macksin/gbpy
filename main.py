import argparse

def main():
    # command line argument for ROM reading
    parser = argparse.ArgumentParser(description="GB Emulator")
    parser.add_argument('path_rom', metavar='R', type=str, help='Path to rom')
    args = parser.parse_args()
    print("ROM = '{}'".format(args.path_rom))

    # read the rom
    with open(args.path_rom, 'rb') as file:
        lines = file.read()
        lines = [hex(line) for line in lines] # read in hex

    # game title
    TITLE = [chr(int(char, 0)) for char in lines[int(0x134):int(0x14c)]]
    TITLE = "".join(TITLE)
    print("Game Title (location $0134-$014c) = '{}'".format(TITLE));

if __name__ == '__main__':
    main()
