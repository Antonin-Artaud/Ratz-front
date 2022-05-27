from PIL import Image, ImageChops


def draw_line(startX, endX, y, screen, color):
    for i in range(startX, endX):
        screen.putpixel((i, y), color)


def draw_line_with_bytes(startX, endX, y, img, bytes, jump=-1):
    hasJumped = False
    for i in range(0, endX - startX):
        if (i != jump):
            if (hasJumped):
                bytesIndex = i - 1
            else:
                bytesIndex = i
            if bytes[bytesIndex] == "1":
                img.putpixel((i + startX, y), 0)
            else:
                img.putpixel((i + startX, y), 1)
        else:
            hasJumped = True


def draw_column(startY, endY, x, screen, color):
    for i in range(startY, endY):
        screen.putpixel((x, i), color)


def draw_column_with_bytes(startY, endY, x, img, bytes, jump=-1):
    hasJumped = False
    for i in range(0, endY - startY):
        if (i != jump):
            if (hasJumped):
                bytesIndex = i - 1
            else:
                bytesIndex = i

            if (bytes[bytesIndex] == "1"):

                img.putpixel((x, i + startY), 0)
            else:
                img.putpixel((x, i + startY), 1)
        else:
            hasJumped = True


def draw_basic_squares(img):
    draw_line(0, 7, 0, img, 0)
    draw_line(0, 7, 6, img, 0)
    draw_column(0, 7, 6, img, 0)
    draw_column(0, 7, 0, img, 0)

    draw_line(2, 5, 2, img, 0)
    draw_line(2, 5, 3, img, 0)
    draw_line(2, 5, 4, img, 0)

    draw_line(0, 7, 14, img, 0)
    draw_line(0, 7, 20, img, 0)
    draw_column(14, 20, 6, img, 0)
    draw_column(14, 20, 0, img, 0)

    draw_line(2, 5, 16, img, 0)
    draw_line(2, 5, 17, img, 0)
    draw_line(2, 5, 18, img, 0)

    draw_line(14, 21, 0, img, 0)
    draw_line(14, 21, 6, img, 0)
    draw_column(0, 7, 14, img, 0)
    draw_column(0, 7, 20, img, 0)

    draw_line(16, 19, 2, img, 0)
    draw_line(16, 19, 3, img, 0)
    draw_line(16, 19, 4, img, 0)


def draw_basic_points(img):
    img.putpixel((8, 6), 0)
    img.putpixel((10, 6), 0)
    img.putpixel((12, 6), 0)

    img.putpixel((6, 8), 0)
    img.putpixel((6, 10), 0)
    img.putpixel((6, 12), 0)

    img.putpixel((8, 13), 0)


def draw_format_information(img, information_format):
    (first_format, second_format) = (
        information_format[:len(information_format) // 2], information_format[len(information_format) // 2:])
    draw_line_with_bytes(0, 8, 8, img, first_format, 6)

    draw_column_with_bytes(0, 8, 8, img, second_format[::-1], 6)
    print(first_format[::-1])
    draw_column_with_bytes(13, 21, 8, img, first_format[::-1], 0)
    draw_line_with_bytes(13, 21, 8, img, second_format)
    return


def fill_content_up(img, startY, endY, x, bytes, jump=-1):
    byteIndex = 0
    for i in range(0, (startY + 1) - endY):
        if i != jump:
            if (bytes[byteIndex] == "1"):
                img.putpixel((x, startY - i), 0)
            else:
                img.putpixel((x, startY - i), 1)

            byteIndex += 1

            if (bytes[byteIndex] == "1"):
                img.putpixel((x - 1, startY - i), 0)
            else:
                img.putpixel((x - 1, startY - i), 1)
            byteIndex += 1


def fill_content_down(img, startY, endY, x, bytes, jump=-1):
    byteIndex = 0
    for i in range(0, (endY + 1) - startY):
        if i != jump:
            if (bytes[byteIndex] == "1"):
                img.putpixel((x, i + startY), 0)
            else:
                img.putpixel((x, i + startY), 1)
            byteIndex += 1

            if (bytes[byteIndex] == "1"):
                img.putpixel((x - 1, i + startY), 0)
            else:
                img.putpixel((x - 1, i + startY), 1)
            byteIndex += 1


def create_qr_code(informationFormat, qrCodeBytes):
    black_img = Image.new('1', (21, 21))

    (firstPart, bytesAfterFirstSlice) = (qrCodeBytes[:24], qrCodeBytes[24:len(qrCodeBytes)])

    (secondPart, bytesAfterSecondSlice) = (
        bytesAfterFirstSlice[:24], bytesAfterFirstSlice[24:len(bytesAfterFirstSlice)])

    (thirdPart, bytesAfterThirdSlice) = (
        bytesAfterSecondSlice[:24], bytesAfterSecondSlice[24:len(bytesAfterSecondSlice)])

    (fourthPart, bytesAfterFourthSlice) = (
        bytesAfterThirdSlice[:24], bytesAfterThirdSlice[24:len(bytesAfterThirdSlice)])

    (fifthPart, bytesAfterFifthSlice) = (
        bytesAfterFourthSlice[:40], bytesAfterFourthSlice[40:len(bytesAfterFourthSlice)])

    (sixthPart, bytesAfterSixthSlice) = (bytesAfterFifthSlice[:40], bytesAfterFifthSlice[40:len(bytesAfterFifthSlice)])

    (seventhPart, bytesAfterSeventhSlice) = (
        bytesAfterSixthSlice[:8], bytesAfterSixthSlice[8:len(bytesAfterSixthSlice)])

    (eighthPart, bytesAfterEighthSlice) = (
        bytesAfterSeventhSlice[:8], bytesAfterSeventhSlice[8:len(bytesAfterSeventhSlice)])

    (ninthPart, bytesAfterNinthSlice) = (
        bytesAfterEighthSlice[:8], bytesAfterEighthSlice[8:len(bytesAfterEighthSlice)])

    (tenthPart, bytesAfterTenthSlice) = (
        bytesAfterNinthSlice[:8], bytesAfterNinthSlice[8:len(bytesAfterNinthSlice)])

    img = ImageChops.invert(black_img)

    draw_basic_squares(img)
    draw_basic_points(img)
    draw_format_information(img, informationFormat)
    fill_content_up(img, 20, 9, 20, firstPart)
    fill_content_down(img, 9, 20, 18, secondPart)
    fill_content_up(img, 20, 9, 16, thirdPart)
    fill_content_down(img, 9, 20, 14, fourthPart)
    fill_content_up(img, 20, 0, 12, fifthPart, 14)
    fill_content_down(img, 0, 20, 10, sixthPart, 6)
    fill_content_up(img, 11, 8, 8, seventhPart)
    fill_content_down(img, 9, 12, 5, eighthPart)
    fill_content_up(img, 12, 9, 3, ninthPart)
    fill_content_down(img, 9, 12, 1, tenthPart)

    return img


def draw(informationFormat, qrCodeBytes):
    # informationFormat = "011010101011111"
    # qrCodeBytes = "1011100100011010100000111100000000110010000001010100010010100101101000010010110101011100001100110110100101100010001110110100000011110101001001000001110100001110010101101101011011000011010001111000110111101110"
    qrCode = create_qr_code(informationFormat, qrCodeBytes)
    return qrCode.resize((256, 256))
