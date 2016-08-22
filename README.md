誤差伝搬をよしなに処理する.

## 例

![img](http://www.sciweavers.org/tex2img.php?eq=D%26%3D%2612.2%5Cpm0.2%5C%20%5Cmathrm%7Bmm%7D%5C%5C%0Ah%26%3D%2625.1%5Cpm0.15%5C%20%5Cmathrm%7Bmm%7D%5C%5C%0AV%26%3D%26%5Cfrac%7B%5Cpi%7D%7B4%7D%20D%5E2h%3D%3F%5Cpm%3F%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

```
$ python3
Python 3.4.3 (default, Mar 10 2016, 22:49:00)
[GCC 4.9.3] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from err_prop import err_prop, valerr_latex
>>> err_prop('sympy.pi/4*D**2*h',D=(12.2,0.2),h=(25.1,0.15))
(2934.1564322659124, 97.78683540802695)
>>> valerr_latex(*err_prop('sympy.pi/4*D**2*h',D=(12.2,0.2),h=(25.1,0.15)))
'(2.93{\\pm}0.10)\\times10^{3}'
```
