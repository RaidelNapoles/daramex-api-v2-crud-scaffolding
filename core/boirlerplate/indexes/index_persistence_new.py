INDEX_PERSISTENCE_CODE_TEMPLATE = """import {{ {class_name}Persistence }} from './{resource_name}.persistence';

export const EntitiesPersistence = [
  {class_name}Persistence,
];

"""
