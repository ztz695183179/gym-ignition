# Copyright (C) 2019 Istituto Italiano di Tecnologia (IIT). All rights reserved.
# This software may be modified and distributed under the terms of the
# GNU Lesser General Public License v2.1 or any later version.

# Import SWIG bindings
# See https://github.com/robotology/gym-ignition/issues/7
#     https://stackoverflow.com/a/45473441/12150968
import sys
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    import os
    dlopen_flags = sys.getdlopenflags()
    if "gympp_bindings" not in sys.modules:
        sys.setdlopenflags(dlopen_flags | os.RTLD_GLOBAL)
    else:
        sys.setdlopenflags(dlopen_flags | os.RTLD_LAZY | os.RTLD_NOLOAD | os.RTLD_GLOBAL)

    import gympp_bindings

    # Restore the flags
    sys.setdlopenflags(dlopen_flags)
else:
    import gympp_bindings

    # try:
    #     import gympp_bindings
    # except:
    #     pass


