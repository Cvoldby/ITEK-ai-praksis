"""
This is a weight calculator.
"""


def weight_calculator(X, W, threshold):
    sum_wx = 0
    
    for idx, x in enumerate(X):
        sum_wx += x*W[idx]
    
    if sum_wx > threshold:
        return 1
    else:
        return 0
    
def x_tables(W, threshold):    
    outputs = {}
    for x1 in range(2):
        for x2 in range(2):
            for x3 in range(2):
                
                outputs[x1,x2,x3] = weight_calculator([x1,x2,x3],W, threshold)

    return outputs



def three_two_one_network(X, W1, W2, W3, threshold):
    w1x = 0
    
    for idx, x in enumerate(X):
        w1x += x*W1[idx]

    if w1x > threshold[0]:
        w1x = 1
    else:
        w1x = 0

    print("n1", w1x)

    w2x = 0
    for idx, x in enumerate(X):
        w2x += x*W2[idx]

    if w2x > threshold[1]:
        w2x = 1
    else:
        w2x = 0

    print("n2", w2x)

    w3x = 0
    for idx, x in enumerate([w1x,w2x]):
        w3x += x*W3[idx]

    print("n3",w3x)

    if w3x > threshold[2]:
        print(1)
        return 1
    else:
        print(0)
        return 0

def exercise1():
    """
    Exercise 1
    """
    x1, x2, x3 = 1, 0, .4
    w1, w2, w3 = 1, 1, .7
    X = [x1, x2, x3]
    W = [w1, w2, w3]
    threshold = .67
    print(weight_calculator(X, W, threshold))

def exercise2():
    """
    Exercise 2
    """
    x1, x2, x3 = 1, 0, .4
    w1, w2, w3 = -1, 1, -.35
    X = [x1, x2, x3]
    W = [w1, w2, w3]
    threshold = .1
    print(weight_calculator(X, W, threshold))

def exercise3():
    """
    Exercise 3
    """
    w1, w2, w3 = 1, 1, 1
    W = [w1, w2, w3]
    threshold = 2.5
    print(x_tables(W, threshold))


def exercise4():
    """
    Exercise 4
    """
    w1, w2, w3 = 2, 2, 1
    W = [w1, w2, w3]
    threshold = 4.1
    print(x_tables(W, threshold))


def exercise5():
    """
    Exercise 5
    """
    w1, w2, w3 = 1, 1, 0
    W = [w1, w2, w3]
    threshold = 1.1
    print(x_tables(W, threshold))


if __name__ == "__main__":
    X = [1, 0, 0.4]
    W = [-1, 1, -0.35]
    threshold = 0.1
    #print(weight_calculator(X, W, threshold))

    W = [-1, 1, -1]
    threshold = 3.3
    
    outputs = {}

    for x1 in range(2):
        for x2 in range(2):
            for x3 in range(2):
                
                outputs[x1,x2,x3] = weight_calculator([x1,x2,x3],W, threshold)

    #print(outputs)

    W1 = [1, 1, 1]
    W2 = [-1, -1, -1]
    W3 = [1, 1]
    tresholds = [2.5, -0.5, .5]
    outputs = {}

    for x1 in range(2):
        for x2 in range(2):
            for x3 in range(2):
                
                outputs[x1,x2,x3] = three_two_one_network([x1,x2,x3],W1,W2,W3, tresholds)

    print(outputs)
    
