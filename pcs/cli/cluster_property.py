from typing import (
    Any,
    Sequence,
)

from pcs.cli.common.errors import CmdLineInputError
from pcs.cli.common.parse_args import (
    InputModifiers,
    prepare_options,
)
from pcs.common import reports


def set_property(lib: Any, argv: Sequence[str], modifiers: InputModifiers):
    """
    Options:
      * --force - allow unknown options
      * -f - CIB file
    """
    modifiers.ensure_only_supported(
        "--force",
        "-f",
    )
    if not argv:
        raise CmdLineInputError()
    force_flags = set()
    if modifiers.get("--force"):
        force_flags.add(reports.codes.FORCE)
    cluster_options = prepare_options(argv)
    lib.cluster_property.set_property(cluster_options, force_flags)


def unset_property(lib: Any, argv: Sequence[str], modifiers: InputModifiers):
    """
    Options:
      * --force - no error when removing not existing properties
      * -f - CIB file
    """
    modifiers.ensure_only_supported(
        "--force",
        "-f",
    )
    if not argv:
        raise CmdLineInputError()
    force_flags = set()
    if modifiers.get("--force"):
        force_flags.add(reports.codes.FORCE)
    lib.cluster_property.unset_property(argv, force_flags)
