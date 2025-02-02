INDEX_CONTROLLER_CODE_TEMPLATE = """import {{ {class_name}Controller }} from './{resource_name}.controller';

export const {microservice_class_name}Controllers = [
  {class_name}Controller,
];
"""
