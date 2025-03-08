def StairCase(n,display):
    result = []
    for i in range(1,n+1):
        result.append(display*i)
    return '\n'.join(result)