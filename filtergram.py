import filters

# main function
def main():
    filename = input("Enter the name of the file you want to open: ")
    opened_image = filters.load_img(filename)

    # original image
    filters.show_img(opened_image)
    filters.save_img(opened_image, "image.jpeg")

    # obama filter
    obama_filter_image = filters.obamicon(opened_image)
    filters.show_img(obama_filter_image)
    filters.save_img(obama_filter_image, "obama.jpeg")

    # invert colors
    inverted_colors_image = filters.invertColors(opened_image)
    filters.show_img(inverted_colors_image)
    filters.save_img(inverted_colors_image, "inverted_colors.jpeg")

    # grayscale
    grayscale_image = filters.grayscale(opened_image)
    filters.show_img(grayscale_image)
    filters.save_img(grayscale_image, "grayscale.jpeg")

if __name__ == "__main__":
    main()
