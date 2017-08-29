# -*- coding: utf-8 -*-
#
"""Python bindings for SuiteSparse QR routines.

Exported functions:
    sparseqr.qr                    QR decomposition
    sparseqr.solve                 solve linear system; LHS sparse, RHS dense
    sparseqr.solve_sparse          solve linear system; both LHS and RHS sparse
    sparseqr.permutation_from_E    convert permutation vector to permutation matrix

The solvers work also for overdetermined linear systems,
making them useful for solving linear least-squares problems.

See the docstrings of the individual functions for details.
"""

from __future__ import absolute_import

__version__ = '1.0.0'

# add any imports here, if you wish to bring things into the library's top-level namespace when the library is imported.
from .sparseqr import qr, permutation_from_E
from .sparseqr import qr_solve as solve
from .sparseqr import qr_solve_sparse as solve_sparse

