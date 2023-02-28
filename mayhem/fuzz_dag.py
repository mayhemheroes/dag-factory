#!/usr/bin/env python3
import random

import atheris
import sys
import fuzz_helpers
import random
import yaml


with atheris.instrument_imports(include=['dagfactory']):
    import dagfactory


def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        with fdp.ConsumeTemporaryFile('.yml', all_data=True, as_bytes=False) as f:
            factory = dagfactory.DagFactory(f)
            factory.get_dag_configs()
            factory.clean_dags(globals())
            factory.generate_dags(globals())
    except (AttributeError, Exception):
        return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
