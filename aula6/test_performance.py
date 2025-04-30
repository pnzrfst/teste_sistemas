import time 
from mycode import functionTime

def test_functionTime():
    start_time = time.time()
    functionTime()
    end_time = time.time()
    duration = end_time - start_time
    assert duration < 6, f"A funcao demorou {duration}, mais do que o esperado"

