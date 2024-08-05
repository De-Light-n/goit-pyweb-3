from multiprocessing import Process, Semaphore, Manager, current_process

def calculate(semaphore: Semaphore, men:dict, number: int):
    with semaphore:
        result = []
        if number % 2 == 1:
            limit = number//3
        else:
            limit = number//2
        
        for i in range(1, limit+1):
            if number % i == 0:
                result.append(i)
        result.append(number)   
        men[current_process().name] = result 
        

def factorize(*number):
    semaphore = Semaphore(4)
    with Manager() as m:
        result = m.dict()
        prs = []
        for num in number:
            pr = Process(target=calculate, args=(semaphore, result, num))
            pr.start()
            prs.append(pr)
            
        [pr.join() for pr in prs]
    
        return [result[pr.name] for pr in prs]


if __name__=="__main__":
    a, b, c, d, e = factorize(90, 255, 76, 10651060, 77)
    print(a, b, c, d, e, sep="\n")