CREATE_DTO_CODE_TEMPLATE = """export class Create{class_name}Dto {{
    // Add dto fields here
}}
"""


UPDATE_DTO_CODE_TEMPLATE = """
import {{ PartialType }} from '@nestjs/swagger';
import {{ Create{class_name}Dto }} from './{dto_create_file_name}';

export class Update{class_name}Dto extends PartialType(Create{class_name}Dto) {{}}

"""


READ_DTO_CODE_TEMPLATE = """export class Read{class_name}Dto {{
    // Add dto fields here
}}
"""
