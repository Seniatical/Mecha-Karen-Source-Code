import json, asyncio

class Cache:
    def __init__(self, cache = None):
        self.cache = cache or {}  ## Load pre-exising cache if you like
        
    async def base_template(self, user_id: int) -> bool:
        if user_id in self.cache:
            return False
        self.cache.update({user_id: {
            "images": [],
            "messages": [],
            "users": [],
            "quotes": []
        }})
        return self.cache.get(user.id)
        
    def to_json(self, path, container):   ## Usually i will have 2 but fish
        ## My Method is to use try and finally to do this :>
        ## not async cus it only used when the bot = dead
        data = self.get_cache(container)
        with open(path, 'w') as f:
            json.dump(f, data, indent=4)
        
    async def update_cache(self, key, value, category, num = None) -> dict:
        if num:
            self.cache[key][category][num] = value
        else:
            self.cache[key][category].append(value)
        return self.cache
    
    async def remove_key(self, **values):
        if 'key' in values:
            value = values['key']
        else:
            value = values['value']
            
        temp = {v: k for k, v in self.cache.items()} if 'value' in values else self.cache
        if temp != self.cache:
            ## keys and values are reversed
            value = temp[value]
        self.cache.pop(value)
        return self.cache

    async def get_value(self, key):
        return self.cache.get(key)
    
    async def get_key_by_value(self, value):
        temp = {v: k for k, v in self.cache.items()}
        return temp.get(value)
    
    async def add_new_container(self, name, cache = None):
        global temp
        cache = cache or {}
        exec('''self.{} = {}'''.format(name, cache))
        exec('''global temp
temp = self.{}
        '''.format(name))
        return temp
    
    async def whole_cache(self, name):
        global temp
        exec('''global temp
temp = self.{}
        '''.format(name))
        return temp
    
    def get_cache(self, name):
        global temp
        exec('''global temp
temp = self.{}
        '''.format(name))
        return temp

async def loop_event(cache: Cache, path: str, timeout: int) -> None:
   while True:
       cache.to_json(path, cache)
       await asyncio.sleep(timeout)
   return True
