INFRASTRUCTURE_REPOSITORY_CODE_TEMPLATE = """import {{ GenericRepository }} from '@ddd/infrastructure/repositories';
import {{ Injectable }} from '@nestjs/common';
import {{ InjectRepository }} from '@nestjs/typeorm';
import {{ Repository }} from 'typeorm';
import {{ {class_name} }} from '../../domain/entities/{resource_name}.entity';
import {{
  I{class_name}Repository,
  {class_name}FilterFields,
}} from '../../domain/repositories/i{resource_name}.repository';
import {{ {class_name}Mappers }} from '../mappers/{resource_name}.mapper';
import {{ {class_name}Persistence }} from '../persistence/{resource_name}.persistence';

@Injectable()
export class {class_name}Repository
  extends GenericRepository<{class_name}, {class_name}Persistence, {class_name}FilterFields>
  implements I{class_name}Repository
{{
  constructor(
    @InjectRepository({class_name}Persistence)
    readonly repository: Repository<{class_name}Persistence>,
  ) {{
    super(
      repository,
      {class_name}Mappers.DomainToPersistence,
      {class_name}Mappers.PersistToDomain,
      '{class_name}Repository',
    );
  }}
}}

"""
