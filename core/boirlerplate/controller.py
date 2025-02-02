CONTROLLER_CODE_TEMPLATE = """
import {{ Result }} from '@app/common/base';
import {{ UniqueEntityID }} from '@ddd/domain/base';
import {{ PaginatedFindResult, PaginationDto }} from '@ddd/presentation/pagination';
import {{
  Body,
  Controller,
  Delete,
  Get,
  Param,
  ParseUUIDPipe,
  Patch,
  Post,
  Query,
}} from '@nestjs/common';
import {{ CommandBus, QueryBus }} from '@nestjs/cqrs';
import {{ ApiTags }} from '@nestjs/swagger';
import {{ Create{class_name}Command }} from '../../application/commands/{resource_name}/create-{resource_name}.command';
import {{ Delete{class_name}Command }} from '../../application/commands/{resource_name}/delete-{resource_name}.command';
import {{ Update{class_name}Command }} from '../../application/commands/{resource_name}/update-{resource_name}.command';
import {{ Create{class_name}Dto }} from '../../application/dtos/{resource_name}/create-{resource_name}.dto';
import {{ Update{class_name}Dto }} from '../../application/dtos/{resource_name}/update-{resource_name}.dto';
import {{ {class_name}GetAllQuery }} from '../../application/queries/{resource_name}/{resource_name}-get-all.query';
import {{ {class_name}GetOneQuery }} from '../../application/queries/{resource_name}/{resource_name}-get-one.query';
import {{ {class_name} }} from '../../domain/entities/{resource_name}.entity';
import {{ {class_name}Mappers }} from '../../infrastructure/mappers/{resource_name}.mapper';

@ApiTags('{resource_camel_case}')
@Controller('{resource_camel_case}')
export class {class_name}Controller {{
  constructor(
    private readonly queryBus: QueryBus,
    private readonly commandBus: CommandBus,
  ) {{}}

  @Get()
  async getAll(@Query() paginationDto: PaginationDto) {{
    const ans: Result<PaginatedFindResult<{class_name}>> = await this.queryBus.execute(
      new {class_name}GetAllQuery(paginationDto),
    );
    const pagination = ans.unwrap();
    return {{
      ...pagination,
      items: {class_name}Mappers.DomainToDtoMultiple(pagination.items),
    }};
  }}

  @Get(':id')
  async getById(@Param('id', ParseUUIDPipe) id: string) {{
    const ans: Result<{class_name}> = await this.queryBus.execute(
      new {class_name}GetOneQuery(new UniqueEntityID(id)),
    );
    const {resource_camel_case} = ans.unwrap();
    return {class_name}Mappers.DomainToDto({resource_camel_case});
  }}

  @Post()
  async create(@Body() create{class_name}Dto: Create{class_name}Dto) {{
    const ans: Result<{class_name}> = await this.commandBus.execute(
      new Create{class_name}Command(
        // pass properties from create{class_name}Dto
      ),
    );

    const {resource_camel_case} = ans.unwrap();
    return {class_name}Mappers.DomainToDto({resource_camel_case});
  }}

  @Patch(':id')
  async update(
    @Param('id', ParseUUIDPipe) id: string,
    @Body() update{class_name}Dto: Update{class_name}Dto,
  ) {{
    const ans: Result<{class_name}> = await this.commandBus.execute(
      new Update{class_name}Command(
        new UniqueEntityID(id),
        // pass properties from update{class_name}Dto
      ),
    );

    const {resource_camel_case} = ans.unwrap();
    return {class_name}Mappers.DomainToDto({resource_camel_case});
  }}

  @Delete(':id')
  async delete(@Param('id', ParseUUIDPipe) {resource_camel_case}Id: string) {{
    const ans: Result<{class_name}> = await this.commandBus.execute(
      new Delete{class_name}Command(new UniqueEntityID({resource_camel_case}Id)),
    );

    const resp = ans.unwrap();
    return resp;
  }}
}}
"""
