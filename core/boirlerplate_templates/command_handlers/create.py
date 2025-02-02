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
