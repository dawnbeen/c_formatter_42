# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    __init__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 10:19:07 by cacharle          #+#    #+#              #
#    Updated: 2020/10/04 10:56:53 by cacharle         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import os
import glob


FORMATTERS = {}

def formatter(func):
    FORMATTERS[func.__name__] = func
    return func

modules = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
__all__ = [os.path.basename(f)[:-3]
           for f in modules
           if os.path.isfile(f) and not f.endswith("__init__.py")]
