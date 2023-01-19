import click

from clinica.pipelines import cli_param
from clinica.pipelines.engine import clinica_pipeline
from clinica.pydra import engine_utils

name = "pydra-t1-freesurfer"


@clinica_pipeline
@click.command(name=name, hidden=True)
@cli_param.argument.bids_directory
@cli_param.argument.caps_directory
@cli_param.option_group.pipeline_specific_options
@cli_param.option.atlas_path
def cli(
    bids_directory: str,
    caps_directory: str,
    atlas_path: str,
) -> None:
    """Cross-sectional pre-processing of T1w volumes with FreeSurfer."""
    from . import pipeline

    parameters = {"atlas_path": atlas_path}

    workflow = pipeline.build_core_workflow(
        name=name,
        input_dir=bids_directory,
        output_dir=caps_directory,
        parameters=parameters,
    )

    engine_utils.run(workflow)


if __name__ == "__main__":
    cli()
