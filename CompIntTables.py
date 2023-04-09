#
# Want to make it super easy to retrieve data from CITs
# Holds values and sums as well
#
# Maverick Reynolds
# 1-30-2022
#

def calc_factor(fn):
    if fn == 'fp':
        return R
    elif fn == 'pf':
        return 1/R
    elif fn == 'pa':
        return (R-1)/(i*R)
    elif fn == 'ap':
        return (i*R)/(R-1)
    elif fn == 'fa':
        return (R-1)/i
    elif fn == 'af':
        return i/(R-1)
    elif fn == 'pg':
        return (1-(1+n*i)/R)/(i**2)
    elif fn == 'ag':
        return (R-(1+n*i))/(i*(R-1))
    elif fn == 'fg':
        return (R-(1+n*i))/(i**2)

# Global to avoid loop reset
values = []
ans = 0
i = 0

while True:
    
    # Special commands
    cmd = input('>>> ')
    cmds = ['sum', 'del', 'show']
    modifs = ['.', '=']

    if cmd in cmds or cmd[0] in modifs:
        if cmd[0] == '=':
            ans = float(eval(cmd[1:]))
            values.append(ans)
        elif cmd[0] == '.':
            p = int(cmd[1:])
            nval = values[-1]*(1+i)**p
            values[-1] = round(nval, 2)
        elif cmd == 'del':
            values.pop()
        elif cmd == 'sum':
            ans = round(sum(values), 2)
            print(ans)
            values = []
        else:
            # If show is called
            pass

        print(values)
        continue

    # Calculations
    func, i, n, *amt = cmd.split()

    i = int(i)*0.01
    n = int(n)
    R = (1+i)**n
    if amt:
        amt = ans if amt[0] == 'ans' else float(amt[0])
    else:
        amt = 1

    ans = calc_factor(func)*amt

    # Print/add amount
    if amt == 1:
        ans = round(ans, 5)
        print(ans)
    else:
        ans = round(ans, 2)
        values.append(ans)
        print(values)