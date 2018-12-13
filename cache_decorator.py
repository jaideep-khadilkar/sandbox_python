def cache_decorator(func):
    def wrapper_func(*args):
        print '-------------------------'
        node = args[0]
        key = (func.__name__, args[1:])
        print 'Key : {0}'.format(key)
        print '{0} : {1}'.format(node.name, node.cachedUserData)
        if key in node.cachedUserData:
            print 'Cached Result'
            return node.cachedUserData[key]
        else:
            rv = func(*args)
            print 'Un-cached Result'
            node.cachedUserData[key] = rv
            return rv

    return wrapper_func


class Node(object):
    def __init__(self, name):
        self.name = name
        self.cachedUserData = {}


node_A = Node('Node A')
node_B = Node('Node B')


@cache_decorator
def add(node, x, y):
    return x + y


@cache_decorator
def mult(node, x, y):
    return x * y


print add(node_A, 1, 2)
print mult(node_A, 1, 2)
print add(node_A, 1, 2)
print mult(node_A, 1, 2)
print add(node_B, 1, 2)
print mult(node_B, 1, 2)
print add(node_B, 1, 2)
print mult(node_B, 1, 2)
