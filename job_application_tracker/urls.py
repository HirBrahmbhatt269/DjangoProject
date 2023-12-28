"""
Here, if you want to import a certain function from a library instead of importing whole library, you can use
from lib_name import functionality...
import X
Imports the module X, and creates a reference to that module in the current namespace.
Then you need to define completed module path to access a particular attribute or method from inside the module
(e.g.: X.name or X.attribute)

from X import *
Imports the module X, and creates references to all public objects defined by that module in the current namespace
(that is, everything that doesn’t have a name starting with _) or whatever name you mentioned.
Or, in other words, after you've run this statement,
you can simply use a plain (unqualified) name to refer to things defined in module X.
But X itself is not defined, so X.name doesn't work. And if name was already defined,
it is replaced by the new version. And if name in X is changed to point to some other object, your module won’t notice.

This makes all names from the module available in the local namespace.
"""

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
]
