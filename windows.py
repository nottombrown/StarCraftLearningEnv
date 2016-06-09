import _winreg

def set_reg(reg_path, name, value):
    try:
        _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, reg_path)
        registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, reg_path, 0,
                                       _winreg.KEY_WRITE)
        _winreg.SetValueEx(registry_key, name, 0, _winreg.REG_SZ, value)
        _winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

def get_reg(name, reg_path):
    try:
        registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, reg_path, 0,
                                       _winreg.KEY_READ)
        value, regtype = _winreg.QueryValueEx(registry_key, name)
        _winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None