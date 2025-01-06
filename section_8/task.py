while True:
    print("")
    print("Type 'encode' to encrypt, type 'decode' to decrypt, type 'exit' to end")
    subroutine = input()
    if subroutine == "exit":
        break
    if not (subroutine == "encode" or subroutine == "decode"):
        print("please input 'encode' or 'decode'")
        continue
    print("Type your message:")
    message = input()
    if not (message and message.isalpha()):
        print("Your message is not valid")
        continue
    message = message.lower()
    print("Type the shift number:")
    shift = input()
    if not (shift and shift.isdigit()):
        print("Your number is not valid")
        continue
    shift = int(shift)
    if shift > 25:
        print("shift number cannot be greater then 25!!")
        continue

    buffer = []
    if subroutine == "encode":
        for char in message:
            ascii_number = ord(char) + shift
            if ascii_number > 122:
                ascii_number -= 26
            buffer.append(chr(ascii_number))
        result = "".join(buffer)
        print(f"Here's the encoded result: {result}")

    else:
        for char in message:
            ascii_number = ord(char) - shift
            if ascii_number < 97:
                ascii_number += 26
            buffer.append(chr(ascii_number))
        result = "".join(buffer)
        print(f"Here's the decoded result: {result}")
