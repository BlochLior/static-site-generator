import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def is_heading(block):
    return re.match(r'#{1,6} ', block) is not None

def is_code(block):
    return block.startswith("```") and block.endswith("```")

def is_quote(block):
    lines = block.splitlines()
    if not lines:
        return False
    return all(line.startswith(">") for line in lines if line)

def is_unordered_list(block):
    lines = block.splitlines()
    if not lines:
        return False
    return all(line.startswith("- ") for line in lines if line)

def is_ordered_list(block):
    lines = block.splitlines()
    if not lines:
        return False
    valid_lines = [line for line in lines if line] #filters out empty lines

    for i, line in enumerate(valid_lines, 1):
        if not line.startswith(f"{i}. "):
            return False
        
    return True


def block_to_block_type(block):
    if is_heading(block):
        return BlockType.HEADING
    elif is_code(block):
        return BlockType.CODE
    elif is_quote(block):
        return BlockType.QUOTE
    elif is_unordered_list(block):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list(block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH