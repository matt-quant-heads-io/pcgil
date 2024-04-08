# TODO: check if env var EVALUATION_SYSTEM_ROOT is set
isort . --atomic
python ci/check_style.py --do_apply_style
black .
