

def check_required_params(list_of_required_params, params_received_from_request):
    for param in list_of_required_params:
        if param not in params_received_from_request:
            return {'error': f'Missing required parameter: {param}'}
        if len(params_received_from_request.get(param)) == 0:
            return {'error': f'Null value for parameter: {param}'}

    return 200

