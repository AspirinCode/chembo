"""
Molecular domain
@author: kkorovin@cs.cmu.edu

An "optimization analog" of Molecule class
that is ties together Molecules and 
optimization over them.

"""

from dragonfly.exd.domains import Domain


class MolConstraintChecker:
    pass


class MolDomain(Domain):
    """ Domain for Molecules. """
    def __init__(self, mol_type, constraint_checker=None):
        """ Constructor. """
        self.mol_type = mol_type  # e.g. can be 'drug-like'
        self.constraint_checker = constraint_checker
        super(MolDomain, self).__init__()

    def get_type(self):
        """ Returns type of the domain. """
        return "molecule"

    def get_dim(self):
        """ Return dimension. """
        return 1

    def is_a_member(self, point):
        """ Returns true if point is in the domain. """
        if not self.mol_type == point.mol_class:
            return False
        else:
            return self.constraint_checker(point)

    @classmethod
    def members_are_equal(cls, point_1, point_2):
        """ Returns true if they are equal. """
        return molecules_are_equal(point_1, point_2)

    def __str__(self):
        """ Returns a string representation. """
        cc_attrs = {key:getattr(self.constraint_checker, key) for
                                key in self.constraint_checker.constraint_names}
        return 'Mol(%s):%s'%(self.mol_type, cc_attrs)


def molecules_are_equal(mol1, mol2):
    # TODO: implement a comparator method


# API -------------------------------------------------------------------------

def get_mol_domain_from_constraints(mol_type, constraint_dict):
    """ mol_type is the type of the molecule.
      See MolConstraintChecker constructors for args and kwargs.
    """

    #--- TODO constructing constraint_checker ---#
    # .......................................... #
    #--- TODO constructing constraint_checker ---#

    return MolDomain(mol_type, constraint_checker)
