#! /usr/bin/python3

import src.image_translator as image_translator
import src.tile_model as tile_model
import src.wave_function_collapse as wave_function_collapse
import src.directions as directions

if __name__ == "__main__":

# Example files and their tile size
    filenames = [
        ["resources/images/example4x4.png", 1],
        ["resources/images/river32x32.png", 1],
        ["resources/images/streets32x32.png", 8]
    ]
    file = 0

    # Translate the input image
    ti = image_translator.ImageTranslator.breakdown_image(*filenames[file])

    # Build a model out of the input image
    tm = tile_model.ModelBuilder.build_model(ti, (2, 2))

    # Initialize the wave function collapse algorithm
    wfc = wave_function_collapse.WaveFunctionCollapse(tm)

    # Generate new images via wave function collapse, rebuild the image and save 
    for i in range(1):
        wfc.generate_map((64, 64))
        reversed_map = tile_model.ModelBuilder.reverse_patterns(wfc.output)
        rebuild_image = image_translator.ImageTranslator.rebuild_image(image_translator.TranslatedImage(ti.tile_map, reversed_map), f"{filenames[file][0][:-4]}_result{i}.png")

