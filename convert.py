import markdownify
import sys

def convert(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Convert html to md
    md = markdownify.markdownify(html, heading_style="ATX", default_title=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)

if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])
