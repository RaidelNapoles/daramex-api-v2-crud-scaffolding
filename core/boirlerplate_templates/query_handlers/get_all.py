GET_ALL_QUERY_HANDLER_CODE_TEMPLATE = """import {{ Result }} from '@app/common/base';
import {{ LoggerService }} from '@app/common/services';
import {{ PaginatedFindResult, PaginationDto }} from '@ddd/presentation/pagination';
import {{ Inject }} from '@nestjs/common';
import {{ IQueryHandler, QueryHandler }} from '@nestjs/cqrs';
import {{ {class_name} }} from '../../../domain/entities/{resource_name}.entity';
import {{ I{class_name}Repository }} from '../../../domain/repositories/i{resource_name}.repository';
import {{ RepositoryNames }} from 'apps/remittance/src/infrastructure/repositories';

export class {class_name}GetAllQuery {{
  constructor(
    public readonly paginationDto: PaginationDto,
    public readonly filtersDto?: any,
    public readonly orderByDto?: any,
  ) {{}}
}}

@QueryHandler({class_name}GetAllQuery)
export class {class_name}GetAllHandler implements IQueryHandler<{class_name}GetAllQuery> {{
  constructor(
    @Inject(RepositoryNames.{class_name}Repository)
    private readonly repository: I{class_name}Repository,
    private readonly logger: LoggerService,
  ) {{}}

  async execute(
    query: {class_name}GetAllQuery,
  ): Promise<Result<PaginatedFindResult<{class_name}>>> {{
    this.logger.log(`Getting {resource_camel_case} paginated with ${{JSON.stringify(query)}}`);
    const ans = await this.repository.getAllPaginatedByDynamicEqualFilter(
      query.paginationDto,
      {{
        ...query.filtersDto,
      }},
      query.orderByDto,
    );

    return Result.Ok(ans);
  }}
}}
"""
