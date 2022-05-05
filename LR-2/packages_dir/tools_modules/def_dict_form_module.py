import ast
import inspect

from packages_dir.tools_modules.ast_to_dict_module import ast_to_dict
from packages_dir.tools_modules.unserialize_funct_module import return_compiled_function
from packages_dir.tools_modules.dic_to_ast_module import unparse_ast_str
from packages_dir.tools_modules.unserialize_funct_module import unparsed_funct


def serialize_to_dict(obj: object, globals_from_main: dict) -> dict:
    '''
    Перевод объекта в словарь для сериализации
    '''
    result = dict()
    globals().update(globals_from_main)
    if isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, str) or isinstance(obj, bool):
        result['type'] = type(obj).__name__
        result['value'] = obj

    elif inspect.isroutine(obj):
        fff = inspect.getsource(obj)
        if fff[:4] == '    ':
            fff = fff[4:]
        ast_tree = ast.parse(fff)
        ser_str = ast_to_dict(ast_tree)
        result[str(type(obj))] = ser_str

    elif inspect.isclass(obj):
        result['type'] = 'class'
        result['class_name'] = obj.__name__
        class_members = inspect.getmembers(obj)
        class_initializers = [i for i in class_members if i[0] == '__init__']
        class_members = [i for i in class_members if i[0][0:2] != '__']
        class_members = class_members + class_initializers

        for class_member in class_members:
            result[class_member[0]] = serialize_to_dict(class_member[1], globals_from_main)

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
        result['class'] = serialize_to_dict(type(obj), globals_from_main)
        obj_members = inspect.getmembers(obj)
        obj_members = [i for i in obj_members if i[0][0:2] != '__']
        for class_member in obj_members:
            result[class_member[0]] = serialize_to_dict(class_member[1], globals_from_main)

    return result


def deserialize_from_dict(incoming_dict: dict, globals_from_main) -> object:
    '''
    Возвращает объект из универсального словаря
    '''
    if 'type' in incoming_dict and incoming_dict['type'] == 'class':
        dict_as_obj = dict()
        for item in incoming_dict.items():
            if type(item[1]) == dict and "<class 'function'>" in item[1]:
                unparsed_funct(unparse_ast_str(item[1]["<class 'function'>"]))
                unprs_fnct = return_compiled_function(unparse_ast_str(item[1]["<class 'function'>"]), globals())
                dict_as_obj[item[0]] = unprs_fnct

        constructed_class = type(f'{incoming_dict["class_name"]}', (object,), dict_as_obj)

        return constructed_class
    elif 'type' in incoming_dict and incoming_dict['type'] == 'instance':
        class_deserialized = deserialize_from_dict(incoming_dict['class'], globals_from_main)

        params_dict = dict()
        for item in incoming_dict.items():
            if type(item[1]) == dict and 'value' in item[1]:
                params_dict[item[0]] = item[1]['value']
            elif type(item[1]) == dict and 'type' in item[1] and item[1]['type'] == 'instance' and len(
                    params_dict) != 0:
                if class_deserialized:
                    for item_in_included in item[1].items():
                        if type(item_in_included) == tuple and 'value' in item_in_included[1]:
                            params_dict[item_in_included[0]] = item_in_included[1]['value']

        # https://stackoverflow.com/questions/334655/passing-a-dictionary-to-a-function-as-keyword-parameters
        constructed_instance = class_deserialized(**params_dict)
        return constructed_instance
    elif "<class 'function'>" in incoming_dict:
        unparsed_funct(unparse_ast_str(incoming_dict["<class 'function'>"]))
        unprs_fnct = return_compiled_function(unparse_ast_str(incoming_dict["<class 'function'>"]), globals())
        return unprs_fnct

    if 'type' in incoming_dict and incoming_dict['type'] == 'list':
        out_list = list()

        for item in incoming_dict.items():
            if 'value' in item[1]:
                out_list.append(type(item[1]['type'])(item[1]['value']))

        return out_list
    elif 'type' in incoming_dict and incoming_dict['type'] == 'tuple':
        out_tuple = tuple()

        for item in incoming_dict.items():
            if 'value' in item[1]:
                out_tuple = list(out_tuple)
                out_tuple.append(type(item[1]['type'])(item[1]['value']))
                out_tuple = tuple(out_tuple)

        return out_tuple

    else:
        else_dict = dict()

        for item in incoming_dict.items():
            if type(item[1]) == dict and 'value' in item[1]:
                else_dict[item[0]] = item[1]['value']

        return else_dict
