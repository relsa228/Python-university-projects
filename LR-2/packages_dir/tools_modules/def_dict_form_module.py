import ast
import inspect

from packages_dir.tools_modules.function_to_serializable_form import ast_to_string_for_dict
from packages_dir.tools_modules.function_to_serializable_form import normilize_ast_str_dictionary


def serialize_to_dict(obj: object) -> dict:
    """
    Нормально работает
    """

    result = dict()

    if isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, str) or isinstance(obj, bool):
        result['type'] = type(obj).__name__
        result['value'] = obj

    elif inspect.isroutine(obj):
        fff = inspect.getsource(obj)
        fff = fff[4:]
        ast_tree = ast.parse(fff)
        ser_str = ast_to_string_for_dict(ast_tree)
        ser_str = normilize_ast_str_dictionary(ser_str)
        result[str(type(obj))] = ser_str

    elif inspect.isclass(obj):
        result['type'] = 'class'
        result['class_name'] = obj.__name__
        class_members = inspect.getmembers(obj)
        class_initializers = [i for i in class_members if i[0] == '__init__']
        class_members = [i for i in class_members if i[0][0:2] != '__']
        class_members = class_members + class_initializers

        for class_member in class_members:
            result[class_member[0]] = serialize_to_dict(class_member[1])

    elif isinstance(obj, dict):
        for item in obj:
            if isinstance(item, int) or isinstance(item, float) or isinstance(item, str) or isinstance(item, bool):
                wrk_dict = dict()
                wrk_dict['type'] = type(obj[item]).__name__
                wrk_dict['value'] = obj[item]
                result[item] = wrk_dict

    elif isinstance(obj, list) or isinstance(obj, tuple):
        wrk_dict = dict()

        if isinstance(obj, list):
            wrk_dict['type'] = 'list'
        else:
            wrk_dict['type'] = 'tuple'

        for item in obj:
            if isinstance(item, int) or isinstance(item, float) or isinstance(item, str) or isinstance(item, bool):
                wrk_tmp = dict()
                wrk_tmp['type'] = type(item).__name__
                wrk_tmp['value'] = item
                wrk_dict[item] = wrk_tmp
        result = wrk_dict

    else:
        result['type'] = 'instance'
        result['class'] = serialize_to_dict(type(obj))
        obj_members = inspect.getmembers(obj)
        obj_members = [i for i in obj_members if i[0][0:2] != '__']
        for class_member in obj_members:
            result[class_member[0]] = serialize_to_dict(class_member[1])

    return result
