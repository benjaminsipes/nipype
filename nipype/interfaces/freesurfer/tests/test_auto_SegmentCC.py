# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import SegmentCC


def test_SegmentCC_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        copy_inputs=dict(),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr="-aseg %s",
            extensions=None,
            mandatory=True,
        ),
        in_norm=dict(
            extensions=None,
            mandatory=True,
        ),
        out_file=dict(
            argstr="-o %s",
            extensions=None,
            hash_files=False,
            keep_extension=False,
            name_source=["in_file"],
            name_template="%s.auto.mgz",
        ),
        out_rotation=dict(
            argstr="-lta %s",
            extensions=None,
            mandatory=True,
        ),
        subject_id=dict(
            argstr="%s",
            mandatory=True,
            position=-1,
            usedefault=True,
        ),
        subjects_dir=dict(),
    )
    inputs = SegmentCC.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_SegmentCC_outputs():
    output_map = dict(
        out_file=dict(
            extensions=None,
        ),
        out_rotation=dict(
            extensions=None,
        ),
    )
    outputs = SegmentCC.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
