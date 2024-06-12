# operation.py

from custom_types import MyInt, MyFloat, MyComplex, MyList, MyDict

# 包含自定义类型的上下文
eval_context = {
    'MyInt': MyInt,
    'MyFloat': MyFloat,
    'MyComplex': MyComplex,
    'MyList': MyList,
    'MyDict': MyDict
}

class Operation:
    def __init__(self, name, content=None):
        self.name = name
        self.content = content
        self.sub_operations = []

    def add_sub_operation(self, operation):
        self.sub_operations.append(operation)

    def execute(self, context):
        if self.name == "打印":
            print(eval(self.content, eval_context, context))
        elif self.name == "赋值":
            try:
                var, expr = self.content.split('=', 1)
                var = var.strip()
                expr = expr.strip()
                context[var] = eval(expr, eval_context, context)
            except Exception as e:
                print(f"赋值操作 '{self.content}' 中的错误: {e}")
        elif self.name == "条件":
            if eval(self.content, eval_context, context):
                for sub_op in self.sub_operations:
                    sub_op.execute(context)
        elif self.name == "逻辑":
            if eval(self.content, eval_context, context):
                for sub_op in self.sub_operations:
                    sub_op.execute(context)
        elif self.name == "转换":
            var, target_type = self.content.split('->')
            var = var.strip()
            target_type = target_type.strip().lower()
            if var in context:
                if target_type == "int":
                    context[var] = MyInt(context[var].value)
                elif target_type == "float":
                    context[var] = MyFloat(context[var].value)
                elif target_type == "complex":
                    context[var] = MyComplex(context[var].value)
                else:
                    raise ValueError(f"未知的目标类型: {target_type}")
            else:
                raise ValueError(f"变量 {var} 不存在")
