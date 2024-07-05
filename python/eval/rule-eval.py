#!/usr/bin/env python

# SETUP

import os

content = """
__import__('datetime').datetime.now()
"""
with open("eval.input","w+") as f:
	f.write(content)

# NOTES
#   String Literals f, """ """, r'', b'', fr"", etc should all be detected by "...", but still some tests are added as assurance. 

# single string argument
#ok: python_eval_rule-eval
eval("1+1")

# literal string concatenation 
#ok: python_eval_rule-eval
print(eval("1"+"+"+"1"))

# implicit string concatenation
#ok: python_eval_rule-eval
eval("1+" "1")

plus="+"
one= "1"

# variable string concatenation
#ok: python_eval_rule-eval
eval("1"+plus+"1")

# format string with single argument
#ok: python_eval_rule-eval
eval(f"1{plus}1")

# raw format string with single argument
#ok: python_eval_rule-eval
eval(rf"1{plus}1")

# format string with multiple arguments
#ok: python_eval_rule-eval
eval(f"1{plus}{one}")

# single string interpolation
#known false positive, semgrep limitations in understanding of Python string interpolations
#ok: python_eval_rule-eval
eval("1%s"%"+1")

# multiple string interpolation
#known false positive, semgrep limitations in understanding of Python string interpolations
#ok: python_eval_rule-eval
eval( "1 %s %s" % ("+", "1") )


# string concatenation with casted integer constant
#known false positive, semgrep limitations in understanding of Python string constants
#ok: python_eval_rule-eval
#eval("1+"+str(1))
#TODO: enable once SemGrep's String Constant Propagation improves.

# string literal and standard library call
#ok: python_eval_rule-eval
print(eval("os.getcwd()"))

# format string literal and standard library call
#ok: python_eval_rule-eval
print(eval(f"os.getcwd()"))

# format string literal and standard library call
#ok: python_eval_rule-eval
print(eval(r"os.getcwd()"))

# triple-quote string literal and standard library call
#ok: python_eval_rule-eval
print(eval("""os.getcwd()"""))

#following call evaluates a hard-coded string which results in a predetermined behavior and a harmless output
#ok: python_eval_rule-eval
content = eval("__builtins__.open('eval.input','r').read()")
print(content)

print(
    #following call, as opposed to the previous one, evaluates a string with known procedence but unknown content and thus exhibits a non-deterministic, externally-controlled behavior
    #ruleid: python_eval_rule-eval
    eval(
       content 
    )
)

print(
    #this call evaluates a hard-coded expression which is parametrized using str.format and externally provided input 
    #ruleid: python_eval_rule-eval
    eval(r"__builtins__.open('{}','r').read()".format(input()))
)

print(
    #this call evaluates a hard-coded expression which is parametrized using string interpolation and externally provided input 
    #ruleid: python_eval_rule-eval
    eval(r"__builtins__.open('%s','r').read()" % input())
)

#ok: python_eval_rule-eval
eval("os.chmod('%s', 0o666)" % 'eval.input')

# User-defined functions and methods named "eval" should not trigger a finding.

class Foo(object):

    #ok: python_eval_rule-eval 
    def eval(self):
        print("User-defined eval method")

    def foo(self):
        #ok: python_eval_rule-eval 
        self.eval()

class Bar(object):
    def bar(self,input):
        #ruleid: python_eval_rule-eval
        eval(input)

        def eval(input):
             print("User-defined eval method")
        #ok: python_eval_rule-eval
        eval(input)

#ok: python_eval_rule-eval 
Foo().eval()

class MyClass:
    def __init__():
          return
    def eval(input):
          print('harmless')
    
#ruleid: python_eval_rule-eval 
eval(content)

# call without arguments, superfluous but not dangerous.
#ok: python_eval_rule-eval 
eval()

#ok: python_eval_rule-eval 
def eval(input):
	print("Harmless user-defined eval function")

#known false positive, requires reflection or ability to compare eval.__module__=='builtins'
#ok: python_eval_rule-eval 
eval(content)


# TEARDOWN

os.remove("eval.input")
