from json import JSONDecoder
from functools import partial


def json_parse(file_object, decoder=JSONDecoder(), buffe_rsize=2048):
    """Get objects from json file"""
    buffer = ''
    for chunk in iter(partial(file_object.read, buffe_rsize), ''):
        buffer += chunk
        while buffer:
            try:
                # read json with extraneous data
                result, index = decoder.raw_decode(buffer)
                for obj in result:
                    yield obj
                buffer = buffer[index:].lstrip()
            except ValueError:
                # not enough data to decode, read more
                break


if __name__ == '__main__':
    # Get objects from json file
    with open('example.json', 'r') as f:
        for json_obj in json_parse(f):
            print(json_obj)
