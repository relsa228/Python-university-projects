import ast


def ast_to_string_for_dict(ast_node):
    if isinstance(ast_node, ast.AST):
        return ("{\'" + ast_node.__class__.__name__ + "\': "
                + '{'
                + ','.join(
                    "\'" + field_name + "\'" + ': ' + ast_to_string_for_dict(child_node)
                    for field_name, child_node in ast.iter_fields(ast_node))
                + '}}')
    elif isinstance(ast_node, list):
        return ('{'
                + ','.join(ast_to_string_for_dict(child_node)
                           for child_node in ast_node)
                + '}')
    else:
        return repr(ast_node)


def normilize_ast_str_dictionary(working_str: str) -> str:
    for i in range(0, len(working_str)):
        if i == len(working_str):
            return working_str

        if working_str[i] == '{' and (working_str[i - 1] == '{' or working_str[i - 1] == ','):
            j = i + 1
            count = 1
            while True:
                if working_str[j] == '{':
                    count += 1
                elif working_str[j] == '}':
                    count -= 1

                if count == 0:
                    working_str = working_str[:j] + working_str[j + 1:]
                    working_str = working_str[:i] + working_str[i + 1:]
                    i -= 1
                    break
                j += 1
