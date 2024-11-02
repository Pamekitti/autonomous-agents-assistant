from typing import Dict, Any
from RestrictedPython import compile_restricted, safe_globals
import io
from contextlib import redirect_stdout
import os

SAFE_BUILTINS = {
    'abs': abs, 'bool': bool, 'dict': dict,
    'float': float, 'int': int, 'len': len,
    'list': list, 'max': max, 'min': min,
    'range': range, 'round': round, 'str': str,
    'sum': sum
}

def execute_code(code: str) -> Dict[str, Any]:
    """Execute code in a restricted environment"""
    safe_globals.update({
        'print': print,
        '__builtins__': SAFE_BUILTINS
    })
    
    try:
        byte_code = compile_restricted(code, '<inline>', mode='exec')
        output = io.StringIO()
        local_vars = {}
        
        with redirect_stdout(output):
            exec(byte_code, safe_globals, local_vars)
            
        return {
            "success": True,
            "output": output.getvalue(),
            "local_vars": {k: v for k, v in local_vars.items() 
                          if not k.startswith('_')}
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "code": code
        } 