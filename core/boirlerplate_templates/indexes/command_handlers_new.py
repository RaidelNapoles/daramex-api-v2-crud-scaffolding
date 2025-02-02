INDEX_COMMAND_HANDLERS_CODE_TEMPLATE = """import {{ Create{class_name}Handler }} from './{resource_name}/create-{resource_name}.command';
import {{ Delete{class_name}Handler }} from './{resource_name}/delete-{resource_name}.command';
import {{ Update{class_name}Handler }} from './{resource_name}/update-{resource_name}.command';


export const {microservice_class_name}CommandHandlers = [
  Create{class_name}Handler,
  Delete{class_name}Handler,
  Update{class_name}Handler,
];
"""
