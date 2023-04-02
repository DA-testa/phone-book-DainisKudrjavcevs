def read_queries():
    n = int(input())
    queries = []
    for _ in range(n):
        query = input().split()
        if query[0] == 'add':
            queries.append(('add', int(query[1]), query[2]))
        elif query[0] == 'del':
            queries.append(('del', int(query[1])))
        else:
            queries.append(('find', int(query[1])))
    return queries


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    contacts = {}
    for query in queries:
        if query[0] == 'add':
            number, name = query[1], query[2]
            contacts[number] = name
        elif query[0] == 'del':
            number = query[1]
            if number in contacts:
                del contacts[number]
        else:
            number = query[1]
            if number in contacts:
                response = contacts[number]
            else:
                response = 'not found'
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))


# Dainis Kudrjavcevs 221RDB136