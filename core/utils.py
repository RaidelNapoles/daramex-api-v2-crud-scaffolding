from pathlib import Path


def to_camel_case(resource_name: str):
    chunks = list(map(lambda item: item.capitalize(), resource_name.split("-")))
    chunks[0] = chunks[0].lower()
    return "".join(chunks)


def to_class_name(resource_name: str):
    name = to_camel_case(resource_name)
    return name[0].upper() + name[1:]


def get_dir_path(base_dir: str, resource_name: str = None):
    dir_path = base_dir
    if resource_name:
        dir_path += f"/{resource_name}"
    Path(dir_path).mkdir(parents=True, exist_ok=True)
    return dir_path


if __name__ == "__main__":
    print(to_camel_case("shop-product-item"))
    print(to_class_name("shop-product-item"))
