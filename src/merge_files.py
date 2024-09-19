#!/usr/bin/env python3

def replace_include(content, include_filename, replacement_content):
    """
    Replace the #include directive in the content with the provided replacement content,
    and add C-style comments to mark the beginning and end of the replacement.
    """
    include_directive = f'#include "{include_filename}"'
    comment_start = f'/* Begin replacement for {include_filename} */\n'
    comment_end = f'\n/* End replacement for {include_filename} */'
    
    # Add comments before and after the replacement content
    replacement_with_comments = f'{comment_start}{replacement_content}{comment_end}'
    return content.replace(include_directive, replacement_with_comments)


def process_files():
    with open('spirv_inc.bt', 'r') as file:
        spirv_inc_content = file.read()

    with open('spirv_core_grammar_inc.bt', 'r') as file:
        spirv_core_grammar_content = file.read()

    spirv_core_grammar_content_replaced = replace_include(spirv_core_grammar_content, 'spirv_inc.bt', spirv_inc_content)

    with open('spirv_main.bt', 'r') as file:
        spirv_main_content = file.read()

    final_content = replace_include(spirv_main_content, 'spirv_core_grammar_inc.bt', spirv_core_grammar_content_replaced)

    with open('spirv.bt', 'w') as file:
        file.write(final_content)

    print("The final result has been written to 'spirv.bt'.")

# Run the processing function
if __name__ == "__main__":
    process_files()
