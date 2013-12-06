# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.cmtk.nbs import NetworkBasedStatistic
def test_NetworkBasedStatistic_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    t_tail=dict(usedefault=True,
    ),
    edge_key=dict(usedefault=True,
    ),
    in_group2=dict(mandatory=True,
    ),
    out_nbs_network=dict(),
    number_of_permutations=dict(usedefault=True,
    ),
    threshold=dict(usedefault=True,
    ),
    in_group1=dict(mandatory=True,
    ),
    node_position_network=dict(),
    out_nbs_pval_network=dict(),
    )
    inputs = NetworkBasedStatistic.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_NetworkBasedStatistic_outputs():
    output_map = dict(nbs_network=dict(),
    network_files=dict(),
    nbs_pval_network=dict(),
    )
    outputs = NetworkBasedStatistic.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value