def modify_typescript_import_and_array(
    code: str, new_import_statement: str, new_class_name: str
):
    if new_class_name in code:
        return

    lines = code.split("\n")

    # Find where to insert the import statement
    import_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith("import"):
            import_index = i

    # Insert the new import statement after existing imports
    if import_index is not None:
        lines.insert(import_index + 1, new_import_statement)
    else:
        lines.insert(0, new_import_statement)

    # Find the EntitiesPersistence array declaration
    entities_array_line = None
    for i, line in enumerate(lines):
        if "EntitiesPersistence" in line and "=" in line:
            entities_array_line = i

    # Add the new class to the array
    if entities_array_line:
        lines[entities_array_line] = (
            f"{lines[entities_array_line].rstrip(',')}\n  {new_class_name},"
        )

    return "\n".join(lines)
