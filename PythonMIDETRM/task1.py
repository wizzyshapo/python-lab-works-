def vtoroi_max(arr):
    m1= None
    m2= None
    for i in arr:
        if m1 is None or i > m1:
            m2 = m1
            m1 = i
        elif i != m1 and (m2 is None or i> m2):
            m2 = i
    return m2

arr = [12, 5, 8, 12, 9, 7]
a = vtoroi_max(arr)
if a is None:
    print("No seconf largest element")
else:
    print(a)