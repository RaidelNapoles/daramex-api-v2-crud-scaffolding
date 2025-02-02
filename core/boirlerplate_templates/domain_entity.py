DOMAIN_ENTITY_CODE_TEMPLATE = """import {{ Result }} from '@app/common/base';
import {{ DomainEntity, EntityProps, ObjectEntity, UniqueEntityID }} from '@ddd/domain/base';
import {{ NotImplementedException }} from '@nestjs/common';

export type {class_name}Props = {{}};

export type New{class_name}Props = Omit<{class_name}Props, 'updatedAt' | 'createdAt'>;

export type Update{class_name}Props = Partial<New{class_name}Props>;

export class {class_name} extends DomainEntity<{class_name}Props> {{
  // get property_name() {{
  //   return this.props.property_name;
  // }}

  public remove() {{
    throw new NotImplementedException('Remove method not implemented');
  }}

  public static new(props: New{class_name}Props): Result<{class_name}> {{
    const allProps: {class_name}Props = {{
      ...props,
      createdAt: new Date(),
      updatedAt: new Date(),
    }};

    return this.create(allProps, new UniqueEntityID());
  }}

  public static create(props: {class_name}Props, id: UniqueEntityID): Result<{class_name}> {{
    const {resource_camel_case} = new {class_name}(props, id);
    return Result.Ok({resource_camel_case});
  }}

  /**
   * Assign all properties from persistence model to domain model,
   *
   * @param {{}} props
   * @returns  {{Result<{class_name}>}}
   * @memberof {class_name}
   */
  public static assign(props: ObjectEntity<{class_name}Props>) {{
    const {resource_camel_case} = {class_name}.create(props, new UniqueEntityID(props._id)).unwrap();
    {resource_camel_case}.createdAt = props.createdAt;
    {resource_camel_case}.updatedAt = props.updatedAt;
    {resource_camel_case}._v = props._v;
    {resource_camel_case}.archived = props.archived;
    return Result.Ok({resource_camel_case});
  }}

  public archive() {{
    this.archived = true;
  }}

  public unarchive() {{
    this.archived = false;
  }}

  public update(props: Update{class_name}Props): Result<{class_name}> {{
    // this.props.property_name = props.property_name ?? this.props.property_name;

    return Result.Ok(this);
  }}

  getPlainObject(): ObjectEntity<{class_name}Props> {{
    return {{
      ...this.props,
      _id: this.id.id.toString(),
      createdAt: this.createdAt,
      updatedAt: this.updatedAt,
      _v: this._v,
      archived: this.archived,
    }};
  }}

  getPropertyKeys(): EntityProps<{class_name}Props>[] {{
    return ['_id', 'createdAt', 'updatedAt', '_v', 'archived'];
  }}
}}
"""
