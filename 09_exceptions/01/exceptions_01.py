# Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp. W pętli spróbuj wykonać dzielenie 10 przez wartość z listy. Złap wyjątki jakie mogą się przy tej okazji wydarzyć.

elements = [13, 'text', 2.45, 0, ('1', '2'), [], {1,2}, {'key':123}, range(10)]

for e in elements:
    try:
        result = 10 / e
    except (TypeError, ZeroDivisionError) as err:
        print(f'{e} - ', err)
    except:
        print('Different error')
