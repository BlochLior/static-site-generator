def markdown_to_blocks(markdown):
    if not isinstance(markdown, str):
        raise TypeError("Unxpected non-string input")
    sections_stage_1 = markdown.splitlines()
    sections = []
    temp_str = ""
    for section in sections_stage_1:
        if section.strip():
            if temp_str != "":
                temp_str += "\n" + section.strip() 
            else:
                temp_str = section.strip()
        if not section.strip():
            if temp_str.strip():
                sections.append(temp_str.strip())
                temp_str = ""
    if sections_stage_1:
        if sections_stage_1[-1].strip():
            if temp_str != "":
                sections.append(temp_str.strip())
    return sections