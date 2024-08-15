import add as ad
import minus as mi
import multiple as mul
import divide as did

try:
    print(ad.add(1, 2))
    print(mi.minus(2, 2))
    print(mul.multiple(5, 2))
    print(did.divide(1, 0))
except Exception as e:
    print(e)
