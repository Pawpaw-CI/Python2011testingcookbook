# -*-coding:utf-8-*-
__author__ = "pawpawDu"
import sys
err = sys.stderr
import nose
import re
from nose.plugins import Plugin

class RegexPicker(Plugin):
    name = "regexpicker"
    def __init__(self):
        Plugin.__init__(self)
        self.verbose = False

    # 重写插件选项，增加可选模式
    def options(self, parser, env):
        Plugin.options(self,parser,env)
        parser.add_option("--re-pattern",dest="pattern",action="store",
                          default=env.get("NOSE_REGEX_PATTERN","test.*"),
                          help=("Run test methods that have a method name"
                                " matching this regular expression"))

    def configure(self, options, conf):#重写配置
        Plugin.configure(self,options,conf)
        self.pattern = options.pattern
        if options.verbosity >= 2:
            self.verbose = True
            if self.enabled:
                err.write("pattern for matching test methods is %s\n"% self.pattern)
    def wantMethod(self,method):
        wanted = re.match(self.pattern,method.func_name) is not None
        if self.verbose and wanted:
            err.write("nose will run %s\n"% method.func_name)
        return wanted

if __name__ =="__main__":
    args = ["","recipe13","--with-regexpicker","--re-pattern=test.*|length","--verbosity=2"]
    print "With verbosity..."
    print "************************"
    nose.run(argv=args,plugins=[RegexPicker()])
    print "Without verbosity..."
    print "========================="

    args = args[:-1]

    nose.run(argv=args,plugins=[RegexPicker()])#书中关键字是plugin，始终失败，通过F1键查看其关键字，其方法应该是plugins
    nose.run
