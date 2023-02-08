from cron_descriptor import get_description
import random

def generate_cron_expr(start: int, stop: int) -> str:
    lst = [str(x) for x in range(start, stop+1)]
    lst.append('*')
    num = random.choice(lst)
    match random.randint(0,4):
        case 0:
            if((start == 1 and stop == 12) or (start == 0 and stop == 6)):
                return num
            else:
                return f"{num}/{str(random.randint(1,1000))}"
        case 1:
            a = random.randint(start, stop)
            b = random.randint(start, stop)
            return f"{a},{b}"
        case 2:
            a = random.randint(start,stop-1)
            b = random.randint(a, stop)
            return f"{a}-{b}"
        case 3:
            return num
        case _:
            return num


def generate_question_and_anwser() -> tuple[str, str]:
    cron_expr = f'{generate_exp(0,59)} {generate_exp(0,23)} {generate_exp(1,31)} {generate_exp(1,12)} {generate_exp(0,6)}'
    cron_desc = get_description(cron_expr)
    return (cron_expr, cron_desc)