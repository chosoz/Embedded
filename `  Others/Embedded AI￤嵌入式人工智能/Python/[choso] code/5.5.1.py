name = "first";
def fn1():
    name = "second";
    def fn2():
        print(name); #// 变量回溯（当前没有，追查上家）
    fn2();
    print(name);

fn1();
print(name);
# fn2(); #// fn2是局部函数，不能访问