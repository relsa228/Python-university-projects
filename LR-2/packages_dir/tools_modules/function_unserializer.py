import ast
import types

glob_ast_str = "ast.Module(body=[ast.FunctionDef(name='govno', args=ast.arguments(posonlyargs=[],args=[ast.arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[ast.Return(value=ast.BinOp(left=ast.Constant(value=2), op=ast.Add(), right=ast.Constant(value=1)))], decorator_list= [])], type_ignores=[])"


def set_glob_str(new_str: str):
    globals()['glob_ast_str'] = new_str


def get_function_name(unparse_str: str) -> str:
    result = ""
    for i in range(4, len(unparse_str)):
        if unparse_str[i] == '(':
            return result
        result += unparse_str[i]


def unparsed_funct():
    ss = eval(glob_ast_str)
    ast.fix_missing_locations(ss)
    unparse_ast = ast.unparse(ss)
    unparse_ast += f"\n\ncompiled_function = {get_function_name(unparse_ast)}\n    "
    unparse_ast = "\n" + unparse_ast
    code_source = compile(unparse_ast, filename="main.py", mode="exec")
    return code_source


compiled_function = types.FunctionType(unparsed_funct(), globals())


def return_compiled_function():
    compiled_function()
    return compiled_function
