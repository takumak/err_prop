from decimal import Decimal

def adjust_precision(a, b):
  if isinstance(a, float):
    a = Decimal.from_float(a)
  if isinstance(b, float):
    b = Decimal.from_float(b)

  digits = b.adjusted()
  if b.as_tuple().digits[0] == 1:
    digits -= 1
  q = Decimal((0, (0,), digits))
  return a.quantize(q), b.quantize(q)

def valerr_latex(a, b, plus_sign = False, force_paren = False, no_err = False, no_exp = False):
  if isinstance(a, float): a = Decimal.from_float(a)
  if isinstance(b, float): b = Decimal.from_float(b)
  if isinstance(a, int): a = Decimal(a)
  if isinstance(b, int): b = Decimal(b)

  a, b = adjust_precision(a, b)
  sign = '-' if a.is_signed() else ('+' if plus_sign else '')
  a = a.copy_sign(1)
  e = 0 if no_exp else a.adjusted()

  if -1 <= e <= 2:
    if no_err:
      return '%s%s' % (sign, a)

    if force_paren or plus_sign or a.is_signed():
      return r'%s(%s{\pm}%s)' % (sign, a, b)
    else:
      return r'%s%s{\pm}%s' % (sign, a, b)

  m = Decimal((0, (1,), -e))
  if no_err:
    return r'%s(%s\times10^{%d})' % (sign, a * m, e)
  return r'%s(%s{\pm}%s)\times10^{%d}' % (sign, a * m, b * m, e)

def err_prop(func_exp, **values):
  import sympy

  for _k in values.keys():
    locals()[_k] = sympy.Symbol(_k)
  _func = eval(func_exp)

  _keys = values.keys()
  def _args(f):
    ret = []
    for a in f.args:
      if isinstance(a, sympy.Symbol):
        ret.append(a.name)
      else:
        ret += _args(a)
    return ret
  _args = _args(_func)
  _keys = sorted(_keys, key=lambda k: _args.index(k))

  _err = []
  _args = []
  _args = []
  for _n in _keys:
    _s = sympy.Symbol(r'\sigma_' + _n)
    _err.append((sympy.diff(_func, locals()[_n])**2)*(_s**2))
    _args += [(_n, values[_n][0]), (_s, values[_n][1])]

  _func_err = sympy.sqrt(sum(_err))
  _val = float(_func.subs(_args))
  _val_ = float(_func_err.subs(_args))
  return _val, _val_
