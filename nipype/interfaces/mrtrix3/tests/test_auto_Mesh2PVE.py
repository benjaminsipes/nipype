# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import Mesh2PVE


def test_Mesh2PVE_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=-3,
        ),
        in_first=dict(
            argstr="-first %s",
            extensions=None,
        ),
        out_file=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=-1,
            usedefault=True,
        ),
        reference=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=-2,
        ),
    )
    inputs = Mesh2PVE.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Mesh2PVE_outputs():
    output_map = dict(
        out_file=dict(
            extensions=None,
        ),
    )
    outputs = Mesh2PVE.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
