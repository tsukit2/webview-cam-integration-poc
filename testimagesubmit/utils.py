
def get_device_name(request):
   agent_str = request.headers['user-agent']
   return 'android' if 'android' in agent_str.lower() else 'ios'
