'''
Created on Apr. 24, 2019

@author: jldupont

state(a,b,c) = action
'''

class StateExists(Exception): pass

class States:
    """
    Collection of [state, action] pairs
    
    The hierarchical map is constructed using the following:
    
      { l1_state1: { l2_state1: { l3_state1: action_state1 } }
       ,l1_state2: { l2_state2: { l3_state2: action_state2 } }
       ,l1_state3: { l2_state3: action_state3 }
       ... 
      }
      
    Whereas 'action' is a callable object and 'state' is a string.
    """
    
    def __init__(self):
        self._map = {}
    
    def add(self, action, *components):
        """
        Add a [state, action] pair
        
        Each positional parameter constitute
        a level in the hierarchy of the map
        """
        assert len(components) > 0, "Must have at least of state component"
        assert callable(action), "Parameter 'action' must be a callable"
        
        def _add(_map, action, cp):
            if len(cp) == 0:
                return
            
            if len(cp) == 1:
                #
                # Is there already something at this state?
                #
                try:
                    _ = map[cp[0]]
                except:
                    pass
                else:
                    raise StateExists("State is already defined at: "+str(components))
                
                _map[cp[0]] = action
                return
            
            down_map = _map.get(cp[0], {})
            
            if callable(down_map):
                raise StateExists("Action already present at this state: "+str(components))
            
            #
            # This is just really necessary to initialize the chain
            #
            _map[cp[0]] = down_map
            
            # Recurse...
            #
            _add(down_map, action, cp[1:])
        
        _add(self._map, action, components)
        
        
    def get(self, default_action, *components):
        """
        Retrieves a mapping [state, action]
        """
        assert callable(default_action), "Must have a default callable action"
        assert len(components) > 0, "Must have at least 1 state component"
        
        def _drill(_map, cp):
            comp = cp[0]
            if len(cp) == 1:
                maybe_action = _map.get(comp, None)
                if maybe_action is None:
                    return default_action
                
                if callable(maybe_action):
                    return maybe_action
                
                #
                # It's not a callable
                #  so it can't be a match at this point...
                #
                return default_action
            
            maybe_next_level = _map.get(comp, None)
            if maybe_next_level is None:
                return default_action
            
            return _drill(maybe_next_level, cp[1:])
        
        return _drill(self._map, components)
    