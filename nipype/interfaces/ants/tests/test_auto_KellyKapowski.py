# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..segmentation import KellyKapowski


def test_KellyKapowski_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        convergence=dict(
            argstr='--convergence "%s"',
            usedefault=True,
        ),
        cortical_thickness=dict(
            argstr='--output "%s"',
            extensions=None,
            hash_files=False,
            keep_extension=True,
            name_source=["segmentation_image"],
            name_template="%s_cortical_thickness",
        ),
        dimension=dict(
            argstr="--image-dimensionality %d",
            usedefault=True,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        gradient_step=dict(
            argstr="--gradient-step %f",
            usedefault=True,
        ),
        gray_matter_label=dict(
            usedefault=True,
        ),
        gray_matter_prob_image=dict(
            argstr='--gray-matter-probability-image "%s"',
            extensions=None,
        ),
        max_invert_displacement_field_iters=dict(
            argstr="--maximum-number-of-invert-displacement-field-iterations %d",
            usedefault=True,
        ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        number_integration_points=dict(
            argstr="--number-of-integration-points %d",
            usedefault=True,
        ),
        segmentation_image=dict(
            argstr='--segmentation-image "%s"',
            extensions=None,
            mandatory=True,
        ),
        smoothing_variance=dict(
            argstr="--smoothing-variance %f",
            usedefault=True,
        ),
        smoothing_velocity_field=dict(
            argstr="--smoothing-velocity-field-parameter %f",
            usedefault=True,
        ),
        thickness_prior_estimate=dict(
            argstr="--thickness-prior-estimate %f",
            usedefault=True,
        ),
        thickness_prior_image=dict(
            argstr='--thickness-prior-image "%s"',
            extensions=None,
        ),
        use_bspline_smoothing=dict(
            argstr="--use-bspline-smoothing 1",
        ),
        warped_white_matter=dict(
            extensions=None,
            hash_files=False,
            keep_extension=True,
            name_source=["segmentation_image"],
            name_template="%s_warped_white_matter",
        ),
        white_matter_label=dict(
            usedefault=True,
        ),
        white_matter_prob_image=dict(
            argstr='--white-matter-probability-image "%s"',
            extensions=None,
        ),
    )
    inputs = KellyKapowski.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_KellyKapowski_outputs():
    output_map = dict(
        cortical_thickness=dict(
            extensions=None,
        ),
        warped_white_matter=dict(
            extensions=None,
        ),
    )
    outputs = KellyKapowski.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
