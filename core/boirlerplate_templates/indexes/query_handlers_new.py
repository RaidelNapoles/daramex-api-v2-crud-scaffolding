INDEX_COMMAND_HANDLERS_CODE_TEMPLATE = """import {{ {class_name}GetAllHandler }} from './{resource_name}/{resource_name}-get-all.query';
import {{ {class_name}GetOneHandler }} from './{resource_name}/{resource_name}-get-one.query';


export const {microservice_class_name}QueryHandlers = [
  {class_name}GetAllHandler,
  {class_name}GetOneHandler,
];
"""
