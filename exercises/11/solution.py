import numpy as np

def readData(x, y, filename):
    with open(filename, 'r') as f:
        arr = f.read()

    arr = arr.replace('\n', ' ')
    arr = arr.split(' ')
    arr = arr[:-1]
    arr = [int(i) for i in arr]
    arr = np.array(arr).reshape(x,y)
    return arr

def prod_h(arr, x, y, window):
    best = {'window': None, 'max':0}
    for i in range(0,y):
        for j in range(0, x - window):
            arrSlice = arr[i, j:j+window]
            arrSlice = [int(k) for k in arrSlice]
            arrSliceProd = np.prod(arrSlice)
            if arrSliceProd > best['max']:
                best['window'] = arrSlice
                best['max'] = arrSliceProd
    return best

def prod_v(arr, x, y, window):
    best = {'window': None, 'max':0}
    for i in range(0,y - window):
        for j in range(0, x):
            arrSlice = arr[i:i+window,j]
            arrSliceProd = np.prod(arrSlice)
            if arrSliceProd > best['max']:
                best['window'] = arrSlice
                best['max'] = arrSliceProd
    return best

def prod_tlbr(arr, x, y, window):
    best = {'window': None, 'max':0}
    for i in range(0, y - window):
        for j in range(0, x - window):
            # diag prod
            arrSlice = [arr[i+k,j+k] for k in range(0,window)]
            arrSliceProd = np.prod(arrSlice)
            if arrSliceProd > best['max']:
                best['window'] = arrSlice
                best['max'] = arrSliceProd
    return best

def prod_trbl(arr, x, y, window):
    best = {'window': None, 'max':0}
    for i in range(0, y - window):
        for j in range(window, x):
            # diag prod
            arrSlice = [arr[i+k,j-k] for k in range(0,window)]
            arrSliceProd = np.prod(arrSlice)
            if arrSliceProd > best['max']:
                best['window'] = arrSlice
                best['max'] = arrSliceProd
    return best

# horizontal:   0 <= x <= 20 - 4,   0 <= y <= 20
# vertical:     0 <= x <= 20,       0 <= y <= 20 - 4
# TL diagonal:  0 <= x <= 20 - 4,   0 <= y <= 20 - 4
# TR diagonal:  0 + 4 <= x <= 20,   0 <= y <= 20 - 4

if __name__ == '__main__':
    x = 20
    y = 20
    window = 4
    arr = readData(x, y, 'data.ssv')
    h = prod_h(arr, x, y, window)['max']
    v = prod_v(arr, x, y, window)['max']
    tlbr = prod_tlbr(arr, x, y, window)['max']
    trbl = prod_trbl(arr, x, y, window)['max']

    print(max(h, v, tlbr, trbl))
    
    
