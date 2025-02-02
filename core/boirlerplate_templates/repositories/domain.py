DOMAIN_REPOSITORY_CODE_TEMPLATE = """import {{ IGenericRepository }} from '@ddd/application/repositories/generic-repository.interface';
import {{ FieldOptions, IQuantitativeFieldOptions }} from '@ddd/infrastructure/repositories';
import {{ {class_name} }} from '../entities/{resource_name}.entity';

export type {class_name}FilterFields = {{
  _id: FieldOptions<string | number>;
  propertyName: IQuantitativeFieldOptions;
}};

export interface I{class_name}Repository
  extends IGenericRepository<{class_name}, {class_name}FilterFields, ''> {{}}
"""
