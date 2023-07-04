###########################################
import labelme
from PIL import Image, ImageDraw
import json
import os

# Function to load and parse Labelme JSON file
def load_labelme_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data

# Function to convert Labelme annotations to masked image
def convert_labelme_to_masked_png(data, labels):
    # Get the image height and width
    img_height = data['imageHeight']
    img_width = data['imageWidth']

    # Create a blank image with a black background
    image = Image.new('L', (img_width, img_height), 0)
    draw = ImageDraw.Draw(image)

    # Iterate through the shapes in the Labelme data
    for shape in data['shapes']:
        label = shape['label']
        mask = labelme.utils.shape_to_mask(
            (img_height, img_width),
            shape['points'],
            shape_type=shape['shape_type']
        )

        # Convert the binary mask to PIL ImageDraw format
        mask_image = Image.fromarray(mask.astype('uint8') * 255)

        # Get the label index
        label_index = labels.index(label)

        # Draw the mask on the image using the label index as the color
        draw.bitmap((0, 0), mask_image, fill=label_index)

    return image

# Function to save the masked image as a PNG file
def save_masked_image(image, output_file):
    image.save(output_file)

# Convert Labelme JSON files to masked PNGs
def convert_labelme_files(json_dir, output_dir, labels):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Process each JSON file in the directory
    for filename in os.listdir(json_dir):
        if filename.endswith('.json'):
            json_file = os.path.join(json_dir, filename)
            output_file = os.path.join(output_dir, filename.replace('.json', '.png'))

            # Load and parse the Labelme JSON file
            data = load_labelme_json(json_file)

            # Convert Labelme annotations to a masked image
            masked_image = convert_labelme_to_masked_png(data, labels)

            # Save the masked image as a PNG file
            save_masked_image(masked_image, output_file)
            print(f"Converted {json_file} to {output_file}")

# Define the labels in the JSON files
labels = ['_background_', 'background', 'land', 'road', 'road_affected', 'house_affected', 'water', 'landslide', 'house']

# Directory paths for JSON files and output masked PNGs
json_dir = 'D:\\Research\\3\\json'
output_dir = 'D:\\Research\\3\\json\\ahsan'

# Convert Labelme JSON files to masked PNGs
convert_labelme_files(json_dir, output_dir, labels)
