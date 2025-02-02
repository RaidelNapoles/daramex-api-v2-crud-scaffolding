PERSISTENCE_CODE_TEMPLATE = """import {{ Entity }} from 'typeorm';
import {{ PersistentEntity }} from '../../../../../libs/infrastructure/src/base/persistent.base';

@Entity({{ name: '{resource_name}' }})
export class {class_name}Persistence extends PersistentEntity {{
    // Add entity columns
}}
"""
