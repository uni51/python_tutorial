# モジュールで定義されている名前
import math

# モジュール内で定義されている名前は、組み込み関数のdirで確認できます。
# dir(モジュール)：モジュールで定義されている名前のリストを返します。
print(' '.join(dir(math)))

# __doc__ __loader__ __name__ __package__ __spec__ acos acosh asin asinh atan atan2 atanh ceil copysign cos cosh degrees e erf erfc exp expm1 fabs factorial floor fmod frexp fsum gamma gcd hypot inf isclose isfinite isinfisnan ldexp lgamma log log10 log1p log2 modf nan pi pow radians remainder sin sinh sqrt tan tanh tau trunc
