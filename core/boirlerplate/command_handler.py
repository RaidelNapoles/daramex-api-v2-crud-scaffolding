CREATE_COMMAND_HANDLER_CODE_TEMPLATE = """
import {{ Result }} from '@app/common/base';
import {{ AppError }} from '@app/common/errors';
import {{ LoggerService }} from '@app/common/services';
import {{ Inject }} from '@nestjs/common';
import {{ CommandHandler, ICommandHandler, QueryBus }} from '@nestjs/cqrs';
import {{ {class_name} }} from '../../../domain/entities/{resource_name}.entity';
import {{ I{class_name}Repository }} from '../../../domain/repositories/i{resource_name}.repository';
import {{ RepositoryNames }} from 'apps/remittance/src/infrastructure/repositories';

export class Create{class_name}Command {{
  constructor(
      // fields needded for create
  ) {{}}
}}

@CommandHandler(Create{class_name}Command)
export class Create{class_name}Handler implements ICommandHandler<Create{class_name}Command> {{
  constructor(
    @Inject(RepositoryNames.{class_name}Repository)
    private readonly repository: I{class_name}Repository,
    private readonly queryBus: QueryBus,
    private readonly logger: LoggerService,
  ) {{}}

  async execute(command: Create{class_name}Command): Promise<Result<{class_name}>> {{
    this.logger.log('[CREATE {resource_all_caps} COMMAND]: called');
    const {{ ...{resource_camel_case}Props }} = command;

    const {resource_camel_case}Resp = {class_name}.new({{
      ...{resource_camel_case}Props,
    }});

    if ({resource_camel_case}Resp.isFailure) {{
      return Result.Fail({resource_camel_case}Resp.errorValue().unwrap());
    }}
    const {resource_camel_case} = {resource_camel_case}Resp.unwrap();

    this.logger.log(`Saving {resource_camel_case} in database`);

    try {{
      await this.repository.save({resource_camel_case});
    }} catch (error) {{
      return Result.Fail(new AppError.UnexpectedError(error));
    }}
    return Result.Ok({resource_camel_case});
  }}
}}
"""


UPDATE_COMMAND_HANDLER_CODE_TEMPLATE = """import {{ Result }} from '@app/common/base';
import {{ AppError }} from '@app/common/errors';
import {{ LoggerService }} from '@app/common/services';
import {{ UniqueEntityID }} from '@ddd/domain/base';
import {{ Inject }} from '@nestjs/common';
import {{ CommandHandler, ICommandHandler, QueryBus }} from '@nestjs/cqrs';
import {{ {class_name} }} from '../../../domain/entities/{resource_name}.entity';
import {{ I{class_name}Repository }} from '../../../domain/repositories/i{resource_name}.repository';
import {{ RepositoryNames }} from 'apps/remittance/src/infrastructure/repositories';

export class Update{class_name}Command {{
  constructor(
    public id: UniqueEntityID,
  ) {{}}
}}

@CommandHandler(Update{class_name}Command)
export class Update{class_name}Handler implements ICommandHandler<Update{class_name}Command> {{
  constructor(
    @Inject(RepositoryNames.{class_name}Repository)
    private readonly repository: I{class_name}Repository,
    private readonly queryBus: QueryBus,
    private readonly logger: LoggerService,
  ) {{}}

  async execute(command: Update{class_name}Command): Promise<Result<{class_name}>> {{
    const {{ id, ...new{class_name}Props }} = command;

    this.logger.log(`Searching {resource_camel_case} with id ${{id.id}}`);
    const {resource_camel_case}Response = await this.repository.findById(command.id);

    if ({resource_camel_case}Response.isNone()) {{
      this.logger.error(`{class_name} ${{command.id.id}} not found`);
      return Result.Fail(new AppError.NotFoundError(`{class_name} ${{command.id.id}} not found`));
    }}

    const {resource_camel_case} = {resource_camel_case}Response.unwrap();
    this.logger.log(`Updating {resource_camel_case} with new fields`);
    const {resource_camel_case}Updated = {resource_camel_case}.update({{
      ...new{class_name}Props,
    }});

    if ({resource_camel_case}Updated.isFailure) {{
      return Result.Fail({resource_camel_case}Updated.errorValue().unwrap());
    }}

    try {{
      await this.repository.save({resource_camel_case});
    }} catch (error) {{
      return Result.Fail(new AppError.UnexpectedError(error));
    }}
    return Result.Ok({resource_camel_case});
  }}
}}
"""


DELETE_COMMAND_HANDLER_CODE_TEMPLATE = """
import {{ Result }} from '@app/common/base';
import {{ AppError }} from '@app/common/errors';
import {{ LoggerService }} from '@app/common/services';
import {{ UniqueEntityID }} from '@ddd/domain/base';
import {{ Inject }} from '@nestjs/common';
import {{ CommandHandler, ICommandHandler }} from '@nestjs/cqrs';
import {{ I{class_name}Repository }} from '../../../domain/repositories/i{resource_name}.repository';
import {{ RepositoryNames }} from 'apps/remittance/src/infrastructure/repositories';

export class Delete{class_name}Command {{
  constructor(public {resource_camel_case}Id: UniqueEntityID) {{}}
}}

@CommandHandler(Delete{class_name}Command)
export class Delete{class_name}Handler implements ICommandHandler<Delete{class_name}Command> {{
  constructor(
    @Inject(RepositoryNames.{class_name}Repository)
    private readonly repository: I{class_name}Repository,
    private readonly logger: LoggerService,
  ) {{}}

  async execute(command: Delete{class_name}Command) {{
    this.logger.log('[DELETE {resource_all_caps} COMMAND]: command called');

    const catResp = await this.repository.findById(command.{resource_camel_case}Id);
    if (catResp.isNone()) {{
      return Result.Fail(new AppError.NotFoundError(`{class_name} not found.`));
    }}

    const {resource_camel_case} = catResp.unwrap();

    try {{
      await this.repository.drop({resource_camel_case});
    }} catch (error) {{
      return Result.Fail(new AppError.UnexpectedError(error, 'Error archiving {resource_camel_case}'));
    }}

    this.logger.log('[DELETE {resource_all_caps} COMMAND]: call finished');
    return Result.Ok();
  }}
}}

"""
