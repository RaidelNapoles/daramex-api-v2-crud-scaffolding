from core.index_modifier import modify_typescript_import_and_array
from core.utils import *


def file_builder(
    resource_name: str,
    base_dir_path: str,
    extension: str,
    code_template: str,
    file_name_prefix: str = "",
    file_name_suffix: str = "",
    add_resource_folder=False,
):
    dir_path = get_dir_path(base_dir_path)
    if add_resource_folder:
        dir_path = get_dir_path(base_dir_path, resource_name)
    file_path = (
        f"{dir_path}/{file_name_prefix}{resource_name}{file_name_suffix}{extension}"
    )
    with open(file_path, "w") as file:
        class_name = to_class_name(resource_name)
        resource_camel_case = to_camel_case(resource_name)
        dto_create_file_name = f"create-{resource_name}{extension}"
        resource_all_caps = resource_name.upper()
        text = code_template.format(
            resource_name=resource_name,
            resource_camel_case=resource_camel_case,
            class_name=class_name,
            dto_create_file_name=dto_create_file_name,
            resource_all_caps=resource_all_caps,
        )
        file.write(text)


def add_or_update_index(
    resource_name: str,
    base_dir_path: str,
    extension: str,
    code_template: str,
    import_statement_template: str,
):
    dir_path = get_dir_path(base_dir_path)
    index_path = f"{dir_path}/index.ts"
    class_name = to_class_name(resource_name)
    resource_camel_case = to_camel_case(resource_name)
    dto_create_file_name = f"create-{resource_name}{extension}"
    resource_all_caps = resource_name.upper()
    if not Path(index_path).is_file():
        with open(index_path, "w") as file:
            text = code_template.format(
                resource_name=resource_name,
                resource_camel_case=resource_camel_case,
                class_name=class_name,
                dto_create_file_name=dto_create_file_name,
                resource_all_caps=resource_all_caps,
            )
            file.write(text)
    else:
        file_content = get_file_content(index_path)
        new_import_statement = import_statement_template.format(
            class_name=class_name, resource_name=resource_name
        )
        new_class_name = f"{class_name}Persistence"
        modified_text = modify_typescript_import_and_array(
            file_content, new_import_statement, new_class_name
        )
        if modified_text:
            with open(index_path, "w") as file:
                modified_text = modify_typescript_import_and_array(
                    file_content, new_import_statement, new_class_name
                )

                file.write(modified_text)
