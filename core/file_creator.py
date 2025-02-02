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
