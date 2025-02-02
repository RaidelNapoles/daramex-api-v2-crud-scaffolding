UPDATE_DTO_CODE_TEMPLATE = """import {{ PartialType }} from '@nestjs/swagger';
import {{ Create{class_name}Dto }} from './{dto_create_file_name}';

export class Update{class_name}Dto extends PartialType(Create{class_name}Dto) {{}}

"""
