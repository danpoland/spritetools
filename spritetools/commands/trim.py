import math

import click
from PIL import Image

from .cli import cli

__all__ = ("trim",)


@cli.command(
    name="trim",
    help="""Trim margins/gutters around sprites in a sprite sheet. 
        Assumes that all the sprites are the same size in the sheet.""",
)
@click.option("--input-path", help="The path to the file to be trimmed.")
@click.option("--output-path", help="The path where the trimmed file will be exported.")
@click.option(
    "--sprite-height",
    prompt="Sprite height",
    help="The height of each sprite in the sheet.",
    type=int,
)
@click.option(
    "--sprite-width",
    prompt="Sprite width",
    help="The width of each sprite in the sheet.",
    type=int,
)
@click.option(
    "--margin", prompt="Margin", help="The margin between sprites to trim.", type=int
)
def trim(input_path, output_path, sprite_height, sprite_width, margin):
    with Image.open(input_path) as source:
        image_width, image_height = source.size
        cols = math.ceil(image_width / (sprite_width + margin))
        rows = math.ceil(image_height / (sprite_height + margin))
        trimmed = Image.new("RGBA", (cols * sprite_width, rows * sprite_height))

        y_offset = 0

        for row in range(rows):
            row_offset = y_offset * row
            y = row * sprite_height + row_offset
            x_offset = 0

            for col in range(cols):
                col_offset = x_offset * col
                x = col * sprite_width + col_offset

                sprite = source.crop((x, y, x + sprite_width, y + sprite_height))
                trimmed.paste(sprite, (x - col_offset, y - row_offset))

                x_offset = margin

            y_offset = margin

    trimmed.save(output_path)
    trimmed.close()
