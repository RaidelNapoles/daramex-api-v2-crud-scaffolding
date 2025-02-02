MAPPER_CODE_TEMPLATE = """import {{ mapProperties }} from '@app/common/base';
import {{ Read{class_name}Dto }} from '../../application/dtos/{resource_name}/read-{resource_name}.dto';
import {{ {class_name} }} from '../../domain/entities/{resource_name}.entity';
import {{ {class_name}Persistence }} from '../persistence/{resource_name}.persistence';

export class {class_name}Mappers {{
  public static DomainToDtoMultiple({resource_camel_case}Entities: {class_name}[]): Read{class_name}Dto[] {{
    return {resource_camel_case}Entities.map({class_name}Mappers.DomainToDto);
  }}

  public static DomainToDto({resource_camel_case}: {class_name}): Read{class_name}Dto {{
    return mapProperties(
      {resource_camel_case}.getPlainObject(),
      {resource_camel_case}.getPropertyKeys(),
      Read{class_name}Dto,
    );
  }}

  public static DomainToPersistence({resource_camel_case}: {class_name}): {class_name}Persistence {{
    return mapProperties(
      {resource_camel_case}.getPlainObject(),
      {resource_camel_case}.getPropertyKeys(),
      {class_name}Persistence,
    );
  }}

  public static PersistToDomain(persist: {class_name}Persistence): {class_name} {{
    return {class_name}.assign({{
      ...persist,
    }}).unwrap();
  }}
}}
"""
