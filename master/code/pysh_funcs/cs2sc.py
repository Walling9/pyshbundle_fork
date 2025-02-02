# -*- coding: utf-8 -*-

import numpy

def cs2sc(field):

#     Created on Thu May  7 18:51:20 2020
#     CS2SC(FIELD) converts the square (L+1)x(L+1) matrix FIELD, containing
#     spherical harmonics coefficients in |C\S| storage format into a 
#     rectangular (L+1)x(2L+1) matrix in  /S|C\format.
    
#     IN:
#     field .... the square (L+1)x(L+1) matrix FIELD , containing
#                    spherical harmonics coefficients in |C\S| storage format
#     OUT: 
#     sc ....... rectangular (L+1)x(2L+1) matrix in  /S|C\format
    
# ----------------------------------------------------------------------------
#      project: GRACEpy
# ----------------------------------------------------------------------------
#     % author: Bramha Dutt Vishwakarma, University of Bristol
#     @author: bv18488
# ----------------------------------------------------------------------------
# license:
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the  Free  Software  Foundation; either version 3 of the License, or
#    (at your option) any later version.
#  
#    This  program is distributed in the hope that it will be useful, but 
#    WITHOUT   ANY   WARRANTY;  without  even  the  implied  warranty  of 
#    MERCHANTABILITY  or  FITNESS  FOR  A  PARTICULAR  PURPOSE.  See  the
#    GNU General Public License for more details.
#  
#    You  should  have  received a copy of the GNU General Public License
#    along with Octave; see the file COPYING.  
#    If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------------

    rows = len(field)
    cols = len(field[0])

    if (rows!=cols) and (cols!=2*rows-1):
        raise Exception("Input neither in cs nor in sc format")
    elif cols==2*rows-1:
        sc = field
    else:
        c    = numpy.tril(field)
        ut   = numpy.triu(field)
        i = numpy.identity(rows)
        i = 1-i
        s    = numpy.fliplr(numpy.transpose(numpy.multiply(ut, i, )))
        sc   = numpy.concatenate((s[:,1:rows], c), axis=1)
        
    return(sc)