import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_dir = Path(dir_path_content)
    
    # Find all markdown files recursively
    markdown_files = list(content_dir.rglob('*.md'))
    
    for md_file in markdown_files:
        # Calculate the relative path from content dir
        relative_path = md_file.relative_to(content_dir)
        
        # Create destination path with the same structure but in dest_dir_path
        dest_file = Path(dest_dir_path) / relative_path
        
        # Change extension from .md to .html
        dest_file = dest_file.with_suffix('.html')
        
        # Generate the page using your existing function
        generate_page(md_file, template_path, dest_file)

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")