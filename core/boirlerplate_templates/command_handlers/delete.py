DELETE_COMMAND_HANDLER_CODE_TEMPLATE = """import {{ Result }} from '@app/common/base';
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
