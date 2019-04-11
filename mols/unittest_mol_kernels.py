"""
Molecular kernels unit tests.
Author: kkorovin@cs.cmu.edu
"""

from mols.molecule import Molecule
from mols import mol_kernels
from dragonfly.utils.base_test_class import BaseTestClass, execute_tests

S1, S2, S3 = "Cc1ccccc1", "C1OC1", "CCOC(=O)C1=C[C@@H](OC(CC)CC)[C@H](NC(C)=O)[C@@H](N)C1"

class MolKernelsTestCase(BaseTestClass):
    def setUp(self):
        S1, S2, S3 = "Cc1ccccc1", "C1OC1", "CCOC(=O)C1=C[C@@H](OC(CC)CC)[C@H](NC(C)=O)[C@@H](N)C1"
        self.mols = [Molecule(S1), Molecule(S2), Molecule(S3)]

    def test_visualize(self):
        ## Plotting this test graph
        # plt.subplot(121)
        # nx.draw(graph)
        # plt.subplot(122)
        # nx.draw(graph, pos=nx.circular_layout(graph), nodecolor='r', edge_color='b')
        # plt.show()

        # TODO: how to visualize igraph mol?
        pass

    def test_conversions(self):
        mol = self.mols[0]
        graph = mol_kernels.mol2graph_igraph(mol)
        print(graph)

    def _test_edgehist_kernel(self):
        params = {"cont_par": 2.}
        print(mol_kernels.compute_edgehist_kernel(self.mols, params))

    def _test_wl_kernel(self):
        print(mol_kernels.compute_wl_kernel(self.mols))

    def test_graphlet_kernel(self):
        params = {"int_par": 4}
        print(mol_kernels.compute_graphlet_kernel(self.mols, params))

    def test_fps_kernel(self):
        kernel = mol_kernels.FingerprintKernel(<TODO: set hyperparameters>)
        res = kernel._child_evaluate(self, self.mols, self.mols)
        print(res)


if __name__=="__main__":
    execute_tests()
