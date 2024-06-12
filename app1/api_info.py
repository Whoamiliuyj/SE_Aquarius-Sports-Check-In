import ast

views_file_path = 'views.py'
output_md_file_path = 'API_Documentation_1.md'


class ViewFunctionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.functions = []

    def visit_FunctionDef(self, node):
        function_info = {
            'name': node.name,
            'methods': set(),
            'params': set(),
            'response': None
        }

        for stmt in node.body:
            # Extract request methods
            if isinstance(stmt, ast.If):
                if isinstance(stmt.test, ast.Compare):
                    if (isinstance(stmt.test.left, ast.Attribute) and stmt.test.left.attr == 'method' and
                            isinstance(stmt.test.comparators[0], ast.Str)):
                        function_info['methods'].add(stmt.test.comparators[0].s)

                # Extract JSON response and request parameters
                for sub_stmt in stmt.body:
                    # Extract parameters from data.get calls
                    if isinstance(sub_stmt, ast.Assign) and isinstance(sub_stmt.value, ast.Call):
                        if (isinstance(sub_stmt.value.func, ast.Attribute) and sub_stmt.value.func.attr == 'get' and
                                isinstance(sub_stmt.value.func.value,
                                           ast.Name) and sub_stmt.value.func.value.id == 'data'):
                            if sub_stmt.value.args and isinstance(sub_stmt.value.args[0], ast.Str):
                                param_name = sub_stmt.value.args[0].s
                                function_info['params'].add(param_name)

                    # Extract JSON response
                    if isinstance(sub_stmt, ast.Expr) and isinstance(sub_stmt.value, ast.Call):
                        if isinstance(sub_stmt.value.func, ast.Name) and sub_stmt.value.func.id == 'JsonResponse':
                            function_info['response'] = self._parse_response(sub_stmt.value)

        self.functions.append(function_info)
        self.generic_visit(node)

    def _parse_response(self, call_node):
        if isinstance(call_node, ast.Call) and isinstance(call_node.func,
                                                          ast.Name) and call_node.func.id == 'JsonResponse':
            if call_node.args:
                return ast.dump(call_node.args[0])
        return None


def parse_views_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read())
    visitor = ViewFunctionVisitor()
    visitor.visit(tree)
    return visitor.functions


def generate_markdown(api_info_list, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write("# API Documentation\n\n")
        for api_info in api_info_list:
            file.write(f"## {api_info['name']}\n")
            file.write(f"**Request Methods:** {', '.join(api_info['methods'])}\n\n")
            file.write(f"**Request Parameters:** {', '.join(api_info['params'])}\n\n")
            file.write(f"**Response Content:** {api_info['response']}\n\n")
            file.write("---\n\n")


if __name__ == "__main__":
    api_info_list = parse_views_file(views_file_path)
    generate_markdown(api_info_list, output_md_file_path)
    print(f"API documentation has been generated and saved to {output_md_file_path}")


