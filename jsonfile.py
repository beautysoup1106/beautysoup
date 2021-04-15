import json

params = {
    'symbol': '12345',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

param_str = json.dumps(params)

print('after json seriallizations')
print('type of param_str={} param_str={}'.format(type(param_str), params))

original_params = json.loads(param_str)

print('after json deserializations')
print('type of original_str={},orginal_str={}'.format(type(original_params), original_params))
