import ase
from dscribe.descriptors import SOAP
from dscribe.descriptors import LMBTR

def get_soap_descriptor(geometries, atom_labels):
    ase_mols = []
    for xyz in geometries:
        ase_mols.append(ase.Atoms(symbols=atom_labels, positions=xyz))
    soap = SOAP(species=set(atom_labels), periodic=False, rcut=6,
                nmax=6, lmax=5, average="outer", sparse=False)
    soap_rep = soap.create(ase_mols, n_jobs=1)
    return soap_rep

def get_lmbtr_descriptor(geometries, atom_labels):
    ase_mols = []
    for xyz in geometries:
        ase_mols.append(ase.Atoms(symbols=atom_labels, positions=xyz))

    lmbtr = LMBTR(
    species=[i for i in atom_labels],
    k2={
        "geometry": {"function": "distance"},
        "grid": {"min": 0, "max": 5, "n": 20, "sigma": 0.1},
        "weighting": {"function": "exp", "scale": 0.2, "threshold": 1e-3},
    },
    k3={
        "geometry": {"function": "angle"},
        "grid": {"min": 0, "max": 180, "n": 20, "sigma": 0.1},
        "weighting": {"function": "exp", "scale": 0.2, "threshold": 1e-3},
    },
    periodic=False,
    normalization="l2_each",
    )
    lmbtr_rep = lmbtr.create(ase_mols, n_jobs=1)
    new_dim = int(lmbtr_rep.shape[1] * lmbtr_rep.shape[2])
    lmbtr_rep = lmbtr_rep.reshape(-1, new_dim)
    return lmbtr_rep


