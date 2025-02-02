from core.constants import *
from core.boirlerplate import *
from core.file_creator import file_builder


def scaffold_dtos(resource: str):
    # build create dto
    file_builder(
        resource,
        BASE_DTOS_DIR_PATH,
        DTO_EXTENSION,
        CREATE_DTO_CODE_TEMPLATE,
        CREATE_PREFIX,
        add_resource_folder=True,
    )

    # build update dto
    file_builder(
        resource,
        BASE_DTOS_DIR_PATH,
        DTO_EXTENSION,
        UPDATE_DTO_CODE_TEMPLATE,
        UPDATE_PREFIX,
        add_resource_folder=True,
    )

    # build read dto
    file_builder(
        resource,
        BASE_DTOS_DIR_PATH,
        DTO_EXTENSION,
        READ_DTO_CODE_TEMPLATE,
        READ_PREFIX,
        add_resource_folder=True,
    )


def scaffold_persistence(resource: str):
    file_builder(
        resource,
        BASE_PERSISTENCE_DIR_PATH,
        PERSISTENCE_EXTENSION,
        PERSISTENCE_CODE_TEMPLATE,
    )


def scaffold_domain_entity(resource: str):
    file_builder(
        resource,
        BASE_DOMAIN_ENTITY_DIR_PATH,
        ENTITY_EXTENSION,
        DOMAIN_ENTITY_CODE_TEMPLATE,
    )


def scaffold_mapper(resource: str):
    file_builder(
        resource,
        BASE_MAPPER_DIR_PATH,
        MAPPER_EXTENSION,
        MAPPER_CODE_TEMPLATE,
    )


def scaffold_domain_repository(resource: str):
    file_builder(
        resource,
        BASE_DOMAIN_REPOSITORY_DIR_PATH,
        REPOSITORY_EXTENSION,
        DOMAIN_REPOSITORY_CODE_TEMPLATE,
        file_name_prefix="i",
    )


def scaffold_infrastructure_repository(resource: str):
    file_builder(
        resource,
        BASE_INFRASTRUCTURE_REPOSITORY_DIR_PATH,
        ENTITY_EXTENSION,
        INFRASTRUCTURE_REPOSITORY_CODE_TEMPLATE,
    )


def scaffold_query_handlers(resource: str):
    file_builder(
        resource,
        BASE_QUERY_DIR_PATH,
        QUERY_EXTENSION,
        GET_ALL_QUERY_HANDLER_CODE_TEMPLATE,
        file_name_suffix=GET_ALL_SUFFIX,
        add_resource_folder=True,
    )

    file_builder(
        resource,
        BASE_QUERY_DIR_PATH,
        QUERY_EXTENSION,
        GET_ONE_QUERY_HANDLER_CODE_TEMPLATE,
        file_name_suffix=GET_ONE_SUFFIX,
        add_resource_folder=True,
    )


def scaffold_command_handlers(resource: str):
    file_builder(
        resource,
        BASE_COMMANDS_DIR_PATH,
        COMMAND_EXTENSION,
        CREATE_COMMAND_HANDLER_CODE_TEMPLATE,
        file_name_prefix=CREATE_PREFIX,
        add_resource_folder=True,
    )

    file_builder(
        resource,
        BASE_COMMANDS_DIR_PATH,
        COMMAND_EXTENSION,
        UPDATE_COMMAND_HANDLER_CODE_TEMPLATE,
        file_name_prefix=UPDATE_PREFIX,
        add_resource_folder=True,
    )

    file_builder(
        resource,
        BASE_COMMANDS_DIR_PATH,
        COMMAND_EXTENSION,
        DELETE_COMMAND_HANDLER_CODE_TEMPLATE,
        file_name_prefix=DELETE_PREFIX,
        add_resource_folder=True,
    )


def scaffold_controller(resource: str):
    file_builder(
        resource,
        BASE_CONTROLLER_DIR_PATH,
        CONTROLLER_EXTENSION,
        CONTROLLER_CODE_TEMPLATE,
    )


def scaffold(resource: str):
    scaffold_dtos(resource)
    scaffold_persistence(resource)
    scaffold_domain_entity(resource)
    scaffold_mapper(resource)
    scaffold_domain_repository(resource)
    scaffold_infrastructure_repository(resource)
    scaffold_query_handlers(resource)
    scaffold_command_handlers(resource)
    scaffold_controller(resource)


if __name__ == "__main__":
    scaffold("user-settings")
